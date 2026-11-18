# Feature and refactoring recipes

## Feature

Trace the affected subsystem and current contracts. Before logic whose shape is unsettled, name the
data/state model and compare interfaces with `/1-codebase-design`; do not require an architecture
ceremony for every function call. Record blocking prerequisites, independent workstreams, shared
mutable resources and the smallest safe ownership split. One cohesive owner is often sufficient.

Delegate only when explicitly authorized. Give a producer actual allowed files, state ownership,
accepted data shape, success criteria and return evidence. Use `/1-competing-solutions` when several
complete alternatives need comparison, not merely because two implementations are imaginable.
Review the resulting diff and verify on the surface the requirement changes. An inconclusive or
wrong-surface check stays unverified. Return to the caller's review/closure steps; PR creation is not
an automatic end to every task.

## Behavior-preserving refactoring

Pin current intended behavior before structural edits: an existing contract test, recorded baseline,
characterization or equivalence harness. Typecheck and lint alone do not establish equivalence.
Keep a known existing defect separate from a structural change unless the user also authorizes its fix.

Name what the new shape improves: ownership, caller knowledge, duplicate policy, illegal states or
reader load. Change the smallest justified surface and keep the behavior pin green at each coherent
step. Reuse the compatibility/cutover owner when callers are independent. Check renames in serialized
data, prose and examples as well as language symbols. Do not delete a useful seam just to shrink lines.

Compare the real before/after artifact, then perform the relevant broader checks and review. A failed
experiment can be removed only from this task's owned changes; never reset unrelated dirty work.
Return changed structure, behavior pin, equivalence evidence, trade-offs and remaining gaps. Commits,
history reshaping, publication and merge remain conditional on the actual requested outcome.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
