# Catalog layout

```text
skills-root/
  skills/<name>/SKILL.md     # live only
  inbox/<name>/              # staging
  archive/<name>/            # tombstones
  archive/vendor/            # offline packs
  hubs/{hub}/hub.html        # + workflow.json
  hubs/flows-chart.html
  guidelines/                # this tree
  wikis/index.md
  wikis/log.md
```

## Discovery

Host install scans **only** `skills/*` and `inbox/*` (directories containing `SKILL.md`).

Never: `archive/`, `hubs/`, `guidelines/`, `wikis/`.

## Membership

Every live skill appears under a domain hub in:

- `skills/butler/references/flows.md`, and/or  
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
