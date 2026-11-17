---
name: 0-implement
description: 'Drive a bounded implementation from a clear request, accepted specification, ticket, or plan. Use for building or changing code and repository artifacts through scoped verification and review. Not for: unresolved product discovery (0-grilling / 1-to-spec), review-only work (1-code-review), raw issue triage (0-triage), or requested branch integration options (1-finish-branch). Hub: /0-implement.

  '
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: hub
    when: ['implement a clear request, accepted specification, ticket, or plan', 'drive a scoped build, verification, and review path']
    not_when: [unresolved product requirements → 0-grilling / 1-to-spec, review only → 1-code-review, raw issues → 0-triage, branch integration/options only → 1-finish-branch]
    next: [1-i18n-sync, 1-migrate-to-shoehorn, 1-to-spec, 1-to-tickets, 1-write-plan, 1-execute-plan, 1-subagent-implement, 1-parallel-agents, 1-constraint-driven-development, 1-git-worktrees, 1-api-and-interface-design, 1-codebase-design, 1-coding-standards, 1-go-best-practices, 1-deprecation-and-migration, 1-error-handling, 1-living-documentation-governor, 1-supabase, 1-supabase-postgres-best-practices, 1-supabase-schema-migration, 1-pending-migration-hygiene, 1-tdd, 1-dev-test, 2-verify-work, 1-code-review, 1-code-comments, 1-inline-comments, 1-execution-flow-comments, 1-stepdown-rule, 1-karpathy-guidelines, 1-atomic-git-commits, 1-finish-branch, 1-pr-summarizer, 1-resolving-merge-conflicts, 1-research, 1-shipping-and-launch, 1-observability-and-instrumentation, 1-ci-cd-and-automation, 1-frontend-ui-engineering, 1-ui-styling, 1-performance-optimization]
    prev: [0-butler, 0-triage, 1-to-tickets, 1-to-spec]
    triggers: [implement, build this, execute this plan, ship tickets, make this change]
    requires_setup: false
---


# Implement

**Hub job:** preserve one requested outcome, candidate, workspace, and authority while selecting only
the implementation specialists and evidence loops that the change actually needs.

## Pipeline

1. **Pin the contract.** Record caller, task/spec/ticket, acceptance criteria, explicit exclusions,
   repository root, requested branch/base, protected/unrelated work, and permitted side effects. A
   concise clear request is enough; route materially unresolved product choices to `/0-grilling` or
   `/1-to-spec`, but do not manufacture a planning ceremony for a small reversible change.
2. **Resolve the workspace.** Inspect exact repo/worktree path, branch/HEAD, status, dirty-file
   ownership, concurrent writers, and local-service ownership. Reuse a matching task workspace. Use
   `/1-git-worktrees` when work would otherwise occur on a protected primary branch, another task owns
   the checkout, unrelated changes overlap, concurrent work needs isolation, or branch-specific local
   state must differ; then resume this pipeline with returned provenance.
3. **Select the slice and evidence loop.** Prefer one independently reviewable outcome. Use
   `/1-tdd` only for known deterministic behavior at an agreed seam; otherwise use specification,
   characterization, prototype/evaluation, or focused runtime evidence. See
   [incremental slices](./references/incremental-slices.md) and [confusion handling](./references/confusion-and-inline-plan.md).
4. **Call specialists conditionally.** Public contract → `/1-api-and-interface-design`; internal seam
   → `/1-codebase-design`; Go → `/1-go-best-practices`; failure policy → `/1-error-handling`; retirement
   → `/1-deprecation-and-migration`; living docs → `/1-living-documentation-governor`; UI behavior →
   `/1-frontend-ui-engineering`; presentation-only UI → `/1-ui-styling`; Supabase product/schema/Postgres/pending cleanup → the corresponding
   Supabase leaf. Each inherits this task, workspace, candidate, dirty ownership, and authority and
   returns here. Workflow/check-contract work → `/1-ci-cd-and-automation`; telemetry for one
   bounded behavior → `/1-observability-and-instrumentation`; a measured bottleneck →
   `/1-performance-optimization`; release-candidate readiness or
   rollout coordination → `/1-shipping-and-launch`; comments and layout use their named child only when in scope.
   `/1-research` answers one bounded evidence question and returns here; it never implements or writes an artifact
   unless that exact persistence effect was requested.
5. **Implement surgically.** Follow repository instructions and `/1-coding-standards`; an explicit
   Karpathy-process request may use `/1-karpathy-guidelines` and return here. Change only task-owned
   files plus the minimum required compatibility surface. Delegation via
   `/1-subagent-implement` or `/1-parallel-agents` occurs only when explicitly requested/authorized
   and its tasks have safe ownership boundaries. Never let concurrent writers share a worktree,
   branch, file, database, port, or mutable service state.
6. **Verify supported claims.** Use existing project commands and authorized local/disposable services.
   Run the narrowest checks that falsify the changed behavior, then broader checks when risk,
   repository policy, or requested completion requires them. Record PASS/FAIL/BLOCKED/SKIPPED and
   candidate identity; never treat an agent-authored happy-path test, typecheck, or stale run as proof
   of runtime correctness. `/2-verify-work` can provide a bounded evidence-only pass.
7. **Review and reconcile.** Run read-only `/1-code-review` on the actual task candidate, including
   task-owned dirty work. Within existing edit authority, resolve verified in-scope findings one at a
   time, re-run affected evidence, and re-review the changed candidate until no blocking in-scope
   findings remain or a real decision/blocker is returned. Broader improvements remain follow-ups.
8. **Close only within authority.** Apply the project [definition of done](./references/definition-of-done.md)
   proportionally. If commits were requested/authorized, use `/1-atomic-git-commits` on the confirmed
   feature branch. Use `/1-pr-summarizer` for a requested summary and `/1-finish-branch` only for
   requested integration/PR options. Never push/merge a protected branch, deploy, publish, or mutate
   remote/production services merely because implementation is complete.

## Output contract

Return task/scope, exact repo/worktree/branch/HEAD, changed and protected paths, specialist returns,
checks with candidate/timestamps or fresh-run identity, review disposition, residual risk, skipped or
blocked evidence, and local artifacts/state left behind. Do not claim completion beyond that evidence.

## References

- Operative: [definition of done](./references/definition-of-done.md), [incremental slices](./references/incremental-slices.md), [confusion handling](./references/confusion-and-inline-plan.md), [explicit delegation](./references/orchestration-patterns.md)
- Historical source only: [vendor DoD](./references/definition-of-done-vendor-full.md), [vendor incremental guide](./references/vendor-incremental-full.md)

## Available specialist additions

- `/1-dev-test` — use for its scoped contract; return to this hub.
- `/1-i18n-sync` — use for its scoped contract; return to this hub.
- `/1-migrate-to-shoehorn` — use for its scoped contract; return to this hub.
