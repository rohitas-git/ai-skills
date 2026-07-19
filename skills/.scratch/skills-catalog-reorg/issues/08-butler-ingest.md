# 08 — butler ingest op + integration gate

**What to build:** Adding or promoting a skill goes through butler ingest: integration test, proposed placement/chain, human confirm, then index/lock/flows updates—without creating wiki atoms.

**Blocked by:** 05 — butler spine; 06 — flows.md chaining SSOT

**Status:** ready-for-agent

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [ ] `ingest-workflow.md` covers draft path, existing folder, and vendor candidate
- [ ] Integration test enforces: gap, no collision/prefer merge, prev/next, hard/soft setup, Matt-short or disclosure plan, never using-agent-skills
- [ ] Dry-run mode proposes plan without writing
- [ ] On confirm: placement, README lines, flows slot if any, skills-lock if needed, then lint handoff
- [ ] Documented handoff: create-skill → butler ingest
- [ ] Demo: dry-run ingest of one vendor candidate or fixture skill shows pass/fail of integration test
