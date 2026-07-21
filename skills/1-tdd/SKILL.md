---
name: 1-tdd
description: >
  Test-driven development (red → green at agreed seams). Use when features or bugs are
  test-first, red-green-refactor phrasing, or Prove-It bug reproduction. Not for: post-green multi-axis
  review (1-code-review), whole-ship orchestration (0-implement). Hub: /0-implement.
  Triggers: tdd, test-first, red green, prove it.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: pipeline
    when:
      - "red-green at agreed seams"
      - "test-first feature or bug"
      - "prove-it reproduction"
    not_when:
      - "multi-axis review after green → 1-code-review"
      - "no implementation context → 0-implement first"
    next: [1-code-review]
    prev: [0-implement]
    cousins: [2-verify-work]
    triggers:
      - "tdd"
      - "test-first"
      - "red green"
      - "prove it"
    requires_setup: false
---

# Test-Driven Development

**One skill.** Vendor pack `test-driven-development` is **not** a second peer — useful material is merged under `references/`.

TDD here is the **red → green** loop at **pre-agreed seams**. Deeper cleanup after green belongs to **`/1-code-review`**, not bulk “refactor as step 3 of every cycle.”

When exploring, read `CONTEXT.md` / ADRs so names match domain language.

## Process

1. **Confirm seams** with the user — public boundaries only. No test at an unconfirmed seam.
2. **Pick the slice**
   - New behavior → failing test first (red), then minimal code (green).
   - Bug → **Prove-It**: [references/prove-it.md](./references/prove-it.md) (failing reproduction before fix).
3. **Write the test** as a behavior spec (see [tests.md](./tests.md), [references/writing-good-tests.md](./references/writing-good-tests.md)).
4. **Green** — only enough implementation to pass. No speculative features.
5. **Suite** — full relevant suite; no skipped tests to “make CI green.”
6. **Closer** — Ship path continues to **`/1-code-review`** (maintainability/refactor pressure lives there).
7. **Portfolio** — shape effort with [references/test-pyramid.md](./references/test-pyramid.md). UI runtime extras: [references/browser-and-runtime.md](./references/browser-and-runtime.md). Mocking: [mocking.md](./mocking.md). Vendor patterns pack: [references/testing-patterns-vendor.md](./references/testing-patterns-vendor.md). Full vendor TDD body: [references/vendor-tdd-full.md](./references/vendor-tdd-full.md). Superpowers TDD harvest: [references/superpowers-tdd-full.md](./references/superpowers-tdd-full.md) · anti-patterns: [references/superpowers/testing-anti-patterns.md](./references/superpowers/testing-anti-patterns.md).

## Rules of the loop

- **Red before green.** A test that passes on first run proves nothing about new behavior.
- **One slice at a time.** One seam, one test, one minimal implementation.
- **Vertical slices**, not horizontal “all tests then all code.”
- **Refactor is not the third mandatory step of every micro-cycle** — 0-review owns structural cleanup (`/1-code-review`). Tiny renames after green are fine if tests stay green.

## Anti-patterns (always)

- **Implementation-coupled** — private methods, internal mocks, DB side-channels.
- **Tautological** — expected value recomputed the same way as production code.
- **Horizontal slicing** — bulk imagined tests before any implementation feedback.
- **Prove without fail** — “fix first, test later” or bug fix without a failing reproduction.

## Related

- **Parent hub:** `/0-implement` (Ship pipeline: 0-implement → **tdd** → 1-code-review)
- **Also soft:** Diagnose hub when debugging with tests
- **Next:** `/1-code-review`
- **Not a peer:** archive vendor `test-driven-development` (merged here only)
