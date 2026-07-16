#!/bin/bash

# Sync skill symlinks bidirectionally:
# 1. Create symlinks in target directories pointing to source skills
# 2. Move any new skills from target directories to source and create symlinks back
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


def print_target_block(label, c, *, moved=None, already=None, conflicts=None, created=None, missing=False):
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

    if already:
        print(f"    {c.wrap(f'✓ {len(already)} already linked', c.gray)}")

    if created:
        print(f"    {c.wrap(f'✓ created ({len(created)})', c.green)}")
        for name in created:
            print(f"      {c.wrap(name, c.green)}")

    if not (moved or already or conflicts or created):
        print(f"    {c.wrap('· no changes', c.dim)}")


with open(CONFIG_FILE) as f:
    config = json.load(f)

source_path = config["source"]
targets = config.get("targets", [])
skills_in_source = set(os.listdir(source_path)) if os.path.isdir(source_path) else set()
c = C()

print(c.wrap("Skill symlink sync", c.bold))
print(f"  Source: {c.wrap(short_target(source_path), c.dim)}")

# ── Phase 1: ingest new real directories from targets into source ─────────────
print_section("Phase 1 · Ingest from targets", c)
moved_total = []
moved_by_target = {}

for target_path in targets:
    if not os.path.isdir(target_path):
        moved_by_target[short_target(target_path)] = {"missing": True}
        continue

    moved = []
    for item_name in sorted(os.listdir(target_path)):
        item_path = os.path.join(target_path, item_name)
        if not os.path.isdir(item_path) or os.path.islink(item_path):
            continue
        if item_name in skills_in_source:
            continue
        shutil.move(item_path, os.path.join(source_path, item_name))
        moved.append(item_name)
        skills_in_source.add(item_name)
        moved_total.append(item_name)

    if moved:
        moved_by_target[short_target(target_path)] = {"moved": moved}

if moved_by_target:
    for label, data in moved_by_target.items():
        print_target_block(label, c, moved=data.get("moved"), missing=data.get("missing", False))
else:
    print(f"  {c.wrap('No new skills to move into source', c.dim)}")

# ── Phase 2: symlink source skills into each target ───────────────────────────
print_section("Phase 2 · Link targets", c)

totals = {"created": 0, "already": 0, "conflicts": 0, "missing_targets": 0}

for target_path in targets:
    label = short_target(target_path)
    if not os.path.isdir(target_path):
        totals["missing_targets"] += 1
        print_target_block(label, c, missing=True)
        continue

    already, conflicts, created = [], [], []

    for skill_name in sorted(skills_in_source):
        skill_dir = os.path.join(source_path, skill_name)
        symlink_path = os.path.join(target_path, skill_name)

        if os.path.islink(symlink_path):
            already.append(skill_name)
        elif os.path.exists(symlink_path):
            conflicts.append(f"{skill_name} — exists but is not a symlink")
        else:
            os.symlink(skill_dir, symlink_path)
            created.append(skill_name)

    totals["created"] += len(created)
    totals["already"] += len(already)
    totals["conflicts"] += len(conflicts)

    print_target_block(
        label,
        c,
        already=already or None,
        conflicts=conflicts or None,
        created=created or None,
    )

# ── Summary (created highlighted last) ────────────────────────────────────────
print_section("Summary", c)

if totals["missing_targets"]:
    print(f"  {c.wrap(f'Missing targets: {totals["missing_targets"]}', c.red)}")
if totals["conflicts"]:
    print(f"  {c.wrap(f'Conflicts: {totals["conflicts"]}', c.yellow)}")
if moved_total:
    print(f"  {c.wrap(f'Moved to source: {len(moved_total)}', c.cyan)}")
print(f"  {c.wrap(f'Already linked: {totals["already"]}', c.gray)}")

if totals["created"]:
    print(f"  {c.wrap(f'Created: {totals["created"]}', c.green)}")
else:
    print(f"  {c.wrap('Created: 0', c.dim)}")

print(c.wrap("\nDone.", c.bold))
PYTHON_EOF