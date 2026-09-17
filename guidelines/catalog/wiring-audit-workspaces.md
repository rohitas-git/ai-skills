# Workspace and plan-execution audit — 2026-09-11

Coverage: `1-git-worktrees`, `1-finish-branch`, `1-execute-plan`,
`1-subagent-implement`. These four skills are reviewed, with final cross-catalog
reconciliation still pending. This is semantic/document review and disposable
helper testing, not an actual application build, worktree lifecycle or DB run.

## Evidence inspected

Read each main skill and all its operative Markdown references. For subagent
execution, also read and exercised task-brief, review-package and sdd-workspace.
Checked source-adaptation notes, Ship/Git parent membership and dispatch, the
Ship F-SP fork, parent workflow JSON/HTML, and the corresponding flows sections.
Git command forms were checked against the official worktree documentation;
the Supabase configuration reference was consulted without operating a stack.

## Decisions and scenario walkthroughs

| Input/state | Previous failure mode | Current instruction/evidence |
|---|---|---|
| Already in another task's linked worktree | Blanket reuse or forbidden second workspace | Verify task/branch/ownership; select a separate non-nested checkout |
| PR workspace requested | New branch implicitly starts at current HEAD | Resolve explicit PR branch/head and registrations before creation |
| Host-managed detached checkout | Assumed automatic branch creation/cleanup | Preserve host lifecycle; record actual identity and ownership |
| Setup on a non-DB project | Service setup treated as universal | Only prepare dependencies and services needed by the task |
| Concurrent local DB work | Setup implicitly authorizes reset/apply | Explicit topology/ownership; migration work hands off within local-only policy |
| Existing local config | Blind file copy/overwrite | Preserve unrelated settings and keys; change only agreed local fields |
| Finish already chosen by user | Menu re-asked; detached merge option | Honor granted choice; detached mode only PR branch or keep |
| Plan resumed after interruption/rebase | Trust completion checkboxes or repeat everything | Reconcile current code, task dependencies and evidence before resuming |
| Tools support delegation but user chose direct execution | Automatic mode switch | F-SP honors selection; availability is not authority |
| Sequential worker finishes | Automatic commit and branch finishing | Bounded worker authority; review then return to caller |
| Dirty implementation submitted for review | Committed-range package drops uncommitted work | Helper refuses dirty checkout; manual package includes baseline/current diffs and task-owned new files |
| Multi-commit task | HEAD~1 omits earlier task commits | Recorded task boundary and all commits in supplied range |
| Reviewer cannot establish a requirement | Approval plus hidden cannot-verify caveat | Evidence gap remains a blocked criterion, not an approval |
| Generated artifact path reused | Existing brief/report/ignore file overwritten | Unique private outputs, no-clobber explicit outputs, preserved ignore rules |
| Helper run from skill directory | Reviews the catalog instead of the app | Absolute helper path, target-checkout working directory, repo identity in package |

The four workflows keep the requested scope: reviews may inspect dependencies to
establish a concrete risk, but do not authorize unrelated edits. Service operations,
commits, publication and cleanup retain their own authority boundaries.

## Verification

- `python3 scripts/test-routing.py`: **7 tests pass**, including actual membership
  for these four skills and all their Markdown links/slash handoffs.
- `python3 scripts/test-sdd-helpers.py`: **11 tests pass** in temporary Git repos:
  shell syntax for all three helpers; target repository and multi-commit coverage;
  dirty/staged rejection with files/index preserved; unique/private output;
  explicit-output no-clobber; invalid/nonancestor revisions; fenced task headings
  and section boundaries; missing/invalid task IDs; ignore-file preservation;
  symlink/tracked workspace refusal; actual artifact ignore exceptions.
- Generated route index reconciles **214 live skills**.
- Catalog lint: **0 critical, 0 warnings, 61 informational findings**.
- `git diff --check`: clean.
- Source diff/JSON/HTML text alignment checked; no rendered-browser verification,
  subagent benchmark, real worktree creation/removal or live Supabase check claimed.
- No catalog commit, push, merge, host sync or runtime install. Helper test commits
  exist only inside temporary fixture repositories.

## Remaining work

Continue with plan authoring, parallel-agent coordination and review specialists.
Other callers may still carry old always-TDD/automatic-finish phrasing; reconcile
those as their individual audits progress. Structural lint and these narrow tests
do not establish completion of the catalog-wide goal.
