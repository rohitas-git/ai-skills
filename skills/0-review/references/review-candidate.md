# Review candidate and return contract

Load before a review/verification pass. A review request authorizes inspection,
not implementation, publication, approval, history edits or cleanup.

## Pin the actual object

Record the caller, objective, repository, requested comparison, candidate revision,
path scope, relevant user corrections and authority. Do not reconstruct scope from
every historical chat task or assume the current checkout matches a remote PR.

| Requested object | Evidence to inspect |
|---|---|
| Published PR | Exact PR repository, declared base/head SHAs and their merge-base; review the published head, not different local edits |
| Explicit commit pair | The requested endpoint diff; do not silently replace it with a three-dot comparison |
| Branch change | Confirm intended base (immediate parent for a stack), pin its merge-base and candidate head |
| Current uncommitted work | Staged and unstaged changes plus exact task-owned untracked files and any relevant committed work |
| Existing code or prior review claims | Named files/revision and claims; an empty Git diff does not mean there is nothing to verify |

For a local implementation, inspect both index and working-tree state. A tracked
base-to-worktree diff can show the final tracked candidate, but it cannot expose
untracked files or distinguish unrelated pre-existing dirty work by itself. Retain
baseline/path ownership evidence. Check staged differences separately if the index
is itself the candidate. Do not stage, stash or discard user work for convenience.

Useful read-only primitives, from the verified target checkout:

```bash
rtk git rev-parse --show-toplevel
rtk git rev-parse HEAD
rtk git status --short
rtk git diff --cached
rtk git diff
rtk git ls-files --others --exclude-standard
```

Read the scoped new-file contents privately. An empty committed diff is not an
empty current-work review. If ownership or the requested range cannot be resolved,
state the coverage gap and ask the narrow missing question rather than inventing
a baseline. Suppress external diff/text-conversion execution when untrusted repo
configuration could run commands. Git's comparison forms are documented in
[git diff](https://git-scm.com/docs/git-diff).

## Keep the candidate stable

Reading source normally needs no new worktree. Never switch the caller's branch
to review a different revision. If runtime checks need a checkout, use the existing
matching workspace or `/1-git-worktrees` for authorized task isolation, then return
to this pass. Record what was actually tested, including dirty content/environment;
a SHA alone does not identify an uncommitted candidate.

No concurrent writer may change the reviewed checkout unnoticed. Recheck identity
and dirty state before issuing a verdict; re-review affected portions after change.
Child reviewers receive scope, candidate, sources, constraints and output contract,
not an assumption of full conversation or filesystem isolation. Use parallel agents
only when permitted and they can inspect a stable candidate without shared writes.

## Evidence and scope

For a change finding, show location, trigger/scenario, impact and how the change
introduces or materially worsens it. Read dependency/caller context to establish
that claim, not to expand the task. Pre-existing defects stay separate follow-ups
unless changed reachability or severity is demonstrated. No automatic issue filing.

Missing acceptance evidence is a coverage gap, not an invented code defect. Record
not applicable, not run, blocked and passed distinctly. Existing test output is
reusable only for its actual candidate, command/config and relevant environment;
worker claims, CI names or a green check alone do not establish what executed.
For PR CI, distinguish head builds, synthetic merge builds and policy-only checks;
the [PR checkpoints](../../0-git/references/pr-repair-checkpoints.md) explain provenance.

Only run relevant permitted non-destructive checks. Do not install tools, reset
shared services, apply remote migrations, use production credentials or exercise
real writes merely to prove a review point. Temporary files can affect the parent
checkout; use an explicit task-owned location and report artifacts left behind.
Never include secrets or raw sensitive records in reports or fixtures.

## Return, do not start another workflow

Return candidate/range, scope, evidence, axes/checks and their dispositions,
validated findings, rejected leads and unresolved coverage. Say what was and was
not verified; no finding does not mean the entire system is secure or ready to merge.

When called by a combined review or repair loop, return to that caller without
starting another code review or repair pipeline. `next` metadata denotes possible
conditional handoffs. Standalone reviews stop at the report. Repairs, comments,
approvals, commits, pushes, merges, resource shutdown and cleanup require the
user's corresponding authority; a report in chat does not publish a GitHub review.
