---
name: 0-implement
description: >
  Build driver for ticket/spec work. Use when implementing a slice from tickets or a written
  spec. Not for: inventing requirements (0-grilling / 1-to-spec), pure multi-axis review (1-code-review),
  incoming issue triage (0-triage). Hub: /0-implement. Triggers: implement, build this, ship tickets.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: hub
    when:
      - "implement from tickets or written spec"
      - "drive ship build path"
    not_when:
      - "unclear requirements → 0-grilling / 1-to-spec"
      - "review only → 1-code-review"
      - "raw issues → 0-triage"
    next: [1-tdd, 1-code-review]
    prev: [1-to-tickets, 1-to-spec]
    triggers:
      - "implement"
      - "build this"
      - "ship tickets"
    requires_setup: false
---
## Process

1. Follow this skill's procedure.


**Build path:** drive `/1-tdd` (red → green slices at agreed seams), then multi-axis `/1-code-review` (Spec + Standards + Maintainability — every applicable axis), then commit. See 0-butler `flows.md` main flow.


Implement the work described by the user in the spec or tickets.

Multi-file work: cut **vertical slices** first — [references/incremental-slices.md](./references/incremental-slices.md) (merged from vendor incremental-implementation).

Standing finish bar (AC + DoD): [references/definition-of-done.md](./references/definition-of-done.md) · full [definition-of-done-vendor-full.md](./references/definition-of-done-vendor-full.md). Spec/code conflict or incomplete requirements: [references/confusion-and-inline-plan.md](./references/confusion-and-inline-plan.md). Full incremental body: [references/vendor-incremental-full.md](./references/vendor-incremental-full.md). Multi-agent patterns: [references/orchestration-patterns.md](./references/orchestration-patterns.md).

Use /1-tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, use /1-code-review to review the work.

Commit your work to the current branch (atomic save-points: `/1-git-commit-helper` + its workflow-discipline ref).
