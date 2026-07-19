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
  "nestedSkillRoots": [],
  "targets": [
    "/Users/rohitasbansal/.gemini/config/skills",
    "/other/path/to/skills"
  ]
}
```

- **source** — canonical skills directory (Matt-style buckets under it)
- **targets** — agent/IDE skill directories that receive top-level symlinks
- **nestedSkillRoots** — optional monorepo packs relative to `source` (normally empty; vendor packs stay out of discovery)
- Skills live at `skills/<bucket>/<skill-name>/SKILL.md`. The sync script flattens bucket children (and any leftover top-level skills) to top-level names in each target.

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
   - Top-level dirs under `source` that contain `SKILL.md` (legacy)
   - Children of catalog buckets (`engineering`, `productivity`, `misc`, `personal`, `in-progress`, `deprecated`)
   - Nested monorepo roots listed in `nestedSkillRoots` (usually empty; `vendor/` is never auto-scanned)
3. On name collision, earlier discovery wins (top-level > bucket > nested)
4. For each target directory:
   - Ingests any new real skill dirs from the target into source
   - Prunes broken links and non-skill junk previously linked by mistake
   - Creates/refreshes skill symlinks (including flattened nested skills)
5. Displays a summary of created/skipped/pruned symlinks

## Adding New Skills

**Bucket skill (preferred):** add `skills/<bucket>/<name>/SKILL.md` (bucket ∈ engineering|productivity|misc|personal|in-progress|deprecated), then run the sync script. Prefer **butler ingest** for catalog placement.

**Nested monorepo / vendor skill:** do **not** put under default discovery. Park under `vendor/` and promote only via butler ingest. `nestedSkillRoots` remains for rare opt-in flatten only.

Or commit and push — the post-merge hook runs sync on the next pull.
