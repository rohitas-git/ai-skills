# Supabase cluster wiring audit

Reviewed `1-supabase`, `1-supabase-schema-migration`, `1-pending-migration-hygiene`,
`1-supabase-postgres-best-practices`, both complete package-local provenance references, Ship parent
surfaces, and adjacent Performance, Diagnose, Playwright, Git commit, deprecation, and day-two database
operation boundaries.

## Result

The four skills remain separate atomic operations: one Supabase product-integration concern; one new
application-owned schema concept; one pending-file cleanup supported by rewrite proof; and one measured
Postgres concern. All now declare Ship as their caller and return there instead of implying an automatic
migration, optimization, test, or commit chain.

Each contract pins the exact repository/worktree/candidate and distinguishes it from project/local-stack,
environment, database, role, data, runtime, and deployed identity. Worktrees do not isolate migration
version allocation, Supabase project IDs, Docker resources, ports, databases, Auth/Storage/function state,
credentials, caches, browser sessions, accounts, or hosted services. Concurrent DB branches therefore use
an already-approved isolated local stack; no skill commits port-only tracked config or resets another
worktree's stack.

Repository edits, local service startup, local reads, destructive local reset/data mutation, dependency
changes, hosted reads/writes, load, schema work, secrets access, Git, and production effects are distinct.
All migration paths prohibit `supabase db push`, linked/remote push, migration repair, remote-ledger
inspection for cleanup proof, and production application. CI owns post-merge application. Local mutation
is limited to an exact owned disposable stack and the approved local workflow.

Pending Migration Hygiene now has a usable proof ladder. Rewrite eligibility requires either observed
end-to-end provenance showing a version remained within the controlled run and named disposable local
stacks, or an authorized human attestation naming the exact versions and covering every non-disposable
environment and out-of-band apply path. An unmerged branch, main-only CI, absence from `origin/main`, a
recent timestamp, missing deployment record, or local-ledger absence is only corroborating negative
evidence. When proof is missing, retaining the file is a successful no-op; the skill never queries a
remote ledger to manufacture confidence.

Schema authoring now rechecks cross-worktree version collisions, preserves schema/DML separation and
mixed-version compatibility, treats local reset as destructive state, avoids unsafe concurrent-index
recipes without verified transaction semantics, and tests denied identities and changed functions.
Postgres analysis separates estimated `EXPLAIN` from executing `EXPLAIN ANALYZE`, bounds hosted/load/data
effects, and returns schema implementation to the migration skill. Supabase integration pins current
official documentation evidence and preserves privileged-function, claims, and RLS boundaries.

## Verification

- Focused Supabase routing and contract tests: 9 passed.
- Ship parent routing tests: 6 passed.
- All package-local links and handoff identifiers resolve through the shared workspace tests.
- Skill lint for all four packages: 0 critical and 0 warnings before route-index regeneration.

No Supabase service, Docker resource, port, local or hosted database, Auth/Storage/function state,
credential, migration ledger, production environment, worktree, Git history, or remote system was read
or changed.
