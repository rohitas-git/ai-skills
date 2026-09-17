# Chesterton's Fence and simplification patterns

Operative evidence prompts for the read-only diff review. They do not authorize deletion or repair.

## Chesterton's Fence

Before proposing removal, establish why the code exists from the changed unit, callers, tests/contracts,
repository patterns, and history/decision evidence as needed. If its purpose remains unknown, record an
uncertain candidate or omit it; do not present removal as a finding.

## Pattern → simplify

| Smell | Prefer |
|-------|--------|
| One-implementation interface | Inline only if it carries no contract/test seam/policy |
| Config nobody sets | Remove or hardcode only after checking deployed/runtime use |
| Wrapper with no policy | Call through when no ownership, compatibility, or observability boundary is lost |
| Hand-rolled utility | Prefer a fitting stdlib/platform feature with equivalent edge-case behavior |
| Premature generality | Defer until a second demonstrated variation exists |

These are hypotheses. The main skill requires candidate-specific evidence, behavior equivalence, risks,
and verification; line reduction is an optional estimate, not the goal.
