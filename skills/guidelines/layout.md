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

Live skill **directory**, frontmatter **`name`**, slash command, and hub package dir — number = **hub-tree depth** (0 … max):

| Depth | Meaning | Example |
|------:|---------|---------|
| **0** | ★ domain hub / hub-of-hubs | `0-butler`, `0-implement` |
| **1** | Child of a domain hub; sub-hub packages | `1-to-tickets`, `1-code-review` |
| **2** | Child of a depth-1 hub (e.g. under a sub-hub) | `2-verify-work`, `2-security-and-hardening` |
| **3** | Child of a depth-2 parent / nested sub-hub | `3-{slug}` when max parent depth is 2 |
| **4** | Child of a depth-3 parent | `4-{slug}` |
| **5** | Child of a depth-4 parent | `5-{slug}` |
| **6** | Child of a depth-5 parent | `6-{slug}` |
| **7+** | Same recurrence — no artificial ceiling | `depth = max(parent_depth + 1)` |

Dual membership uses **deepest** parent for the number. Full rule: `skills/0-skill-manager/references/depth-prefix-names.md`.

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
