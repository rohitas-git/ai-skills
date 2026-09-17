---
name: 2-thermo-nuclear-code-quality-review
description: >
  Extremely strict maintainability-only review for abstraction quality, giant files,
  spaghetti-condition growth, and code-judo restructuring. Use when: thermo-nuclear
  code quality review, thermonuclear review, deep code quality audit, or especially
  harsh maintainability review. Not for: full Spec/Standards closer (1-code-review),
  over-engineering-only delete pass (2-ponytail-review), or mid-build verify
  (2-verify-work). Hub: /1-code-review. Triggers: thermo-nuclear, thermonuclear,
  deep code quality audit, harsh maintainability.
disable-model-invocation: true
metadata:
  catalog:
    hub: 1-code-review
    role: cousin
    when:
      - "harsh maintainability-only review"
      - "thermo-nuclear / code-judo audit of a diff"
    not_when:
      - "full Spec/Standards closer → 1-code-review"
      - "delete-only over-engineering → 2-ponytail-review"
      - "mid-build verify → 2-verify-work"
    cousins: [1-code-review, 2-ponytail-review, 2-verify-work]
    triggers:
      - "thermo-nuclear"
      - "thermonuclear"
      - "thermo-nuclear-code-quality-review"
      - "deep code quality audit"
      - "harsh maintainability"
    requires_setup: false
---

# Thermo-Nuclear Code Quality Review

## Boundary

| Need | Skill |
|------|--------|
| Harsh maintainability-only / code-judo review | **this** |
| Multi-axis diff/PR closer (Spec + Standards + Maintainability) | `/1-code-review` |
| Over-engineering-only delete pass | `/2-ponytail-review` |
| Mid-build verify (diffs, builds, tests) | `/2-verify-work` |
| Which review mode? | `/0-review` (F-R1) |

**Not for:** ship closer (use `/1-code-review`). This skill runs **only** the Maintainability axis.

## Process

1. Pin the requested candidate using [the shared contract](../0-review/references/review-candidate.md), including task-owned uncommitted files when applicable. An empty committed diff is not an empty current-work review.
2. Load the Maintainability SSOT in **explicit thermo-nuclear mode** and run only that axis: [axis-maintainability.md](../1-code-review/references/axis-maintainability.md). Stay read-only and within the requested change.
3. Do **not** run Spec or Standards. If the user wanted those too, redirect to `/1-code-review`.
4. Report findings in that axis's priority order, with concrete structural impact and scoped remedies. Do not rubber-stamp “it works,” but do not invent defects or broaden the PR to satisfy the harsh label. Return to the caller without repairs or publication.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full ambition bar, review questions, remedies, approval bar | [axis-maintainability.md](../1-code-review/references/axis-maintainability.md) |

## Related

- **Parent sub-hub:** `/1-code-review` (this is a cousin; body SSOT is the Maintainability axis)
- **Domain hub:** `/0-review`
- **Cousins:** `/2-ponytail-review`, `/2-verify-work`
