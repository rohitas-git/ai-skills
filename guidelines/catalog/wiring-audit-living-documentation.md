# Living-documentation-governor wiring audit

Date: 2026-09-11  
Skill: `1-living-documentation-governor`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete main skill, every operative reference and example JSON, the full historical
vendor source, Architecture and Ship parent bodies/HTML/workflows/flows/generated routes, catalog
descriptions, worktree/hook behavior, and regression coverage. This audit validates the governance
workflow; it does not install a checker/hook or evaluate another repository's docs.

## Decisions and changes

- Kept one atomic contract: align one pinned code/configuration candidate with its canonical current
  documentation, or return evidence of drift. Concept wikis, inline/API comments, design-time ADRs,
  CI implementation, and changelogs retain their owners.
- Added the missing Ship membership while retaining Architecture ownership. Design/assessment can
  start from Architecture; scoped code-adjacent doc updates inherit the Ship worktree/candidate and
  return to its build path. Both parent surfaces now agree.
- Added candidate provenance covering repository, exact worktree/branch/HEAD, explicit PR/base/head,
  task-owned committed/staged/unstaged/untracked paths, dirty ownership, mode, and caller. The skill
  creates no worktree, switches no branch, fetches no base, and stashes no work.
- Separated read-only drift assessment, scoped documentation update, and enforcement design.
  Implementing a checker, CI job, or hook requires the requested Ship/CI workflow; missing tooling is
  never initialized automatically.
- Replaced the universal source-precedence ladder with claim-specific authority: pinned code/tests for
  repository implementation, schemas/specs for public contracts, accepted decisions for rationale,
  and runtime/deployment evidence for deployed behavior. Archive remains historical.
- Introduced an obligation ledger. Path matches identify candidate obligations; a filename/no-op edit
  does not prove semantic alignment, and a behavior change may require docs even when a pattern misses
  it. Each obligation must be addressed, explicitly attested with reviewable rationale/owner, or remain
  unresolved.
- Removed the unsafe ad-hoc glob-to-regex example. Trigger maps now require a tested pathspec/glob
  implementation, safe paths, stable IDs, existing current-doc targets, rename handling, exact caller
  candidate semantics, and explicit coverage limits.
- Removed hard-coded `origin/main`, environment/commit-message skip bypasses, and path-filtered
  required-check gaps. Required contexts must report on every required PR path, while green mechanical
  checks remain limited evidence rather than proof of truthful docs.
- Reversed the automatic hook recommendation. Tracked checker + CI/direct command come first. Hook
  installation is separate authority because linked worktrees may share Git common-dir hooks and
  `core.hooksPath`; existing hooks can never be overwritten as a docs side effect.
- Replaced universal README/page/diagram/language/ADR rules with repository-sensitive baselines.
  Diagrams are conditional, README sections are evidence-backed, and ADR signals return to
  `1-domain-modeling` without inventing alternatives or rewriting accepted history.
- Simplified read-only Q&A to answer + relevant evidence + actual gaps; empty headings and automatic
  persistence prompts are gone.
- Marked the full vendor guide historical/non-operative and reduced the package from 982 to 674 lines;
  every operative Markdown reference is at most 59 lines.
- Prohibited source edits, unrelated doc normalization, installs, branch mutation, commit, publication,
  deployment, merge, and remote/shared-service mutation.

## Verification

- `python3 -m unittest scripts/test-routing.py`: **83 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 64 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- `LivingDocumentationRouteTests` covers both parent surfaces, caller/candidate/worktree authority,
  trigger honesty, required-check presence, worktree-shared hook safety, example-map bypass removal,
  operative reference size, optional diagrams, lean Q&A, and historical-source status.

## Remaining limits

- Trigger semantics and canonical ownership depend on each target repository and need project-level
  tests before enforcement.
- Other Architecture/Ship children remain semantically pending.
