#!/bin/bash

# Sync skill symlinks bidirectionally:
# 1. Create symlinks in target directories pointing to source skills
# 2. Move any new skills from target directories to source and create symlinks back
# 3. Flatten nested monorepo skill roots (e.g. agent-skills/skills/*) into each target
# Only entries that look like skills (directory containing SKILL.md) are synced.
# Configuration: symlink-targets.json

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/symlink-targets.json"

if [ ! -f "$CONFIG_FILE" ]; then
  echo "Error: Config file not found: $CONFIG_FILE"
  exit 1
fi

SKILLS_SOURCE=$(python3 -c "import json; print(json.load(open('$CONFIG_FILE'))['source'])")

if [ ! -d "$SKILLS_SOURCE" ]; then
  echo "Error: Skills source directory not found: $SKILLS_SOURCE"
  exit 1
fi

python3 << PYTHON_EOF
import json
import os
import shutil
import sys

CONFIG_FILE = "$CONFIG_FILE"

# Top-level names that must never be treated as skills (even if they look like dirs).
SKIP_NAMES = {
    ".DS_Store",
    "skills-lock.json",
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CLAUDE.md",
    "AGENTS.md",
    "agent-skills",  # legacy monorepo name; prefer vendor/agent-skills (not discovered)
    "vendor",  # third-party packs — out of default discovery
    "engineering",
    "productivity",
    "misc",
    "personal",
    "in-progress",
    "deprecated",
}

# Bucket dirs that hold discoverable skills (one level of children with SKILL.md).
# vendor is intentionally excluded. personal/in-progress/deprecated ARE discovered
# for host install (symlinked) but are not "promoted" on root README.
DISCOVER_BUCKETS = {
    "engineering",
    "productivity",
    "misc",
    "personal",
    "in-progress",
    # deprecated: tombstones stay in git only — not host-installed
}


class C:
    """ANSI colors when stdout is a TTY and NO_COLOR is unset."""

    def __init__(self):
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

    def wrap(self, text, *styles):
        return f"{''.join(styles)}{text}{self.reset}"


def short_target(path):
    home = os.path.expanduser("~")
    if path.startswith(home + os.sep):
        return "~" + path[len(home) :]
    return path


def print_section(title, c):
    print(c.wrap(f"\n{title}", c.bold, c.blue))
    print(c.wrap("─" * min(72, max(len(title), 40)), c.dim))


def print_target_block(
    label,
    c,
    *,
    moved=None,
    already=None,
    conflicts=None,
    created=None,
    pruned=None,
    missing=False,
):
    print(c.wrap(f"\n  {label}", c.bold, c.cyan))
    if missing:
        print(f"    {c.wrap('✗ target directory not found', c.red)}")
        return

    if conflicts:
        for msg in conflicts:
            print(f"    {c.wrap('⚠', c.yellow)} {c.wrap(msg, c.yellow)}")

    if moved:
        print(f"    {c.wrap('↗ moved to source', c.cyan)} ({len(moved)})")
        for name in moved:
            print(f"      {c.wrap(name, c.cyan)}")

    if pruned:
        print(f"    {c.wrap(f'✂ pruned non-skill links ({len(pruned)})', c.yellow)}")
        for name in pruned:
            print(f"      {c.wrap(name, c.yellow)}")

    if already:
        print(f"    {c.wrap(f'✓ {len(already)} already linked', c.gray)}")

    if created:
        print(f"    {c.wrap(f'✓ created ({len(created)})', c.green)}")
        for name in created:
            print(f"      {c.wrap(name, c.green)}")

    if not (moved or already or conflicts or created or pruned):
        print(f"    {c.wrap('· no changes', c.dim)}")


def is_skill_dir(path):
    """True if path is a real or linked directory containing SKILL.md."""
    if not os.path.isdir(path):
        return False
    return os.path.isfile(os.path.join(path, "SKILL.md"))


def collect_skill_paths(source_path, nested_roots):
    """
    Map skill_name -> absolute path.

    Discovery order (later cannot override earlier):
    1. Top-level skill dirs (legacy flat layout)
    2. Children of DISCOVER_BUCKETS (Matt-style catalog)
    3. nestedSkillRoots monorepo packs (opt-in; vendor packs should not be listed)

    vendor/ is never auto-scanned. Top-level / bucket skills win on name collision.
    """
    skills = {}  # name -> path
    origins = {}  # name -> origin label

    if os.path.isdir(source_path):
        for name in sorted(os.listdir(source_path)):
            if name in SKIP_NAMES or name.startswith("."):
                continue
            path = os.path.join(source_path, name)
            if is_skill_dir(path):
                skills[name] = path
                origins[name] = "top-level"

        # Bucket children: skills/<bucket>/<skill>/SKILL.md
        for bucket in sorted(DISCOVER_BUCKETS):
            bucket_path = os.path.join(source_path, bucket)
            if not os.path.isdir(bucket_path):
                continue
            for name in sorted(os.listdir(bucket_path)):
                if name in SKIP_NAMES or name.startswith("."):
                    continue
                path = os.path.join(bucket_path, name)
                if not is_skill_dir(path):
                    continue
                if name in skills:
                    # Prefer earlier origin; skip duplicate
                    continue
                skills[name] = path
                origins[name] = f"bucket:{bucket}"

    nested_added = []
    nested_skipped = []
    for rel_root in nested_roots:
        nest_path = os.path.join(source_path, rel_root)
        if not os.path.isdir(nest_path):
            nested_skipped.append(f"{rel_root} (missing)")
            continue
        for name in sorted(os.listdir(nest_path)):
            if name in SKIP_NAMES or name.startswith("."):
                continue
            path = os.path.join(nest_path, name)
            if not is_skill_dir(path):
                continue
            if name in skills:
                nested_skipped.append(f"{name} (collision with {origins[name]})")
                continue
            skills[name] = path
            origins[name] = rel_root
            nested_added.append(name)

    return skills, nested_added, nested_skipped


with open(CONFIG_FILE) as f:
    config = json.load(f)

source_path = config["source"]
targets = config.get("targets", [])
nested_roots = config.get("nestedSkillRoots", [])
c = C()

skill_paths, nested_added, nested_skipped = collect_skill_paths(source_path, nested_roots)
skills_in_source = set(skill_paths.keys())

print(c.wrap("Skill symlink sync", c.bold))
print(f"  Source: {c.wrap(short_target(source_path), c.dim)}")
print(f"  Skills: {c.wrap(str(len(skill_paths)), c.dim)} (top-level + nested)")
if nested_roots:
    print(f"  Nested roots: {c.wrap(', '.join(nested_roots), c.dim)}")
if nested_added:
    print(f"  Nested flattened: {c.wrap(str(len(nested_added)), c.cyan)}")
if nested_skipped:
    print(f"  Nested skipped: {c.wrap(str(len(nested_skipped)), c.yellow)}")
    for item in nested_skipped[:20]:
        print(f"    {c.wrap(item, c.dim)}")
    if len(nested_skipped) > 20:
        print(f"    {c.wrap(f'… and {len(nested_skipped) - 20} more', c.dim)}")

# ── Phase 1: ingest new real skill directories from targets into source ───────
print_section("Phase 1 · Ingest from targets", c)
moved_total = []
moved_by_target = {}

for target_path in targets:
    if not os.path.isdir(target_path):
        moved_by_target[short_target(target_path)] = {"missing": True}
        continue

    moved = []
    for item_name in sorted(os.listdir(target_path)):
        if item_name in SKIP_NAMES or item_name.startswith("."):
            continue
        item_path = os.path.join(target_path, item_name)
        # Only ingest real (non-symlink) skill dirs not already known.
        if os.path.islink(item_path) or not os.path.isdir(item_path):
            continue
        if not is_skill_dir(item_path):
            continue
        if item_name in skills_in_source:
            continue
        dest = os.path.join(source_path, item_name)
        shutil.move(item_path, dest)
        moved.append(item_name)
        skill_paths[item_name] = dest
        skills_in_source.add(item_name)
        moved_total.append(item_name)

    if moved:
        moved_by_target[short_target(target_path)] = {"moved": moved}

if moved_by_target:
    for label, data in moved_by_target.items():
        print_target_block(
            label, c, moved=data.get("moved"), missing=data.get("missing", False)
        )
else:
    print(f"  {c.wrap('No new skills to move into source', c.dim)}")

# ── Phase 2: symlink source skills into each target; prune junk links ─────────
print_section("Phase 2 · Link targets", c)

source_real = os.path.realpath(source_path)
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

    already, conflicts, created, pruned = [], [], [], []

    # Prune broken links and non-skill entries we previously synced by mistake.
    for item_name in sorted(os.listdir(target_path)):
        item_path = os.path.join(target_path, item_name)
        if not os.path.islink(item_path):
            continue

        # Broken symlink
        if not os.path.exists(item_path):
            os.unlink(item_path)
            pruned.append(f"{item_name} (broken)")
            continue

        # Dotfiles / known junk we should not keep as skill links
        if item_name in SKIP_NAMES or item_name.startswith("."):
            os.unlink(item_path)
            pruned.append(item_name)
            continue

        # Linked but not a skill dir (no SKILL.md) and not in our skill set
        if item_name not in skills_in_source and not is_skill_dir(item_path):
            try:
                real = os.path.realpath(item_path)
            except OSError:
                real = ""
            if real.startswith(source_real + os.sep) or real == source_real:
                os.unlink(item_path)
                pruned.append(item_name)

    for skill_name in sorted(skill_paths.keys()):
        skill_dir = skill_paths[skill_name]
        symlink_path = os.path.join(target_path, skill_name)
        desired_real = os.path.realpath(skill_dir)

        if os.path.islink(symlink_path):
            try:
                current = os.readlink(symlink_path)
                current_real = os.path.realpath(symlink_path)
            except OSError:
                current = ""
                current_real = ""
            if current_real != desired_real and current != skill_dir:
                os.unlink(symlink_path)
                os.symlink(skill_dir, symlink_path)
                created.append(f"{skill_name} (relinked)")
            else:
                already.append(skill_name)
        elif os.path.exists(symlink_path):
            conflicts.append(f"{skill_name} — exists but is not a symlink")
        else:
            os.symlink(skill_dir, symlink_path)
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

# ── Summary ───────────────────────────────────────────────────────────────────
print_section("Summary", c)

if totals["missing_targets"]:
    print("  " + c.wrap("Missing targets: " + str(totals["missing_targets"]), c.red))
if totals["conflicts"]:
    print("  " + c.wrap("Conflicts: " + str(totals["conflicts"]), c.yellow))
if totals["pruned"]:
    print("  " + c.wrap("Pruned: " + str(totals["pruned"]), c.yellow))
if moved_total:
    print("  " + c.wrap("Moved to source: " + str(len(moved_total)), c.cyan))
if nested_added:
    print("  " + c.wrap("Nested flattened: " + str(len(nested_added)), c.cyan))
print("  " + c.wrap("Already linked: " + str(totals["already"]), c.gray))

if totals["created"]:
    print("  " + c.wrap("Created: " + str(totals["created"]), c.green))
else:
    print("  " + c.wrap("Created: 0", c.dim))

print("  " + c.wrap("Total skills linked: " + str(len(skill_paths)), c.dim))
print(c.wrap("\nDone.", c.bold))
PYTHON_EOF
