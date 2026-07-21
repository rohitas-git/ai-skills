---
name: 1-execute-plan
description: >
  Execute a written implementation plan in a separate session with review checkpoints.
  Load plan, raise concerns, run tasks, then finish the branch. Prefer
  /1-subagent-implement when subagents are available in-session. Triggers: execute plan,
  run the plan, /1-execute-plan. Use when: Execute a written implementation plan in a
  separate session with review checkpoints. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "Execute a written implementation plan in a separate session with review checkpoints"
    triggers:
      - "execute plan"
      - "run the plan"
      - "1-execute-plan"
    requires_setup: false
---

# Execute plan (separate session)

**Announce:** "Using `/1-execute-plan` to implement this plan."

## Boundary

| Need | Skill |
|------|--------|
| Run plan in a **new** session | **execute-plan** (this) |
| Run plan **same** session with subagents | `/1-subagent-implement` |
| Write the plan | `/1-write-plan` |
| Finish merge/PR/cleanup | `/1-finish-branch` |
| Isolated workspace | `/1-git-worktrees` |

## Process

1. Load plan file; review critically; raise concerns before coding.
2. Create todos; for each task: in progress → follow steps → verify → complete.
3. Prefer TDD via `/1-tdd` where the plan calls for it.
4. When all tasks verified → **`/1-finish-branch`**.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full steps | [references/full-guide.md](./references/full-guide.md) |

## Related

- Ship soft under `/0-implement` · **F-SP** with `/1-subagent-implement`
- Upstream: `archive/vendor/superpowers` (`executing-plans`)
