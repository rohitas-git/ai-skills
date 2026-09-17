# Axis: Spec and correctness

Evaluate the requested change against its authoritative requirements and observable
contracts. Follow the parent review's pinned candidate, read-only authority and scope.

## Inputs

Prefer the user's current request/corrections and supplied specification. Then
resolve relevant issue/PR context or project contracts. Do not substitute an old
commit message or test expectation for a newer explicit requirement. If a tracker
cannot be read, use supplied evidence and report the missing coverage; do not
configure a tracker or start setup just to inspect a supplied diff.

If product requirements are absent, report that limit. Still inspect the changed
logic, edge cases, failure handling and test/source contracts for demonstrable
correctness regressions. Label this contract-baseline review rather than claiming
complete product-spec compliance.

## Pass

1. Map each known requirement to changed or preserved behavior and relevant tests.
2. Check missing/partial behavior, misunderstood rules and excluded scope added
   by the change. For unchanged behavior, establish how the PR affects it.
3. Trace relevant boundary inputs, error paths, state transitions and side effects.
   A passing test that merely restates implementation assumptions is not enough.
4. Resolve contradictions among user intent, source, unit and integration/E2E tests
   before concluding that either code or a test is wrong.
5. Return evidence-backed findings and unverified criteria. Quote only the short
   requirement needed, cite its source and code location, and state the scenario.

Do not judge personal style here or repair findings during review. A missing spec
does not justify inventing acceptance criteria or calling the axis fully passed.
