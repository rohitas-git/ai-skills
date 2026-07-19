---
name: 1-tdd
description: >
  Test-driven development (red → green at agreed seams). Use for features or bugs
  test-first, red-green-refactor phrasing, integration tests, or Prove-It bug
  reproduction. Ship pipeline after implement; before code-review. Sole TDD skill
  in this catalog (vendor test-driven-development is merged, not a peer).
disable-model-invocation: true
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
7. **Portfolio** — shape effort with [references/test-pyramid.md](./references/test-pyramid.md). UI runtime extras: [references/browser-and-runtime.md](./references/browser-and-runtime.md). Mocking: [mocking.md](./mocking.md). Vendor patterns pack: [references/testing-patterns-vendor.md](./references/testing-patterns-vendor.md). Full vendor TDD body: [references/vendor-tdd-full.md](./references/vendor-tdd-full.md).

## Rules of the loop

- **Red before green.** A test that passes on first run proves nothing about new behavior.
- **One slice at a time.** One seam, one test, one minimal implementation.
- **Vertical slices**, not horizontal “all tests then all code.”
- **Refactor is not the third mandatory step of every micro-cycle** — review owns structural cleanup (`/1-code-review`). Tiny renames after green are fine if tests stay green.

## Anti-patterns (always)

- **Implementation-coupled** — private methods, internal mocks, DB side-channels.
- **Tautological** — expected value recomputed the same way as production code.
- **Horizontal slicing** — bulk imagined tests before any implementation feedback.
- **Prove without fail** — “fix first, test later” or bug fix without a failing reproduction.

## Related

- **Parent hub:** `/0-implement` (Ship pipeline: implement → **tdd** → code-review)
- **Also soft:** Diagnose hub when debugging with tests
- **Next:** `/1-code-review`
- **Not a peer:** archive vendor `test-driven-development` (merged here only)
