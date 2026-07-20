# 05 — butler spine (four ops, no atoms)

**What to build:** A user-invoked **butler** skill exists as catalog steward: thin dispatcher + reference stubs for query, ingest, lint, organize; hard rules forbid wiki atoms and dual routers.

**Blocked by:** 02 — Skills rehoused into buckets

**Status:** done

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [x] `productivity/0-butler/` (or assigned bucket) contains `SKILL.md` with session start + op dispatch (~80–120 lines)
- [x] `disable-model-invocation: true`; triggers include which-skill / ingest / lint / organize language
- [x] Reference stubs exist: `catalog-layout.md`, `flows.md`, `ingest-workflow.md`, `lint-checklist.md`, `query-workflow.md`, `hard-rules.md`
- [x] Hard rules state: no concept atoms; confirm before multi-file mutate; never promote `using-agent-skills`
- [x] Butler listed in productivity bucket README and root README (promoted)
- [x] Does not replace `1-writing-great-skills`, `1-create-skill`, or `1-session-skill-reflect`—only cites handoffs to them
