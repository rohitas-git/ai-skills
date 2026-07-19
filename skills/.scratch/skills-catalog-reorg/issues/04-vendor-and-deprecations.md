# 04 — Vendor park agent-skills + early deprecations

**What to build:** The nested agent-skills pack cannot co-route with the Rohitas catalog; toxic / superseded skills are tombstoned with successors named.

**Blocked by:** 02 — Skills rehoused into buckets

**Status:** done

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [x] `agent-skills/` tree lives under `vendor/agent-skills/` (or equivalent) and is excluded from default skill discovery
- [x] `using-agent-skills` is not loadable as a peer meta-router
- [x] `software-architecture` moved to `deprecated/` with successor note (e.g. codebase-design / improve-codebase-architecture / software-architect if kept)
- [x] `deprecated/README.md` lists tombstones and successors
- [x] Vendor README states “promote only via butler ingest”
