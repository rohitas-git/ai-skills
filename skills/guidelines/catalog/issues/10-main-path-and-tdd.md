# 10 — Main path craft, hard/soft deps, single tdd

**What to build:** The engineering main path is consistent on disk: grill wrappers, hard/soft setup pointers, implement→tdd→code-review story, and one canonical **tdd** skill (agent-skills TDD merged in, not a second skill).

**Blocked by:** 03 — setup-rohitas-skills; 04 — vendor and deprecations; 06 — flows.md chaining SSOT

**Status:** done

**Parent:** Spec issue https://github.com/rohitas-git/ai-skills/issues/1 · local `SPEC.md`

- [x] `0-grilling` is the interview SSOT; grill-me / grill-with-docs are thin wrappers (or equivalent single-body design)
- [x] `1-to-spec`, `1-to-tickets`, `0-triage` hard-dep one-liners point at `/0-setup-rohitas-skills` (not setup-matt-…)
- [x] Soft deps (tdd, diagnosing-bugs, improve-codebase-architecture) use CONTEXT/ADR if present only—no forced setup spam
- [x] Single `1-tdd` skill remains; useful ideas from vendor test-driven-development merged selectively; no second TDD skill in discovery
- [x] implement skill text (or flows) states it drives tdd then code-review
- [x] wayfinder / triage docs match flows (wayfinder exits via to-spec; do not re-triage to-tickets output)
