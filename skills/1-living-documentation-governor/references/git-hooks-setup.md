# Optional Git-hook integration

Hooks are not the default adoption path. Prefer a tracked checker runnable directly and in CI; add a
local hook only when the user/team explicitly requests it after evaluating developer friction.

## Worktree hazards

Linked Git worktrees may share the common Git directory, hook configuration, and `core.hooksPath`.
Installing or replacing a hook from one worktree can affect other branches and users of the clone.
Before proposing installation inspect:

- `git rev-parse --git-dir` and `--git-common-dir`;
- existing `core.hooksPath` and hook contents;
- repository hook manager/package convention;
- whether the checker is safe in every linked worktree and dirty state.

Never overwrite `.git/hooks/pre-commit`, change `core.hooksPath`, or make a script executable as a
side effect of a docs assessment/update. Hook installation is a separate explicit Git/setup action.

## Safer shape

- Keep the checker and tests tracked in the repository.
- If a hook is adopted, make it a tiny wrapper that invokes the tracked checker from the current
  worktree root; do not embed a second implementation.
- Preserve existing hooks by using the repository's configured composition mechanism.
- Fail with actionable obligations and no automatic edits.
- Do not fetch/switch branches, install dependencies, mutate docs, or use a hidden skip.

## Verification and rollback

Test normal repository and linked-worktree invocation, paths with spaces, absent dependencies,
committed/staged/unstaged/untracked candidates, and existing-hook composition. Document how to remove
only the added integration without deleting unrelated hooks. CI remains the authoritative team-wide
enforcement surface when configured.
