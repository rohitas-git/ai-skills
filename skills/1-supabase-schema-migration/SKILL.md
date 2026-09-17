---
name: 1-supabase-schema-migration
description: >
  Author and locally verify one application-owned Supabase schema change. Not for rewriting pending
  files, broad query tuning, day-two database operations, or applying migrations remotely. Hub:
  /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when: ["author one application-owned Supabase schema change as migration files"]
    not_when:
      - "clean proven-unapplied files → 1-pending-migration-hygiene"
      - "measured Postgres concern → 1-supabase-postgres-best-practices"
      - "apply, repair, or push a remote migration → CI applies after merge"
    prev: [0-implement, 1-supabase, 1-supabase-postgres-best-practices, 1-pending-migration-hygiene]
    next: [0-implement, 1-pending-migration-hygiene, 1-atomic-git-commits]
    cousins: [1-supabase, 1-pending-migration-hygiene, 1-supabase-postgres-best-practices, 1-atomic-git-commits]
    triggers: [Supabase schema migration, add RLS policy, add database table, add database column, create database function, create Postgres index]
    requires_setup: false
---

# Supabase Schema Migration

Author **one application-owned schema concept** as safe migration files and verify it on one exact
disposable local stack. DDL and data movement remain separate even when they support the same feature.

## Boundary

| Need | Route |
|---|---|
| Author one new schema concept | **this skill** |
| Rewrite or remove existing pending files | `/1-pending-migration-hygiene` |
| Diagnose product integration | `/1-supabase` |
| Prove and improve a query, lock, or RLS-performance concern | `/1-supabase-postgres-best-practices` |
| Apply remotely or repair a ledger | do not perform; CI applies after merge |

## Contract

1. Pin caller, requested schema concept/non-goals, repository rules, exact repository/worktree/branch/
   `HEAD`, dirty ownership, base/head or working-tree candidate, migration directory/conventions,
   existing ledger snapshot, version-allocation rule, application compatibility window, data size/load/
   lock budget, roles/data class, exact disposable local stack and owner, tests, and repository, local-DB,
   service, Git, remote, and production authority.
2. A worktree does not isolate migration version allocation, Docker names, project IDs, ports, databases,
   Auth/Storage/function state, or caches. Before allocating a version, inspect concurrent task-owned
   migration files and repository conventions. Never reset or apply against a stack owned by another
   worktree. Do not commit a tracked config change whose only purpose is local port isolation.
3. Every schema change is a migration file. Never edit a file that may have been applied outside
   disposable/local environments; append an expand-compatible forward migration. Only
   `/1-pending-migration-hygiene` can establish rewrite eligibility for an existing candidate.
4. Keep one concept per file and schema separate from DML/backfills/seeds/transformations. Preserve
   mixed-version application compatibility across deployment order. A rollback note is not proof that
   destructive reversal is safe, and a down migration is required only when repository policy supports it.
5. Design for short locks and bounded scans. New tables start closed: revoke `anon`/`authenticated`,
   enable RLS, then grant and policy narrowly. Expensive index builds are separate and use a repository-
   supported concurrent/non-transaction path only after verifying tool semantics; never paste
   `CREATE INDEX CONCURRENTLY` into an incompatible transaction wrapper.
6. Write the smallest migration sequence. Parameterize application queries, constrain functions and
   privileges, pin safe `search_path` for justified definer functions, and preserve unknown repository
   conventions. Recheck file/version uniqueness immediately before verification and before any commit.
7. Verify from scratch only on the pinned disposable local stack using the repository-approved local
   script, `rtk supabase db push --local`, or local `psql`. Reset/recreate is destructive local state and
   requires exact stack ownership. Exercise upgrades when relevant, allowed and denied RLS identities,
   constraints, compatibility paths, and every changed function with representative and failure inputs.
8. Keep CI claims honest: CI—not this agent—owns applied-file immutability, unique versions, ledger
   ordering, drift, schema parity, and merge-time application. Ledger drift and schema parity are
   distinct; per-object evidence beats counts that can hide offsetting differences. Missing credentials
   or evidence must fail visibly, not silently skip or recommend a remote bypass.
9. Return caller, candidate/worktree, migration/version ledger, local-stack identity, compatibility and
   lock reasoning, files, commands, checks/identities/functions exercised, limitations, and unperformed
   data/Git/remote work. Use `/1-atomic-git-commits` only when commit authority exists; never start it,
   push, repair, linked application, or production work automatically.

## Hard stops

- Existing-file rewrite eligibility is absent or uncertain.
- Local stack identity/ownership, version uniqueness, application compatibility, or authorization is unclear.
- Local-from-scratch, upgrade, policy, constraint, or changed-function verification fails.
- The proposed next action is a linked, remote, repair, or production migration command.
