# Deprecation and migration — adapted lifecycle guide

Use after the live skill pins the old capability, consumers, authority, and evidence sources.
Examples are patterns, not permission to deploy or delete. Database-file authorship and local
verification stay with the project's migration workflow; Supabase uses
`/1-supabase-schema-migration`. See [vendor-source.md](./vendor-source.md) for provenance.

## Overview

Code can provide durable value and also impose maintenance, security, dependency, and cognitive
cost. Deprecation is justified when evidence shows a capability's continuing value no longer
outweighs its cost or risk, and migration moves affected consumers without silently breaking them.

Most engineering organizations are good at building things. Few are good at removing them. This skill addresses that gap.

## When to Use

- Replacing an old system, API, or library with a new one
- Sunsetting a feature that's no longer needed
- Consolidating duplicate implementations
- Removing dead code that nobody owns but everybody depends on
- Planning the lifecycle of a new system (deprecation planning starts at design time)
- Deciding whether to maintain a legacy system or invest in migration

## Core Principles

### Code Is a Liability

Every line of code has ongoing cost: it needs tests, documentation, security patches, dependency updates, and mental overhead for anyone working nearby. The value of code is the functionality it provides, not the code itself. When the same functionality can be provided with less code, less complexity, or better abstractions — the old code should go.

### Hyrum's Law Makes Removal Hard

With enough users, every observable behavior becomes depended on — including bugs, timing quirks, and undocumented side effects. This is why deprecation requires active migration, not just announcement. Users can't "just switch" when they depend on behaviors the replacement doesn't replicate.

### Deprecation Planning Starts at Design Time

When building something new, ask: "How would we remove this in 3 years?" Systems designed with clean interfaces, feature flags, and minimal surface area are easier to deprecate than systems that leak implementation details everywhere.

## The Deprecation Decision

Before deprecating anything, answer these questions:

```
1. Does this system still provide unique value?
   → If yes, maintain it. If no, proceed.

2. How many users/consumers depend on it?
   → Quantify the migration scope.

3. Is the capability still required?
   → If yes, prove an adequate replacement or compatibility path before removal. If no, define
     how consumers and retained data exit safely without inventing a replacement.

4. What's the migration cost for each consumer?
   → If trivially automated, do it. If manual and high-effort, weigh against maintenance cost.

5. What's the ongoing maintenance cost of NOT deprecating?
   → Security risk, engineer time, opportunity cost of complexity.
```

## Compulsory vs Advisory Deprecation

| Type | When to Use | Mechanism |
|------|-------------|-----------|
| **Advisory** | Migration is optional, old system is stable | Warnings, documentation, nudges. Users migrate on their own timeline. |
| **Compulsory** | Old system has security issues, blocks progress, or maintenance cost is unsustainable | Hard deadline. Old system will be removed by date X. Provide migration tooling. |

Choose advisory versus compulsory from risk, ownership, contractual commitments, consumer control,
support capacity, and urgency. There is no universal default. A compulsory timeline needs a
credible migration path and escalation/support plan; advisory status still needs an owner and
review date or it can become permanent limbo.

## The Migration Process

### Step 1: Prove the destination or exit

When consumers still need the capability, the replacement should:

- Cover all critical use cases of the old system
- Have documentation and migration guides
- Have evidence proportional to its risk: tests, compatibility checks, staged use, or production
  observation where authorized. A low-risk internal retirement need not manufacture a production
  dual-run merely to satisfy a ritual.

### Step 2: Announce and Document

```markdown
## Deprecation Notice: OldService

**Status:** Deprecated as of 2025-03-01
**Replacement:** NewService (see migration guide below)
**Removal date:** Advisory — no hard deadline yet
**Reason:** OldService requires manual scaling and lacks observability.
            NewService handles both automatically.

### Migration Guide
1. Replace `import { client } from 'old-service'` with `import { client } from 'new-service'`
2. Update configuration (see examples below)
3. Run the migration verification script: `npx migrate-check`
```

### Step 3: Migrate Incrementally

Migrate consumers one at a time, not all at once. For each consumer:

```
1. Identify all touchpoints with the deprecated system
2. Update to use the replacement
3. Verify behavior matches (tests, integration checks)
4. Remove references to the old system
5. Confirm no regressions
```

**The Churn Rule:** If you own the infrastructure being deprecated, you are responsible for migrating your users — or providing backward-compatible updates that require no migration. Don't announce deprecation and leave users to figure it out.

### Step 4: Remove the Old System

Only after the consumer/evidence ledger satisfies its removal gate and removal is explicitly
authorized:

```
1. Reconcile known consumers and unknowns using more than one appropriate evidence source
2. Remove the code
3. Remove associated tests, documentation, and configuration
4. Remove the deprecation notices
5. Verify rollback/recovery posture and record the decision/evidence
```

## Migration Patterns

### Strangler Pattern

Run old and new systems in parallel and route traffic incrementally where that is operationally
justified. Reaching 0% observed traffic is only one input to the removal gate; telemetry coverage,
offline consumers, ownership, retention obligations, and an adequate observation window still apply.

```
Phase 1: New system handles 0%, old handles 100%
Phase 2: New system handles 10% (canary)
Phase 3: New system handles 50%
Phase 4: New system handles 100%, old system idle
Phase 5: Remove old system
```

### Adapter Pattern

Create an adapter that translates calls from the old interface to the new implementation. Consumers keep using the old interface while you migrate the backend.

```typescript
// Adapter: old interface, new implementation
class LegacyTaskService implements OldTaskAPI {
  constructor(private newService: NewTaskService) {}

  // Old method signature, delegates to new implementation
  getTask(id: number): OldTask {
    const task = this.newService.findById(String(id));
    return this.toOldFormat(task);
  }
}
```

### Feature Flag Migration

Use feature flags to switch consumers from old to new system one at a time:

```typescript
function getTaskService(userId: string): TaskService {
  if (featureFlags.isEnabled('new-task-service', { userId })) {
    return new NewTaskService();
  }
  return new LegacyTaskService();
}
```

### Database schema lifecycle (concept only)

Application and schema versions may coexist during rollout, so destructive database changes often
need an expand → migrate data/callers → contract lifecycle. That sequence is a planning model, not
a universal SQL recipe: nullable additions, defaults, constraints, indexes, dual writes, backfills,
locks, transactions, reversibility, and rollback all depend on the database, table, traffic, and
deployment system. An additive statement can still lock, rewrite, expose data, or break strict
consumers. A down migration can itself be destructive and is not always the correct recovery plan.

This skill records phase dependencies and consumer evidence only. For Supabase, author every schema
change through `/1-supabase-schema-migration`: never edit an applied migration, never run linked or
remote migration commands, separate DDL from DML, verify locally, and use a later forward migration
when an earlier version may have escaped disposable/local environments. Pending-file consolidation
belongs to `/1-pending-migration-hygiene` and requires proof of non-application.

## Zombie Code

Zombie code is code that nobody owns but everybody depends on. It's not actively maintained, has no clear owner, and accumulates security vulnerabilities and compatibility issues. Signs:

- No commits in 6+ months but active consumers exist
- No assigned maintainer or team
- Failing tests that nobody fixes
- Dependencies with known vulnerabilities that nobody updates
- Documentation that references systems that no longer exist

**Response:** Either assign an owner and maintain it properly, or deprecate it with a concrete migration plan. Zombie code cannot stay in limbo — it either gets investment or removal.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "It still works, why remove it?" | Working code that nobody maintains accumulates security debt and complexity. Maintenance cost grows silently. |
| "Someone might need it later" | Identify actual obligations and plausible consumers. Preserve a recoverable archive or compatibility path when evidence warrants it; do not keep or delete solely on speculation. |
| "The migration is too expensive" | Compare risk-adjusted migration cost with ongoing maintenance, security, support, and opportunity cost. Either outcome can be rational. |
| "We'll deprecate it after we finish the new system" | Deprecation planning starts at design time. By the time the new system is done, you'll have new priorities. Plan now. |
| "Users will migrate on their own" | Do not assume they will. Measure adoption, communicate, provide tooling/support, and assign ownership for unresolved consumers. |
| "We can maintain both systems indefinitely" | Two systems doing the same thing is double the maintenance, testing, documentation, and onboarding cost. |
| "Just rename the column, it's one line" | First establish coexistence, lock, compatibility, data, and deployment constraints with the database specialist; in-place rename may be unsafe but one ritual is not universally correct. |
| "An additive migration is automatically safe" | Adds can still lock, rewrite, weaken access control, or break strict consumers. Verify the actual operation and rollout. |
| "A down migration guarantees rollback" | Recovery may require a forward fix, restore, reconciliation, or code rollback. Prove the chosen recovery path without destroying newer data. |

## Red Flags

- Deprecated systems with no replacement available
- Deprecation announcements with no migration tooling or documentation
- "Soft" deprecation that's been advisory for years with no progress
- Zombie code with no owner and active consumers
- New features added to a deprecated system (invest in the replacement instead)
- Deprecation without measuring current usage
- Removing code from zero observed traffic without proving instrumentation coverage, ownership,
  offline/delayed use, and an adequate observation window
- A schema/code rollout with no verified compatibility window or recovery plan
- A destructive column change performed before consumer and database-specific evidence permits it
- Database lifecycle work performed here instead of through the database-specific migration owner

## Verification

After completing a deprecation:

- [ ] Required capability has a replacement or intentional exit with risk-proportional evidence
- [ ] Migration guide exists with concrete steps and examples
- [ ] Known consumers are migrated and unknown-consumer risk is bounded using appropriate code,
  ownership, telemetry, support, and delayed/offline-use evidence
- [ ] Old code, tests, documentation, and configuration are fully removed
- [ ] No references to the deprecated system remain in the codebase
- [ ] Deprecation notices are removed (they served their purpose)

For a database schema lifecycle plan (implementation verified by its database owner):

- [ ] The change ships in additive phases (expand → backfill → contract), not a single in-place edit
- [ ] Old and new code are both valid against the schema at every deploy step
- [ ] Each phase has an explicit recovery plan appropriate to its actual data and deployment state
- [ ] Destructive steps (drop/rename) ship in their own deploy after no code references the old shape
