# 07 — butler query op + retire ask-matt

**What to build:** “Which skill should I use?” is answered only by butler query from disk + flows.md; ask-matt is gone as a live router.

**Blocked by:** 06 — flows.md chaining SSOT

**Status:** ready-for-agent

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [ ] `query-workflow.md` fully specifies: load flows + bucket indexes + on-disk skills; never invent skills
- [ ] Query recommends a named skill or path and may note “why not” for cousins
- [ ] Manual smoke: at least 5 utterances map to expected skills (grill, to-spec, bug, vault, which-skill)
- [ ] `ask-matt` removed from discovery and tombstoned in deprecated with successor **butler**
- [ ] No remaining live references treating ask-matt as the router
