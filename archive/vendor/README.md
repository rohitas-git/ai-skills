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
| ui-ux-pro-max-skill | [ui-ux-pro-max-skill/](./ui-ux-pro-max-skill/) | Parked. Selective promote into Domain 15 `/0-ui-ux` (see harvest table). CLI/`src`/`stack` stay archive-only. |
| superpowers (obra/Jesse Vincent) | [superpowers/](./superpowers/) | Parked v6.1.1. Selective promote + merges 2026-07-20. **Never** promote `using-superpowers` (dual meta-router). |

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

### ui-ux-pro-max-skill pack (Domain 15)

| Vendor skill | Live winner | Hub |
|--------------|-------------|-----|
| ui-ux-pro-max | `1-ui-ux-pro-max` | `/0-ui-ux` pipeline |
| design | `1-design` | `/0-ui-ux` leaf |
| brand | `1-brand` | `/0-ui-ux` leaf |
| design-system | `1-design-system` | `/0-ui-ux` leaf |
| ui-styling | `1-ui-styling` | `/0-ui-ux` leaf |
| banner-design | `1-banner-design` | `/0-ui-ux` leaf |
| slides | `1-slides` | `/0-ui-ux` leaf (HTML decks; not `/1-pptx`) |
| *(dual)* | `1-frontend-ui-engineering` | Ship primary + soft dual UI/UX |

Do **not** peer-promote near-duplicates of grill / to-spec / to-tickets / tdd / code-review.

### superpowers pack (obra · v6.1.1)

| Upstream skill | Disposition | Live winner / name |
|----------------|-------------|-------------------|
| using-superpowers | **Refuse** (meta-router) | archive only |
| test-driven-development | **Merge** | `1-tdd` → `references/superpowers-tdd-full.md` |
| systematic-debugging | **Merge** | `0-diagnosing-bugs` → `references/superpowers-debugging-full.md` |
| requesting-code-review | **Merge** | `1-code-review` → `references/superpowers-request-review.md` |
| verification-before-completion | **Merge** | `2-verify-work` → `references/superpowers-evidence-gate.md` |
| writing-skills | **Merge** | `1-writing-great-skills` → `references/superpowers-writing-skills-full.md` |
| brainstorming | **Promote** | `1-brainstorm` (Design on-ramp) |
| writing-plans | **Promote** | `1-write-plan` |
| executing-plans | **Promote** | `1-execute-plan` |
| subagent-driven-development | **Promote** | `1-subagent-implement` |
| dispatching-parallel-agents | **Promote** | `1-parallel-agents` |
| using-git-worktrees | **Promote** | `1-git-worktrees` |
| finishing-a-development-branch | **Promote** | `1-finish-branch` |
| receiving-code-review | **Promote** | `1-receive-review` |

See also pack `VENDOR-SOURCE.md`.
