# One-source ingest checklist

The active contract is the parent `SKILL.md`. This checklist adds no authority.

| Phase | Required evidence |
|---|---|
| Pin | root SSOT, caller, exact source snapshot/coverage, requested outcome, authority |
| Orient | active schema/index locations and optional Git/worktree/dirty candidate |
| Reconcile | minimum plausible existing notes plus source/user/existing/synthesis ledger |
| Plan | exact create/update/link/archive/consume/log items and files intentionally unchanged |
| Gate | unresolved conflicts, destructive handling, sensitive persistence, schema expansion |
| Apply | last-moment target/source recheck and smallest authorized edits |
| Verify | containment, syntax, touched links/locators, ledger coverage, idempotence |
| Return | applied/unapplied deltas, conflicts, gaps, versions, and caller continuation point |

An explicit “ingest this” request permits fitting non-destructive permanent-note writes. It
does not implicitly permit fetching an unspecified source, processing all Inbox items,
deleting/moving the capture, archiving a full source, changing top-level schema, installing
plugins, publishing, syncing, or Git operations.

If application is partial, preserve the observed state. Do not restore stale snapshots over
concurrent edits or claim transactionality across independent files. Report the exact last
successful write and the remaining ledger so the caller can safely resume.
