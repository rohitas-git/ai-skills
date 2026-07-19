# 12 — Polish: smoke fixtures, README, optional promotes, reflect bridge

**What to build:** The catalog is navigable in two minutes, smoke-checked, and meta skills hand off cleanly to butler; any remaining agent-skills promotes are intentional ingest only.

**Blocked by:** 07 — butler query; 08 — butler ingest; 09 — butler lint + organize; 11 — cousin budget vault SSOT

**Status:** ready-for-agent

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [ ] Root README quickstart: run setup-rohitas-skills (once per repo) → use butler for navigation / catalog ops
- [ ] Smoke fixture list documented (query utterances + expected skills; lint clean on promoted set or known exceptions)
- [ ] Optional `scripts/lint-skills` present if not done in 09, aligned with lint-checklist
- [ ] reflect / create-skill docs mention butler lint or ingest handoff
- [ ] Any selective agent-skills promote (security, ship, API, UI, etc.) only via butler ingest with flows.md update—or explicitly deferred with note in vendor README
- [ ] Success metrics from the spec are measurable (steward=butler, single tdd, no ask-matt, no setup-matt name in discovery, vendor dual-router offline)
