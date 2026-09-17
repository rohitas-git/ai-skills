# Shipping and launch wiring audit

Date: 2026-09-11  
Skill: `1-shipping-and-launch`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill and every operative reference, its Ship and DevOps parents
across bodies/workflows/HTML/flows/generated routes, neighboring lifecycle ownership, candidate/
worktree/authority behavior, and routing regressions. The archived upstream remains source material,
not execution authority. This audit did not deploy, promote, roll back, publish, tag, change flags,
apply migrations, notify people, or inspect a real production environment.

## Decisions and changes

- Kept one atomic lifecycle object: assess or coordinate one immutable release candidate through
  readiness, stage decisions, observation, and closure. Modes are plan/advice, read-only readiness
  or observation, and explicitly authorized remote execution.
- Narrowed triggers to release-candidate go/no-go, rollout, promotion, and rollback decisions.
  Candidate implementation, branch integration, CI/CD authoring, telemetry implementation, and
  active incidents retain their specialist owners.
- Formalized Ship and DevOps as callers and returns. Both parent bodies/workflows/HTML/flows now
  pass the same exact candidate/worktree/authority packet and state that planning does not authorize
  a deployment.
- Required repository/worktree/branch/HEAD, immutable artifact digest/version, target environment/
  tenant/region, deployed baseline, dependency and migration ordering, decision owner, and allowed
  Git/remote/production/communication effects. Planning and read-only modes create no worktree; a
  worktree does not isolate shared registries, databases, flags, queues, tenants, or credentials.
- Replaced the universal checklist with a risk- and policy-derived readiness ledger. Each applicable
  gate records candidate, environment, evidence time, PASS/FAIL/BLOCKED/SKIPPED, owner, and action.
- Made rollout type, cohort size, soak condition, thresholds, and error-budget behavior contextual.
  Unknown values remain decisions instead of copied percentages, durations, or cutoffs.
- Added compatibility and state classification before rollback. Code reversal is not assumed to
  reverse schemas, data, queues, caches, external side effects, or mixed-version obligations;
  expand/contract and forward recovery remain valid alternatives.
- Required one-stage-at-a-time remote execution, fresh state before action, exact provider evidence,
  a decision after each stage, and no inferred approval for later stages.
- Scoped versioning to repositories/ecosystems that actually have a version contract. Compatibility
  uncertainty blocks classification; it no longer defaults blindly to a major bump. Tags, releases,
  package publication, pushes, and notifications remain separately authorized effects.
- Replaced the 330-line absolute-heavy guide with a concise operative adaptation and preserved the
  full upstream snapshot for provenance.

## Verification

- `python3 -m unittest scripts.test-routing.ShippingAndLaunchRouteTests`: **6 tests passed**.
- `python3 -m unittest scripts/test-routing.py`: **117 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 64 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- Regression coverage proves two-parent dispatch/returns, immutable candidate and environment
  identity, conditional worktrees, mode/authority separation, evidence-based gates, state-aware
  recovery, versioning boundaries, and removal of unsafe vendor absolutes and commands.

## Remaining limits

- Any real hosted or production state must be re-inspected against the exact candidate and requires
  separately scoped authority before action.
- Other Ship and DevOps children remain pending semantic review.
