# Addy Osmani agent-skills refresh

Date: 2026-11-15. Mode: apply selected reference merges after repository assessment.
Source: https://github.com/addyosmani/agent-skills/tree/39b723ceebf81474d0557c1fecd01eddab585563
Pinned commit: `39b723ceebf81474d0557c1fecd01eddab585563`. License: [MIT](../../archive/vendor/addyosmani-agent-skills-2026-11-15/LICENSE), copyright 2025 Addy Osmani.
Catalog baseline: `main` at `5806c621ca8477b80e509f0f84ca567ce54a0f44`, including pre-existing dirty work.
Prior archived source: `6ca0cd7db39b41b1c37e26d335c507ee92382c6d`; that snapshot remains intact.

## Disposition

All 25 upstream skills already have capability owners. Merge five focused updates; retain 19
other owners and exclude the duplicate router. No new live skill or runtime integration is needed.
This is a selective capability refresh, not a claim that existing bodies match the latest upstream.

| Upstream skill | Disposition / live owner |
|---|---|
| api-and-interface-design | Retain `1-api-and-interface-design` |
| browser-testing-with-devtools | Merge settled-layout capture into `1-browser-testing-with-devtools` |
| ci-cd-and-automation | Merge shell-input/cache guidance and report-gate contract into `1-ci-cd-and-automation` |
| code-review-and-quality | Retain `1-code-review`; do not import automatic candidate mutation during review |
| code-simplification | Retain `2-ponytail-review` and `0-ponytail` |
| constraint-driven-development | Merge scanner execution/report/threshold distinction into `1-constraint-driven-development` |
| context-engineering | Retain `1-strategic-compact`, `1-handoff`, and `1-context-monitor` |
| debugging-and-error-recovery | Retain `0-diagnosing-bugs` |
| deprecation-and-migration | Retain `1-deprecation-and-migration` |
| documentation-and-adrs | Merge meaning-preserving prose/history checks into `1-living-documentation-governor` |
| doubt-driven-development | Retain bounded `1-doubt-driven-development` |
| frontend-ui-engineering | Retain `1-frontend-ui-engineering` and UI/UX owners |
| git-workflow-and-versioning | Retain `0-git` and `1-atomic-git-commits` |
| idea-refine | Retain `1-brainstorm` and `0-grilling` |
| incremental-implementation | Retain `0-implement` |
| interview-me | Retain `0-grilling` and `1-grill-me` |
| observability-and-instrumentation | Retain `1-observability-and-instrumentation`; source skill body unchanged |
| performance-optimization | Retain controlled `1-performance-optimization`; disclosure refactor does not justify replacing it |
| planning-and-task-breakdown | Retain `1-to-tickets` and `1-write-plan` |
| security-and-hardening | Retain `2-security-and-hardening`; preserve the catalog's scoped security workflow |
| shipping-and-launch | Retain `1-shipping-and-launch` |
| source-driven-development | Retain `1-research` |
| spec-driven-development | Merge version/deferred/delta guidance into `1-to-spec` |
| test-driven-development | Retain `1-tdd`; no blanket TDD policy imported |
| using-agent-skills | Exclude: `0-butler` owns meta-routing |

The upstream web-performance persona, plugin adapters, commands, hooks, installers, evaluation
harness, and nonselected reference updates are not adopted. Existing measurement and review owners
remain authoritative; no persona, alternate router, host configuration, or auto-run loop is installed.

## Integration gate

| Check | Result |
|---|---|
| Gap | Five small improvements fit existing jobs; no unowned lifecycle skill found |
| Collision / merge | Merge into existing owners; no peer skill or identity change |
| Prev / next | Existing callers, boundaries, and return paths preserved |
| Setup | No new hard dependency, onboarding, or runtime permission |
| Thin / disclosure | Main bodies unchanged; details remain in linked references |
| Forbidden | No whole-pack promotion or `using-agent-skills` promotion |
| Hub slot | Existing Implement, Diagnose, and Architecture memberships retained |
| Forks | No new material branch or automatic downstream action |
| Route surface | Existing descriptions, catalog metadata, and invocation policies unchanged |
| Skill lint | See recorded validation below |

## Static supply-chain review

Caller: `0-skill-manager`, using `2-skill-supply-chain-audit` read-only review criteria.
Scope: changed passages selected for adaptation, the complete new quality-gate helper and floor-guard
reference, and resulting local prose. All 25 source bodies received capability/diff screening;
this does not establish exhaustive security coverage of retained packages or the whole repository.
No target code, hooks, installers, dependencies, or evaluation harness were executed.

Expected capability: existing explicit workflows produce scoped local artifacts/evidence.
No runtime permissions change. Data path remains authorized project evidence → local assessment or
artifact → caller. No credentials were read, private data uploaded, or third-party service configured.

Eight source files, including the MIT license, are preserved with SHA-256 hashes in
[the selected snapshot manifest](../../archive/vendor/addyosmani-agent-skills-2026-11-15/manifest.json).
The helper is stored as `.mjs.txt`, without executable permission. Markdown contains historical
commands for inspection only; the archive is outside live discovery. The manifest also records all
25 body hashes and dispositions; nonarchived bodies are inventory, not retained security evidence.

| ID | Evidence / interpretation | Adaptation / disposition |
|---|---|---|
| AO-1 | `constraint-driven-development/scripts/quality-gate.mjs` validates report structure and known severities, but its HTTP URL check alone cannot establish that axe reached the intended screen. Observed, high confidence; medium correctness risk when used as an accessibility gate. | Archive helper as text; adopt a verification contract requiring target identity, navigation, complete coverage, and actual-invocation controls. No executable helper adopted. |
| AO-2 | Updated `references/floor-guard.md` fixes nonzero diff handling, but `flag()` retains matched source text and the final output prints it. Observed, high confidence; medium disclosure risk if sensitive changed text matches a guard pattern. This is retained source risk, not an introduced regression. | Keep the existing redacted floor-review contract; do not adopt the source checker. It also remains heuristic about filenames, thresholds, and lost test protection. |
| AO-3 | `documentation-and-adrs/SKILL.md` labels docs current from code/doc commit order. Observed, high confidence; medium correctness risk because ordering cannot establish semantic agreement. | Adopt chronology only as an investigation clue; require comparison with the pinned contract/implementation. Preserve unknown history and existing decision logs. |
| AO-4 | Source spec/interview workflows require a later-turn approval and automatic stop even when downstream authority may already exist. Source review guidance asks for candidate mutation; other bodies retain automatic commit/tool-install patterns. Observed in screened passages; bounded authority risk if transplanted literally. | Preserve existing caller/return boundaries and session authority. Adopt no automatic mutation, install, commit, forced approval ceremony, or workflow loop. |

Recommendation: accept the five adapted reference merges for their existing explicit scope.
This is static source/adaptation evidence, not malware certification or downstream runtime proof.
New executable adoption would require its own contract, review, and representative tests.

## Change-set ledger

- Applied: spec version/deferred/delta guidance; scanner-gate assessment and linked CI contract;
  CI input/cache guidance; bounded browser readiness; prose/history checks.
- Applied: selected source archive/license/manifest, scoped provenance additions in existing locked
  owners, vendor index, wiki index/log, and this ingestion record.
- Preserved: all live identities, main bodies, hub/flow membership, route metadata, runtime policies,
  old vendor snapshot, existing provenance, and unrelated dirty work.
- Not applied: new skills, executable source, hooks, plugins, global/runtime sync, installs,
  commit, push, publication, or external mutation.
- Generated projections: check freshness; regenerate only if inputs changed. Reference-only edits
  do not change the route-index inputs.

## Validation

- `rtk ./scripts/lint-skills --format json`: exit 0, Gate PASS; 0 critical, 5 warnings,
  45 informational findings, matching the pre-change baseline. No target warnings. Existing warnings
  concern inbox PR Explainer, browser-use, and impeccable.
- `rtk ./scripts/generate-route-index --check`: exit 0; projections current for 296 live skills.
  No regeneration needed because no route-index input changed.
- `rtk python3 scripts/test-routing.py`: exit 0, all 746 tests passed. The first run found the
  Living Documentation guide exceeded its existing 70-line limit; shortened the addition and reran
  successfully. No test expectation or threshold was weakened.
- Read-only `rtk python3 -c` integrity check: exit 0; all eight archived-file hashes match the
  pinned source; 25 source identities/hashes and five merge dispositions accounted for; all owner
  paths, 13 initial local links, provenance-import targets, archive file modes, router exclusion,
  and the guide line limit verified. Final source/license link also checked.
- `rtk proxy git diff --check`: exit 0. Reviewed scoped diffs and the new report-gate contract;
  pre-existing EGM/other imports remain present. Existing skill-body lock hashes/source fields were
  retained, with nested reference-import records added only for the two already locked owners.
- Manual mode-skill review of the five owners: identities, existing hub slots, caller/return paths,
  invocation policies, disclosure reachability, and unchanged main bodies satisfy the structural
  gate. The new CI reference is reachable through the existing full-guide link.

Results cover the working tree at catalog `HEAD` `5806c621ca8477b80e509f0f84ca567ce54a0f44`,
including unrelated pre-existing changes; there is no new commit. The five merges are reference-only.

Coverage limits: no downstream spec, scanner, CI job, browser scenario, or documentation maintenance
task is exercised by this import. Existing retained workflows and nonselected source packages were
not exhaustively re-audited or refreshed. No application build/typecheck is applicable to these
Markdown reference and provenance changes.
