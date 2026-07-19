# 02 — Skills rehoused into buckets

**What to build:** Every live skill folder lives under the correct bucket; indexes and lock paths match reality so discovery uses the new layout.

**Blocked by:** 01 — Catalog buckets scaffold

**Status:** done

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [x] All skill directories (except vendor, buckets themselves, tooling) moved via git-aware moves into an assigned bucket
- [x] Bucket READMEs list each skill with a linked name and one-line description
- [x] Root README lists only promoted-bucket skills (no personal / in-progress / deprecated / vendor)
- [x] `skills-lock.json` paths updated for every locked skill that moved
- [x] Broken relative links inside moved skills fixed or noted
- [x] Short install note documents that skills now live under bucket paths (for multi-agent hosts)
