# Context-sensitive craftsmanship principles

Use these as hypotheses about maintainability, not universal laws. Repository standards and
measured constraints decide implementation details.

## Cost of change

- Optimize for likely future changes, not hypothetical flexibility everywhere.
- Prefer clear names and cohesive responsibilities when they reduce caller knowledge and review
  effort. Function/class size and argument counts are signals, not thresholds.
- Leave nearby code better only when the cleanup is safe, in scope, and independently verifiable;
  do not smuggle a refactor into unrelated work.

## Dependencies and boundaries

- Keep stable policy from depending unnecessarily on volatile delivery/storage/framework details,
  but introduce an abstraction only for a real variation, ownership, privilege, process, testing,
  or change-cost boundary.
- Business rules can legitimately depend on database capabilities, latency, or external contracts.
  Isolate what needs to vary; do not pretend infrastructure is freely swappable.
- Start with the simplest deployable architecture that preserves required ownership and failure
  boundaries. A structured monolith is often appropriate; services add coordination and operations.

## Cohesion and SOLID

- **SRP:** group things that change for the same actors/reasons; split when independent changes
  repeatedly collide. “One reason” is evidence about change, not one tiny method per class.
- **OCP:** introduce extension points after credible variation exists. Editing clear local code can
  be cheaper than maintaining a speculative plugin system.
- **LSP:** a substitute preserves the caller-visible behavioral contract, including errors and
  performance assumptions that matter.
- **ISP:** consumers should not depend on capabilities they do not use, while too many micro-
  interfaces can increase navigation and wiring cost.
- **DIP:** place dependency direction to protect stable policy; an interface with one accidental
  implementation is not automatically useful.

## Tests, errors, and comments

- Choose tests from risk and oracle quality. TDD fits known deterministic behavior at an agreed
  seam; exploratory/probabilistic work may need a specification, prototype, evaluation, or
  characterization tests first. An agent-authored test is not independent proof of its own code.
- Treat failure behavior as part of the caller contract. Exceptions, tagged results, optionals, and
  error codes can each fit; use `/1-error-handling` for the detailed choice.
- Prefer code that communicates intent, but preserve comments explaining constraints, safety,
  non-obvious trade-offs, public contracts, or why an apparently simpler approach is wrong.

## Decision questions

1. Which expected change becomes cheaper, and for whom?
2. What new concept, abstraction, deployment, or test maintenance cost is introduced?
3. What evidence shows the current design is causing harm?
4. Can a smaller reversible step test the hypothesis?
5. Which performance, legacy, prototype, or team constraint would justify bending the principle?
