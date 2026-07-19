---
name: shipping-and-launch
description: >
  Pre-launch checklist, staged rollout, monitoring, and rollback planning. Use when preparing production deploy, canary/flag rollout, or go/no-go for a release.
disable-model-invocation: true
---

# Shipping and Launch

Lean catalog skill. **Full vendor body:** [references/full-guide.md](./references/full-guide.md). Versioning/changelog: [references/versioning-changelog.md](./references/versioning-changelog.md). Pointer: [references/vendor-source.md](./references/vendor-source.md).

## Process

1. Confirm scope and environments (prod/stage).
2. Run pre-launch checklist (deps, migrations, flags, observability, support).
3. Define rollout (big-bang / canary / flag) and success metrics.
4. Write rollback plan before deploy.
5. For consumer-facing releases: semver bump + changelog entry (see versioning ref).
6. Launch; watch metrics; execute rollback if thresholds breach.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent APIs, metrics, or CI status — verify in the repo/env.
- When overlapping another skill, load the specialist (see Related).

## Related

- Ship soft under `/implement` · after code-review green · not feature build (`/implement`/`/tdd`)
- Upstream harvest only; winner name is **`/shipping-and-launch`**
