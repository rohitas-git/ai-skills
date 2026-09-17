---
name: 1-atomic-git-commits
description: >
  Partition a worktree into small, independently understandable and revertible groups, then create one verified commit per group.
  Use when: commit changes, split a large change into atomic commits, stage coherent groups, or clean up mixed work before committing.
  Not for: isolated workspaces (1-git-worktrees), conflict resolution (1-resolving-merge-conflicts),
  or branch merge/PR/cleanup choices (1-finish-branch). Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: pipeline
    when:
      - "partition changed files or hunks into independently meaningful commits"
      - "stage, verify, and commit each atomic group"
    not_when:
      - "create an isolated workspace → 1-git-worktrees"
      - "resolve merge or rebase conflicts → 1-resolving-merge-conflicts"
      - "finish, merge, or clean a branch → 1-finish-branch"
    prev: [0-implement]
    next: [1-finish-branch]
    cousins: [1-git-worktrees, 1-resolving-merge-conflicts, 1-finish-branch]
    triggers: ["atomic commits", "commit in groups", "split changes into commits", "split a large change into small commits", "commit these changes"]
    requires_setup: false
---

# Atomic Git Commits

Create the smallest sequence of independently understandable, valid commits that represents the work.

## Boundary

| Need | Skill |
|------|-------|
| Group, stage, verify, and commit current changes | **atomic-git-commits** |
| Create an isolated worktree | `/1-git-worktrees` |
| Resolve merge/rebase conflicts | `/1-resolving-merge-conflicts` |
| Merge, open a PR, retain, or clean the branch | `/1-finish-branch` |
| Draft PR prose | `/1-pr-summarizer` |

If the request matches a cousin, ask **F-G1** through `/0-git`; do not silently perform that workflow here.

## Atomicity standard

A proposed commit needs **one purpose, one reason to revert, and one verification story**.
Every staged file and hunk must be necessary for that same purpose. The commit should be
understandable and safely revertible without relying on an unrelated later commit. A commit
that is technically revertible but too large to review is not atomic enough.

## Process

1. **Inspect safely.** Confirm repository/worktree and branch, then read status, staged diff, unstaged diff, and untracked filenames. Preserve unrelated user changes, including their staged state. If another operation is in progress, return to its controller or `/1-resolving-merge-conflicts`; do not create an ordinary commit inside an unresolved rebase/merge.
2. **Check authority.** Never commit directly to `main` or `master` without explicit permission. Never push without explicit permission. Never force-push. Never bypass hooks unless specifically asked.
3. **Inventory intent and ownership.** Map each changed file and mixed-file hunk to the user-visible behavior, defect, refactor, migration, generated artifact, documentation contract, or cleanup that caused it. Leave changes with unknown ownership uncommitted.
4. **Design small groups.** Apply [the atomic grouping guide](./references/atomic-grouping.md). Keep implementation with only the tests, types, schema, and documentation needed to make that behavior valid. Separate independent behavior, preparatory refactors, formatting, dependency upgrades, migrations/backfills, generated churn, and cleanup.
5. **Apply the size-pressure gate.** If a proposed group contains more than roughly 300 manually authored changed lines or eight substantive files, default to splitting it. Keep a larger group only when splitting would create invalid intermediate history, and record the exact inseparability reason. Smaller groups can still be non-atomic. Never use a later squash as the plan for an oversized or mixed commit.
6. **Resolve ambiguity.** For mixed-purpose files, uncertain dependencies, or unclear ownership, use **F-G2** before staging. Prefer leaving one ambiguous part uncommitted over hiding it in a plausible group.
7. **Stage explicitly.** Use `git add <specific-file>` for whole-file groups or interactive/patch staging for mixed files. Never use `git add .` or `git add -A`. Existing unrelated staged content is not part of the requested group: do not include or unstage it without resolving ownership and preservation first.
8. **Verify atomicity and validity.** Inspect `git diff --cached`, `git diff --cached --stat`, and the staged file list. Reapply the purpose, revert, dependency, verification, and review-size tests from the grouping guide. Check for secrets, debug residue, accidental files, and incomplete dependencies. Run relevant repository-required checks against the staged candidate; unstaged dependencies invalidate that proof.
9. **Commit once.** Use `<type>(<optional-scope>): <imperative summary>`, at most 72 characters, with a body only when it adds why, impact, or an exceptional inseparability reason. Do not use `--no-verify`.
10. **Repeat from fresh state.** Re-read status and diffs after every commit. Re-plan the remainder; never assume the original groups are still correct.
11. **Report evidence.** Return hashes/messages, each commit's purpose and size, tested candidate, verification, any justified large-group exception, and deliberately uncommitted changes. `/1-finish-branch` applies only when branch-outcome work is requested; a commit helper called during PR repair returns to that repair loop.

## Fork

| Fork | When | Question | Recommended | Branches |
|------|------|----------|-------------|----------|
| **F-G2** | grouping is materially ambiguous | How should mixed changes be grouped? | by independently revertible behavior | proposed atomic groups · user-specified grouping · leave ambiguous changes uncommitted · **Agent judgment** |

## Progressive disclosure

| Load when | File |
|-----------|------|
| Designing or challenging commit groups | [references/atomic-grouping.md](./references/atomic-grouping.md) |
| Inspecting staged/untracked changes | [scripts/get-git-changes.sh](./scripts/get-git-changes.sh) |
| Broader Git workflow discipline | [references/workflow-discipline.md](./references/workflow-discipline.md) |
| Historical provenance only; not an operational procedure | [references/vendor-git-workflow-full.md](./references/vendor-git-workflow-full.md) |
