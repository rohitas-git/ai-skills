# Formal-check drift contract

Use for a fixed check after covered code changes. A stale model can keep passing while the code's
behavior has moved. A commit timestamp alone does not establish correspondence.

1. Identify the last evidenced source/model correspondence, covered files/symbols, properties,
   assumptions, bounds and toolchain. If no sync revision is recorded, a last-edited commit is only
   an investigation starting point, not proof that the model was synchronized then.
2. Inspect relevant changes, including moves, split functions and new writers of guarded state.
   Classify no semantic effect, model/harness drift, intended contract change, or possible product bug.
   Include task-owned dirty changes; HEAD alone may not describe the delivered candidate.
3. A changed test or commit message is evidence of intent, not automatic approval to change a
   required property. Reconcile with the accepted contract and decision owner. Report conflicts.
4. Return needed model/proof/harness changes to their author/caller; this check does not rewrite
   the model or product. Authorized state-model updates can use `/1-statechart-modeling`.
5. On the revised candidate, check correspondence, seeded violations and a clean control again.
   Replay feasible counterexamples only within execution authority. Preserve an existing real
   failure rather than requiring a fabricated clean baseline.
6. Record outcomes separately: correspondence established/unknown; drift found/reconciled; property
   satisfied/violated/unknown/unavailable. A check can have reconciled drift and still reveal a bug.
   Advance a sync record only when its owner authorizes the update and the evidence supports it.

Explain the bounds and omitted code. Do not silently lower a bound, remove a property, rewrite a
model to fit the desired verdict, install a tool or commit a verification change during assessment.

Modified from pstack create/maintain-formal-verification guidance, MIT.
[Source and review](../../../guidelines/catalog/ingest-pstack-2026-11-15.md).
