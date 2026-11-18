# Sustained measured improvement

Use for an explicitly requested sustained optimization objective. A single controlled optimization
remains the normal workflow. Pin realistic workload dimensions and reproduce the complaint before
freezing a metric. Agree direction, target, guard conditions, budget and stop predicate. Do not invent
a minimum iteration floor or keep spending after the user's success/stop condition is satisfied.

Build or reuse a repeatable measurement command and prove it separates a known slower/wrong control
from the intended workload. Have it report error and actual-work counts. Capture a stable baseline
and correctness gate, then freeze workload, metric and measurement version. A necessary harness
correction is a new experiment with disclosed baseline invalidation, not a hidden route to a win.

Order hypotheses by avoiding unnecessary work, reusing its result, doing less, deferring appropriately,
moving work off a critical path, parallelizing safely and finally making it cheaper. Keep real user
latency, accessibility, freshness, failure semantics and resource limits intact; hidden deferred work
still needs accounting. Stop at the first adequate solution for a one-off optimization.

For each iteration, state a mechanism, change one causal variable when feasible, remeasure with the
frozen protocol and run the regression gate. Keep a change only when evidence and accepted trade-offs
justify it. Remove only the owned rejected experiment, preserving unrelated edits. Log attempts,
including no improvement, regressions and inconclusive outcomes, using the canonical decision trail.

Parallel hypotheses need explicit delegation and separate mutable state. Commit/push only within the
caller grant. At a plateau revisit categories and the premise rather than stacking near-misses or
relaxing correctness. Return the target, baseline/final evidence, kept/rejected attempts, uncertainty,
trail and next plausible experiment. A null result is valid evidence.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
