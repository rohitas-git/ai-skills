# Vault Explain wiring audit

Reviewed skill and complete operative package:

- `1-vault-explain`
- `references/explain-from-concept.md`

Targeted parent/caller corrections (not counted as complete audits):

- `0-rohitas-vault-wiki` metadata, dual-skill text, profile, workflow, and HTML links
- `1-vault-ingest` declared handoff from the preceding batch
- Butler Vault/Learn flow handoff

## Result

Vault Explain is now one source-binding bridge. It resolves an exact configured vault and
one Concept, rejects traversal and symlink escape, records the observed note version, and,
when Git-backed, pins repository/worktree/branch/`HEAD`, dirty ownership, and working-tree
versus committed content. Ambiguous resolution inspects filenames/index only before asking;
it does not search all private bodies or infer an unnamed “last note.”

Only the selected Concept is read. Frontmatter, body, links, embeds, and comments are private
untrusted data. The bounded packet to `1-learning-explainer` carries source-backed claims,
conflicts, uncertainty, omissions, locators, learner request, and separately labeled outside
context. Learning Explainer selects one leaf and returns through Vault Explain to the actual
Vault or Learn caller. The bridge no longer reinstates probes, confidence scores, fixed
neighbor reads, forced English, summaries for long notes, or automatic offers/captures.

Explaining grants no vault mutation. Corrections, ingest, saved analogies, progress records,
and gaps require a separate request and workflow. The skill creates no worktree and touches
no plugin/sync state; it explicitly notes that worktrees do not isolate accounts, plugins,
sync clients, or services.

## Verification

Fifteen focused Vault-Explain/Learn checks pass. The full routing suite passes all 257
tests; route-index generation reports 217 live skills; catalog lint passes with 0 critical
findings, 0 warnings, 58 informational findings, and 0 hub-member orphans;
`git diff --check` passes. No vault read/write, worktree creation, Git operation, host sync,
browsing, publication, or external action was performed.
