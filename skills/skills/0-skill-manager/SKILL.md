---
name: 0-skill-manager
description: >
  Catalog facilities manager: CRUD skills, place them under a domain hub workflow,
  create new hubs, ingest/promote, organize (move/rename/deprecate), atomize overlapping
  skills, and lint catalog health. Use when adding, rehousing, or deprecating skills —
  not for "which skill should I use?" (that is 0-butler). User-invoked. Triggers:
  0-skill-manager, ingest skill, rehouse, deprecate skill, new hub, lint skills, place
  skill, organize catalog, atomize skills.
disable-model-invocation: true
---

# Skill Manager

You renovate the skills catalog. You are **not** the concierge — **`/0-butler`** routes humans to domain hubs. You **mutate** the house: create/place skills, wire hub workflows, lint, tombstone.

## Session start

1. Resolve **catalog root** (six folders: `skills/`, `inbox/`, `archive/`, `hubs/`, `guidelines/`, `wikis/`).
2. Confirm Matt buckets + `vendor/` exist.
3. State paths: catalog root, `skills/0-butler/references/flows.md` (hub SSOT — you **write** slots here), root `README.md`, `skills-lock.json`.
4. Default mode: **dry-run** until the user confirms multi-file writes.

## Dispatch

| Op | When | Load |
|----|------|------|
| **create** | new skill body needed | hand off **`/0-skill-creator`** (or `/1-create-skill` wrapper), then **place** (must include skill-lint) |
| **read / list** | what skills exist under a hub/bucket | [crud.md](./references/crud.md) + flows.md |
| **update** | re-place, fix name==dir, indexes — not craft rewrite | [crud.md](./references/crud.md) → skill-lint |
| **delete / deprecate** | retire a skill | [crud.md](./references/crud.md) + organize |
| **place** | attach skill to an existing domain hub | [hub-workflow.md](./references/hub-workflow.md) → **skill-lint** gate |
| **new-hub** | create domain hub + workflow section | [hub-workflow.md](./references/hub-workflow.md) → skill-lint hub package |
| **ingest** | draft / existing / vendor candidate → catalog | [ingest-workflow.md](./references/ingest-workflow.md) → **skill-lint** |
| **organize** | move / rename / deprecate with indexes | [lint-checklist.md](./references/lint-checklist.md) organize section |
| **atomize** | content overlap → one-job skills + Boundary + ask-user forks | load **`/1-skill-atomize`** + [atomic-skills.md](./references/atomic-skills.md) |
| **lint** | health-check skills + hubs + membership | load **`/1-skill-linter`** + [lint-checklist.md](./references/lint-checklist.md) |

If the user only wants routing (“which skill?”), **stop** and load **`/0-butler`**.

If the user wants overlap cleanup / atomic skills / skills-reorg, **load `/1-skill-atomize`** (do not invent a parallel reorg flow here).

## Hard rules

See [hard-rules.md](./references/hard-rules.md). Always:

1. No wiki/concept atoms.
2. Confirm before multi-file mutate; dry-run default.
3. Never promote `using-agent-skills`.
4. Prefer merge into an existing hub child over a second peer skill.
5. Every live skill must be a **hub member** (parent hub + link type) — ADR 0006.
6. At pipeline forks, ensure an **F# ask-user** question exists in flows.md (or propose one).
7. **skill-lint** after create/place/ingest — zero critical before treat as healthy (load `/1-skill-linter`).
8. Sprawl / multi-pipeline mega-skills → split or **sub-domain hub** (1-skill-linter refs), not silent growth.

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
| 7 | **Hub slot** — parent hub + link type (wrapper\|hard\|soft\|pipeline\|on-ramp\|leaf\|axis\|satellite\|sub-hub) |
| 8 | **Forks** — branch skills have F# questions |
| 9 | **skill-lint** — `/1-skill-linter` mode skill (or hub) reports **Gate: PASS** (0 critical) |

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
