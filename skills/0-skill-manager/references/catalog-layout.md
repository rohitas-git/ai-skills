# Catalog layout

```text
<catalog-root>/
  skills/<name>/SKILL.md
  inbox/
  archive/   (+ archive/vendor/)
  hubs/{hub}/
  guidelines/
  wikis/index.md  wikis/log.md
  CLAUDE.md  README.md  AGENTS.md  skills-lock.json
```

**Live path:** always `skills/<name>/`. Dual membership is logical (hubs + flows only).

**Discovery:** `skills/` + `inbox/` only.

**Wiki:** `wikis/index.md` + `wikis/log.md` (update on place/ingest/organize).  
**Version / history:** root `catalog.yaml` + `docs/FEATURE-LOG.md` (bump on ADR / convention change).  
**Butler route skim:** `skills/0-butler/references/route-index.md` (generated).

**Hub packages:** `hubs/{hub}/hub.html` + `workflow.json`.

Detail: `guidelines/layout.md`.
