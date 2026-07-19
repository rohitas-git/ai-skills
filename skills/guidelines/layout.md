# Catalog layout

```text
skills-root/
  skills/{depth}-{slug}/SKILL.md   # live only; depth-prefix hard rule
  inbox/{depth}-{slug}/            # staging (same naming)
  archive/<name>/                  # tombstones (may keep old names)
  archive/vendor/                  # offline packs (upstream names)
  hubs/{depth}-{hub}/hub.html      # + workflow.json; matches hub skill
  hubs/flows-chart.html
  guidelines/                      # this tree
  wikis/index.md
  wikis/log.md
```

## Depth-prefix names (hard)

Live skill **directory**, frontmatter **`name`**, slash command, and hub package dir — number = **hub-tree primary depth**:

| Depth | Meaning | Example |
|------:|---------|---------|
| **0** | ★ domain hub / hub-of-hubs (identity wins over dual edges) | `0-butler`, `0-implement` |
| **1** | Child of a domain hub; sub-hubs stay `1-` even if also pipeline elsewhere | `1-to-tickets`, `1-code-review` |
| **2+** | Primary parent only is deeper (soft dual under a sub-hub does not force this) | `2-…` |

**Dual domain:** one primary for naming; dual listings never rename. Full rule: `skills/0-skill-manager/references/depth-prefix-names.md`.

## Discovery

Host install scans **only** `skills/*` and `inbox/*` (directories containing `SKILL.md`).

Never: `archive/`, `hubs/`, `guidelines/`, `wikis/`.

## Membership

Every live skill appears under a domain hub in:

- `skills/0-butler/references/flows.md`, and/or  
- `hubs/*/workflow.json` → `children[].skills`

## Ops path effects

| Op | Files touched |
|----|----------------|
| place / ingest | `skills/`, hubs, flows, `wikis/index.md`, `wikis/log.md`, lock, README blurbs if needed |
| deprecate | `archive/`, archive README, flows †, wikis, lock |
| new-hub | `hubs/{hub}/`, flows Domain section, wikis overview |

## Related

- Agent rules: `../CLAUDE.md`  
- Human entry: `../README.md`  
- Index: `../wikis/index.md`
