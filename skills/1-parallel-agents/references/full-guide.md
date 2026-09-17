# Bounded parallel coordination

Use only when parallel work is requested or permitted by the active task policy,
and two or more concrete workstreams can run independently alongside useful work.
If the next step depends on one result, keep that critical step local or sequence
the dependency. Different failing files do not prove independent root causes.

## 1. Establish the task graph

Record the caller, objective, acceptance criteria, scope exclusions, available
tools/concurrency, and consequential actions requiring approval. Define each task
by its output, inputs, dependencies, one owner, write targets and verification.

Check for hidden shared state: checkout/index/branch, fixtures, generated files,
lockfiles, running app, database/schema, ports, external accounts and rate limits.
Resolve shared contracts before independent implementation. Keep tightly coupled
work serial through the caller or `/1-subagent-implement` when requested.

| Work | Workspace contract |
|---|---|
| Read-only investigations of a stable revision | May share a checkout; no simultaneous writer and no mutating tests |
| Independent code writers | Separate task-matching worktrees via `/1-git-worktrees`; explicit file ownership and base revisions |
| Tests that mutate DB/files/services | Separate task-owned state or serialized execution |
| Shared contract, migration order, lockfile or history operation | One owner, serialized integration |
| No repository involved | No Git/worktree ceremony; isolate only actual shared resources |

Separate branches in one checkout are not isolation. Worktrees still share some
Git state and do not isolate external services; the controller coordinates history
operations and local-service ownership. If safe isolation is unavailable, keep
workers read-only or serialize the edits rather than silently sharing writers.

## 2. Brief each worker

Supply enough context to answer the task without the whole conversation:

- Task ID, precise question/deliverable and explicit non-goals.
- Canonical repository/worktree, branch and pinned revision, or named source inputs.
- Dependencies already satisfied; relevant interfaces and binding requirements.
- Allowed/protected files and baseline dirty state.
- Read-only versus edit authority; no inherited right to commit, publish, deploy,
  alter permissions, reset data or delegate again.
- Needed runtime/service readiness and permitted checks.
- Output/evidence format, report destination and escalation conditions.

A “fix tests” brief must establish the intended behavior from current contracts;
do not bias a worker into weakening tests to get green. Reading needed callers
is permitted within the question; expanding implementation scope requires a
controller decision within the original user authority.

Use the host's documented delegation API. Inherit the current model unless the
user or applicable policy requests an available override. Do not promise numerical
cost/speed savings or invent a vendor-specific model tier.

## 3. Dispatch and track actual state

Dispatch only dependency-ready tasks, respecting actual concurrency limits.
Record live agent/tool handles and task status. Do not duplicate a pending task
merely because a wait returned no output. Poll the existing handle or inspect
authoritative terminal state before replacement. A progress file alone is not
evidence that a worker is still running.

If context is missing, the worker returns checked evidence, precise unknowns,
candidate paths/search terms and why they matter. Supply only relevant evidence;
do not broaden scope. Repeated no-progress attempts need changed inputs, a
smaller question or escalation, not identical redispatch.

If a task fails, mark dependent tasks blocked; independent tasks may continue.
If tasks prove coupled or edits conflict, stop affected writers, preserve every
version and reconcile through one owner. Inspect partial artifacts before recovery.
Cancellation must be verified before starting a replacement writer in its checkout;
do not remove its workspace while its process may still run.

## 4. Inspect handoffs and integrate

Require status (complete/partial/blocked/failed), result, cited evidence, changed
files/resources, exact checks and tested revision/environment, uncertainties and
outstanding decisions. A worker's “done” is not the controller's completion proof.

Compare findings against primary files/logs/tests; resolve disagreements through
evidence, not majority vote or model preference. Distinguish independently
confirmed results from worker reports. Recheck stale inputs and cross-task
assumptions before downstream work.

For code changes, the controller first reviews per-task scope and then integrates
in dependency order into the confirmed target checkout. Branch commits/cherry-picks
require granted authority; if workers returned uncommitted patches, account for
all tracked and untracked task changes. Never stage, stash or delete unrelated
work to simplify integration. Run the checks that prove the combined candidate,
including interactions not exercised by isolated tests.

## 5. Return to the actual caller

- Investigation/research: return synthesis, evidence, disagreements and limits;
  no forced code review, implementation or workspace creation.
- Implemented change: return the integrated candidate, verification, scope review
  through `/1-code-review`, and remaining findings to the requesting workflow.
- Every path: account for each dispatched task and any still-live handles, retained
  worktrees, services and artifacts. Stop only task-owned resources when authorized.

`next` lists possible conditional handoffs, not a mandatory sequence.
Publication, merging and worktree cleanup never follow implicitly from synthesis.
