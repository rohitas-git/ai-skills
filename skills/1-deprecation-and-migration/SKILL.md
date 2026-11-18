---
name: 1-deprecation-and-migration
description: >
  Plan and execute the lifecycle for retiring an application feature, API, library, or system.
  Use when: inventorying consumers, running a compatible cutover, or proving an old path can be
  removed. Not for: authoring database migration files (1-supabase-schema-migration for Supabase),
  consolidating unapplied migrations (1-pending-migration-hygiene), or launch operations alone
  (1-shipping-and-launch). Hub: /0-improve-codebase-architecture.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: soft
    when:
      - "retiring a feature, API, library, or system and migrating its consumers"
    not_when:
      - "author Supabase migration files → 1-supabase-schema-migration"
      - "consolidate proven-unapplied migrations → 1-pending-migration-hygiene"
      - "launch operations only → 1-shipping-and-launch"
    next: [0-implement, 1-shipping-and-launch, 1-observability-and-instrumentation, 1-supabase-schema-migration, 1-code-review]
    prev: [0-improve-codebase-architecture, 0-implement]
    cousins: [1-api-and-interface-design, 1-shipping-and-launch, 1-supabase-schema-migration, 1-pending-migration-hygiene]
    triggers:
      - "1-deprecation-and-migration"
      - "deprecation and migration"
      - "sunset this feature"
      - "migrate callers"
      - "remove legacy path"
    requires_setup: false
---

# Deprecation and Migration

**Atomic job:** move every in-scope consumer off one old capability and produce evidence for a
separately authorized removal. Load the [adapted lifecycle guide](./references/full-guide.md) and
[source map](./references/vendor-source.md) when the cutover needs patterns or checklists.

## Boundary

| Need | Skill |
|------|-------|
| Retire a feature or safely migrate callers | **`/1-deprecation-and-migration` (this)** |
| Implement a ready migration slice | `/0-implement` |
| Plan launch communications and rollout | `/1-shipping-and-launch` |
| Instrument adoption and old-path use | `/1-observability-and-instrumentation` |
| Author/local-verify a Supabase schema migration | `/1-supabase-schema-migration` |
| Rewrite or consolidate proven-unapplied migration files | `/1-pending-migration-hygiene` |

## Process

1. **Pin scope and authority.** Record caller, advisory/read-only planning versus authorized implementation, old capability, intended replacement or intentional removal, consumers, owners, compatibility promise, deadlines, and workspace identity. Planning never edits or deletes.
2. **Build a consumer/evidence ledger.** Combine repository references, dependency ownership, telemetry coverage, support commitments, offline/batch clients, data retention, and unknowns. Absence from one search or dashboard is not proof of no consumers.
3. **Design phases and stop conditions.** Choose only justified compatibility adapters, dual paths, flags, or strangler routing. For each phase state entry evidence, reversible action, observation window, rollback/reconciliation, consumer communication, and exit proof. Database lifecycle sequencing may be planned here, but migration files and verification go to the database specialist.
4. **Execute only authorized phases.** Hand implementation slices to `/0-implement`; reuse its matching worktree or conditionally `/1-git-worktrees`. Route rollout/communications to `/1-shipping-and-launch` and usage signals to `/1-observability-and-instrumentation`, then return their evidence to this ledger.
5. **Prove removal readiness separately.** Require known consumers migrated, telemetry coverage understood, contractual/retention obligations satisfied, rollback or recovery decided, and an explicit removal approval. Then remove only the scoped old path, verify references and behavior, and follow Ship's review path.
6. **Return evidence.** Report phase status, migrated/unknown consumers, compatibility and runtime evidence, unresolved risks, skipped checks, and the next authorized decision. Do not commit, publish, deploy, or remove anything merely because the plan is complete.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent APIs, metrics, or CI status — verify in the repo/env.
- Never treat zero observed traffic as proof of zero consumers unless instrumentation coverage,
  observation duration, delayed/offline use, and ownership are accounted for.
- Never edit an applied database migration or run a linked/remote migration command through this
  lifecycle skill. Supabase work follows `/1-supabase-schema-migration` and project policy.
- When overlapping another skill, load the specialist (see Related).

## Related

- **Primary:** Architecture soft. **Conditional caller:** Ship (`/0-implement`).
- **Returns:** lifecycle ledger to the requester; implemented phase to Ship and its normal review.

## Conditional methods

Load only for the requested phase, within this skill’s authority: [Coordinated internal cutover](./references/coordinated-cutover.md).
