# Skill Symlink Automation

This directory contains scripts to automate the creation and management of skill symlinks.

## Files

- **sync-skills-symlinks.sh** - Main script that creates symlinks for all skills
- **symlink-targets.json** - Configuration file listing all target directories

## Configuration

Edit `symlink-targets.json` to add or remove target directories:

```json
{
  "source": "/Users/rohitasbansal/Development/AI-Skills/skills",
  "targets": [
    "/Users/rohitasbansal/.gemini/config/skills",
    "/other/path/to/skills"
  ]
}
```

## Usage

### Manual Sync
```bash
./sync-skills-symlinks.sh
```

### Automatic Sync
The script is automatically run after git pull/merge via the `.git/hooks/post-merge` hook.

## What It Does

1. Reads the source skills directory from config
2. For each target directory in config:
   - Checks which skills have symlinks
   - Creates missing symlinks
   - Reports skipped existing symlinks
3. Displays a summary of created/skipped symlinks

## Adding New Skills

When you add a new skill to the `skills/` directory:
1. Run `./sync-skills-symlinks.sh` manually, OR
2. Commit and push the changes (the post-merge hook will run on next pull)

All symlinks will be automatically created in all configured target directories.
