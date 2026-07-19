---
name: deprecation-and-migration
description: >
  Sunset APIs/features and migrate callers safely. Use when removing systems, expand/contract schema changes, or dual-running during cutover.
disable-model-invocation: true
---

# Deprecation and Migration

Lean catalog skill. **Full vendor body:** [references/full-guide.md](./references/full-guide.md). Pointer only: [references/vendor-source.md](./references/vendor-source.md).

## Process

1. Classify advisory vs compulsory deprecation timeline.
2. Choose pattern (strangler, adapter, feature flag, expand/contract).
3. Ship dual-path; migrate callers; monitor.
4. Remove old path only when metrics show zero/acceptable traffic.
5. Document in ADR/living docs if decision is durable.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent APIs, metrics, or CI status — verify in the repo/env.
- When overlapping another skill, load the specialist (see Related).

## Related

- Architecture soft · pairs with `/shipping-and-launch` for cutover
- Upstream harvest only; winner name is **`/deprecation-and-migration`**
