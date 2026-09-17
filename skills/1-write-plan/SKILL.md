---
name: 1-write-plan
description: >
  Write a bite-sized implementation plan from an approved design/spec before coding.
  Map files, dependencies, acceptance checks, and conditional execution. Use after design or when multi-step work
  needs a plan. Not for: resolving unknown requirements (0-grilling) or executing an existing plan
  (1-execute-plan). Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "write an implementation plan from an approved design or specification"
    not_when:
      - "requirements or design are unresolved → 0-grilling"
      - "written plan is ready to execute → 1-execute-plan"
    next: [1-execute-plan, 1-subagent-implement]
    cousins: [0-grilling, 1-execute-plan, 1-subagent-implement, 1-parallel-agents, 1-prototype, 1-git-worktrees]
    triggers:
      - "write plan"
      - "implementation plan"
      - "1-write-plan"
      - "plan this implementation"
      - "break implementation into steps"
    requires_setup: false
---

# Write plan

Give an implementer enough grounded context to execute small, verifiable tasks. Planning alone does not authorize execution.

## Boundary

| Need | Skill |
|------|--------|
| Implementation plan from design/spec | **write-plan** (this) |
| Product/spec artifact | `/1-to-spec` |
| Ticket breakdown | `/1-to-tickets` |
| Requested sequential delegated execution | `/1-subagent-implement` |
| Direct execution, current or new session | `/1-execute-plan` |
| Workspace isolation when execution needs it | `/1-git-worktrees` |

## Process

1. Read the approved design/spec and relevant source; identify actual unresolved decisions instead of restarting design by default.
2. Map requirements, exclusions, real files, task dependencies and shared contracts. Record the source revision and workspace/service needs without creating a worktree just to plan.
3. Decompose into verifiable deliverables with suitable acceptance checks; use TDD only for known deterministic behavior, not every task. Future-state operations get discovery and authority gates.
4. Self-review coverage and consistency. Save at the requested/project plan location (fallback: `docs/superpowers/plans/YYYY-MM-DD-<feature>.md`), preserving existing artifacts; report-only requests receive the plan in chat.
5. Return the plan and unresolved gates to the caller. Only if execution is requested, honor its chosen mode or offer **F-SP**: direct `/1-execute-plan`, delegated sequential `/1-subagent-implement`, or **Agent judgment**. Do not automatically start workers or commit the plan.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full guide | [references/full-guide.md](./references/full-guide.md) |
| Plan document reviewer prompt | [references/plan-document-reviewer-prompt.md](./references/plan-document-reviewer-prompt.md) |

## Related

- Ship soft under `/0-implement`
- Upstream: `archive/vendor/superpowers` (`writing-plans`)
