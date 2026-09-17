# Presentation-mode wiring audit

Date: 2026-09-11  
Skills: `1-response-effort-calibrator`, `1-caveman`, `1-bro`, `1-quick-recap`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the four complete live packages, every linked local reference, Butler
membership, workflow JSON, HTML, flow map, metadata handoffs, and focused routing
regressions. The archived Quick Recap snapshot and Bro/Caveman vendor examples were
treated as provenance or style examples, not operative authority. No consumer repo,
worktree, task, external service, catalog installation/sync, commit, push, or merge
was touched.

## Decisions and changes

- Made all four explicit presentation leaves with Butler caller-return wiring.
  Presentation choices cannot change substantive scope, acceptance criteria,
  evidence, verification, safety, authority, or required final structure.
- Replaced fixed word/sentence/search quotas in response calibration with qualitative
  levels. Detail no longer authorizes research or tools, and brevity cannot hide
  uncertainty, skipped checks, or safety requirements.
- Narrowed Caveman triggers to explicit style intent. Generic token or concise cues
  stay with the effort calibrator; compression preserves technical and permission
  semantics and performs no task or workspace action.
- Made Bro target exactly one prior assistant reply or user-identified excerpt,
  route new topics directly without a forced question, preserve caveats and evidence,
  and distinguish corrections from re-expression. Vendor examples are style-only.
- Made Quick Recap evidence-driven without conflating its red display label with a
  task/goal `blocked` status. The historical source is no longer reread as live
  instructions, and higher-priority final suffixes remain intact.

## Verification

- `python3 -m unittest scripts.test-routing.PresentationModeRouteTests`: **7 passed**.
- `python3 -m unittest scripts/test-routing.py`: **199 passed**.
- `scripts/generate-route-index`: regenerated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 61 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

Individual catalog reviews represented by this document are 65–68 of 215.

## Remaining limits

- These modes depend on truthful status from the owning substantive workflow; they
  do not independently verify the underlying work.
- Parent Butler has already been audited, but catalog-wide semantic reconciliation
  remains pending.
