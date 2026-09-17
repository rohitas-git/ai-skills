---
name: 1-pending-migration-hygiene
description: >
  Consolidate, rewrite, or remove only migration versions proven never applied outside disposable/local
  environments. Otherwise retain them or append a forward migration. Not for feature deprecation or
  remote-ledger inspection/application. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when: ["clean redundant or superseded pending migration files with rewrite proof"]
    not_when:
      - "application outside disposable/local is possible → retain or append forward"
      - "retire a feature or API → 1-deprecation-and-migration"
      - "inspect, repair, or apply a remote ledger → prohibited"
    prev: [0-implement, 1-supabase-schema-migration]
    next: [0-implement, 1-supabase-schema-migration, 1-atomic-git-commits]
    cousins: [1-supabase, 1-supabase-schema-migration, 1-supabase-postgres-best-practices, 1-deprecation-and-migration]
    triggers: [pending migration hygiene, consolidate pending migrations, squash unapplied migrations, remove redundant migration, clean pending SQL migrations]
    requires_setup: false
---

# Pending Migration Hygiene

Reduce redundant pending migration files **only** when every target version is proven never applied
outside disposable/local environments. Missing proof produces a successful retention/no-op outcome.

## Boundary

| Need | Route |
|---|---|
| Rewrite/remove proven-unapplied pending files | **this skill** |
| Add a compatible change when application is possible | `/1-supabase-schema-migration` |
| Retire an application feature/API | `/1-deprecation-and-migration` |
| Inspect or repair a remote migration ledger | prohibited here |

## Contract and proof

1. Pin caller, cleanup intent/non-goals, exact repository/worktree/branch/`HEAD`, dirty ownership, base/
   head or working-tree candidate, target versions and hashes, migration conventions/ledger snapshot,
   known environments/apply paths, evidence cutoff, local-stack identity/owner, protected references,
   tests, and repository, local-DB, Git, remote, and production authority.
2. Build a per-version proof ledger: origin, all commits/branches/remotes/releases/CI artifacts known to
   contain it, every possible apply path/environment, local applications, out-of-band possibility,
   supporting evidence, and disposition. Accept rewrite proof only from either:
   - observed end-to-end provenance: the version was created in the controlled current run and evidence
     shows it was never committed, pushed, exported, or applied except to named disposable local stacks; or
   - an authorized human attestation naming the exact versions and confirming coverage of every
     non-disposable environment and out-of-band apply path.
   Repository/CI evidence may corroborate that proof but cannot replace missing environment coverage.
3. An unmerged branch, main-only CI, absence from `origin/main`, no deployment record, a recent timestamp,
   or a local ledger miss is negative evidence only. None alone proves no manual/out-of-band application.
   Never query a linked/remote ledger to close the gap. Ask for the bounded attestation or retain the file.
4. A worktree does not isolate migration versions, remotes, CI/deploy history, Docker resources, project
   IDs, ports, databases, Auth/Storage/function state, or local ledgers. Never reset another worktree's
   stack or infer environment history from the current checkout.

## Process

1. Classify each file by one schema or one data purpose. Consolidate only same-purpose files and never
   fold DML/backfills/seeds/transformations into DDL merely to reduce count.
2. Search exact filenames, versions, objects, function signatures, and assumptions across code, tests,
   docs, scripts, CI, generated inventories, fixtures, migration tooling, Git history, and task-owned
   untracked files. A pinned reference is a dependency to assess and intentionally update—not automatic
   proof of application and not permission for broad cleanup.
3. If every target passes the proof ledger, create the smallest replacement sequence and update only
   references made stale by it. Recheck hashes, dirty ownership, version collisions, and references
   immediately before writing. Otherwise preserve the files and report a no-op with exact missing proof.
4. Verify from scratch only on the named disposable local stack using the repository-approved local
   workflow. Local reset/recreate is destructive and requires exact ownership. Exercise schema/data
   outcomes, allowed and denied identities, upgrade order where relevant, and every changed function
   with representative and failure inputs—not merely successful creation.
5. Return caller, candidate/worktree, proof ledger, retained/rewritten/removed files, reference updates,
   local-stack actions, verification, limitations, and unperformed remote/Git work. If a commit is
   authorized, keep cleanup separate from feature work via `/1-atomic-git-commits`; do not start it,
   push, repair, inspect remote ledgers, or apply remotely automatically.

## Hard stops

- Any target lacks complete observed provenance or exact authorized human attestation.
- DDL and DML would be combined, a stale reference remains, or a concurrent version collision exists.
- The exact disposable local stack is not owned, or from-scratch/function/security verification fails.
- The proposed next action is remote inspection, linked push, migration repair, or production apply.
