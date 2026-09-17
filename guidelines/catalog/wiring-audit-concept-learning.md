# Concept-learning pipeline wiring audit

Date: 2026-09-11  
Skills: `1-learning-explainer`, `1-learning-diagnostic`, `1-level-explainer`,
`1-mental-model-builder`, `1-progressive-deep-dive`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed all five live skill bodies, the complete shared reference package, Learn and
Vault memberships, direct/caller-return handoffs, and focused routing/reference
regressions. No teaching session, source research, repository, vault, worktree,
external service, catalog sync/install, commit, push, or merge was performed.

## Decisions and changes

- Kept Learning Explainer as a compatibility router that selects exactly one diagnostic,
  first explanation, mental model, or one-layer deep dive. It now carries Learn/Vault
  caller identity and prevents audience/depth cues from granting research authority.
- Made Learning Diagnostic reuse supplied evidence, ask only one material question at
  a time, prefer demonstrated work over numeric self-rating, avoid demographic ability
  inference, and return a non-persisted evidence-labeled profile.
- Made Level Explainer change vocabulary/prerequisites without changing truth, source,
  safety, or scope standards. Examples and limitations are conditional, not rituals.
- Required Mental Model Builder to expose one relationship, one prediction/use, and
  the model's breaking point; rendered diagrams remain a separately requested artifact.
- Limited Progressive Deep Dive to one identified target and one layer per invocation;
  “deep” no longer authorizes browsing, audience escalation, adjacent topics, or an
  automatic next interaction.
- Replaced the 13-file shared library's fixed sentence counts, mandatory probes/models/
  confidence scores, uncited topic facts, automatic search, and “always offer” rules
  with compact audience, evidence, model, layer, CLT, example, and template guidance.

## Verification

- `python3 -m unittest scripts.test-routing.ConceptLearningRouteTests`: **7 passed**.
- `python3 -m unittest scripts/test-routing.py`: **228 passed**.
- `scripts/generate-route-index`: regenerated **216 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 59 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

Individual catalog reviews represented here are 79–83 of 216.

## Remaining limits

- Actual explanation quality varies by topic and evidence; this audit verifies the
  workflow contract, not factual mastery across domains.
- Other Learn leaves remain individually pending.
- Catalog-wide semantic reconciliation remains pending.
