# Skill Symlink Automation

This directory contains scripts to automate the creation and management of skill symlinks.

## Files

- **sync-skills-symlinks.sh** - Main script that creates symlinks for all skills
- **symlink-targets.json** - Configuration file listing targets and nested skill roots

## Configuration

Edit `symlink-targets.json` to add or remove target directories and nested monorepos:

```json
{
  "source": "/Users/rohitasbansal/Development/AI-Skills/skills",
  "nestedSkillRoots": [
    "agent-skills/skills"
  ],
  "targets": [
    "/Users/rohitasbansal/.gemini/config/skills",
    "/other/path/to/skills"
  ]
}
```

- **source** — canonical skills directory
- **targets** — agent/IDE skill directories that receive top-level symlinks
- **nestedSkillRoots** — paths relative to `source` that hold monorepo skill packages (each child dir with `SKILL.md` is flattened to the top level of every target)

## Usage

### Manual Sync
```bash
./sync-skills-symlinks.sh
```

### Automatic Sync
The script is automatically run after git pull/merge via the `.git/hooks/post-merge` hook.

## What It Does

1. Reads the source skills directory from config
2. Collects skills from:
   - Top-level dirs under `source` that contain `SKILL.md`
   - Nested monorepo roots listed in `nestedSkillRoots` (e.g. `agent-skills/skills/*`)
3. On name collision, **top-level skills win** over nested ones
4. For each target directory:
   - Ingests any new real skill dirs from the target into source
   - Prunes broken links and non-skill junk previously linked by mistake
   - Creates/refreshes skill symlinks (including flattened nested skills)
5. Displays a summary of created/skipped/pruned symlinks

## Adding New Skills

**Top-level skill:** add `skills/<name>/SKILL.md`, then run the sync script.

**Nested monorepo skill:** add under a configured root, e.g. `skills/agent-skills/skills/<name>/SKILL.md`, then run the sync script. It will appear as `~/.…/skills/<name>` in every target.

Or commit and push — the post-merge hook runs sync on the next pull.
