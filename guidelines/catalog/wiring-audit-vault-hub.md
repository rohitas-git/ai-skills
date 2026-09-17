# Personal Vault hub wiring audit

Reviewed skill and complete operative package:

- `0-rohitas-vault-wiki`
- all nine files under `references/`
- Vault workflow JSON, hub HTML, and Butler flow section

Targeted caller correction (not counted as another audit):

- `1-setup-vault-root` now returns to either Setup or the requesting Vault hub

## Result

The Vault parent now selects exactly one operation. Clear requests route directly to root
setup, capture, ingest, lint, query, Concept explanation, Markdown, CLI, Bases, bounded source
summary, or Concept-pedagogy routing. F11 and F-D2 are asked only for material operation or
destination ambiguity. The hub itself reads/writes nothing, creates no worktree, invokes no
tools, and returns one leaf result to Butler or the actual caller without automatic
capture→ingest→explain→lint behavior.

Every handoff preserves the configured-root source, exact target and candidate version,
read/write/external authority, privacy limits, dirty ownership, and, when Git applies,
repository/worktree/branch/`HEAD` plus working-tree versus committed content. Notes, links,
embeds, queries, and imports are private untrusted data. Worktrees are explicitly not treated
as isolation for sync clients, plugins, accounts, or remote services.

The reference package shrank from 714 to 158 lines. It now supplies only bounded schema,
layout, property, safety, ownership, query, format/plugin compatibility, and historical
provenance contracts. Removed behavior includes fixed line/takeaway/paragraph quotas,
English-only content, weekly cleanup, mass frontmatter/link changes, automatic offers/writes,
assumed Dataview installation, generic syntax duplication, hard-coded host/global paths, and
an operative historical seed map. The active vault always wins over catalog defaults.

Workflow metadata, HTML, and Butler flows expose the same live children, current local links,
direct pipeline, and material-only forks. The root-setup leaf has a symmetric Vault caller
return.

## Verification

Sixteen focused Vault-hub/bridge checks and the affected Setup return checks pass. The full
routing suite passes all 265 tests; route-index generation reports 217 live skills; catalog
lint passes with 0 critical findings, 0 warnings, 58 informational findings, and 0 hub-member
orphans; `git diff --check` passes. No vault access or mutation, setup write, worktree
creation, plugin/host operation, Git action, publication, sync, or external action was
performed.
