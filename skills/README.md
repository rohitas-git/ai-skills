# Skills catalog

Flat live skills under `skills/`. Domain structure lives in **hubs** + **wikis**, not folders.

## Quickstart

1. `/0-setup-rohitas-skills` once per consumer repo  
2. `/0-butler` when lost  
3. `/0-skill-manager` to place, rehouse, deprecate, lint  

## Root map

| Path | Purpose |
|------|---------|
| [skills/](./skills/) | Live skills (`skills/<name>/`) |
| [inbox/](./inbox/) | Staging |
| [archive/](./archive/) | Tombstones + vendor packs |
| [hubs/](./hubs/) | Domain hub workflows |
| [wikis/index.md](./wikis/index.md) | Categorized skill index |
| [guidelines/](./guidelines/) | Layout + catalog docs |
| [CLAUDE.md](./CLAUDE.md) | Agent hard rules |

## Install

`scripts/sync-skills-symlinks.sh` installs children of `skills/` and `inbox/` only.

## Stewardship

| Role | Skill |
|------|--------|
| Route | 0-butler |
| Mutate | 0-skill-manager |
| Lint | 1-skill-linter |

Flows: `skills/0-butler/references/flows.md` · Chart: `hubs/flows-chart.html`
