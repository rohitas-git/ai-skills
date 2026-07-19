---
name: performance-optimization
description: >
  Measure-first performance work across FE/BE/DB. Use when Core Web Vitals, load times, N+1 queries, or profiling show regressions or budgets.
disable-model-invocation: true
---

# Performance Optimization

Lean catalog skill. **Full vendor body:** [references/full-guide.md](./references/full-guide.md).
Checklist: [references/performance-checklist.md](./references/performance-checklist.md). Pointer only: [references/vendor-source.md](./references/vendor-source.md).

## Process

1. Measure baseline (profiler, CWV, query plans, traces).
2. Identify top bottleneck with evidence.
3. Fix one bottleneck; re-measure.
4. Guard with a test or budget check when possible.
5. Stop when budget met — no speculative rewrites.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent APIs, metrics, or CI status — verify in the repo/env.
- When overlapping another skill, load the specialist (see Related).

## Related

- Diagnose soft · after `/diagnosing-bugs` feedback loop · not premature micro-opts while greenfield building
- Upstream harvest only; winner name is **`/performance-optimization`**
