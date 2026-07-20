# Vendor

Third-party skill packs kept **out of default discovery**.

## Policy

- **Promote only via butler ingest** — never co-load a whole pack as peer skills, and never promote `using-agent-skills` (dual meta-router).
- Packs here are offline from symlink sync unless explicitly listed in `scripts/symlink-targets.json` `nestedSkillRoots` (default: empty).
- Prefer merging useful content into an existing catalog winner over promoting a near-duplicate.

## Packs

| Pack | Path | Status |
|------|------|--------|
| agent-skills (Addy Osmani et al.) | [agent-skills/](./agent-skills/) | Parked. Selective promotes only via butler ingest. TDD ideas merge into catalog `tdd`, not a second skill. |

## Harvest status (ingest into live winners)

**Forbidden peer:** `using-agent-skills` (dual meta-router) — never promote.

| Vendor skill / pack ref | Live winner | Where depth lives |
|-------------------------|-------------|-------------------|
| shipping-and-launch | `shipping-and-launch` | `references/full-guide.md` + versioning-changelog |
| observability-and-instrumentation | `observability-and-instrumentation` | `full-guide.md` + observability-checklist |
| performance-optimization | `performance-optimization` | `full-guide.md` + performance-checklist |
| api-and-interface-design | `api-and-interface-design` | `full-guide.md` |
| frontend-ui-engineering | `frontend-ui-engineering` | `full-guide.md` + accessibility-checklist |
| ci-cd-and-automation | `ci-cd-and-automation` | `full-guide.md` |
| browser-testing-with-devtools | `browser-testing-with-devtools` | `full-guide.md` |
| deprecation-and-migration | `deprecation-and-migration` | `full-guide.md` |
| doubt-driven-development | `doubt-driven-development` | `full-guide.md` |
| security-and-hardening | `security-and-hardening` | existing refs + security-checklist-vendor-pack |
| debugging-and-error-recovery | `diagnosing-bugs` | vendor-debugging-full + extras |
| code-review-and-quality | `code-review` | vendor-code-review-full + axes |
| code-simplification | `ponytail-review` | vendor-simplification-full |
| incremental-implementation | `implement` | vendor-incremental-full + slices |
| test-driven-development | `tdd` | vendor-tdd-full + testing-patterns-vendor |
| source-driven-development | `research` | source-driven-full |
| planning-and-task-breakdown | `to-tickets` (+ implement DoD) | vendor-planning-full + sizing-checkpoints |
| spec-driven-development | `to-spec` | vendor-spec-full |
| interview-me | `grilling` | interview-intent |
| idea-refine | `grilling` | vendor-idea-refine-full + frameworks/criteria/examples |
| context-engineering | `strategic-compact` (+ implement) | vendor-context-full + hierarchy |
| documentation-and-adrs | `living-documentation-governor` (+ domain-modeling) | vendor-docs-adrs-full + readme skeleton |
| git-workflow-and-versioning | `git-commit-helper` (+ shipping) | vendor-git-workflow-full + workflow-discipline |
| references/definition-of-done | `implement` | definition-of-done + vendor full |
| references/orchestration-patterns | `implement` | orchestration-patterns.md |
| references/*-checklist (obs/perf/a11y/sec/test) | matching winners above | copied |

Do **not** peer-promote near-duplicates of grill / to-spec / to-tickets / tdd / code-review.
