---
name: 1-git-worktrees
description: >
  Ensure feature work runs in an isolated workspace: detect existing isolation, prefer
  platform native worktree tools, fall back to git worktree. Use before plan execution
  or long feature branches. Triggers: worktree, isolated workspace, /1-git-worktrees. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "Ensure feature work runs in an isolated workspace: detect existing isolation, prefer platform native"
    triggers:
      - "worktree"
      - "isolated workspace"
      - "1-git-worktrees"
    requires_setup: false
---

# Git worktrees

**Core:** detect existing isolation first → native tools → `git worktree` fallback. Never fight the harness.

## Boundary

| Need | Skill |
|------|--------|
| Isolated workspace for feature/plan work | **git-worktrees** (this) |
| Commit messages | `/1-git-commit-helper` |
| Merge conflicts | `/1-resolving-merge-conflicts` |
| Finish branch after green | `/1-finish-branch` |

## Process

1. Detect existing worktree / submodule (do not nest worktrees).
2. If already isolated → report path/branch; continue project setup.
3. Else create isolation via platform native tool or `git worktree`.
4. Project setup in the new workspace; hand off to plan exec or implement.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full detect/create steps | [references/full-guide.md](./references/full-guide.md) |

## Related

- Ship soft under `/0-implement` (before `/1-execute-plan` / `/1-subagent-implement`)
- Upstream: `archive/vendor/superpowers` (`using-git-worktrees`)
