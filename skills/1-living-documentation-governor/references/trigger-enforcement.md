# Trigger enforcement

Triggers identify documentation obligations from a pinned change candidate. They do not establish
that a documentation edit is truthful.

## Candidate set

- Use the caller's explicit base/head or published PR endpoints; do not hard-code `origin/main`.
- For local implementation include caller-owned committed, staged, unstaged, and untracked paths.
- Detect renames/copies and consider both old and new paths where ownership may change.
- Never fetch, switch, reset, stash, or rewrite the worktree to calculate the set.
- Report missing base objects or a moving candidate instead of silently selecting another range.

## Map validation

Validate before matching:

- supported schema version and object shape;
- unique stable rule IDs;
- nonempty safe repository-relative path patterns and doc targets;
- no traversal, absolute paths, archive-only targets, duplicate/contradictory ownership, or missing
  canonical targets;
- patterns interpreted by an established, tested pathspec/glob library with documented semantics.

Do not implement globs by ad-hoc regex substitution. Test separators, `*` versus `**`, leading dots,
directories, negation if supported, Unicode, renames, and monorepo roots.

## Disposition

For every matched obligation require one of:

1. **Addressed:** a relevant canonical-doc delta whose claim is checked against changed behavior.
2. **Reviewed no-doc-impact:** a structured, reviewable attestation naming rule, rationale, owner, and
   optional expiry/follow-up.
3. **Unresolved:** fail or report the obligation, depending on the adopted enforcement phase.

Any edit to any mapped document is not enough. Empty/timestamp-only changes, unrelated wording, and
archive edits do not satisfy an obligation.

## Adoption and required-check honesty

Begin in report-only mode on representative changes, measure false positives/misses, then ratchet to
required enforcement with repository approval. A required check must emit a result for every required
PR path; do not make its context disappear behind path filtering. Validate the exact candidate CI
checks, and do not claim semantic correctness from a green trigger gate.

## Exemptions

Avoid untracked environment-variable or commit-message bypasses such as `DOCS_CHECK_SKIP=1` or
`[docs-skip]`. Prefer a visible, reviewable attestation with rationale and ownership. Emergency
override policy, if the repository has one, remains a human-controlled repository decision.
