# 04 — Vendor park agent-skills + early deprecations

**What to build:** The nested agent-skills pack cannot co-route with the Rohitas catalog; toxic / superseded skills are tombstoned with successors named.

**Blocked by:** 02 — Skills rehoused into buckets

**Status:** ready-for-agent

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [ ] `agent-skills/` tree lives under `vendor/agent-skills/` (or equivalent) and is excluded from default skill discovery
- [ ] `using-agent-skills` is not loadable as a peer meta-router
- [ ] `software-architecture` moved to `deprecated/` with successor note (e.g. codebase-design / improve-codebase-architecture / software-architect if kept)
- [ ] `deprecated/README.md` lists tombstones and successors
- [ ] Vendor README states “promote only via butler ingest”
