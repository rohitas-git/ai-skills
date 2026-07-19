# 09 — butler lint + organize ops

**What to build:** Catalog health-check and rehousing are first-class butler ops with a severity report; optional script may mirror the same checklist later.

**Blocked by:** 05 — butler spine

**Status:** done

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [x] `lint-checklist.md` covers: name==dir, frontmatter, bucket/README membership, root promotion rule, model-invoked budget, trigger collisions, hard-dep `/setup-rohitas-skills` on to-spec/to-tickets/triage, forbidden names, broken links, vault SSOT, sprawl, deprecated successors
- [x] Lint produces a structured report by severity (not only free prose)
- [x] Organize op: move/rename/deprecate updates indexes + flows + tombstones with confirm-before-write
- [x] After a successful lint on the real catalog, critical findings are either fixed or filed as follow-ups
- [x] (Optional in this ticket or 12) `scripts/lint-skills` mirrors the checklist for non-LLM runs
