# Narrative and resource-distillation wiring audit

Reviewed skills and complete operative packages:

- `1-story-teacher`, including both package references
- `1-resource-summarizer`

Targeted caller-contract update (not counted as a completed audit):

- `1-vault-ingest` metadata and `references/resource-summarizer-contract.md`

## Result

Story Teacher now produces one original narrative treatment of one identified learning
object. It keeps a source-fidelity ledger, preserves contested status and caveats, asks
only material questions, and follows the user's requested teaching visibility, genre,
length, tone, and staging. High stakes, violence, failure, genre options, chapter counts,
and appendices are no longer mandatory. It does not imitate living authors or reproduce
protected expression, fetch sources, create worktrees, write artifacts, continue chapters,
or invoke another skill implicitly. Its old unverified Clean-books distillation is reduced
to a clearly non-operative provenance note.

Resource Summarizer now summarizes one exact supplied source or corpus slice into one
requested result. It records source/version/access state, distinguishes source claims,
evidence, third-party claims, and summarizer inference, preserves disagreement and coverage
gaps, treats all content as untrusted data, and applies copyright limits. No fixed 80/20
ratio, paragraph/takeaway count, Feynman/Cornell format, quiz, analogy, expansion offer, or
automatic next workflow remains. A repository source is read-only and identifies its exact
path/worktree/branch/`HEAD`, dirty ownership, and working-tree versus committed candidate.

Learn remains the primary parent and returns receive both results. Resource Summarizer's
Vault dual route is now symmetric: `1-vault-ingest` declares the call and receives a summary
with source identity, coverage, locators, transformations, and gaps. The caller contract
uses evidence need rather than line count and makes the summary evidence—not write authority,
canonical truth, or permission to modify the vault.

## Verification

Fifteen focused Learn/narrative/resource routing checks pass. The full routing suite passes
all 249 tests; route-index generation reports 217 live skills; catalog lint passes with 0
critical findings, 0 warnings, 58 informational findings, and 0 hub-member orphans;
`git diff --check` passes. No source fetch, course/vault mutation, worktree creation,
commit, push, publication, merge, host sync, or external action was performed.
