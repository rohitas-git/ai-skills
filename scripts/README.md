# Skill symlink automation

Scripts that flatten the **AI-Skills catalog** into host agent skill directories.

## Layout (catalog source)

```text
skills/                 # catalog root (config "source")
  skills/<name>/        # live skills — host-discovered
  inbox/<name>/         # staging — host-discovered, not promoted
  archive/              # tombstones — never host-discovered
  hubs/ guidelines/ wikis/
```

See `skills/guidelines/layout.md` and ADR 0007 / ADR 0003.

## Files

| File | Role |
|------|------|
| **sync-skills-symlinks.sh** | Discover skills, optional ingest, prune, symlink |
| **symlink-targets.json** | Source path, discover packages, host targets |
| **lint-skills** | Catalog health (separate) |

## Configuration (`symlink-targets.json`)

```json
{
  "source": "/path/to/AI-Skills/skills",
  "discoverPackages": ["skills", "inbox"],
  "neverDiscover": ["archive", "hubs", "guidelines", "wikis", "vendor"],
  "nestedSkillRoots": [],
  "ingestDestination": "inbox",
  "targets": ["~/.claude/skills", "..."]
}
```

| Key | Meaning |
|-----|---------|
| `source` | Catalog root (six-folder layout) |
| `discoverPackages` | Children of these dirs with `SKILL.md` become flat host names |
| `neverDiscover` | Never scan (archive, hubs, …) |
| `nestedSkillRoots` | Optional monorepo packs relative to source (default empty; vendor not auto-scanned) |
| `ingestDestination` | Where new real dirs from targets are moved (`inbox`) |
| `targets` | Agent/IDE skill dirs receiving top-level symlinks |

## Usage

```bash
# From this directory
./sync-skills-symlinks.sh

./sync-skills-symlinks.sh --dry-run      # report only
./sync-skills-symlinks.sh --no-ingest    # do not move new skills from hosts
./sync-skills-symlinks.sh --verbose      # list every create/prune
```

Typically wired from a git `post-merge` hook after pull.

## What it does

1. **Discover** — `skills/*` and `inbox/*` that contain `SKILL.md` (plus optional nested roots). Live `skills/` wins name collisions over `inbox/`.
2. **Ingest (phase 1)** — Real (non-symlink) skill dirs found only on a target and not in the catalog are moved to `source/inbox/<name>/`.
3. **Link (phase 2)** — For each target:
   - Prune broken links and catalog links that left discovery (e.g. archived).
   - Create/fix flat `target/<name>` → absolute path of the skill directory.
4. **Never** install `archive/`, hubs, guidelines, wikis, or whole vendor packs.

## Adding skills

1. Prefer **butler** → **skill-manager** place/ingest into `skills/` or `inbox/`.
2. Or drop `inbox/<name>/SKILL.md`, then run this script.
3. Or put a real skill folder in a host dir; next sync moves it into `inbox/`.

**Do not** promote vendor packs by listing them in `nestedSkillRoots` unless intentional.
