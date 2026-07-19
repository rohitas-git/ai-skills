#!/usr/bin/env bash
# Sync host skill directories with the AI-Skills catalog.
#
# Layout (catalog root = config "source"):
#   skills/<name>/SKILL.md   live, host-discovered
#   inbox/<name>/SKILL.md    staging, host-discovered (not promoted)
#   archive/                 tombstones — never host-discovered
#   hubs/ guidelines/ wikis/ — never host-discovered
#
# For each target (~/.claude/skills, ~/.codex/skills, …):
#   1. Optionally ingest new real skill dirs from the target → source/inbox/
#   2. Prune broken / stale / non-skill symlinks that pointed at this catalog
#   3. Create or fix flat top-level symlinks <name> → catalog skill dir
#
# Usage:
#   ./sync-skills-symlinks.sh
#   ./sync-skills-symlinks.sh --dry-run
#   ./sync-skills-symlinks.sh --no-ingest
#   ./sync-skills-symlinks.sh --verbose
#
# Config: symlink-targets.json (same directory)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="${SCRIPT_DIR}/symlink-targets.json"

DRY_RUN=0
NO_INGEST=0
VERBOSE=0

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --no-ingest) NO_INGEST=1 ;;
    --verbose|-v) VERBOSE=1 ;;
    --help|-h)
      sed -n '2,22p' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *)
      echo "Unknown option: $arg (try --help)" >&2
      exit 2
      ;;
  esac
done

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "Error: config not found: $CONFIG_FILE" >&2
  exit 1
fi

export CONFIG_FILE DRY_RUN NO_INGEST VERBOSE

python3 <<'PY'
from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path

CONFIG_FILE = os.environ["CONFIG_FILE"]
DRY_RUN = os.environ.get("DRY_RUN") == "1"
NO_INGEST = os.environ.get("NO_INGEST") == "1"
VERBOSE = os.environ.get("VERBOSE") == "1"

# Names that must never be treated as skills (root files / package folders).
SKIP_NAMES = frozenset(
    {
        ".DS_Store",
        "skills-lock.json",
        "SKILL.md",
        "README.md",
        "LICENSE",
        "CLAUDE.md",
        "AGENTS.md",
        "wiki.md",
        "wiki-log.md",
        # six-folder package names (not skills)
        "skills",
        "inbox",
        "archive",
        "hubs",
        "guidelines",
        "wikis",
        "vendor",
        "Skills",  # legacy flat index name
    }
)

DEFAULT_DISCOVER = ("skills", "inbox")
DEFAULT_NEVER = ("archive", "hubs", "guidelines", "wikis", "vendor", ".scratch", ".system", ".claude")


class C:
    def __init__(self) -> None:
        use = sys.stdout.isatty() and not os.environ.get("NO_COLOR")
        self.reset = "\033[0m" if use else ""
        self.bold = "\033[1m" if use else ""
        self.dim = "\033[2m" if use else ""
        self.red = "\033[31m" if use else ""
        self.green = "\033[32m" if use else ""
        self.yellow = "\033[33m" if use else ""
        self.blue = "\033[34m" if use else ""
        self.cyan = "\033[36m" if use else ""
        self.gray = "\033[90m" if use else ""

    def wrap(self, text: str, *styles: str) -> str:
        return f"{''.join(styles)}{text}{self.reset}"


def short_target(path: str) -> str:
    home = os.path.expanduser("~")
    if path == home or path.startswith(home + os.sep):
        return "~" + path[len(home) :]
    return path


def is_skill_dir(path: str) -> bool:
    return os.path.isdir(path) and os.path.isfile(os.path.join(path, "SKILL.md"))


def load_config() -> dict:
    with open(CONFIG_FILE, encoding="utf-8") as f:
        return json.load(f)


def collect_skills(
    source: str,
    discover_packages: list[str],
    nested_roots: list[str],
) -> tuple[dict[str, str], dict[str, str], list[str], list[str]]:
    """
    Returns:
      skills: name -> absolute path
      origins: name -> label
      nested_added, nested_skipped
    """
    skills: dict[str, str] = {}
    origins: dict[str, str] = {}
    nested_added: list[str] = []
    nested_skipped: list[str] = []

    # Priority: skills/ (live) then inbox/ (staging), then nested opt-in.
    # Within a package, real dirs win over accidental symlinks.
    for package in discover_packages:
        pkg_path = os.path.join(source, package)
        if not os.path.isdir(pkg_path):
            continue
        for name in sorted(os.listdir(pkg_path)):
            if name in SKIP_NAMES or name.startswith("."):
                continue
            path = os.path.join(pkg_path, name)
            if not is_skill_dir(path):
                continue
            if name in skills:
                # Prefer non-symlink primary if we somehow have both.
                existing = skills[name]
                if os.path.islink(existing) and not os.path.islink(path):
                    skills[name] = path
                    origins[name] = f"{package}/"
                continue
            # Live package wins over later packages (skills before inbox).
            skills[name] = path
            origins[name] = f"{package}/"

    for rel_root in nested_roots:
        nest = os.path.join(source, rel_root)
        if not os.path.isdir(nest):
            nested_skipped.append(f"{rel_root} (missing)")
            continue
        for name in sorted(os.listdir(nest)):
            if name in SKIP_NAMES or name.startswith("."):
                continue
            path = os.path.join(nest, name)
            if not is_skill_dir(path):
                continue
            if name in skills:
                nested_skipped.append(f"{name} (collision with {origins[name]})")
                continue
            skills[name] = path
            origins[name] = rel_root
            nested_added.append(name)

    return skills, origins, nested_added, nested_skipped


def ensure_dir(path: str, dry: bool) -> None:
    if dry or os.path.isdir(path):
        return
    os.makedirs(path, exist_ok=True)


def unlink_path(path: str, dry: bool) -> None:
    if dry:
        return
    os.unlink(path)


def move_path(src: str, dest: str, dry: bool) -> None:
    if dry:
        return
    shutil.move(src, dest)


def symlink_force(target: str, link_path: str, dry: bool) -> None:
    """Create absolute symlink link_path -> target."""
    if dry:
        return
    if os.path.lexists(link_path):
        os.unlink(link_path)
    os.symlink(os.path.abspath(target), link_path)


def print_section(title: str, c: C) -> None:
    print(c.wrap(f"\n{title}", c.bold, c.blue))
    print(c.wrap("─" * min(72, max(len(title), 40)), c.dim))


def print_target_block(
    label: str,
    c: C,
    *,
    moved: list[str] | None = None,
    already: list[str] | None = None,
    conflicts: list[str] | None = None,
    created: list[str] | None = None,
    pruned: list[str] | None = None,
    missing: bool = False,
) -> None:
    print(c.wrap(f"\n  {label}", c.bold, c.cyan))
    if missing:
        print(f"    {c.wrap('✗ target directory not found', c.red)}")
        return
    if conflicts:
        for msg in conflicts:
            print(f"    {c.wrap('⚠', c.yellow)} {c.wrap(msg, c.yellow)}")
    if moved:
        print(f"    {c.wrap('↗ moved to source inbox', c.cyan)} ({len(moved)})")
        for name in moved:
            print(f"      {c.wrap(name, c.cyan)}")
    if pruned:
        print(f"    {c.wrap(f'✂ pruned ({len(pruned)})', c.yellow)}")
        if VERBOSE:
            for name in pruned:
                print(f"      {c.wrap(name, c.yellow)}")
        else:
            print(f"      {c.wrap(', '.join(pruned[:12]) + ('…' if len(pruned) > 12 else ''), c.dim)}")
    if already:
        print(f"    {c.wrap(f'✓ {len(already)} already linked', c.gray)}")
    if created:
        print(f"    {c.wrap(f'✓ created/relinked ({len(created)})', c.green)}")
        if VERBOSE or len(created) <= 20:
            for name in created:
                print(f"      {c.wrap(name, c.green)}")
        else:
            for name in created[:12]:
                print(f"      {c.wrap(name, c.green)}")
            print(f"      {c.wrap(f'… and {len(created) - 12} more', c.dim)}")
    if not (moved or already or conflicts or created or pruned):
        print(f"    {c.wrap('· no changes', c.dim)}")


def main() -> int:
    c = C()
    cfg = load_config()
    source = os.path.abspath(cfg["source"])
    targets: list[str] = [os.path.abspath(os.path.expanduser(t)) for t in cfg.get("targets", [])]
    discover = list(cfg.get("discoverPackages") or DEFAULT_DISCOVER)
    never = set(cfg.get("neverDiscover") or DEFAULT_NEVER)
    nested_roots: list[str] = list(cfg.get("nestedSkillRoots") or [])
    ingest_dest = cfg.get("ingestDestination") or "inbox"

    if not os.path.isdir(source):
        print(c.wrap(f"Error: source not found: {source}", c.red), file=sys.stderr)
        return 1

    # Safety: never put archive etc. into discover
    discover = [p for p in discover if p not in never and p not in ("archive", "hubs", "guidelines", "wikis")]

    skill_paths, origins, nested_added, nested_skipped = collect_skills(
        source, discover, nested_roots
    )
    known = set(skill_paths)
    source_real = os.path.realpath(source)

    print(c.wrap("Skill symlink sync", c.bold))
    if DRY_RUN:
        print(c.wrap("  mode: DRY-RUN (no filesystem writes)", c.yellow))
    print(f"  Source: {c.wrap(short_target(source), c.dim)}")
    print(f"  Discover: {c.wrap(', '.join(discover), c.dim)}")
    print(f"  Skills: {c.wrap(str(len(skill_paths)), c.dim)}")
    if VERBOSE:
        by_origin: dict[str, int] = {}
        for o in origins.values():
            by_origin[o] = by_origin.get(o, 0) + 1
        for o, n in sorted(by_origin.items()):
            print(f"    {c.wrap(o, c.dim)}: {n}")
    if nested_roots:
        print(f"  Nested roots: {c.wrap(', '.join(nested_roots) or '(none)', c.dim)}")
    if nested_added:
        print(f"  Nested flattened: {c.wrap(str(len(nested_added)), c.cyan)}")
    if nested_skipped:
        print(f"  Nested skipped: {c.wrap(str(len(nested_skipped)), c.yellow)}")
        for item in nested_skipped[:15]:
            print(f"    {c.wrap(item, c.dim)}")

    # ── Phase 1: ingest real skill dirs from targets → source/inbox/ ─────────
    print_section("Phase 1 · Ingest from targets → inbox/", c)
    moved_total: list[str] = []
    moved_by_target: dict[str, dict] = {}

    if NO_INGEST:
        print(f"  {c.wrap('Skipped (--no-ingest)', c.dim)}")
    else:
        inbox_path = os.path.join(source, ingest_dest)
        for target_path in targets:
            label = short_target(target_path)
            if not os.path.isdir(target_path):
                moved_by_target[label] = {"missing": True}
                continue
            moved: list[str] = []
            for item_name in sorted(os.listdir(target_path)):
                if item_name in SKIP_NAMES or item_name.startswith("."):
                    continue
                item_path = os.path.join(target_path, item_name)
                if os.path.islink(item_path) or not os.path.isdir(item_path):
                    continue
                if not is_skill_dir(item_path):
                    continue
                if item_name in known:
                    continue
                ensure_dir(inbox_path, DRY_RUN)
                dest = os.path.join(inbox_path, item_name)
                if os.path.exists(dest) and not DRY_RUN:
                    # Collision in inbox — leave on target as conflict later
                    continue
                move_path(item_path, dest, DRY_RUN)
                moved.append(item_name)
                if not DRY_RUN:
                    skill_paths[item_name] = dest
                    known.add(item_name)
                    origins[item_name] = f"{ingest_dest}/"
                moved_total.append(item_name)
            if moved:
                moved_by_target[label] = {"moved": moved}

        if moved_by_target:
            for label, data in moved_by_target.items():
                print_target_block(
                    label, c, moved=data.get("moved"), missing=data.get("missing", False)
                )
        else:
            print(f"  {c.wrap('No new skills to move into source', c.dim)}")

    # ── Phase 2: prune + link ────────────────────────────────────────────────
    print_section("Phase 2 · Link targets", c)

    totals = {
        "created": 0,
        "already": 0,
        "conflicts": 0,
        "missing_targets": 0,
        "pruned": 0,
    }

    for target_path in targets:
        label = short_target(target_path)
        if not os.path.isdir(target_path):
            totals["missing_targets"] += 1
            print_target_block(label, c, missing=True)
            continue

        already: list[str] = []
        conflicts: list[str] = []
        created: list[str] = []
        pruned: list[str] = []

        # Prune stale/broken catalog-owned links
        for item_name in sorted(os.listdir(target_path)):
            item_path = os.path.join(target_path, item_name)
            if not os.path.islink(item_path):
                continue

            # Broken
            if not os.path.exists(item_path):
                unlink_path(item_path, DRY_RUN)
                pruned.append(f"{item_name} (broken)")
                continue

            if item_name in SKIP_NAMES or item_name.startswith("."):
                unlink_path(item_path, DRY_RUN)
                pruned.append(item_name)
                continue

            try:
                real = os.path.realpath(item_path)
            except OSError:
                real = ""

            under_catalog = real == source_real or real.startswith(source_real + os.sep)

            # Link into this catalog but name is no longer a discoverable skill
            # (e.g. moved to archive/, or old Matt-bucket path).
            if under_catalog and item_name not in known:
                unlink_path(item_path, DRY_RUN)
                pruned.append(f"{item_name} (left catalog discovery)")
                continue

            # Link under catalog but not a skill dir
            if under_catalog and not is_skill_dir(item_path):
                unlink_path(item_path, DRY_RUN)
                pruned.append(f"{item_name} (not a skill)")
                continue

        # Create / fix skill links
        for skill_name, skill_dir in sorted(skill_paths.items()):
            link_path = os.path.join(target_path, skill_name)
            desired = os.path.abspath(skill_dir)
            desired_real = os.path.realpath(skill_dir)

            if os.path.islink(link_path):
                try:
                    current_real = os.path.realpath(link_path)
                except OSError:
                    current_real = ""
                if current_real == desired_real:
                    already.append(skill_name)
                else:
                    symlink_force(desired, link_path, DRY_RUN)
                    created.append(f"{skill_name} (relinked)")
            elif os.path.lexists(link_path):
                conflicts.append(f"{skill_name} — exists but is not a symlink")
            else:
                symlink_force(desired, link_path, DRY_RUN)
                created.append(skill_name)

        totals["created"] += len(created)
        totals["already"] += len(already)
        totals["conflicts"] += len(conflicts)
        totals["pruned"] += len(pruned)

        print_target_block(
            label,
            c,
            already=already or None,
            conflicts=conflicts or None,
            created=created or None,
            pruned=pruned or None,
        )

    # ── Summary ──────────────────────────────────────────────────────────────
    print_section("Summary", c)
    if DRY_RUN:
        print("  " + c.wrap("DRY-RUN — no changes written", c.yellow))
    if totals["missing_targets"]:
        print("  " + c.wrap(f"Missing targets: {totals['missing_targets']}", c.red))
    if totals["conflicts"]:
        print("  " + c.wrap(f"Conflicts: {totals['conflicts']}", c.yellow))
    if totals["pruned"]:
        print("  " + c.wrap(f"Pruned: {totals['pruned']}", c.yellow))
    if moved_total:
        print("  " + c.wrap(f"Moved to inbox: {len(moved_total)}", c.cyan))
    if nested_added:
        print("  " + c.wrap(f"Nested flattened: {len(nested_added)}", c.cyan))
    print("  " + c.wrap(f"Already linked: {totals['already']}", c.gray))
    print(
        "  "
        + (
            c.wrap(f"Created/relinked: {totals['created']}", c.green)
            if totals["created"]
            else c.wrap("Created/relinked: 0", c.dim)
        )
    )
    print("  " + c.wrap(f"Total skills: {len(skill_paths)}", c.dim))
    print(c.wrap("\nDone.", c.bold))
    return 0 if totals["conflicts"] == 0 else 0  # conflicts are warnings, not fail


if __name__ == "__main__":
    sys.exit(main())
PY
