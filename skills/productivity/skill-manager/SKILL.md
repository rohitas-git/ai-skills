---
name: skill-manager
description: >
  Catalog facilities manager: CRUD skills, place them under a domain hub workflow,
  create new hubs, ingest/promote, organize (move/rename/deprecate), and lint catalog
  health. Use when adding, rehousing, or deprecating skills — not for "which skill
  should I use?" (that is butler). User-invoked. Triggers: skill-manager, ingest skill,
  rehouse, deprecate skill, new hub, lint skills, place skill, organize catalog.
disable-model-invocation: true
---

# Skill Manager

You renovate the skills catalog. You are **not** the concierge — **`/butler`** routes humans to domain hubs. You **mutate** the house: create/place skills, wire hub workflows, lint, tombstone.

## Session start

1. Resolve **catalog root** (has `engineering/`, `productivity/`, `misc/`, `CLAUDE.md`).
2. Confirm Matt buckets + `vendor/` exist.
3. State paths: catalog root, `productivity/butler/references/flows.md` (hub SSOT — you **write** slots here), root `README.md`, `skills-lock.json`.
4. Default mode: **dry-run** until the user confirms multi-file writes.

## Dispatch

| Op | When | Load |
|----|------|------|
| **create** | new skill body needed | hand off **`/skill-creator`** (or `/create-skill` wrapper), then **place** |
| **read / list** | what skills exist under a hub/bucket | [crud.md](./references/crud.md) + flows.md |
| **update** | re-place, fix name==dir, indexes — not craft rewrite | [crud.md](./references/crud.md) |
| **delete / deprecate** | retire a skill | [crud.md](./references/crud.md) + organize |
| **place** | attach skill to an existing domain hub | [hub-workflow.md](./references/hub-workflow.md) |
| **new-hub** | create domain hub + workflow section | [hub-workflow.md](./references/hub-workflow.md) |
| **ingest** | draft / existing / vendor candidate → catalog | [ingest-workflow.md](./references/ingest-workflow.md) |
| **organize** | move / rename / deprecate with indexes | [lint-checklist.md](./references/lint-checklist.md) organize section |
| **lint** | health-check structure + hubs + forks | [lint-checklist.md](./references/lint-checklist.md) |

If the user only wants routing (“which skill?”), **stop** and load **`/butler`**.

## Hard rules

See [hard-rules.md](./references/hard-rules.md). Always:

1. No wiki/concept atoms.
2. Confirm before multi-file mutate; dry-run default.
3. Never promote `using-agent-skills`.
4. Prefer merge into an existing hub child over a second peer skill.
5. Every live skill should declare a **parent hub** + link type when placed.
6. At pipeline forks, ensure an **F# ask-user** question exists in flows.md (or propose one).

## Integration test (ingest / place / new-hub)

All must pass before apply:

| # | Check |
|---|--------|
| 1 | Gap in flows/catalog |
| 2 | No collision — prefer merge |
| 3 | Prev/next or standalone explicit |
| 4 | Hard vs soft setup correct |
| 5 | Matt-short or progressive disclosure |
| 6 | Forbidden names / no dual meta-router |
| 7 | **Hub slot** — parent hub + link type (wrapper\|hard\|soft\|pipeline\|on-ramp\|leaf\|axis) |
| 8 | **Forks** — branch skills have F# questions |

## Handoffs

- Body craft / evals → `/skill-creator` (entry `/create-skill`)
- Predictability theory → `/writing-great-skills`
- Human lost / which skill → `/butler`
- Session learnings → `/reflect` may return here for lint/organize

## Layout

See [catalog-layout.md](./references/catalog-layout.md). Domain hubs live in [flows.md](../butler/references/flows.md).
