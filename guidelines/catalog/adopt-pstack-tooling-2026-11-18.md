# Pstack tooling and workflow adoption

User request: apply the comparison's recommendations and copy or adopt pstack's tooling/scripts.
Owner: `0-skill-manager`, with bounded implementation, static package review, and serial code review.
Source: [cursor/plugins e1cc031](https://github.com/cursor/plugins/tree/e1cc03121a0e71129a4fb730d7c5528a0a3e43c8/pstack), pstack 0.15.43, MIT, Lauren Tan.
Catalog: `/Users/rohitasbansal/Development/AI-Skills/skills`, branch `codex/generalize-skill-catalog`.
Existing catalog work was committed by another workflow during this task; its content was preserved.
This task creates no commit, PR, push, merge, runtime sync, plugin activation, or global configuration.

## Applied recommendations

| Recommendation | Concrete result |
|---|---|
| Easier common workflows | Six task recipes with starter prompts, existing owners, and completion evidence in the generated [daily guide](./daily-workflows.md) |
| Exercise compositions | Four real Codex fixture runs for diagnosis, implementation, review-only and verification-only; final linked-candidate rerun recorded below |
| Reduce repeated bookkeeping | One recipe JSON plus the existing route collector generate the human guide; replace the README's 234-line manual skill index with generated/source-backed indexes; shared PR checkpoints hold watcher policy; freshness and hash checkers detect drift |
| Blinded comparisons | Matched-case packet preparer and [method](../../skills/0-skill-creator/references/blinded-comparison.md); no hard-coded models, automatic agent panel or comparative quality claim |

The guide is an on-ramp, not another meta-router. Existing hubs, skill identities, permission boundaries,
runtime invocation policies, and membership remain intact. No new selectable skill is introduced.
No house convention or ADR changes, so the catalog convention version remains 1.4.0.

## Tooling disposition

| Source group | Live owner | Adaptation |
|---|---|---|
| statechart CLI, pure compiler passes, tests and replay corpus | `1-statechart-modeling/scripts`; execution by `1-formal-verification` | Existing local Java/JAR required; automatic mise installation removed; 120-second default deadline; renderer tests opt-in with existing dependencies |
| watch-pr CLI, GitHub reader, policy, renderer and tests | `1-pr-repair/scripts`; shared Git checkpoints | Automatic bootstrap removed; frozen explicit dependency setup; normal semantics for every approval check; reject cyclic PR base chains |
| worktree-audit.sh | `1-git-worktrees/scripts/worktree-audit.py` | Standard-library local-only rewrite; explicit base; no fetch, provider lookup, transcript access, size scan or deletion; preserve untracked work |
| show-me-your-work/log.sh | `0-implement/scripts/log-decision.py` | Standard-library POSIX adapter; locked appends, mode 0600 for new files, header/file checks and whitespace-aware formula escaping |
| eval playbook | `0-skill-creator/scripts/blind-packets.py` | Local reviewed exports, matched prompts/cases, randomized public labels, separate private mapping; no provider orchestration |
| bootstrap and superseded shell entry points | non-discoverable archive | Originals retained as provenance only |
| poteto mode, model setup, agent definitions, companion plugins and Benny automations | not activated | Existing catalog owners retained; no messaging, schedules, model configuration or runtime installation |

The [manifest](./pstack-tooling-manifest.json) pins copied source and adapted file hashes/modes. It is an
integrity inventory, not a security certificate. Earlier 0.15.42 skill-body provenance stays intact;
new tooling has separate 0.15.43 provenance in the lock and manifest.

## Static supply-chain review

Review covered executable entry points, runtime/toolchain discovery, subprocess construction, GitHub
read commands, data-to-code boundaries, output publication, cleanup, package manifests/locks and test
execution setup. Source code was treated as data. Pure transformation modules additionally have upstream
corpus tests and Node import-graph checks. The full plugin, every pure algorithm, npm dependency
implementation, Java/TLC binary, and optional renderer implementation were not exhaustively audited.

| ID | Observed behavior and implication | Disposition and evidence |
|---|---|---|
| PT-1 | bootstrap installed dependencies when the watcher started | Remove bootstrap from the live tool; require explicit frozen install with lifecycle hooks ignored |
| PT-2 | statechart found/installed Java and TLC through mise | Remove installer/discovery branch; require an existing reviewed `TLA2TOOLS` and optional `JAVA` |
| PT-3 | render tests installed npm packages into a global cache | Remove install/cache writes; renderer checks require opt-in and local packages |
| PT-4 | upstream audit fetched origin, queried providers and scanned Cursor transcripts despite its read-only label | Replace with local metadata-only audit; no network/provider/transcript code retained |
| PT-5 | watcher classified `Code Review Gate` specially, excluding it from ordinary pending/failure treatment | Preserve every named check as an ordinary check; adapted upstream tests cover both read paths |
| PT-6 | PR base-chain discovery could loop on A→B→A | Add a visited set and typed nonretryable error; a bounded regression test failed before the fix and passed afterward |
| PT-7 | statechart view modules execute JavaScript, and TLC may load trusted Java overrides | Keep these as explicit reviewed executable inputs; CLI is not a sandbox; no automatic view execution by the modeling skill |
| PT-8 | log cells with whitespace before a formula could remain spreadsheet-active; concurrent first appends could duplicate headers | Escape after whitespace inspection; lock header validation and append; concurrent and negative-control tests |
| PT-9 | partial evaluation exports can leak candidate identity through prose | Strip metadata/IDs, separate mapping, require manual text screening; describe output as metadata-blinded only |

Recommendation: accept the adapted tools for the documented local scope, with trusted executable
inputs and existing permission boundaries. Execution tests used synthetic data, recorded TLC replay
fixtures, fake GitHub readers, disposable repositories and explicit development dependencies.
No real PR was changed or queried, no private transcript was scanned, and no global toolchain was installed.

Residual limits: `--status-only` is query success, not readiness; GitHub CI provenance and branch policy
still need caller evidence. Watcher polling timeout does not interrupt a stalled `gh` subprocess.
Local worktree ancestry cannot prove squash-merge status or permit cleanup. Model-check success does
not prove source correspondence. Blinding does not establish causality or quality improvement.

## Verification

| Check | Result |
|---|---|
| PR watcher | 55 tests PASS, including approval-gate handling and cyclic-stack rejection; strict TypeScript PASS |
| Statechart on Bun 1.3.14 | 189 PASS, 151 explicitly skipped, 0 failed |
| Statechart on installed Node 26.7.0 | 195 PASS, 145 explicitly skipped, 0 failed; includes V8/import-graph checks |
| Statechart strict TypeScript | PASS; add explicit exit-code union and void test callback results for current compiler types |
| Local adapters | Seven focused checks PASS: private/formula-safe/concurrent logs, non-overwrite controls, local worktree preservation, blind matching/privacy and checker deadline cleanup |
| Catalog routing | 746 tests PASS |
| Route projections and daily guide | Freshness checks PASS, 308 live skills |
| Catalog lint | Gate PASS, 0 critical, 4 existing inbox warnings; no new warning |
| Java/TLC differential and renderer integrations | NOT RUN: Java runtime/JAR and renderer packages are not installed/configured; skipped explicitly without installation |
| Runtime sync, protected Git operations and remote mutation | NOT RUN; outside this catalog/tooling change |

The statechart suites exercise parser/projection logic, recorded checker results, publication safeguards,
and signal/cleanup behavior. They do not establish that a real TLC invocation or renderer works here.
Node/Bun test adaptations preserve behavior assertions while handling runtime-specific capabilities,
canonical macOS temporary paths, and synthetic Java replay entry points.

Initial provider-backed workflow evidence: `.scratch/pstack-adoption/workflow-smoke.jsonl`, 4/4 PASS,
Codex runtime default, source HEAD `163b03982c510345a06a0ab1ed784e1440d3956d`, catalog content hash
`c0f0bae56ecccc7d020dda18162a285ec7619a52dd5e85046c46f1f74c2aab36` before the final reference links.
Cases and assertions were the existing frozen `ai-native-cases.json`; no expectations were weakened.
These are small fixture smoke cases, one repetition, with no baseline quality comparison or broad
application verification. Raw prompts/transcripts remain private under `.scratch/`.

Final linked-candidate evidence: `.scratch/pstack-adoption/workflow-final.jsonl`, 4/4 PASS with no runtime
warnings, same source HEAD `163b03982c510345a06a0ab1ed784e1440d3956d`. Catalog content hash
`6d16dbfcc067e02857ae925c93f1f134b14f92e8573e89ceffbbe2273a0a8613` was rechecked after the run and
matches the final skill/tool tree, including explicit local development dependencies. Dirty fingerprint
at run start: `81289f28dcda804dd42f0daafc4b1a09ec116a20a141888a619b03507c145e8e`.
The initial and final runs are retained separately; they are smoke evidence, not a blinded A/B result.

Additional final checks:

- `rtk python3 scripts/check-pstack-tooling --source-root /private/tmp/pstack-comparison-20261117/pstack`:
  440 adopted/support files match their frozen hashes and modes; applicable upstream hashes match.
- `rtk python3 scripts/test-skill-evaluation.py`: 15 PASS.
- The two changed statechart signal-test callbacks were re-exercised with the installed Node runner:
  five selected signal/publication cases PASS. The explicit exit-code return annotation also passes
  strict TypeScript; it changes no runtime behavior.
- `rtk git diff --check`: PASS. Final lint/freshness checks remain required when these files change.
- Snapshot preservation: all 1,929 protected files from the 1,942-file starting content ledger are
  byte-identical. The 13 changed paths in that ledger are explicitly owned by this task; the vendor
  index append and new files are additional owned changes. Unrelated dirty vendor submodules remain.
- Serial Spec, Standards and Maintainability review found and reconciled the approval-gate and
  cyclic-stack issues above. No remaining blocking finding in the reviewed surfaces; algorithm,
  dependency-implementation, live-provider and optional-toolchain coverage limits remain explicit.

Test logs are retained under `.scratch/pstack-adoption/verification/`; provider records and raw local
transcripts remain under `.scratch/pstack-adoption/`. The full Node/Bun runs preceding the final
type-only callback annotations are retained alongside the focused final callback run.
