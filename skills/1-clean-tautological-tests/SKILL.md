---
name: 1-clean-tautological-tests
description: >
  Audits, flags, and rewrites tautological, echo, and zero-signal unit tests into behavioral tests.
  Use when reviewing test suites, cleaning up AI-generated tests, improving mutation scores, or auditing
  test quality. Not for writing a new red-green slice (1-tdd) or reviewing a whole change (1-code-review).
  Hub: /0-review.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-review
    role: leaf
    when:
      - "audit a test suite for tautological, echo, mock-only, or zero-assertion tests"
      - "rewrite AI-generated or low-signal tests into behavioral tests with a mutation check"
    not_when:
      - "write the failing test first for a new behavior → 1-tdd"
      - "multi-axis review of a change or PR → 1-code-review"
      - "mid-build verification of a change → 2-verify-work"
    prev: [0-review, 1-code-review]
    next: [1-code-review, 1-tdd]
    cousins: [1-tdd, 2-verify-work]
    triggers:
      - "1-clean-tautological-tests"
      - "clean up tautological tests"
      - "audit test quality"
      - "find zero-signal tests"
      - "rewrite echo tests"
    requires_setup: false
---

# Audit and Clean Tautological Unit Tests

## Objective
Identify and eliminate tests that pass by logical necessity or mirror production implementation without verifying independent, externally observable behavior.

## Audit Workflow

### Step 1: Scan and Classify
Inspect the target test files and flag any test exhibiting these anti-patterns:
1. **Zero-Signal Assertions:** Asserting hardcoded literals (`expect(true).toBe(true)`, `assert True`), identical references (`assert x == x`), or tests with zero assertions.
2. **Mirrored Implementation (Echo Tests):** Re-implementing production formulas, regexes, or helper logic inside the test to compute the `expected` value.
3. **Over-Mocking / Mock-Only Verification:** Mocking the system under test (SUT) or asserting solely on internal private method call counts rather than return values or state changes.
4. **Always-True Catch Blocks:** Wrapping assertions in `try/catch` blocks that pass silently if no exception is thrown without an explicit failure guard.

### Step 2: Rewrite Using Behavioral Rules
For every flagged test, rewrite it following strict Arrange-Act-Assert (AAA) structure:
- **Use Oracle Values:** Replace dynamically computed expected values with hardcoded, domain-verified input/output examples and boundary edge cases.
- **Test Observable Outcomes:** Assert on return values, thrown domain errors, emitted events, or persisted state, never internal implementation steps.
- **Unmock the SUT:** Only mock external I/O boundaries (network, database, clock, filesystem).

### Step 3: Mutation Verification Gate
Before finalizing any rewritten test:
1. Temporarily introduce a deliberate bug into the target production logic (e.g., flip a comparison operator, invert a boolean, or alter a return value) OR run the project's mutation runner if installed (`npx stryker run`, `mutmut run`, `cargo mutants`).
2. Run the rewritten test and confirm it **FAILS** against the broken logic.
3. Revert the temporary production mutation and re-run the test suite to confirm it **PASSES**.

## Output Format
When auditing a file or directory, provide:
- A brief summary table of flagged tests (`File:Line`, `Anti-Pattern`, `Action Taken: Rewritten | Deleted`).
- Clean, runnable replacement test code matching the repository's existing test runner and assertion conventions.
