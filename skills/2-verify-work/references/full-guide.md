# Verification procedure

Verify whether the scoped work satisfies the current request. Inspection and
relevant non-destructive checks are the job; implementation, repair, monitoring
and external publication are not implicit next steps.

## 1. Establish the contract

Read the [candidate contract](../../0-review/references/review-candidate.md).
Record the active request and corrections, caller, exclusions, target repository
or artifact, exact candidate and available evidence. A supplied focus narrows the
verdict, not the evidence needed to substantiate it.

Do not automatically complete an adjacent coding task before verifying it. An
implementation caller chooses its checkpoint; a standalone request checks the
state that exists now. Do not revive unrelated historical requests or infer
permission to perform an operation merely because its completion is being checked.

Use the real requested start point for committed changes, plus staged, unstaged
and task-owned new files for a current-work candidate. Do not substitute HEAD~1
or the last three commits for the task boundary. For a review of unchanged code,
inspect the cited source and claims even when the diff is empty.

## 2. Build the evidence checklist

For each deliverable or claim, identify what could prove or contradict it:

| Kind | Relevant evidence |
|---|---|
| Behavior or regression | Actual contract, source/callers, focused execution and meaningful assertions |
| Build/type/lint status | Completed matching command, configuration, candidate and exit result |
| Review finding | Cited code, reachable scenario, impact and attempted counterexample |
| PR/CI or submitted job | Read-only source-system identity and status, tied to the actual revision/run |
| Document or explanation | Requested content and authoritative source material |
| Requested operation | Observable result, not merely code that could perform it |

Distinguish observed actions, reported claims, inferred effects and unknown state.
A successful tool call is not proof that every requested outcome occurred.
A green test suite is not proof of criteria it does not exercise.

## 3. Inspect and check

Read relevant source, artifacts and applicable repository instructions. Look for
missing requirements, demonstrated defects, scope drift and weak test oracles.
Stay within scope; unchanged context establishes causality, not permission for
a full audit. Verify a prior review's claims rather than automatically repeating
every possible code/security review.

Choose checks proportional to the requested claim and risk. Full-suite/build
checks are required where the project or task requires them; do not run a whole
application build to validate a prose-only correction without a relevant reason.
Read command outcomes, failures and skipped coverage, not just exit status.

Existing evidence can be reused when the exact candidate, command/configuration
and relevant environment match; otherwise rerun affected checks. Distinguish a
test failure, an unrelated baseline failure, and a check that never started.
Do not blame the PR without causal evidence, or call a broken environment passing.

Verification does not authorize installs, production access, remote database
commands, shared-service resets, destructive tests or real external writes.
If a check needs those, report the precise limit. For runtime isolation, request
or reuse an appropriate task workspace through the caller; do not move its HEAD.
Subagents share files unless actual isolation has been established.

Additional probes must be permitted, non-destructive and scoped. Use a private
task-owned temporary location for scratch checks; no application/test edits,
stashes or fix/revert cycles in the caller's checkout. Do not remove unrelated
artifacts. Report any task-created artifacts left behind.

## 4. Optional independent verifier

Use a documented host delegation API only when permitted. Local serial
verification remains valid. Supply this brief explicitly; do not assume inherited
chat, a particular model, available credentials or a private filesystem:

- Active request, corrections, exclusions and caller.
- Candidate/repository/artifact identity and relevant dirty-state ownership.
- Exact evidence sources and claims to verify.
- Allowed checks, protected resources and environmental constraints.
- Read-only authority and the report format below.

Ask the verifier to seek counterevidence before accepting claims. Treat its report
as evidence to inspect, not unquestioned proof. No concurrent writer may silently
change the candidate while verification is running.

## 5. Return the verdict

Recheck candidate identity and relevant dirty state. If it changed, refresh
affected evidence or report the verdict as incomplete.

Return:
- Scope, caller, candidate and source identities.
- Requirement/claim → evidence → disposition.
- Commands actually run or reused, their outcomes, and skipped/blocked checks.
- Confirmed issues with location/scenario/impact; separate unrelated failures,
  optional suggestions, rejected leads and missing evidence.
- Mutation state and any scratch artifacts.

Use one verdict:
- **PASS:** every in-scope required claim is supported by applicable evidence.
- **FAIL:** evidence contradicts at least one required criterion; retain unknown
  items separately rather than hiding them behind the failure.
- **BLOCKED:** no contradiction established, but missing evidence or access
  prevents a complete verdict. This is a report status, not a goal-state update.

Return to the caller. Verification-only stops here; do not fix until green or
launch a new review/finish pipeline. An authorized implementation/repair caller
decides fixes, then requests verification on the new candidate.
