# Vault Ingest wiring audit

Reviewed skill and complete operative package:

- `1-vault-ingest`
- all five files under `references/`

## Result

Vault Ingest now reconciles one fixed, materialized source snapshot or coherent capture set
with the minimum permanent-note change set. It pins source version/hash/provenance/coverage,
configured root, caller, privacy and authority, plus repository/worktree/branch/`HEAD`, dirty
ownership, and working-tree candidate when Git applies. It creates no worktree and does not
mistake worktrees for isolation of sync clients, plugins, accounts, or services.

Source, user, existing-note, synthesized, conflicting, unknown, and sensitive claims remain
distinct. Retrieval starts with the minimum indexes/titles/metadata and opens only plausible
targets; filenames or keywords alone cannot trigger a merge. Every create, update, link/index
change, source archive, Inbox consume/move/delete, and log entry is an explicit ledger item.
The ingest request authorizes fitting non-destructive note writes, while conflicts,
destructive source handling, sensitive persistence, schema/top-level changes, and broader
multi-note scope pause for a decision.

Targets and source versions are rechecked immediately before writing. The leaf preserves
voice, metadata, provenance, and unrelated edits, verifies every resulting file and touched
link, and reports exact applied/unapplied state after partial failure rather than claiming a
cross-file transaction or restoring stale snapshots. Archive, source consumption, Inbox
emptying, unrelated index edits, lint, explanation, Git, publication, and sync are never
automatic.

The URL boundary allows a single read-only fetch only for an explicitly ingested URL, never a
URL merely present in capture content; it prohibits login/paywall bypass, installs, page-code
execution, broad crawling, unauthorized copying, and silent source substitution. The summary
handoff preserves one snapshot and grants no write authority. Historical compiler principles
are now explicitly non-operative.

## Verification

Twenty-three focused Ingest/Inbox/Vault-hub checks pass. The full routing suite passes all
280 tests; route-index generation reports 217 live skills; catalog lint passes with 0
critical findings, 0 warnings, 57 informational findings, and 0 hub-member orphans;
`git diff --check` passes. No vault/source access or mutation, URL fetch, worktree operation,
Git action, plugin/sync action, host sync, publication, or external action was performed.
