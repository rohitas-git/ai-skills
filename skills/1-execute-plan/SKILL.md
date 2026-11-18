---
name: 1-execute-plan
description: >
  Execute a written implementation plan directly with review checkpoints, including in a new session.
  Load the plan, surface material concerns, execute tasks, and verify the resulting branch.
  Not for: creating the plan (1-write-plan) or parallelizing independent workstreams (1-parallel-agents).
  Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "execute an existing implementation plan with review checkpoints"
    not_when:
      - "no written plan exists → 1-write-plan"
      - "independent concurrent workstreams → 1-parallel-agents"
    next: [1-tdd, 1-code-review, 1-finish-branch]
    cousins: [1-write-plan, 1-subagent-implement, 1-parallel-agents, 1-git-worktrees]
    triggers:
      - "execute plan"
      - "run the plan"
      - "1-execute-plan"
      - "follow this implementation plan"
    requires_setup: false
---

# Execute plan (direct execution)

**Announce:** "Using `/1-execute-plan` to implement this plan."

## Boundary

| Need | Skill |
|------|--------|
| Run a written plan directly, including in a new session | **execute-plan** (this) |
| Run plan **same** session with subagents | `/1-subagent-implement` |
| Write the plan | `/1-write-plan` |
| Finish merge/PR/cleanup | `/1-finish-branch` |
| Isolated workspace | `/1-git-worktrees` |

## Process

1. Load the plan and known canonical project continuation record before broad discovery; reconcile completed tasks against current code and verification evidence before resuming. Raise material scope or dependency concerns before affected work.
2. Confirm repository, branch, and existing changes; use `/1-git-worktrees` for needed isolation, then resume this plan at the current task. Create todos; for each task: in progress → follow steps → verify → complete.
3. Use `/1-tdd` when the agreed plan has a known deterministic behavior and independent acceptance criteria; exploratory or probabilistic work needs a specification/prototype or evaluation rubric, not an assumed TDD loop.
4. When all tasks are verified, review the scoped diff through `/1-code-review`; handle findings within the plan's scope. Use `/1-finish-branch` when integration or PR options are requested, carrying the verified SHA and workspace ownership.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full steps | [references/full-guide.md](./references/full-guide.md) |

## Related

- Ship soft under `/0-implement` · **F-SP** with `/1-subagent-implement`
- Upstream: `archive/vendor/superpowers` (`executing-plans`)

For multi-step execution, maintain the [project checkpoint lifecycle](../0-implement/references/project-continuity.md)
at verified units, decisions, blockers and safe pause/finish boundaries; a plan or read-only request grants no extra effects.
