---
name: 1-doubt-driven-development
description: >
  Fresh-context adversarial review of non-trivial decisions before they stand (CLAIM→EXTRACT→DOUBT→RECONCILE). Use when correctness stakes are high, unfamiliar code, or confident output is cheaper to verify now than debug later.
disable-model-invocation: true
---

# Doubt-Driven Development

Lean catalog skill. **Full vendor body:** [references/full-guide.md](./references/full-guide.md). Pointer only: [references/vendor-source.md](./references/vendor-source.md).

## Process

1. State the CLAIM (decision or conclusion) in one sentence.
2. EXTRACT assumptions and evidence that support it.
3. DOUBT: adversarial pass tries to disprove (fresh reasoning; optional separate agent).
4. RECONCILE: keep, revise, or drop the claim; list residual risks.
5. STOP when doubt is exhausted or user accepts residual risk.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent APIs, metrics, or CI status — verify in the repo/env.
- When overlapping another skill, load the specialist (see Related).

## Related

- Parent `/0-review` soft · after implement mid-flight · not multi-axis closer `/1-code-review`
- Upstream harvest only; winner name is **`/1-doubt-driven-development`**
