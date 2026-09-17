# Workspace setup and caller return

Use with `/1-git-worktrees`. This is a setup helper, not permission to implement,
commit, publish, reset a database, or clean up another workspace.

## 1. Establish task identity

Record caller/task, repository root, current directory, branch or detached SHA,
index/working-tree changes, and any active merge/rebase/cherry-pick. Inspect:

```bash
rtk git rev-parse --show-toplevel
rtk git rev-parse --show-superproject-working-tree
rtk git worktree list --porcelain
rtk git status --short
```

Use canonical paths when comparing identities. A submodule's Git directory layout
does not establish task isolation; confirm its superproject and repository-specific
setup. An active sequencer belongs to its current checkout: resolve it through
`/1-resolving-merge-conflicts` when requested, not by switching or recreating it.

| Current state | Action |
|---|---|
| Task-matching linked workspace | Reuse; verify ownership and baseline |
| Unrelated linked workspace | Preserve it; choose a separate, non-nested workspace |
| Host-managed or detached workspace assigned to this task | Preserve host lifecycle and branch state; no automatic branch creation |
| Main checkout with unrelated changes | Preserve changes; isolate the requested work |
| Read-only advice without execution | No worktree needed; return to caller |

A worktree isolates checkout files and the index, not every external service or
shared repository operation. Do not concurrently move the same branch, run
conflicting Git history operations, or assume separate directories isolate a DB.

## 2. Resolve creation and location

Honor the user's requested worktree and existing project preference. Do not ask
again for an already authorized setup. If the task does not establish whether
isolation is wanted and the choice materially changes its workspace, ask once.
Declining isolation does not authorize editing a protected or unrelated checkout.

Prefer an available platform-native tool when its documented behavior fits the
task. Inspect its returned path, branch/SHA and ownership; do not assume that every
native tool creates a branch or automatically cleans up. If unsuitable or absent,
use Git's worktree mechanism within granted authority.

Resolve before creation:

- Intended repository, task branch and explicit starting commit. For PR work,
  use the verified PR head/branch; do not recreate it from the default branch.
- Branch registration: reuse its appropriate checkout rather than forcing the
  same branch into another worktree. Never use `-B` or `--force` to make setup pass.
- Destination: explicit preference, then the repository's established worktree
  directory, then a suitable proposed location. Do not place a new worktree inside
  the currently linked worktree or reuse an existing directory's contents.
- For a project-local destination, verify the exact selected path is ignored.
  If not, prefer an approved external location or narrow local exclude. A tracked
  ignore-file edit and a commit require their own task scope and authority.

For an authorized new branch, supply both branch and start explicitly:

```bash
rtk git worktree add -b "$task_branch" "$task_worktree_path" "$task_start_sha"
```

For an existing branch not checked out elsewhere:

```bash
rtk git worktree add "$task_worktree_path" "$task_branch"
```

These variables are resolved task inputs, not defaults. Verify the resulting
registration and SHA before editing. If permissions block creation, use the host's
approval mechanism; do not silently work in an unsuitable checkout instead.

## 3. Prepare only the required environment

Read the selected checkout's instructions, runtime pins and lockfiles. Install or
build only required components through its declared tooling and reproducible mode.
Do not install every ecosystem in a monorepo or change dependency versions merely
to prepare a workspace. Preserve existing local configuration and secrets; copying
an environment file from another branch can connect to the wrong service.

For Supabase, use [concurrent-local-services.md](./concurrent-local-services.md).
For other stateful dependencies, record the same ownership and endpoint distinction.
Do not start a service when the task only needs static inspection.

## 4. Verify and return

Run relevant baseline checks not already evidenced for this exact checkout and
environment. Distinguish passed, failed, blocked and not-run checks; preserve
pre-existing failures rather than quietly repairing unrelated code. Ask only if
an unresolved decision or missing authority prevents the task from proceeding.

Return to the caller's paused step, not to the first skill in a fixed pipeline:

- Canonical worktree path, repository, branch/detached SHA and start point.
- Reused versus created workspace; ownership and cleanup authority.
- Preserved dirty paths and active Git operation, if any.
- Baseline commands/results tied to the tested state.
- Needed local-service identity/endpoints and ownership, with no credentials.
- Remaining blockers or readiness limits.

Invoked alone, report readiness and stop. Workspace removal is a later,
authorized `/1-finish-branch` decision, never a side effect of returning.

## Reference

Command forms and shared/per-worktree state:
[Git worktree documentation](https://git-scm.com/docs/git-worktree).
