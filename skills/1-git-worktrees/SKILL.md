---
name: 1-git-worktrees
description: >
  Ensure feature work runs in an isolated workspace: detect existing isolation, prefer
  platform native worktree tools, fall back to git worktree, and select safe local-service isolation.
  Use before plan execution, long feature branches, or concurrent local Supabase work. Not for: grouping
  commits (1-atomic-git-commits), a Supabase product integration (1-supabase), or finishing a branch
  (1-finish-branch). Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: pipeline
    when:
      - "create or verify an isolated workspace before feature work"
      - "run concurrent worktrees with separate local Supabase stacks"
    triggers:
      - "worktree"
      - "isolated workspace"
      - "parallel local Supabase"
      - "multiple worktrees"
      - "create a worktree"
      - "separate local services per worktree"
      - "1-git-worktrees"
    not_when:
      - "group or create commits → 1-atomic-git-commits"
      - "Supabase product integration → 1-supabase"
      - "finish a branch → 1-finish-branch"
    next: [0-implement, 1-execute-plan, 1-subagent-implement, 1-pr-repair, 1-pr-review-and-repair]
    cousins: [1-atomic-git-commits, 1-resolving-merge-conflicts, 1-finish-branch, 1-supabase, 1-stacked-pr-repair, 1-stacked-pr-review-and-repair]
    requires_setup: false
---

# Git worktrees

**Core:** detect existing isolation first → native tools → `git worktree` fallback → give stateful local services an explicit isolation decision. Never fight the harness.

## Boundary

| Need | Skill |
|------|--------|
| Isolated workspace for feature/plan work | **git-worktrees** (this) |
| Supabase product integration or diagnosis | `/1-supabase` |
| Atomic commit groups | `/1-atomic-git-commits` |
| Merge conflicts | `/1-resolving-merge-conflicts` |
| Finish branch after green | `/1-finish-branch` |

## Process

1. Record the requesting workflow, task, repository, branch, dirty paths, and current directory. Inspect registered worktrees and any superproject; a submodule alone does not establish task isolation. Do not nest worktrees.
2. Reuse an existing workspace only when its branch and ownership match this task. An unrelated linked worktree is not automatically suitable. Preserve host-managed and detached workspaces.
3. Otherwise create isolation via an available platform-native tool or `git worktree`, respecting the existing user preference. Resolve the intended start branch/SHA and inspect existing branch registrations first; never move a branch already checked out elsewhere. Follow the full guide for directory and permission handling.
4. Project setup in the new workspace. For local stateful services, choose shared versus isolated state before starting anything:
   - Share a local Supabase stack only when the worktrees use compatible schema and test data. Do not reset, seed, or locally apply migrations from one branch while another relies on it.
   - For migration, schema, seed, or DB-dependent work in parallel, use one local Supabase stack per worktree. Each needs a distinct `project_id`, every host-exposed port, app-server port, and app environment pointing to that stack.
   - Keep worktree-specific configuration out of commits. Prefer an existing repository-approved untracked override or launcher. `--workdir` / `SUPABASE_WORKDIR` switches the entire Supabase project directory, so do not treat it as a config-only overlay when migrations or functions must remain from the worktree.
5. Verify only the services the task needs. For local Supabase, inspect status privately, configure the worktree's untracked environment without printing keys, and check app/Auth URLs and ports. Never run linked, remote, repair, or production Supabase commands; CI owns migration application after merge. Non-Supabase projects skip this branch.
6. Return to the requesting workflow at its paused step with path, branch/SHA, baseline result, service ownership, and preserved dirty paths. `next` lists possible callers, not a sequence to run. If invoked alone, report readiness and the next task. Cleanup belongs to `/1-finish-branch` when authorized; directory name alone is not proof of ownership.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full detect/create steps | [references/full-guide.md](./references/full-guide.md) |
| Local-only inventory before a workspace decision | [worktree audit](../../guidelines/catalog/pstack-tooling.md#local-worktree-audit), using `scripts/worktree-audit.py` |
| Concurrent local Supabase stacks | [references/concurrent-local-services.md](./references/concurrent-local-services.md) |

## Related

- Git pipeline under `/0-git`; on-ramp from Ship before `/1-execute-plan` / `/1-subagent-implement`
- Upstream: `archive/vendor/superpowers` (`using-git-worktrees`)
