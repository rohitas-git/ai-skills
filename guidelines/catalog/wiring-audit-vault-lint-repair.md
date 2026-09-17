# Vault lint and repair wiring audit

Reviewed skills and complete operative package:

- `1-vault-lint`
- `references/lint-checklist.md`
- `references/karpathy-lint-principles.md`
- new `1-vault-repair`

## Result

Vault Lint is now strictly read-only. It pins the configured root, requested scope/checks,
privacy boundary, evidence cutoff, snapshot identity, and optional Git repository/worktree/
branch/`HEAD`/dirty candidate. It inventories names/metadata first and reads only what the
selected checks need. Notes and plugin/query output are private untrusted data; no code,
links, attachments, web sources, tools, or state are followed implicitly.

Every finding carries a stable ID, severity, exact locator, observation, active invariant,
impact, confidence/limits, and owning action. Check definitions distinguish broken links from
aliases/anchors, schema defects from variants, overlaps from title similarity, contradictions
from differing conditions, and topological orphans from actual defects. Sampling declares its
population and cannot prove uninspected areas clean; changed evidence makes a finding stale.
The old periodic/automatic LLM-wiki checklist is historical only.

Vault Repair consumes exactly one accepted finding. It revalidates the original snapshot and
current targets before any write; stale, conflicting, or unsupported findings produce no
change. It changes only approved files/hunks, preserving dirty user work. Rename/move/delete,
merge/split, source consumption, schema expansion, `.obsidian/`, and other high-impact effects
need explicit action-specific authority. Knowledge/provenance changes route to Vault Ingest.
Targeted reproduction proves only that finding; Repair never claims the full vault is clean or
starts another audit.

Both skills create no worktree and treat sync clients, plugins, accounts, and services as
shared. Neither installs, logs, syncs, commits, publishes, pushes, or merges. Parent metadata,
workflow JSON, HTML, Butler flows, wiki index, and caller returns expose the split.

## Verification

- Focused routing/contract tests: 16 passed.
- Full routing suite: 288 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 57 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No vault read/write, worktree operation, source research, plugin/sync action, Git action,
host sync, publication, or external action was performed.
