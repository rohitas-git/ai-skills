---
name: 1-skill-atomize
description: >
  Reorg live skills toward one job each: Boundary tables, hard redirects, ask-user forks for collisions.
  Use when: skill overlap, atomize skills, skills-reorg, /1-skill-atomize, high-overlap pass.
  Not for: report-only lint (1-skill-linter), body craft (0-skill-creator), path move without atomize (0-skill-manager organize).
  Hub: /0-skill-manager.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-manager
    role: pipeline
    when:
      - "de-overlap skills / Boundary + forks"
      - "atomize / skills-reorg"
    not_when:
      - "lint report only → 1-skill-linter"
      - "craft rewrite → 0-skill-creator"
      - "rename/move only → 0-skill-manager organize"
    prev: [0-skill-manager]
    cousins: [1-skill-linter, 0-skill-creator]
    triggers:
      - "skill atomize"
      - "1-skill-atomize"
      - "skills reorg"
      - "skill overlap"
    requires_setup: false
---

# Skill atomize

**Atomic job:** one job per live skill; collisions **ask the user** (never silent cousin load).

**Contract:** [atomic-skills.md](../0-skill-manager/references/atomic-skills.md) · **Detail:** [workflow.md](./references/workflow.md)

## Boundary

| Need | Skill |
|------|--------|
| Atomize / de-overlap | **this** |
| Health report only | `/1-skill-linter` |
| Move / rename / tombstone | `/0-skill-manager` organize |
| Place / ingest / new-hub | `/0-skill-manager` |
| Thin craft rewrite | `/0-skill-creator` + `/1-writing-great-skills` |
| Which skill for a task | `/0-butler` |

## Forks (ask)

| Fork | Question | Recommended | Branches |
|------|----------|-------------|----------|
| **F-A1** | Scope? | High-overlap only | high · high+medium · full · **Agent judgment** |
| **F-A2** | Collision fix? | Keep both + Boundary + forks | keep-both · merge · split · **Agent judgment** |
| **F-A3** | Write files? | Dry-run first | dry-run · apply · **Agent judgment** |

## Process

1. **Orient** — catalog root; flows SSOT; dry-run default.  
2. **Detect** — content-overlap clusters (description + blurb). Exclude intentional hub links (wrapper/pipeline/…). See workflow.md.  
3. **Rank** — High (same job) · Medium (trigger confusion) · Low (shared theme).  
4. **Plan** — one-job lines, Boundary, F# forks, flows + hub JSON, README blurbs. Present dry-run.  
5. **Confirm** F-A3.  
6. **Apply** — Boundary + hard redirect; strip cousin full procedures; update flows/hubs. No silent merge unless F-A2 = merge.  
7. **Gate** — `/1-skill-linter` → **Gate: PASS**.  
8. **Summary** — clusters, forks, deferred low items.

**Default if user said only “atomize”:** high-overlap · keep-both · dry-run → confirm → apply → lint.

## Hard rules

1. Multi-file writes need confirm; dry-run default.  
2. Never invent skills.  
3. Merge only true duplicates (F-A2).  
4. No dual meta-router / no `using-agent-skills`.  
5. No wiki atoms.  
6. Forks always ask (recommended first) + **Agent judgment**.  
7. Lint Gate PASS before “done”.

## Related

Parent: `/0-skill-manager` · optional pre-pass: `/1-skill-linter`.
