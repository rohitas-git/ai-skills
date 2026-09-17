---
name: 1-subagent-implement
description: >
  Execute an implementation plan in the current session by dispatching a fresh
  implementer subagent per task, reviewing after each, then whole-branch review. Use
  when delegated sequential plan execution is requested and subagents are available.
  Not for: concurrent workstreams (1-parallel-agents) or writing plans (1-write-plan).
  Triggers: subagent implement, SDD, /1-subagent-implement. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "requested delegated execution of a ready plan with sequential implementer subagents and review checkpoints"
    not_when:
      - "no implementation plan exists → 1-write-plan"
      - "tasks are independent and can run concurrently → 1-parallel-agents"
    next: [1-code-review]
    cousins: [1-write-plan, 1-execute-plan, 1-parallel-agents, 1-git-worktrees, 1-finish-branch]
    triggers:
      - "subagent implement"
      - "SDD"
      - "sequential task agents"
      - "1-subagent-implement"
      - "implement with subagents"
    requires_setup: false
---

# Subagent implement (same session)

Execute a plan by **one fresh implementer subagent per task**, task review after each, then a broad branch review.

## Boundary

| Need | Skill |
|------|--------|
| Same-session plan via subagents | **subagent-implement** (this) |
| Direct plan execution, including a new session | `/1-execute-plan` |
| Independent multi-domain investigations | `/1-parallel-agents` |
| Worktree isolation | `/1-git-worktrees` |
| Multi-axis closer | `/1-code-review` |
| Finish branch | `/1-finish-branch` |

## Process

1. Ensure workspace isolation (`/1-git-worktrees` if needed).
2. Inspect the worktree first; preserve user-dirty files and keep shared contracts, migrations, generated files, lockfiles, and global configuration serial.
3. Load plan; reconcile any progress record with current code and evidence, then establish task order and one explicit file-ownership brief per worker. One worker writes to one checkout at a time, including the controller.
4. For each task: dispatch implementer → task review (spec + quality) → fix loop if needed.
5. After all tasks: verify integration in dependency order, then review the complete requested diff through `/1-code-review`, including task-owned uncommitted changes. A worker report or committed-range package alone is not proof of the current candidate.
6. Return evidence and workspace ownership to the caller. Use **`/1-finish-branch`** only for requested integration or PR options, not automatically after every plan.

## Hard rules

- Delegate bounded tasks with satisfied dependencies. Keep shared state and coupled work serial; tool availability alone does not authorize a switch to delegation.
- A task brief names allowed files, protected files, acceptance criteria, and verification.
- The controller integrates and performs final review; a worker report is not proof of completion.
- Workers have no implicit commit, push, rebase, merge or cleanup authority. Read-only task reviews must not race an active writer.

Source adaptation: [subagent-driven-development](./references/subagent-driven-development-source.md).

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full SDD flow + workspace layout | [references/full-guide.md](./references/full-guide.md) |
| Implementer subagent prompt | [references/implementer-prompt.md](./references/implementer-prompt.md) |
| Task reviewer prompt | [references/task-reviewer-prompt.md](./references/task-reviewer-prompt.md) |

## Related

- Ship soft under `/0-implement` · **F-SP**
- Upstream: `archive/vendor/superpowers` (`subagent-driven-development`)
