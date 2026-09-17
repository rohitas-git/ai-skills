# Vault Inbox wiring audit

Reviewed skill and complete operative package:

- `1-vault-inbox`
- `references/inbox-note-format.md`

## Result

Vault Inbox now captures exactly one item already supplied by the user/caller into one new
Inbox file. A URL remains text and embedded instructions remain data; the skill never fetches,
summarizes, classifies, validates, links, or ingests the payload. If the caller asked for a
later ingest too, capture returns first with exact identity so the caller can separately
select `1-vault-ingest`.

The leaf resolves the configured root canonically, proves the Inbox destination remains
inside it, and returns to the Vault hub when setup is missing. Git-backed vaults preserve
repository/worktree/branch/`HEAD`, dirty ownership, allowed path, and scoped diff; no worktree
is created or switched. Worktrees are not treated as isolation for sync clients, plugins,
accounts, or services.

Sensitive-data ambiguity triggers a pause or proposed redaction rather than a false claim
that the vault is private or encrypted. Filenames follow the active convention, reject
traversal/platform-invalid input, and use a case-insensitive last-moment collision recheck
plus exclusive create. Existing notes are never overwritten, appended, or merged. Metadata
is minimal and truthful; the body preserves literal text/newline intent and records any
redaction or filename transformation. The result is re-read and verified for containment,
payload, syntax, collision, and exact scope.

## Verification

Fifteen focused Inbox/Vault-hub checks pass. The full routing suite passes all 272 tests;
route-index generation reports 217 live skills; catalog lint passes with 0 critical findings,
0 warnings, 58 informational findings, and 0 hub-member orphans; `git diff --check` passes.
No vault read/write, source fetch, worktree operation, Git action, plugin/sync action, host
sync, publication, or external action was performed.
