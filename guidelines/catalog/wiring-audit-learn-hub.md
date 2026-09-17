# Learn hub and Tutor wiring audit

Date: 2026-09-11  
Skills: `0-learn`, `1-tutor`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed Learn's complete live package, parent flow projections, workflow/HTML/
manifest artifact routes, all child memberships, and the former tutor-mode reference.
Also checked targeted references from Code Explainer, Learning Diagnostic, and Resource
Summarizer that named the old hidden mode. Other Learn leaves remain individually
pending. No learning source, vault, codebase, worktree, external service, catalog
install/sync, commit, push, or merge was touched.

## Decisions and changes

- Reduced Learn to a read-only one-leaf router with exact caller-return payload. Clear
  concept, selected-material, practice, code, course, story, summary, and Vault intent
  route directly; F-L1 appears only for material deliverable ambiguity.
- Reframed F-L2 as detail versus distillation rather than silently summarizing a
  source because it is “huge.” F-L3 remains owned by Learning Explainer and is not
  reimplemented in the hub.
- Promoted hidden tutor behavior from a duplicated hub reference into new atomic
  `1-tutor`. It handles one bounded interactive problem with a progressive hint ladder,
  learner-response waits, transfer evidence, assessment integrity, no-worktree
  semantics, and optional—not automatic—progress recording.
- Replaced the old tutor reference with a compatibility pointer and rewired Code
  Explainer, Learning Diagnostic, Resource Summarizer, workflow JSON, flow SSOT, HTML,
  and flows chart to the live leaf.
- Expanded hub metadata to the exact workflow child union plus Butler return, repaired
  stale hub paths, and made every HTML child link navigable.

## Verification

- `python3 -m unittest scripts.test-routing.LearnHubRouteTests`: **7 passed**.
- `python3 -m unittest scripts/test-routing.py`: **221 passed**.
- `scripts/generate-route-index`: regenerated **216 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 59 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

This adds one live skill; individual reviews represented here are 77–78 of 216.

## Remaining limits

- Learn's other children retain their own pending semantic audits; parent parity does
  not prove those procedures correct.
- The new Tutor skill was contract-tested, not exercised with a real learner session.
- Catalog-wide semantic reconciliation remains pending.
