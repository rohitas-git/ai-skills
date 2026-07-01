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

echo "Syncing skill symlinks..."
echo "Source: $SKILLS_SOURCE"
echo ""

# Get targets array from JSON and process each target
python3 << PYTHON_EOF
import json
import os
import shutil

with open('$CONFIG_FILE') as f:
    config = json.load(f)
    targets = config.get('targets', [])

source_path = config['source']
skills_in_source = set(os.listdir(source_path)) if os.path.isdir(source_path) else set()

# Phase 1: Move new skills from targets to source
print("Phase 1: Moving new skills from target directories to source...")
print("-" * 50)
new_skills_moved = 0

for target_path in targets:
    if not os.path.isdir(target_path):
        print(f"⚠️  Target directory not found: {target_path}")
        continue

    for item_name in os.listdir(target_path):
        item_path = os.path.join(target_path, item_name)

        # Skip if not a directory
        if not os.path.isdir(item_path):
            continue

        # Skip if already a symlink
        if os.path.islink(item_path):
            continue

        # Skip if already in source
        if item_name in skills_in_source:
            continue

        # Move new skill to source
        dest_path = os.path.join(source_path, item_name)
        print(f"↗️  Moving new skill: {item_name}")
        shutil.move(item_path, dest_path)
        new_skills_moved += 1
        skills_in_source.add(item_name)

if new_skills_moved > 0:
    print(f"Moved {new_skills_moved} new skill(s) to source")
else:
    print("No new skills to move")

print("")
print("Phase 2: Creating symlinks in target directories...")
print("-" * 50)

# Phase 2: Create symlinks in targets to source skills
for target_path in targets:
    if not os.path.isdir(target_path):
        print(f"⚠️  Target directory not found: {target_path}")
        continue

    for skill_name in skills_in_source:
        skill_dir = os.path.join(source_path, skill_name)
        symlink_path = os.path.join(target_path, skill_name)

        if os.path.islink(symlink_path):
            print(f"✓ Already linked: {skill_name}")
        elif os.path.exists(symlink_path):
            print(f"⚠️  Exists but not a symlink: {symlink_path}")
        else:
            os.symlink(skill_dir, symlink_path)
            print(f"✓ Created symlink: {skill_name}")

print("")
print("Done!")
PYTHON_EOF
