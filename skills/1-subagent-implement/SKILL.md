---
name: 1-subagent-implement
description: >
  Execute an implementation plan in the current session by dispatching a fresh
  implementer subagent per task, reviewing after each, then whole-branch review. Use
  when the plan is ready and subagents are available. Triggers: subagent implement, SDD,
  parallel task agents, /1-subagent-implement. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "the plan is ready and subagents are available"
    triggers:
      - "subagent implement"
      - "SDD"
      - "parallel task agents"
      - "1-subagent-implement"
    requires_setup: false
---

# Subagent implement (same session)

Execute a plan by **one fresh implementer subagent per task**, task review after each, then a broad branch review.

## Boundary

| Need | Skill |
|------|--------|
| Same-session plan via subagents | **subagent-implement** (this) |
| Separate-session plan run | `/1-execute-plan` |
| Independent multi-domain investigations | `/1-parallel-agents` |
| Worktree isolation | `/1-git-worktrees` |
| Multi-axis closer | `/1-code-review` |
| Finish branch | `/1-finish-branch` |

## Process

1. Ensure workspace isolation (`/1-git-worktrees` if needed).
2. Load plan; create progress tracking.
3. For each task: dispatch implementer → task review (spec + quality) → fix loop if needed.
4. After all tasks: whole-branch review (e.g. `/1-code-review` or reviewer template in refs).
5. Complete with **`/1-finish-branch`**.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full SDD flow + workspace layout | [references/full-guide.md](./references/full-guide.md) |
| Implementer subagent prompt | [references/implementer-prompt.md](./references/implementer-prompt.md) |
| Task reviewer prompt | [references/task-reviewer-prompt.md](./references/task-reviewer-prompt.md) |

## Related

- Ship soft under `/0-implement` · **F-SP**
- Upstream: `archive/vendor/superpowers` (`subagent-driven-development`)
