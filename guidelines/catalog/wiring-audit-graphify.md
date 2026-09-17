# Graphify wiring audit

Date: 2026-09-11  
Skill: `1-graphify`  
Status: reviewed; final catalog sweep pending

## Evidence boundary

Reviewed the complete live skill, Architecture parent body/HTML/workflow/flow and generated route,
the archived source ledger, upstream command/help implementation relevant to extract/output/query
behavior, and routing regressions. The upstream repository remains archived and non-operative; this
audit does not install or execute Graphify against a project.

## Decisions and changes

- Kept one explicit satellite job: extract or interrogate one approved local code graph. General
  review, architecture decisions, project wikis, and hand-authored diagrams retain their owners.
- Preserved explicit-only invocation under Architecture and aligned the parent workflow/HTML/flow
  description with corpus, worktree, output-ownership, and freshness requirements.
- Corrected the command contract: the live CLI has `extract`, `query`, `path`, and `explain`; it does
  not have a `build` subcommand. The argument hint and examples now use the actual command surface.
- Added caller/candidate provenance: resolve corpus and graph paths; record repository root, exact
  worktree/branch/HEAD, dirty ownership, output path, CLI version, mutation state, and exclusions.
  Graphify creates no worktree and cannot switch branches.
- Isolated artifacts per worktree. Before extraction, inspect the output and Git state; never share
  one mutable graph across worktrees, overwrite unknown/user-owned artifacts, or use `--force` or
  `--allow-partial` without separate evidence-based authority.
- Made the default extraction command explicit and local: `graphify extract <absolute-corpus>
  --code-only --out <approved-output>`, subject to the installed version's help. Repository ignore
  rules remain active unless the user expressly includes ignored material after a privacy decision.
- Removed implicit setup paths. If the executable is absent, stop; do not invoke `uvx`, `pip`, or
  another downloader. Installers, hooks, strict/always-on rules, remote backends, graph stores,
  watchers, servers, MCP, browsers, and background work stay out of this skill.
- Kept graph reads non-persistent by disabling optional query logging for the invocation and using an
  explicit graph path. A query never silently repairs or rebuilds a stale graph.
- Strengthened evidence semantics: extracted and inferred edges both require cited-source/test
  verification before correctness, runtime, security, or architectural claims. Staleness,
  ambiguity, missing evidence, and conflicts are returned to the caller.
- Graph artifacts are never staged, committed, or published merely because the skill ran.

## Verification

- `python3 -m unittest scripts/test-routing.py`: **71 tests passed**.
- `scripts/generate-route-index`: generated **215 skill rows**.
- `scripts/lint-skills`: **Gate PASS**, 0 critical, 0 warnings, 63 informational findings, and
  0 hub-member orphans.
- `git diff --check`: passed.
- `GraphifyRouteTests` covers explicit Architecture membership, worktree/output ownership,
  code-only extraction, non-persistent reads, excluded installation/persistence, and command naming.

## Remaining limits

- No local corpus or installed Graphify version was supplied, so artifact-root metadata and output
  behavior were verified from the archived pinned source rather than a runtime extraction.
- Other Architecture children remain semantically pending.
