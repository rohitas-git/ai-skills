---
name: 1-doubt-driven-development
description: >
  Fresh-context adversarial review of non-trivial decisions (CLAIM→EXTRACT→DOUBT→RECONCILE).
  Use when correctness stakes are high or confident output is cheaper to verify now. Not for: routine
  multi-axis PR review (1-code-review). Hub: /0-review. Triggers: doubt-driven, adversarial review, stress-test decision.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-review
    role: soft
    when:
      - "high-stakes decision needs adversarial doubt"
      - "verify confident output now"
    not_when:
      - "routine PR multi-axis → 1-code-review"
    cousins: [1-code-review, 1-thinking-steel-manning]
    triggers:
      - "doubt-driven"
      - "adversarial review"
      - "stress-test decision"
    requires_setup: false
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

- Parent `/0-review` soft · after 0-implement mid-flight · not multi-axis closer `/1-code-review`
- Upstream harvest only; winner name is **`/1-doubt-driven-development`**
