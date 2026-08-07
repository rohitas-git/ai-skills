---
name: 1-session-skill-reflect
description: >
  Extract session corrections and approvals into proposed skill updates ("correct once, never again").
  Use when: /1-session-skill-reflect, end-of-session skill improve, "reflect on skill X".
  Not for: handoff compact without skill edits (1-handoff), place/rehouse (0-skill-manager), atomize overlap (1-skill-atomize).
  Hub: /0-skill-manager.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-manager
    role: soft
    when:
      - "session learnings → skill body updates"
      - "/1-session-skill-reflect"
    not_when:
      - "session handoff only → 1-handoff"
      - "catalog structure → 0-skill-manager"
    cousins: [1-handoff, 0-skill-manager, 1-skill-atomize]
    triggers:
      - "session skill reflect"
      - "1-session-skill-reflect"
      - "reflect on skill"
    requires_setup: false
---

# Session skill reflect

**Leading word: correct once** — high-confidence user corrections become permanent skill text.

## Boundary

| Need | Skill |
|------|--------|
| Session → skill body diffs | **this** |
| Catalog place / lint / organize | `/0-skill-manager` |
| Overlap / Boundary reorg | `/1-skill-atomize` |
| Compact for next agent (no skill edit) | `/1-handoff` |

Do not load deprecated `task-observer` / `continuous-learning-v2`.

## Process

1. **Scan session** for signals:  
   - HIGH — explicit correction (“do X not Y”, always/never workflow)  
   - MEDIUM — strong approval of a pattern  
   - LOW — soft suggestion  
   **Done when:** signals listed with confidence.
2. **Map to skills** — which live skill + which section (gotcha, step, description). Prefer **gotchas** / defaults that prevent recurrence.  
   **Done when:** each HIGH has a target section or “no skill yet → create”.
3. **Propose** — show diff + rationale; preserve frontmatter. Offer backup path.  
   **Done when:** user can approve/modify/skip.
4. **Apply only after approval** — edit body; timestamped backup (e.g. `.backups/`); commit. Push only if user wants remote (`git@github.com:rohitas-git/ai-skills.git` or current origin).  
   **Done when:** file matches approved diff.
5. **Catalog structure?** — if learnings imply hub/flows/tombstone → hand off `/0-skill-manager` (and craft lean via `/0-skill-creator` + `/1-writing-great-skills` if body rewrites are large).

## Commands

| Invoke | Scope |
|--------|--------|
| `/1-session-skill-reflect <skill>` | One skill |
| `/1-session-skill-reflect` | Session-wide |
| status / git check | Last reflections + dirty tree (if user asks) |

## Report shape

Summary (HIGH/MED/LOW counts) · learnings · proposed diffs · impact on future runs.

## Hard rules

1. Never apply multi-file skill edits without approval.  
2. Explicit workflow overrides beat old skill defaults — update the conflicting line.  
3. Prefer prune + leading words over essay growth (`/1-writing-great-skills`).  
4. Reflect edits **bodies**; manager owns indexes/flows.

## Related

Parent: `/0-skill-manager`.
