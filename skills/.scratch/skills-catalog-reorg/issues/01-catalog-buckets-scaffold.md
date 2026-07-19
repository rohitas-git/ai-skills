# 01 — Catalog buckets scaffold

**What to build:** The skills catalog root has Matt-style buckets and rules so a human or agent can see where skills are *supposed* to live—even before every skill is moved.

**Blocked by:** None — can start immediately.

**Status:** ready-for-agent

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [x] Six bucket directories exist: `engineering/`, `productivity/`, `misc/`, `personal/`, `in-progress/`, `deprecated/`
- [x] Each bucket has a `README.md` stub (title + purpose line; skill list may be empty)
- [x] Root `README.md` states the promotion rule: only engineering + productivity + misc are listed as promoted
- [x] `CLAUDE.md` (or `AGENTS.md` if that is the house file) records Matt’s bucket rules in short form
- [x] `vendor/` directory exists (empty or with placeholder README) as the future home for non-discovered packs
