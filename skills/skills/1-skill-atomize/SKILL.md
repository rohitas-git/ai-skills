---
name: 1-skill-atomize
description: >
  Make catalog skills atomic: one job each, Boundary tables, hard redirects, and
  ask-user forks for collision paths. Scans for content overlap (excluding intentional
  hub/wrapper/pipeline links), then dry-runs and applies reorg under skill-manager.
  Use for skill overlap, atomize skills, skills-reorg, boundary redirects, high-overlap
  pass, or /1-skill-atomize. Parent hub: skill-manager. Not report-only lint (/1-skill-linter)
  and not body craft (/0-skill-creator).
disable-model-invocation: true
---

# Skill Atomize

**Atomic job:** reorganize **live skills** so each has one job and collision paths **ask the user**.

**Parent hub:** `/0-skill-manager` · **Contract:** [atomic-skills.md](../0-skill-manager/references/atomic-skills.md) · **Detail:** [workflow.md](./references/workflow.md)

You **mutate** (after dry-run confirm). You are **not** the report-only linter and not a product-feature skill.

## Boundary

| Need | Skill |
|------|--------|
| Atomize / de-overlap / Boundary + forks | **skill-atomize** (this) |
| Health report only | `/1-skill-linter` |
| Move / rename / deprecate paths | `/0-skill-manager` **organize** |
| Place / new-hub / ingest | `/0-skill-manager` |
| Rewrite craft/evals of a body | `/0-skill-creator` |
| Which skill for a user task | `/0-butler` |

## Hard redirect

- Lint findings only, no reorg → `/1-skill-linter`
- Physical move/rename/tombstone without atomize → `/0-skill-manager` organize
- Greenfield skill body → `/0-skill-creator` then 0-skill-manager place

Ask once if ambiguous; never silent-branch.

## Session start

1. Resolve **catalog root** (six folders: `skills/`, `inbox/`, `archive/`, `hubs/`, `guidelines/`, `wikis/`).
2. State: flows SSOT `skills/0-butler/references/flows.md`, [atomic-skills.md](../0-skill-manager/references/atomic-skills.md).
3. Default **dry-run** until user confirms multi-file writes.
4. Ask scope + resolution if not already decided (forks below).

## Forks (ask user)

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-A1** | How far this pass? | High-overlap clusters only | high · high+medium · full catalog · **Agent judgment** |
| **F-A2** | When two skills collide? | Keep both + Boundary + ask-user forks | keep-both · merge/tombstone · split thinner · **Agent judgment** |
| **F-A3** | Apply multi-file changes now? | Dry-run first, then confirm | dry-run only · apply after confirm · **Agent judgment** |

## Process

1. **Orient** — catalog root, buckets, flows.md.
2. **Detect** — content-overlap clusters (descriptions + blurb). **Exclude** intentional hub links (wrapper/pipeline/satellite/axis/hard/soft children of same hub, e.g. 0-grilling ↔ 1-grill-me). See [workflow.md](./references/workflow.md).
3. **Rank** — High (same job packaging) · Medium (trigger confusion) · Low (shared theme, clear split).
4. **Plan** — For each in-scope cluster: one-job lines, Boundary tables, F# forks, flows + hub `workflow.json` slots, README blurbs. Present dry-run.
5. **Confirm** — F-A3; wait for user.
6. **Apply** — edit skill bodies (Boundary + redirect + lean strip of cousin procedures), update flows.md + hub packages + READMEs. No silent merges unless F-A2 = merge.
7. **Gate** — run `/1-skill-linter` (skill or catalog) → **Gate: PASS** (0 critical). Fix criticals or report.
8. **Summary** — clusters touched, forks added, non-goals left for later.

## Default policy (when user said “just atomize”)

- Scope: **high-overlap only**
- Resolution: **keep both + hard redirects + forks**
- Dry-run → confirm → apply → skill-lint

## Hard rules

1. Confirm multi-file writes; dry-run default.
2. Never invent skills; only re-bound skills on disk + flows.
3. Prefer merge only for **true** duplicate jobs (user F-A2).
4. Never promote `using-agent-skills`; no dual meta-router.
5. No wiki/concept atoms.
6. Forks always **ask the user** (recommended first); never silent cousin load.
7. skill-lint Gate: PASS before treating pass as done.
8. Do not own 0-butler routing or 1-skill-linter report format.

## Related

- **Parent:** `/0-skill-manager` (pipeline/op: atomize)
- **Detect first:** `/1-skill-linter` (optional pre-pass)
- **Craft thin bodies:** `/0-skill-creator` + `/1-writing-great-skills`
- **Route humans:** `/0-butler`
