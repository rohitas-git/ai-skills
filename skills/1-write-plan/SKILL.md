---
name: 1-write-plan
description: >
  Write a bite-sized implementation plan from an approved design/spec before coding.
  Maps files, tasks, tests, and commit cadence. Use after design or when multi-step work
  needs a plan. Triggers: write plan, implementation plan, /1-write-plan. Use when: Write
  a bite-sized implementation plan from an approved design/spec before coding. Hub:
  /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "Write a bite-sized implementation plan from an approved design/spec before coding"
    triggers:
      - "write plan"
      - "implementation plan"
      - "1-write-plan"
    requires_setup: false
---

# Write plan

Assume the implementer has little codebase context. Produce a plan of small, testable tasks (DRY, YAGNI, TDD).

## Boundary

| Need | Skill |
|------|--------|
| Implementation plan from design/spec | **write-plan** (this) |
| Product/spec artifact | `/1-to-spec` |
| Ticket breakdown | `/1-to-tickets` |
| Same-session plan execution | `/1-subagent-implement` |
| Separate-session plan execution | `/1-execute-plan` |
| Isolated workspace first | `/1-git-worktrees` |

## Process

1. Confirm approved design/spec exists (else `/1-brainstorm` or `/1-to-spec`).
2. Map files to create/modify and responsibilities.
3. Decompose into bite-sized tasks (each with test cycle + review gate).
4. Save plan (default: `docs/superpowers/plans/YYYY-MM-DD-<feature>.md` or user preference).
5. Hand off via **F-SP**: same session → `/1-subagent-implement`; new session → `/1-execute-plan`.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full guide | [references/full-guide.md](./references/full-guide.md) |
| Plan document reviewer prompt | [references/plan-document-reviewer-prompt.md](./references/plan-document-reviewer-prompt.md) |

## Related

- Ship soft under `/0-implement`
- Upstream: `archive/vendor/superpowers` (`writing-plans`)
