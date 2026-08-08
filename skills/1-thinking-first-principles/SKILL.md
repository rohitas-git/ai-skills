---
name: 1-thinking-first-principles
description: >
  When a constraint is treated as fixed, separate physics from convention, keep only independently supported primitives, and rebuild the simplest solution that satisfies real constraints.
  Use when: When a constraint is treated as fixed, separate physics from convention, keep only independently supported primitives, and rebuild the simplest solution that satisfies real constraints.
  Not for: architecture deepen (0-improve-codebase-architecture).
  Hub: /0-thinking. Triggers: thinking first principles, first-principles.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "When a constraint is treated as fixed, separate physics from convention, keep only independently supported primitives…"
    not_when:
      - "architecture deepen → 0-improve-codebase-architecture"
      - "The constraint is verified physics, hard regulation, or measured capacity → accept it a…"
      - "A proven standard library, protocol, or known-good pattern already fits → use it; do no…"
      - "Time-critical incidents → act on the most likely cause first; reserve first-principles …"
    cousins:
      - "0-improve-codebase-architecture"
    triggers:
      - "1-thinking-first-principles"
      - "thinking first principles"
      - "first principles"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-first-principles
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# First Principles

Strip assumed constraints to independently supported primitives, then rebuild. Escape analogy when convention fails or looks artificially expensive.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| First Principles (this) | **1-thinking-first-principles** (this) |
| architecture deepen | `/0-improve-codebase-architecture` |
| House routing (which domain) | `/0-butler` |

## When to Use

- A constraint is treated as fixed ("too expensive," "impossible," "always done this way") without independent support.
- Convention or analogy has failed, stalled, or only yields weak incremental variants.
- Greenfield design where industry defaults may smuggle false requirements.
- Cost or feasibility claims rest on pricing, precedent, or authority rather than physics, math, or measured need.

## When NOT to Use

- The constraint is verified physics, hard regulation, or measured capacity → accept it and optimize within it.
- A proven standard library, protocol, or known-good pattern already fits → use it; do not re-derive.
- Time-critical incidents → act on the most likely cause first; reserve first-principles rebuild for post-incident redesign.
- Incremental polish of a working system with no false-constraint signal → skip.

## Process

1. **State the problem and claimed constraints.** List every limit treated as fixed (cost, scale, stack, process, "must use X").
2. **Classify each constraint.** Tag as `physics/math`, `regulation/contract`, `measured fact`, or `convention/analogy/authority`. Keep only the first three as binding unless evidence upgrades a convention.
3. **Decompose to primitives.** Required inputs, conservation/complexity bounds, true non-negotiables. Demand independent support (measurement, derivation, primary requirement)—not vendor pricing or competitor precedent.
4. **Discard unsupported assumptions.** For each convention tag, state a falsifier. Drop or renegotiate anything lacking support.
5. **Rebuild from remaining primitives only.** Simplest solution that satisfies binding constraints and ignores artificial ones. Prefer commodity inputs and fewer moving parts over analogy.
6. **Validate and stop.** Check against real physics, contracts, and measured needs. Define the cheapest kill test. Stop when a coherent rebuild plus discriminating validation exists, or when only verified hard constraints remain.

## Output

Emit a first-principles rebuild:

- `claimed_constraints`: list with classification tags
- `primitives`: independently supported truths only
- `discarded_assumptions`: conventions dropped and why
- `rebuild`: solution derived only from primitives
- `binding_residuals`: real limits that remain
- `kill_test`: cheapest check that would falsify the rebuild

## Verification

- **Independence check:** every primitive must cite measurement, derivation, or primary requirement—not precedent alone.
- **No smuggled analogy:** if the rebuild still depends on "how others do it" without a primitive, strip it.
- **Constraint honesty:** verified physics/regulation must remain; do not wish them away.
- **Over-application guard:** if a standard solution is already optimal under verified constraints, do not rebuild for novelty.
- **Stop:** one decompose → classify → rebuild → kill-test pass; do not recurse without new evidence.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-first-principles/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
