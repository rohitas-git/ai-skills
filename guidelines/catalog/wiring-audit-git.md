# Git wiring audit evidence — 2026-09-11

Coverage: 13 skills reviewed in this batch. See wiring-audit.md for inventory and
remaining skills. This is a document/code review with local tooling checks, not a
claim that an actual PR was rebased, repaired, published, or merged.

## Sources inspected

Read the SKILL.md for 0-git, 1-pr-repair, 1-pr-review-and-repair, 1-stacked-pr-repair,
1-stacked-pr-review-and-repair, 1-atomic-git-commits, 1-resolving-merge-conflicts,
1-receive-review, 1-pr-summarizer, 1-github-cli, 1-github-pr-comment-intake,
1-pr-comment-drafter, and 1-git-changelog.

Read atomic-commit workflow discipline, historical vendor guide and summary helper;
review-reception full guide; GitHub/intake/changelog/summarizer provenance; summarizer
evals; conflict agent metadata; Git hub JSON/HTML and flows Domain 17. Read the shared
PR checkpoints while authoring. Verified actual primary/dual memberships for all 13.

GitHub's workflow-event reference establishes the head versus synthetic-merge revision
distinction. The shared checkpoints link that reference and require actual run/event/
checkout evidence before applying the distinction to a real PR check.

## Scenario walkthroughs

| Input / state | Defect or ambiguity addressed | Current instruction |
|---|---|---|
| Binary text diff routed by Git hub | Child absent from dispatch/next | Normalization is in dispatch, metadata, fork, HTML |
| PR repair calls a workspace/commit/conflict helper | Unrelated finish or implementation loop | Return to caller with state and evidence |
| Unrelated staged content during a conflict/commit | Stage-everything directive | Exact paths; preserve staged ownership; hold completion if unresolved |
| Tests rely on extra unstaged edits | Worktree green mistaken for valid commit | Verify staged candidate independently or regroup dependencies |
| Synthetic merge check has a different SHA | Different SHA always called stale | Establish head/base/checkout provenance; unknown stays unknown |
| User asks to assess feedback | Automatic implementation | Return validity, scope and evidence without edits |
| PR repair calls feedback helper | Recursive next-route risk | Resume caller, not another PR repair workflow |
| Many review threads and nested comments | Pagination unspecified | Exhaust surfaces, retain source IDs and report coverage gaps |
| Outdated unresolved comment | Location status can hide feedback | Retain for assessment |
| Literal backslash-n in quoted code | Blanket escape prohibition | Preserve code escapes; real paragraph breaks in prose |
| Comment creation times out | Blind retry can duplicate objects | Inspect uncertain result before retrying |
| Individual-comment request sent to summarizer | Old eval demanded a comment | Route to comment drafter |
| Read-only changelog/intake/prose | Workspace and next behavior unclear | No checkout setup; publication only when requested |

## Verification

- Five routing regression tests pass; catalog lint: 0 critical, 0 warnings, 61 info.
- All operative Markdown links in this batch resolve on disk. Historical vendor
  guide is explicitly non-operative, not an execution procedure.
- Commit-helper shell syntax passes; invalid mode exits 2 with usage before Git inspection.
- PR-summarizer eval JSON validated and expectations aligned with the current boundary.
- Hub JSON parsed by lint; HTML labels/forks compared with JSON and flows. No browser
  rendering or visual redesign is claimed.
- `git diff --check` passes. No commits, pushes, merges, runtime installs or host sync.

## Remaining scope

Text normalization still needs its individual audit. Worktrees and branch finishing
were subsequently reviewed in [the workspace batch](./wiring-audit-workspaces.md).
Other domains remain in the main ledger. Recheck reviewed routes during the final
catalog sweep after later shared-reference or graph changes.
