---
name: ci-cd-and-automation
description: >
  Build/test/deploy pipelines and quality gates. Use when setting up or changing CI, release automation, or agent feedback from failed pipelines.
disable-model-invocation: true
---

# CI/CD and Automation

Lean catalog skill. **Full vendor body:** [references/full-guide.md](./references/full-guide.md). Pointer only: [references/vendor-source.md](./references/vendor-source.md).

## Process

1. Map required gates (lint, typecheck, test, security, deploy).
2. Keep pipelines fast and deterministic; fail closed on quality.
3. Wire clear logs for agent/human diagnosis on failure.
4. Prefer staged deploy hooks over implicit prod push.
5. Document skip policies (rare, explicit).

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent APIs, metrics, or CI status — verify in the repo/env.
- When overlapping another skill, load the specialist (see Related).

## Related

- Ship soft · with `/shipping-and-launch` · not app feature code (`/implement`)
- Upstream harvest only; winner name is **`/ci-cd-and-automation`**
