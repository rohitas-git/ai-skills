# Statechart projection and counterexamples

Name states and actions using the reader's vocabulary. Use flat, nested or parallel-region charts
only when they preserve the behavior relevant to the question. Keep the authoritative state/action
mapping alongside the diagram so visual simplification remains auditable.

- Preserve initial-state reachability, guards, terminal conditions and relevant outgoing transitions.
- A hidden step is still a model step. Explain what the chart omits and why.
- Do not merge states that violate different invariants without preserving which rule fails where.
- When one displayed state includes both passing and failing model states, mark the mixed result;
  do not label every represented state bad or claim all are safe.
- If a transition changes hidden data that determines a future result, label that distinction or
  split the state. A self-loop hidden by one label can carry the entire bug mechanism.
- Distinguish safety violation paths from temporal/liveness counterexamples that require a loop.
- Say when symmetry, view reduction, state/action constraints, depth limits or timeouts change
  coverage. A compact chart may omit reachable behavior even when its source model is valid.

For a supplied checker result, report each property separately: checked and satisfied within scope,
violated, unknown/uncompleted, or unavailable. Cite the exact tool result; absence of a red node
does not prove that every rule was checked. “Shortest path” requires evidence from the tool/protocol.

Tell a counterexample as initial state → action/guard → resulting state, with source locators.
If the implementation cannot take a modeled step, investigate model drift or an abstraction error
before declaring a product bug. A successful replay still proves only that scenario.

Use native Mermaid or existing project tooling. Do not auto-install Java, TLC, mise, Pele or a
renderer, and do not execute downloaded scripts or JavaScript view callbacks as part of drawing.

Modified from pstack statechart guidance, MIT.
[Source and review](../../../guidelines/catalog/ingest-pstack-2026-11-15.md).
