# Extraction and drift

These commands are templates, not permission to execute. Substitute the pinned source, base, backup, and branch names. Honor repository command wrappers such as `rtk` when required. Do not run interactive hunk commands through a runner that cannot present and answer their prompts; prepare an exact reviewed patch instead.

## Fresh-branch extraction

Start in a clean, task-owned workspace. Confirm status and intended base before switching or restoring. A source backup must already exist and match the recorded SHA.

```bash
git switch -c split/prep <base-sha>
git restore --source backup/original-large-pr -- path/to/owned-file
git restore -p --source backup/original-large-pr -- path/to/mixed-file
git diff --stat <immediate-base>
git diff <immediate-base> -- path/to/owned-file path/to/mixed-file
```

Path restoration replaces that path in the working tree. Use it only when all source differences for the path belong in this PR and it cannot erase unrelated or already-reviewed parent changes. The source's `git checkout backup/original-large-pr -- path/to/file` alternative also stages the restored content; prefer worktree-only `restore`, then explicit staging after inspection. For a mixed file, inspect every selected hunk and resulting interactions; overlapping parent edits may require a manually reconstructed patch.

A stacked child starts from its immediate parent tip; an independent PR starts from the pinned shared base. Do not start parallel branches from the combined source. Build and verify each candidate before using it as another PR's parent. If the split cannot be independently verified, revise review units rather than hide dependencies.

## Restacking after feedback

Before an authorized rebase, record each dependent branch, old parent tip, old child tip, target parent tip, and order. The old parent boundary is essential: without it, a rebase can replay already-replaced parent commits. For a simple linear child:

```bash
git rebase --onto <new-parent-tip> <old-parent-tip> <child-branch>
git range-diff <old-parent-tip>..<old-child-tip> <new-parent-tip>..<new-child-tip>
```

Do not apply this template blindly to merge-heavy histories. Inspect topology and use the repository's established stack tool where appropriate. Preserve commits by default; dropping, squashing, skipping, or otherwise discarding work needs explicit scope and authority. Stop and inspect if the graph differs from the recorded plan. Resolve conflicts toward the reviewed direction while retaining descendant intent; record the reason for every intentional change and re-run affected checks.

Use range-diff to identify changed, dropped, added, or reordered patches after rebases and conflict resolution. Summarize meaningful results and verification for reviewers when a stack is updated. A force-push itself supplies no old range: save pre-rewrite SHAs before rewriting. If a remote update is authorized, re-check its expected SHA and use a specifically scoped force-with-lease for a rewritten branch; never bare force. An unexpected remote change requires inspection before proceeding.

## Compare intent, not only bytes

For a linear stack, compare its tip tree with the backup and compare both against their recorded base. For parallel PRs, use the per-unit ledger; no single branch represents the combined result. If needed, construct a disposable integration candidate without modifying the original or approved branches, and record its merge order and checks. Base updates and review feedback can explain legitimate differences.

Classify each original review unit as extracted (branch plus commit/file/hunk evidence), still remaining, superseded by review (decision plus replacement), or explicitly deferred/excluded (reason and authority). Completion requires an evidence-backed disposition for every unit and verification of every split candidate; tree equality alone cannot establish it.
