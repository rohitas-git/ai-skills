# Clean-craftsmanship wiring audit

Date: 2026-09-11  
Skill: `1-clean-craftsmanship`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete 147-line prior main skill and 265-line book distillation, Architecture
parent routes, F-C1 surfaces, catalog descriptions, and worktree/caller behavior. This audit
verifies principle-level guidance and routing; it does not enforce a philosophy on application code.

## Decisions and changes

- Kept one atomic job: explain maintainability and Clean Code/Clean Architecture principles with
  context, trade-offs, and low-risk next steps. Repository enforcement, module design, system
  review, diagnosis, and detailed failure policy retain their specialist owners.
- Reduced the main skill below the 120-line lean target and added direct triggers, exclusions,
  caller return, no-worktree/no-edit authority, and F-C1 behavior.
- Added `references/principles.md` as the operative, context-sensitive guide. It treats function
  size, argument count, abstractions, adapters, dependency direction, purity, comments, and SOLID
  as evidence-dependent heuristics rather than universal thresholds.
- Made tests proportional to risk and oracle quality: TDD fits known deterministic behavior at an
  agreed seam, while exploratory/probabilistic work may need specification, prototypes, evals, or
  characterization first. Agent-authored tests are not independent proof of their own code.
- Preserved the long book distillation as historical source context and clearly marked it non-
  operative because it contains prescriptive/datable claims. Removed the non-portable attachment
  dependency from live instructions.
- Prevented scope creep: the skill suggests edits/tests/measurements only when they address the
  stated risk, then hands actual edits to the appropriate implementation/review owner.
- Updated README/wiki descriptions and added routing tests for lean shape, advice-only/worktree
  boundaries, historical-source status, adapted principles, and F-C1 parent consistency.

## Verification

- `python3 -m unittest scripts/test-routing.py`: **57 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 62 informational findings,
  and 0 hub-member orphans. The previous `lean-soft` finding for this skill is gone.
- `git diff --check`: passed.
- All operative and historical package files were read; local links resolve through the catalog gate.

## Remaining limits

- No concrete code-quality decision was supplied, so the adapted heuristics were not evaluated
  against application-specific performance, legacy, team, or delivery constraints.
- Other Architecture style/design children remain semantically pending.
