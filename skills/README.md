# Skills catalog

Flat live skills under `skills/`. Domain structure lives in **hubs** + **wikis**, not folders.

**Naming (hard):** live skills are `{depth}-{kebab-slug}` for full hub-tree depth — `0-` domain hubs, `1-` children/sub-hubs, `2-` under depth-1 parents, then **`3-` / `4-` / `5-` / `6-` / …** via the same `max(parent_depth+1)` rule (no artificial cap). See [depth-prefix-names.md](./skills/0-skill-manager/references/depth-prefix-names.md) and [CLAUDE.md](./CLAUDE.md).

## Quickstart

1. `/0-setup-rohitas-skills` once per consumer repo  
2. `/0-butler` when lost  
3. `/0-skill-manager` to place, rehouse, deprecate, lint  

## Root map

| Path | Purpose |
|------|---------|
| [skills/](./skills/) | Live skills (`skills/{depth}-{slug}/`) |
| [inbox/](./inbox/) | Staging (same depth-prefix names) |
| [archive/](./archive/) | Tombstones + vendor packs |
| [hubs/](./hubs/) | Domain hub packages (`hubs/0-{hub}/`; sub-hubs at parent+1, often `1-`) |
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
