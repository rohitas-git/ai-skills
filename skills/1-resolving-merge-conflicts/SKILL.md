---
name: 1-resolving-merge-conflicts
description: >
  Resolve an in-progress Git merge or rebase conflict while preserving the intent of both sides.
  Use when: conflict markers or an active merge/rebase blocks progress. Not for: grouping ordinary
  changes into commits (1-atomic-git-commits) or choosing how to finish a green branch (1-finish-branch). Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: leaf
    when:
      - "you need to resolve an in-progress git merge/rebase conflict"
    triggers:
      - "1-resolving-merge-conflicts"
      - "resolving merge conflicts"
      - "merge conflict"
      - "rebase conflict"
      - "conflict markers"
    not_when:
      - "group ordinary changes into commits → 1-atomic-git-commits"
      - "finish a green branch → 1-finish-branch"
    next: [1-pr-repair, 1-pr-review-and-repair, 1-stacked-pr-repair, 1-stacked-pr-review-and-repair, 0-implement]
    cousins: [1-atomic-git-commits, 1-finish-branch]
    requires_setup: false
---

# Resolve Merge Conflicts

## Boundary

| Need | Skill |
|------|-------|
| Resolve an active merge or rebase conflict | **resolving-merge-conflicts** |
| Group and commit ordinary changes | `/1-atomic-git-commits` |
| Choose the completed branch outcome | `/1-finish-branch` |

## Process

1. **Pin the operation.** Record repository/worktree, branch, sequencer state, base/head commits, requesting workflow, and its granted authority. Resolve the conflict in the checkout where the operation is active; do not create another worktree or switch branches mid-operation. If no operation is active, return that finding rather than starting a merge or rebase.
2. **Preserve existing work.** Record unmerged paths and the pre-existing staged/unstaged state. Never stage unrelated files or use a broad stash. An unrelated pre-staged change must not enter a merge commit; pause completion until its ownership and preservation are resolved.
3. **Recover intent.** Read both source commits and the relevant contract/spec. For generated files, resolve source inputs first and use the repository's generator. Applied-migration conflicts require a forward-compatible decision through `/1-supabase-schema-migration`; never edit an applied migration to make the conflict disappear.
4. **Resolve and verify.** Preserve both intents within the caller's scope. When intent is incompatible or unsupported, report the exact decision needed. Stage only explicitly resolved paths/hunks, inspect the staged diff and remaining unmerged paths, and run checks affected by the resolution. Fix only attributable breakage.
5. **Continue the existing operation.** Use its operation-specific continuation when authorized; a rebase continuation is not a request to create a separate ordinary commit. Preserve hooks. Do not skip commits or abort without authority; if the user requests an abort, verify its effects on local work first.
6. **Return to the caller.** Report resolved paths, remaining conflicts, final SHA/sequencer state, checks, and preserved unrelated work. Resume the PR/stack/build step that requested resolution. If invoked alone, finish with this report; no automatic push, new review, branch finishing, or extra commit workflow.


## Related

Parent hub: `/0-git`; recovery returns to its requesting workflow. Listed `next` routes are possible callers, not a sequence.
