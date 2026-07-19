---
name: 1-frontend-ui-engineering
description: >
  Accessible, responsive, production-quality UI (not generic AI aesthetics). Use when building or hardening user-facing pages, forms, empty/error states, or keyboard/focus behavior.
disable-model-invocation: true
---

# Frontend UI Engineering

Lean catalog skill. **Full vendor body:** [references/full-guide.md](./references/full-guide.md).
A11y: [references/accessibility-checklist.md](./references/accessibility-checklist.md). Pointer only: [references/vendor-source.md](./references/vendor-source.md).

## Process

1. Clarify IA, states (loading/empty/error), and audience.
2. Build accessible structure first (semantics, focus, labels).
3. Style for hierarchy and density; avoid decorative AI-slop defaults.
4. Responsive and keyboard paths; test with DevTools skill when available.
5. Keep components deep modules — simple props, hidden complexity.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent APIs, metrics, or CI status — verify in the repo/env.
- When overlapping another skill, load the specialist (see Related).

## Related

- Ship soft · with `/1-browser-testing-with-devtools` for runtime check
- Upstream harvest only; winner name is **`/1-frontend-ui-engineering`**
