---
name: 0-implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

**Build path:** drive `/1-tdd` (red → green slices at agreed seams), then multi-axis `/1-code-review` (Spec + Standards + Maintainability — every applicable axis), then commit. See 0-butler `flows.md` main flow.


Implement the work described by the user in the spec or tickets.

Multi-file work: cut **vertical slices** first — [references/incremental-slices.md](./references/incremental-slices.md) (merged from vendor incremental-implementation).

Standing finish bar (AC + DoD): [references/definition-of-done.md](./references/definition-of-done.md) · full [definition-of-done-vendor-full.md](./references/definition-of-done-vendor-full.md). Spec/code conflict or incomplete requirements: [references/confusion-and-inline-plan.md](./references/confusion-and-inline-plan.md). Full incremental body: [references/vendor-incremental-full.md](./references/vendor-incremental-full.md). Multi-agent patterns: [references/orchestration-patterns.md](./references/orchestration-patterns.md).

Use /1-tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, use /1-code-review to review the work.

Commit your work to the current branch (atomic save-points: `/1-git-commit-helper` + its workflow-discipline ref).
