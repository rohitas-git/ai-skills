---
name: 1-api-and-interface-design
description: >
  Stable APIs and module boundaries (REST/GraphQL/types). Use when designing public interfaces, versioning contracts, or validating at trust boundaries.
disable-model-invocation: true
---

# API and Interface Design

Lean catalog skill. **Full vendor body:** [references/full-guide.md](./references/full-guide.md). Pointer only: [references/vendor-source.md](./references/vendor-source.md).

## Process

1. Name consumers and stability expectation (public vs internal).
2. Design contract first (types/OpenAPI); validate at boundary.
3. Apply one-version / compatibility rules (Hyrum-aware).
4. Document errors, pagination, auth assumptions.
5. Prefer deep modules: small interface, hidden complexity.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent APIs, metrics, or CI status — verify in the repo/env.
- When overlapping another skill, load the specialist (see Related).

## Related

- Architecture soft · with `/1-codebase-design` · not full system persona `/2-software-architect`
- Upstream harvest only; winner name is **`/1-api-and-interface-design`**
