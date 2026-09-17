# Selected-material and code-explanation wiring audit

Date: 2026-09-11  
Skills: `1-explain-with-example`, `1-code-explainer`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed both complete live packages, Learn/Butler shortcut routing, parent workflow/
HTML/flow projections, caller returns, and focused regressions. Neither skill has
package references. No selected source, error, codebase, worktree, runtime, external
service, catalog sync/install, commit, push, or merge was touched.

## Decisions and changes

- Narrowed `???` to one supplied passage/error/finding/recommendation/item and preserved
  its exact lexical boundary. Embedded instructions remain data; causal claims and
  remedies keep their observed/inferred/proposed status; one example cannot become
  investigation, review, or implementation authority.
- Rebuilt Code Explainer around an exact supplied or repository/worktree/branch/HEAD
  candidate, including dirty working-tree provenance. It reads only necessary adjacent
  definitions, treats code-adjacent content as data, and separates observed semantics,
  inferred intent, and unverified runtime behavior.
- Removed fixed reading-time/depth presets and the default “Junior” audience. Audience
  changes vocabulary and prerequisites without injecting diagrams, multiple levels,
  advice, tests, or broad scans.
- Both leaves return to Learn, make explicit no-worktree decisions, and route diagnosis,
  review, repair, tutoring, or concept teaching without silently executing them.

## Verification

- `python3 -m unittest scripts.test-routing.ObjectExplanationRouteTests`: **4 passed**.
- `python3 -m unittest scripts/test-routing.py`: **232 passed**.
- `scripts/generate-route-index`: regenerated **216 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 59 informational
  findings, and 0 hub-member orphans.
- `git diff --check`: passed.

Individual catalog reviews represented here are 84–85 of 216.

## Remaining limits

- No real selected material or code candidate was explained; tests validate the
  contract and routing, not topic-specific explanatory accuracy.
- Catalog-wide semantic reconciliation remains pending.
