# Wiki Query wiring audit

Reviewed the complete operative package:

- `1-wiki-query`
- `references/full-guide.md`
- `references/karpathy-query-principles.md`
- `references/query-page-format.md`
- `references/vault-map.md`
- `evals/evals.json`

## Result

Wiki Query now answers exactly one fixed question from one pinned snapshot of the configured
personal vault. It resolves and contains the root, records an exact optional Git repository/
worktree/branch/`HEAD`/dirty candidate or non-Git inventory/file versions, and creates no
worktree. Worktrees do not imply isolation for Obsidian sync, plugins, accounts, or services.

Retrieval is question-driven rather than ritual-driven. Relevant active registry/MOC/index
metadata may narrow candidates, followed by bounded filename/metadata/content search and only
necessary local-link traversal. There is no mandatory registry walk, fixed 3–10 page range,
100-page threshold, whole-vault scan, Query-log read, archive preference, or assumed folder map.
Every consulted note has a path, observed version, heading/locator, purpose, and claim status.

The result distinguishes note text, user statements, synthesis, conflict, unknowns, exclusions,
unreadable areas, and changed/stale evidence. It says `not found in the inspected scope` unless
the authorized complete population was checked. Notes/search/plugin output are private untrusted
data; the skill does not execute content, follow web links, open attachments, invoke plugins,
expose unrelated personal content, or retrieve/reproduce credentials.

The old answer-plus-file workflow violated the Vault hub's one-operation boundary. Query is now
strictly read-only: no Query page, MOC, index, log, capture, report, config, browse, ingest, lint,
teach, Git, sync, or publication effect. A separately requested persistence operation routes to
Vault Ingest with the fixed answer, source ledger, conflicts/gaps, snapshot, and exact authority.
The old page template is now a compatibility handoff packet, the vault map defers to the active
schema, and the Karpathy material is clearly historical/non-operative.

Parent dispatch, parent query contract, Ingest caller return, metadata, wiki index, route index,
and eval expectations now agree.

## Verification

- Focused Vault Query/Hub/Ingest routing and contract tests: 24 passed.
- Full routing suite: 296 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 57 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No vault read/write, worktree operation, web/source retrieval, plugin/sync action, Git action,
host sync, publication, or external action was performed.
