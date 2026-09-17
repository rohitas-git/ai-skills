# Code reviewer brief

Fill these inputs when delegating an authorized review:

- Caller and review scope: <task, exclusions, requested axes>.
- Requirements and applicable project rules: <sources>.
- Candidate: <repository/worktree, base/comparison, head and dirty-state evidence>.
- Evidence package: <all committed/staged/unstaged/new task files as applicable>.
- Verification: <available results, permitted checks and environment limits>.
- Output: <findings, axis verdicts, coverage gaps and evidence>.

Read [the shared candidate contract](../../../0-review/references/review-candidate.md).
Do not assume you inherited the conversation or an isolated filesystem.

Review the requested candidate only. Inspect callers/dependencies to validate a
concrete risk, not as an excuse for an unrelated audit. Remain read-only: no fixes,
staging, history movement, new worktrees, tool installs, publication or cleanup.
If a runtime check needs isolation or authority, report the need to the controller.

Check behavior, error paths, tests and the requested structure/standards axes.
Separate actual findings from missing inputs or unverified claims. Cite location,
trigger/scenario, impact, evidence and a scoped correction. Do not promise all edge
cases are covered or produce boilerplate praise unsupported by inspection.

Return axis statuses, findings and coverage limits. No findings is a bounded review
outcome, not merge approval. The controller owns scope adjudication and any
authorized repair; after a fix, review refreshed evidence rather than an old package.
