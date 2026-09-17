---
name: 1-shipping-and-launch
description: >
  Assess readiness or coordinate the bounded rollout of one exact release candidate.
  Use for release go/no-go, staged exposure, launch observation, or rollback criteria.
  Not for authoring CI/CD, implementing the feature, branch integration choices, or
  commanding an active incident. Hubs: /0-implement and /0-devops.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "assessing one exact release candidate for go, hold, or no-go"
      - "planning or explicitly executing a staged rollout with observation and rollback gates"
    not_when:
      - "author CI/CD workflow or deployment automation → 1-ci-cd-and-automation"
      - "implement or repair the release candidate → 0-implement"
      - "choose branch or PR integration outcome → 1-finish-branch"
      - "contain an active outage or compromise → 1-incident-response"
    prev: [0-implement, 0-devops]
    next: [0-implement, 0-devops, 1-ci-cd-and-automation, 1-observability-and-instrumentation, 1-incident-response, 1-resilience-and-disaster-recovery, 1-security-auditor, 1-performance-optimization, 1-finish-branch]
    cousins: [1-ci-cd-and-automation, 1-observability-and-instrumentation, 1-incident-response, 1-finish-branch]
    triggers:
      - "1-shipping-and-launch"
      - "release readiness review"
      - "production rollout plan"
      - "release go no-go"
      - "canary promotion criteria"
      - "rollback decision for this release"
    requires_setup: false
---

# Shipping and Launch

Coordinate **one immutable release candidate** through readiness, rollout decisions,
observation, and closure. Modes are plan/advice, read-only readiness or observation, and
explicitly authorized remote execution. Planning a launch never authorizes performing it.

## Boundary

| Need | Route |
|---|---|
| Assess or coordinate rollout of an exact built candidate | **this skill** |
| Build, test, or repair candidate contents | `/0-implement` |
| Choose merge, PR, or branch disposition | `/1-finish-branch` |
| Author deployment workflow or required checks | `/1-ci-cd-and-automation` |
| Add missing telemetry | `/1-observability-and-instrumentation` |
| Contain an active incident | `/1-incident-response` |

## Input contract

Inherit caller, mode, release intent/exclusions, exact repository/worktree/branch/HEAD,
immutable artifact/image/package identity, target environment/tenant/region, current deployed
version, dependency and migration order, dirty/shared-state ownership, approved checks, decision
owner, maintenance/support window, and allowed Git, remote, production, and communication effects.

Readiness, planning, and read-only observation create no worktree. An authorized repository
edit reuses the caller's matching owned worktree or conditionally routes through
`/1-git-worktrees`, then returns. A worktree does not isolate registries, feature flags,
databases, queues, tenants, dashboards, credentials, or deploy targets.

## Process

1. **Pin candidate and authority.** Resolve the exact artifact digest/version and source SHA,
   environment identity, deployed baseline, mode, operator, and permitted commands. If the
   candidate can still change, return to Ship; do not certify a moving target.
2. **Build a readiness ledger.** Derive required evidence from repository policy and release
   risk: build/tests/review, security/privacy, performance/capacity, compatibility, migrations,
   configuration/secrets presence, dependency readiness, support/comms, observability, and
   recovery. Record PASS/FAIL/BLOCKED/SKIPPED with candidate and evidence time; “all checks” is
   not a substitute for naming applicable gates.
3. **Map irreversible and coupled changes.** Identify database/data transitions, message or API
   compatibility, external consumers, cache/state changes, and infrastructure dependencies.
   Prefer expand/contract or forward recovery where rollback would lose data or break old/new
   coexistence; route schema work to the database specialist.
4. **Choose exposure from evidence.** Direct, rolling, blue/green, canary, cohort, or flag rollout
   is a contextual choice, not a default ladder. Record stages/cohorts, concurrency, soak or
   observation condition, promotion owner, and blast radius. Feature flags need an owner,
   retirement condition, both-state compatibility where relevant, and an operational kill path.
5. **Define decision gates before execution.** Each promote/hold/rollback/forward-fix gate names
   the user/system signal, baseline or SLO, threshold/window, query/dashboard, data freshness,
   decision owner, and exact response. Unknown values remain decisions; do not copy generic
   percentages, durations, or error-budget cutoffs.
6. **Write recovery as an executable decision tree.** Pin last-known-good artifacts and safe
   commands, prerequisites, permissions, data consequences, verification, communications, and
   escalation. Never assume code rollback reverses schema/data or external side effects.
7. **Apply the mode boundary.** Plan/advice returns the ledger and runbook. Read-only mode may
   inspect authorized status and telemetry. Remote execution performs only the named stage and
   only after explicit authority for that environment/action; re-confirm destructive or
   difficult-to-reverse steps. Stop on identity drift, failed gates, lost observability, or
   unexpected effects.
8. **Observe and close.** Compare the exact stage with its baseline, record the decision and
   evidence, then either promote one stage, hold, recover, or hand an active incident to
   `/1-incident-response`. Closure records deployed identity, remaining exposure, flag/debt
   owner and due condition, residual risks, and follow-ups; it does not silently perform cleanup.

## Hard rules

- A green local tree, old CI run, mutable tag, or successful deploy command does not prove the
  target environment runs the intended candidate or that user behavior is healthy.
- Do not invent gates, thresholds, approval, production state, rollback safety, or notification.
- Do not commit, tag, push, merge, publish, change flags/secrets/rules, apply migrations,
  deploy, promote, roll back, page, or mutate remote/production state without explicit authority.

## References

- Operative: [release and rollout guide](./references/full-guide.md), [versioning and changelog](./references/versioning-changelog.md)
- Provenance: [vendor source](./references/vendor-source.md)
