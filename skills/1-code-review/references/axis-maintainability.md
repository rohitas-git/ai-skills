# Axis: Maintainability

Assess how the requested change affects structure, comprehension and future change
cost. This is an inspection pass, never permission to refactor the checkout.
Follow the parent review's scope and candidate contract.

## Select the requested bar

- **Ordinary multi-axis review:** flag material structural regressions and
  explain their practical effect. Simpler alternatives may be nonblocking advice.
- **Explicit thermo-nuclear review:** use the demanding bar below and actively
  seek substantially simpler designs. A concrete missed simplification can be an
  Important finding when its benefit and bounded remedy are demonstrated. This
  mode does not expand the PR or override project policy.

## Inspect the changed design

Trace the changed behavior and its actual boundaries, then ask:

- Did the change add concepts, modes or indirection without a corresponding benefit?
- Is logic in the owning module, or scattered through unrelated/shared paths?
- Could an existing canonical helper serve the same contract without harmful
  coupling? Similar spelling does not establish behavioral equivalence.
- Do repeated conditionals obscure an invariant or state transition?
- Are wrappers, casts, optional values or generic machinery hiding a simple contract?
- Does an abstraction reduce what a reader must understand or just relocate it?
- Do related updates risk partial state; are dependencies/order explicit?
- Is sequential or parallel orchestration justified by real state dependencies?
- Does growth make a cohesive file materially harder to change or test?

A thousand-line file or a large diff is an inspection signal, not a universal
hard limit. Honor explicit repository limits when present. Focus on what the PR
adds or worsens rather than demanding cleanup of every pre-existing large file.

## Demanding structural pass

For explicit harsh review, look for a clear reframe that removes unnecessary
branches, layers, duplicated decisions or state. Do not stop at a rename when the
underlying ownership or model is demonstrably wrong. Show the before/after
concepts and how behavior would remain intact.

Prefer the smallest effective structural remedy: reuse a suitable helper, collapse
duplicate behavior, move logic to its owner, make an invariant explicit, or split
a genuinely incohesive unit. Extraction, a state machine, polymorphism and parallel
execution are options, not automatic improvements. Deletion is not proof of
simplicity when it loses a contract or useful isolation.

Require an evidence-backed explanation for a serious structural regression or
avoidable complexity. Do not turn a merely plausible redesign or personal taste
into a blocking requirement. If the proposed remedy would exceed PR scope,
describe a separate follow-up; do not make unrelated changes a condition of repair.

## Findings and verdict

Prioritize structural regressions, demonstrated substantial simplifications,
boundary/state problems, then local legibility. Each finding needs a location,
affected change scenario, expected maintenance/correctness consequence and focused
remedy. State when a concern is only a hypothesis.

A working implementation can still have a real maintainability defect. Conversely,
a nonempty diff need not produce findings. Return no findings when evidence
supports that outcome; do not inflate severity to meet the “harsh” label.
Keep requirements/standards findings in their own axes, and return to the caller
without performing repairs, opening issues or publishing approval.
