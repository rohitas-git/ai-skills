# 07 — butler query op + retire ask-matt

**What to build:** “Which skill should I use?” is answered only by butler query from disk + flows.md; ask-matt is gone as a live router.

**Blocked by:** 06 — flows.md chaining SSOT

**Status:** done

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [x] `query-workflow.md` fully specifies: load flows + bucket indexes + on-disk skills; never invent skills
- [x] Query recommends a named skill or path and may note “why not” for cousins
- [x] Manual smoke: at least 5 utterances map to expected skills (grill, to-spec, bug, vault, which-skill)
- [x] `ask-matt` removed from discovery and tombstoned in deprecated with successor **butler**
- [x] No remaining live references treating ask-matt as the router
