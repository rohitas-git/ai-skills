# Codebase-design wiring audit

Date: 2026-09-11  
Skill: `1-codebase-design`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the live `SKILL.md`, `DEEPENING.md`, `DESIGN-IT-TWICE.md`, agent metadata,
Architecture parent routes, and Ship caller routes. This verifies the skill's vocabulary,
decision process, workspace behavior, and catalog surfaces; it does not prove that a module
redesign is appropriate in a particular codebase without its concrete evidence.

## Decisions and changes

- Narrowed the atomic job to one module's internal interface, seam, cohesion, and depth.
  Public contracts, system architecture, repository-wide discovery, and implementation retain
  their existing owners.
- Moved the long glossary and heuristics into `references/vocabulary.md`, leaving a lean process
  in the main file and preserving established project/domain terminology.
- Replaced rigid claims—exactly one interface, exact vocabulary, method-count proxies, one-versus-
  two-adapter rules—with evidence-based heuristics about caller knowledge, locality, ownership,
  volatility, privilege, and change patterns.
- Corrected deepening guidance: pure/local code is not automatically mergeable; test doubles do
  not replace contract/integration evidence; external mocks prove only modeled behavior; old tests
  are removed only after replacement evidence preserves their useful coverage.
- Made Design It Twice local by default. Parallel sub-agents are allowed only when explicitly
  requested and independent, while code edits remain with the owning caller/worktree.
- Added design/advice, read-only assessment, and authorized implementation modes. Authorized work
  returns to Ship and reuses its workspace, conditionally invoking `1-git-worktrees`; design alone
  neither creates a worktree nor edits code.
- Added formal Ship membership and aligned parent metadata, dispatch body, workflow JSON, HTML,
  Architecture HTML, flows, and generated route index.
- Added regression checks for both parents, `next` metadata, HTML links, disclosure, workspace
  return, explicit delegation, coverage-preserving tests, and corrected Design It Twice behavior.

## Verification

- `python3 -m unittest scripts/test-routing.py`: **43 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 62 informational findings,
  and 0 hub-member orphans.
- `git diff --check`: passed.
- Main skill is below the 120-line lean target and links all operative supporting files.

## Remaining limits

- No concrete module candidate was supplied, so the design heuristics have not been exercised
  against application-specific coupling, performance, or migration constraints.
- The Architecture and Ship hubs still require their separate full semantic audits.
