# Behavior-test design

Use after the main skill's fit gate and oracle are established.

## A useful red test

A test should:

- exercise the public seam that represents the requested behavior;
- derive expected results from an external contract or independently confirmed example;
- fail on the pinned before candidate for the predicted behavioral reason;
- distinguish product behavior from harness, fixture, toolchain, or environment failure;
- own its setup/state and remain deterministic under the repository's execution model;
- survive behavior-preserving implementation changes.

One behavior may require several related assertions. Split only when separate failures
need separate meaning; “one assertion per test” is not a universal rule.

## Avoid false confidence

- Do not assert private methods, incidental call order, or internal SQL/DOM structure
  unless that structure is the explicit public contract.
- Do not recompute the expected result with the same algorithm as production.
- Do not broaden text/DOM matchers, snapshots, tolerances, timeouts, or retries just to
  obtain green.
- Do not infer edge cases. Cover those required by the contract, observed failure, risk,
  or established repository conventions.
- Do not confuse a passing mock with an exercised integration boundary.

Prefer state or externally observable outcome assertions. Interaction assertions are
appropriate when the interaction itself is contractual—for example, no message sent,
one idempotency key used, or a dependency not called after authorization fails.

## Red disposition

| Initial result | Meaning | Action |
|---|---|---|
| Expected behavioral failure | valid red evidence | proceed to the minimal implementation |
| Pass | behavior may already exist or test may not discriminate | inspect the seam/oracle; do not manufacture failure |
| Compile/setup/fixture failure | harness is red, not behavior | repair the harness within authority, then rerun |
| Different behavioral failure | nearby defect or wrong scenario | classify and return to caller/Diagnose |
| Flaky result | unstable evidence | isolate cause; retries are observations, not a pass |

Record the exact command, candidate, test identity, output, and disposition.
