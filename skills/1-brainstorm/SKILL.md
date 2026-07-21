---
name: 1-brainstorm
description: >
  Hard-gate design before implementation: explore context, ask one question at a time,
  propose approaches, present a design, get approval, write a design doc. Use for new
  features/components/behavior changes before coding. Triggers: brainstorm, design
  first, idea to design, /1-brainstorm. Use when: Hard-gate design before implementation:
  explore context, ask one question at a time, propose approac. Hub: /0-grilling.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-grilling
    role: on-ramp
    when:
      - "Hard-gate design before implementation: explore context, ask one question at a time, propose approac"
    triggers:
      - "brainstorm"
      - "design first"
      - "idea to design"
      - "1-brainstorm"
    requires_setup: false
---

# Brainstorm (idea → design)

**Hard gate:** do not implement, scaffold, or load ship skills until a design is presented and the user approves.

## Boundary

| Need | Skill |
|------|--------|
| Idea → approved design before code | **brainstorm** (this) |
| Relentless plan/requirements interview | `/0-grilling` · `/1-grill-me` · `/1-grill-with-docs` |
| Spec artifact for multi-session ship | `/1-to-spec` |
| Bite-sized implementation plan after design | `/1-write-plan` |

## Process

1. Explore project context (files, docs, recent commits).
2. Ask clarifying questions **one at a time** (purpose, constraints, success).
3. Propose 2–3 approaches with trade-offs + recommendation.
4. Present design in sections; get approval as you go.
5. Write design doc (default path: `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` or user preference).
6. Spec self-review (placeholders, contradictions, scope).
7. User reviews written spec → next: **`/1-write-plan`**.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full checklist + flow | [references/full-guide.md](./references/full-guide.md) |
| Visual companion (JIT browser UI) | [references/visual-companion.md](./references/visual-companion.md) |
| Spec self-review prompt | [references/spec-document-reviewer-prompt.md](./references/spec-document-reviewer-prompt.md) |

## Related

- Design hub: `/0-grilling` (soft / on-ramp; **F-B1** vs grill)
- After design: `/1-write-plan` → Ship
- Source harvest: `archive/vendor/superpowers` (upstream `brainstorming`)
