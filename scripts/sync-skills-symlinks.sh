#!/bin/bash

# Sync skill symlinks from source to target directories
# Reads configuration from symlink-targets.json

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/symlink-targets.json"

if [ ! -f "$CONFIG_FILE" ]; then
  echo "Error: Config file not found: $CONFIG_FILE"
  exit 1
fi

# Parse JSON config using Python
parse_json() {
  python3 -c "import json, sys; config = json.load(open('$CONFIG_FILE')); print(json.dumps(config['$1']))"
}

SKILLS_SOURCE=$(python3 -c "import json; print(json.load(open('$CONFIG_FILE'))['source'])")

if [ ! -d "$SKILLS_SOURCE" ]; then
  echo "Error: Skills source directory not found: $SKILLS_SOURCE"
  exit 1
fi

created_count=0
skipped_count=0

echo "Syncing skill symlinks..."
echo "Source: $SKILLS_SOURCE"
echo ""

# Get targets array from JSON and process each target
python3 << PYTHON_EOF
import json

with open('$CONFIG_FILE') as f:
    config = json.load(f)
    targets = config.get('targets', [])

for target_path in targets:
    if not __import__('os').path.isdir(target_path):
        print(f"⚠️  Target directory not found: {target_path}")
        continue

    # List skills in source
    source_path = config['source']
    if not __import__('os').path.isdir(source_path):
        print(f"Error: Source not found: {source_path}")
        continue

    import os
    for skill_name in os.listdir(source_path):
        skill_dir = os.path.join(source_path, skill_name)
        if not os.path.isdir(skill_dir):
            continue

        symlink_path = os.path.join(target_path, skill_name)

        if os.path.islink(symlink_path):
            print(f"✓ Already linked: {skill_name}")
        elif os.path.exists(symlink_path):
            print(f"⚠️  Exists but not a symlink: {symlink_path}")
        else:
            os.symlink(skill_dir, symlink_path)
            print(f"✓ Created symlink: {skill_name}")
PYTHON_EOF

echo ""
echo "Done!"
