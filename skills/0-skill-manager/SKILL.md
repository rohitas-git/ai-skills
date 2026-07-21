---
name: 0-skill-manager
description: >
  Catalog facilities: place, ingest, new-hub, organize, lint, atomize. Use when mutating
  the skills catalog. Not for: which skill to use (0-butler), crafting skill body only (0-skill-creator).
  Hub: /0-skill-manager. Triggers: ingest skill, rehouse, place skill, lint skills, new hub.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-manager
    role: hub
    when:
      - "place/ingest/organize/lint/new-hub/atomize catalog"
    not_when:
      - "route which skill → 0-butler"
      - "author body only → 0-skill-creator then place"
    next: [1-skill-linter]
    cousins: [0-skill-creator, 1-skill-atomize]
    triggers:
      - "ingest skill"
      - "rehouse"
      - "place skill"
      - "lint skills"
      - "new hub"
    requires_setup: false
---

# Skill Manager

You renovate the skills catalog. You are **not** the concierge — **`/0-butler`** routes humans to domain hubs. You **mutate** the house: create/place skills, wire hub workflows, lint, tombstone.

## Session start

1. Resolve **catalog root** (six folders: `skills/`, `inbox/`, `archive/`, `hubs/`, `guidelines/`, `wikis/`).
2. Read **`catalog.yaml`** — note `version` (product conventions) and `paths` (route-index, feature log).
3. Confirm catalog buckets (`skills/`, `inbox/`, `archive/`) + `vendor/` exist.
4. State paths: catalog root, `skills/0-butler/references/flows.md` (hub SSOT — you **write** slots here), `catalog.yaml`, `docs/FEATURE-LOG.md`, `skills-lock.json`.
5. Default mode: **dry-run** until the user confirms multi-file writes.

## Dispatch

| Op | When | Load |
|----|------|------|
| **create** | new skill body needed | **`/0-skill-creator`** (or `/1-create-skill`) — require route surface draft — then **place** |
| **read / list** | what skills exist under a hub/bucket | [crud.md](./references/crud.md) + flows.md + route-index |
| **update** | re-place, fix name==dir, indexes, catalog frontmatter — not deep craft rewrite | [crud.md](./references/crud.md) → re-validate route surface → skill-lint → regen route-index if needed |
| **delete / deprecate** | retire a skill | [crud.md](./references/crud.md) + organize + regen route-index |
| **place** | attach skill to an existing domain hub | [hub-workflow.md](./references/hub-workflow.md) → **gate-route** + **skill-lint** |
| **new-hub** | create domain hub + workflow section | [hub-workflow.md](./references/hub-workflow.md) → skill-lint hub package |
| **ingest** | draft / existing / vendor candidate → catalog | [ingest-workflow.md](./references/ingest-workflow.md) → **gate-route** + skill-lint |
| **organize** | move / rename / deprecate with indexes | [lint-checklist.md](./references/lint-checklist.md) organize section + route-index |
| **atomize** | content overlap → one-job skills + Boundary + ask-user forks | load **`/1-skill-atomize`** + [atomic-skills.md](./references/atomic-skills.md) |
| **lint** | health-check skills + hubs + membership + route surface | **`/1-skill-linter`** + [lint-checklist.md](./references/lint-checklist.md) + `scripts/lint-skills` |
| **release-note** | accepted ADR or convention change | bump `catalog.yaml` version + prepend [FEATURE-LOG.md](../../../docs/FEATURE-LOG.md) |

If the user only wants routing (“which skill?”), **stop** and load **`/0-butler`**.

If the user wants overlap cleanup / atomic skills / skills-reorg, **load `/1-skill-atomize`** (do not invent a parallel reorg flow here).

## Hard rules

See [hard-rules.md](./references/hard-rules.md). Always:

1. No wiki/concept atoms.
2. Confirm before multi-file mutate; dry-run default.
3. Never promote `using-agent-skills`.
4. **Depth-prefix names** — live skills are `{depth}-{slug}` only ([depth-prefix-names.md](./references/depth-prefix-names.md)); lint `depth-prefix` critical.
5. **Route surface** — description contract + `metadata.catalog` (no top-level route keys); regenerate butler route-index after place. See [skill-route-surface.md](./references/skill-route-surface.md).
6. Prefer merge into an existing hub child over a second peer skill.
7. Every live skill must be a **hub member** (parent hub + link type) — ADR 0006.
8. At pipeline forks, ensure an **F# ask-user** question exists in flows.md (or propose one).
9. **skill-lint** after create/place/ingest — zero critical before treat as healthy (load `/1-skill-linter`).
10. Sprawl / multi-pipeline mega-skills → split or **sub-domain hub** (1-skill-linter refs), not silent growth.

## Integration test (ingest / place / new-hub)

All must pass before apply:

| # | Check |
|---|--------|
| 1 | Gap in flows/catalog |
| 2 | No collision — prefer merge |
| 3 | Prev/next or standalone explicit |
| 4 | Hard vs soft setup correct |
| 5 | thin or progressive disclosure |
| 6 | Forbidden names / no dual meta-router |
| 7 | **Depth-prefix** — `{depth}-{slug}`; hub = `0-`; child = `1-`+; name==dir |
| 8 | **Hub slot** — parent hub + link type (wrapper\|hard\|soft\|pipeline\|on-ramp\|leaf\|axis\|satellite\|sub-hub) |
| 9 | **Forks** — branch skills have F# questions |
| 10 | **Route surface (`gate-route`)** — description contract + `metadata.catalog` (`hub`, `role`, `when`\|`triggers`); no top-level route keys ([skill-route-surface.md](./references/skill-route-surface.md)); regenerate route-index |
| 11 | **skill-lint** — `/1-skill-linter` mode skill (or hub) reports **Gate: PASS** (0 critical) |

## Handoffs

- Body craft / evals → `/0-skill-creator` (entry `/1-create-skill`)
- Per-skill / catalog health report → `/1-skill-linter`
- Overlap / atomic reorg apply → `/1-skill-atomize`
- Predictability theory → `/1-writing-great-skills`
- Human lost / which skill → `/0-butler`
- Session learnings → `/1-session-skill-reflect` may return here for lint/organize/atomize

## Layout

See [catalog-layout.md](./references/catalog-layout.md). Domain hubs live in [flows.md](../0-butler/references/flows.md). Atomic one-job skills: [atomic-skills.md](./references/atomic-skills.md).

**Agent judgment:** every user-facing fork must offer **Agent judgment** (agent chooses best branch and proceeds without more questions on that fork).
