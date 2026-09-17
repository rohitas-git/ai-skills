# Diagnosis guide

Use this guide only after the main skill has pinned scope, workspace, environment,
authority, and the reported symptom.

## Choose the evidence loop

| Failure shape | Useful first loop | Specialist |
|---|---|---|
| Focused unit/integration/build failure | repository-native exact command | remain here |
| User-interface state needs interactive inspection | one read-only browser session | `/1-browser-testing-with-devtools` |
| Browser behavior needs a durable check | one focused Playwright scenario | `/1-playwright-browser-testing` |
| Quantified latency/resource regression | controlled before/after experiment | `/1-performance-optimization` |
| Several demonstrably independent failures | separate read-only investigations | `/1-parallel-agents`, only when delegation was requested |
| Live service impact requiring containment | incident workflow | `/1-incident-response` |

A good loop is discriminating, repeatable enough for the claim, appropriately fast,
and safe for the target. No universal duration, iteration count, or reproduction rate
fits every failure. Record why the chosen sample or repetition is sufficient.

## Reproduction and observation

Reproduction is strongest when it exercises the reported path under matching conditions.
Before calling a loop red, distinguish:

- the reported defect from setup/toolchain failure;
- product failure from stale or incorrect test expectation;
- current worktree state from published PR/CI state;
- head-build, merge-build, and base/policy evidence;
- deterministic failure from timing, order, load, data, or environment dependence.

When direct reproduction is unsafe or unavailable, use existing logs, traces, dumps,
screenshots, metrics, or user steps. Pin time range, revision, environment, and source.
State what the artifact can and cannot prove. Do not fabricate certainty from absence.

## Localize the causal boundary

Trace the failing value, event, or state backward through actual callers and boundaries.
At each relevant boundary record expected input/output and observed input/output. Prefer
narrow inspection over logging everything. Compare with a genuinely analogous working
path only after confirming the important preconditions match.

Minimize by changing or removing one condition at a time and re-running the loop. Stop
when further reduction changes the failure or violates realism. A tiny reproduction is
useful only if it preserves the causal pattern.

## Hypothesis ledger

| Hypothesis | Evidence for | Prediction/probe | Result | Disposition |
|---|---|---|---|---|
| Candidate cause | observations | one falsifying check | measured result | supported / weakened / ruled out / unknown |

Rank by evidence and information gain, not novelty. Use read-only probes first. A
temporary code/config change is an experiment only when authorized, isolated, reversible,
and attributable to one variable. Revert only task-created probes; preserve user work.

If successive probes fail, revisit premises, candidate identity, and system boundaries.
There is no magic number that proves the architecture is wrong. Escalate an architectural
finding when evidence shows the present seams or coupling prevent safe localization,
not merely because several attempts failed.

## Fix and verification handoff

Diagnosis-only output stops at the supported causal chain. An authorized repair handoff
must include:

- exact allowed behavior/files and excluded scope;
- repository/worktree/branch/HEAD and dirty-state ownership;
- failing command/scenario and raw evidence location;
- causal chain, confidence, alternatives, and remaining unknowns;
- proposed minimal correction and risks;
- verification that could falsify success.

Choose regression evidence at the seam that actually represents the bug. Do not force
test-first work during exploration, add a shallow test for appearance, or let an agent's
own test suite serve as the sole independent oracle. After an authorized fix, verify the
focused seam and original scenario; broader checks follow repository policy and risk.

## Temporary instrumentation

Tag task-created probes uniquely, minimize captured fields, and avoid secrets, tokens,
credentials, health data, or full request/response bodies. Record each probe's path or
runtime location. Remove it only after ownership and the final diff are verified. Durable
telemetry proposals route to `/1-observability-and-instrumentation` and hosted changes
require separate authority.

## Return states

- `supported`: one causal chain best explains the evidence and survived falsification.
- `inconclusive`: evidence narrows the space but does not support a unique cause.
- `blocked`: a named missing prerequisite prevents a meaningful probe.
- `not reproduced`: the pinned scenario did not show the report; include limits and the
  next evidence needed.

Never translate `not reproduced`, a passing nearby test, or a clean log into “no bug.”
