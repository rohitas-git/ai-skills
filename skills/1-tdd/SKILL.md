---
name: 1-tdd
description: >
  Execute one test-driven red-to-green behavior slice at a settled seam with an
  independent oracle. Use when TDD/test-first is explicit or a Ship/Diagnose caller
  selects it for deterministic behavior. Not for exploratory, probabilistic, static,
  or underspecified work. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: pipeline
    when:
      - "execute one red-to-green behavior slice at a settled seam with an independent oracle"
      - "prove one deterministic bug or behavior with an intentionally failing test before implementation"
    not_when:
      - "exploratory prototype or unsettled interface → 1-prototype or 1-write-plan"
      - "probabilistic model, RAG, or variable output → 1-agent-evaluation"
      - "root cause is unknown or no valid red seam exists → 0-diagnosing-bugs"
      - "review an already-green candidate → 1-code-review"
    prev: [0-implement, 0-diagnosing-bugs, 1-execute-plan]
    next: [0-implement, 0-diagnosing-bugs, 1-execute-plan, 1-code-review]
    cousins: [2-verify-work, 1-agent-evaluation, 1-prototype, 1-write-plan, 1-playwright-browser-testing, 1-git-worktrees]
    triggers:
      - "1-tdd"
      - "use TDD for this behavior"
      - "write the failing test first"
      - "red-green this change"
      - "prove this bug with a failing test"
    requires_setup: false
---

# Test-driven development

**Atomic job:** complete one agreed behavior slice from discriminating red evidence to
minimal green implementation, then return the same candidate to its caller.

## Boundary

| Need | Route |
|---|---|
| One fitting deterministic red→green slice | **this skill** |
| Coordinate the implementation | caller, usually `/0-implement` or `/1-execute-plan` |
| Diagnose an unexplained failure | `/0-diagnosing-bugs` |
| Explore or settle behavior/interface | `/1-prototype` or `/1-write-plan` |
| Evaluate variable model/RAG behavior | `/1-agent-evaluation` |
| Durable browser scenario | `/1-playwright-browser-testing` |
| Review the resulting candidate | caller may use `/1-code-review` |

## Fit gate

Use TDD only when all are true:

- the behavior and public seam are settled enough to state before implementation;
- an external requirement, contract, confirmed bug, or independently derived expected
  result provides an oracle rather than the agent's first guess;
- the outcome is deterministic enough for a stable assertion;
- the caller grants test and implementation edits in the same bounded slice.

Do not force TDD for exploration, prototypes, static content/configuration, generated
artifacts, migrations whose primary proof is schema/data behavior, or probabilistic
systems. Specification, characterization, runtime evidence, migration verification, or
evaluation may fit better. If fit is ambiguous, use **F-TDD1** and return to the caller.
Token cost alone does not override a required quality contract, but the smallest fitting
test seam avoids mechanical red-green churn.

## Input and workspace contract

Inherit the caller's task/acceptance source, allowed behavior/files, exclusions, exact
repository/worktree path, branch/HEAD, dirty-path ownership, local-service ownership,
authority, and return route. Record the repository-native focused and broader commands,
test framework/config, fixture/state boundary, and the exact before candidate.

Use the caller's matching worktree; create none automatically. Route required isolation
through `/1-git-worktrees`, then resume here. A worktree does not isolate ports, databases,
queues, browsers, credentials, external services, or processes. Never let another writer
share this task's worktree or mutable test state, and never stash/reset/delete user work.

## Process

1. **Discover the seam and toolchain.** Read repository instructions, adjacent tests,
   source contracts, and native focused-test commands. Do not install or reconfigure tools
   merely to enter the loop.
2. **State the oracle and red prediction.** Name the behavior, input/preconditions,
   expected public outcome, evidence source, and why the proposed test would discriminate
   missing/wrong behavior from harness failure.
3. **RED.** Add the smallest authorized behavior test and run the exact focused command
   against the pinned before candidate. It must fail for the predicted behavioral reason,
   not compilation, setup, fixture, environment, or unrelated failure. Preserve output.
4. **GREEN.** Change only the authorized implementation and minimum compatibility surface.
   Re-run the same focused command. Do not weaken the assertion, broaden retries, mock away
   the path, or add speculative behavior to obtain green.
5. **Refine within the slice.** If useful, perform small behavior-preserving cleanup and
   rerun affected evidence. Structural redesign and unrelated refactoring return to the
   caller or review workflow.
6. **Verify proportionately.** Run adjacent/broader checks required by repository policy,
   changed risk, or caller acceptance—not a universal full suite after every micro-step.
   Record candidate identity and PASS/FAIL/BLOCKED/SKIPPED per command.
7. **Return.** Report the red and green candidates/output, changed paths, oracle provenance,
   behavior proven, coverage limits, state created/cleaned, and remaining risks to the
   exact caller. Do not commit, push, publish, deploy, merge, or start branch finishing.

## Hard rules

- If the test passes initially, errors for the wrong reason, or contradicts a stronger
  current contract, stop and reassess the seam/oracle. Do not manufacture red.
- Never delete or hide pre-existing/user-authored implementation to reenact strict TDD.
  Use an available before revision, characterization, or diagnose-first evidence instead.
- A test and implementation authored by the same agent from the same assumption are not
  independent validation. A separate agent also adds no independence when given the same
  unverified premise; ground the oracle and use review/verification where risk warrants.
- Test state must be task-owned and disposable. Cleanup only what this slice created.
  Real payments, messages, accounts, production data, or remote schema changes require
  separate explicit authority and ordinarily do not belong in this loop.

Focused guidance: [tests](./tests.md) · [mocking](./mocking.md) · [bug reproduction](./references/prove-it.md) · [test portfolio](./references/test-pyramid.md) · [browser/runtime](./references/browser-and-runtime.md) · [additional patterns](./references/writing-good-tests.md) · [behavior oracles](./references/behavioral-oracles.md). Upstream material is retained only as [historical source snapshots](./references/source-snapshots.md).
