# Selected pstack skills and workflows ingestion

Date: 2026-11-15. Mode: apply selected skill bodies, reference merges and optional workflow compositions.
Source: https://github.com/cursor/plugins/tree/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7/pstack
Pinned repository commit: `bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7`. Plugin version: `0.15.42`.
License: [MIT, copyright 2026 Lauren Tan](../../archive/vendor/pstack-2026-11-15/LICENSE).
Catalog root: `/Users/rohitasbansal/Development/AI-Skills/skills`, `main` at
`5806c621ca8477b80e509f0f84ca567ce54a0f44`, with extensive pre-existing dirty work.
This change set preserves earlier imports, PR Explainer edits and unrelated catalog changes.

## Disposition

The source contains 58 main skills, 23 playbooks, three dormant Benny automation skills and two
agent definitions. The [manifest](../../archive/vendor/pstack-2026-11-15/manifest.json) accounts for all
86 entries and records metadata/hashes for all 560 source files. Hashing is inventory, not security review.

| Source group | Disposition |
|---|---|
| Four selected main skills | Four new adapted leaves |
| Two maintenance skills | Support the new map/formal-check boundaries |
| blast-radius and correct | Merge into two existing owners |
| encode-lessons-in-structure | Support the correction/enforcement merge |
| Other main skills | 44 existing capability matches retained, two deferred integrations/media workflows, three excluded routing/setup/style entries |
| Playbooks | 21 existing capability matches retained; two reviewed as composition context |
| Benny automations and agent definitions | Five deferred; no messaging, tracker, schedule, model or runtime configuration imported |

Retaining an existing capability does not assert every pstack recipe is implemented there. No
whole-pack promotion, second router, runtime plugin installation, model pinning or source helper
execution is part of this import. Deferred entries are inventory, not live skill recommendations.

## New skills and merges

| Result | Owner and output | Source |
|---|---|---|
| `1-design-rationale` | Learn leaf: a cited explanation from decision history, with intent/inference/unknowns separated | why |
| `1-runtime-feature-map` | Implement leaf: a scoped feature map/recipe proposal or authorized doc patch; no runtime driving | create/maintain-verification-skill and feature-map examples |
| `1-statechart-modeling` | Architecture leaf: states/actions/guards/invariants, source mapping and reader-facing chart; no checker execution | statechart |
| `1-formal-verification` | Review leaf: design, supplied-result analysis or authorized execution for one fixed check; per-property scope and gaps | create/maintain-formal-verification-skill |
| Existing `1-change-impact` | Conditional safety-premise ledger; preserve its read-only mode | blast-radius |
| Existing `1-agent-workflow-observer` | Conditional recurrence-to-enforcement proposal; preserve its read-only fixed-snapshot boundary | correct and encode-lessons-in-structure |

Each new leaf has a matching depth-prefixed directory/name, explicit invocation manifest and full
MIT license. Main bodies are lean. Detail is conditional, and every skill returns to its caller.
The existing pstack CLI and TypeScript model-checking/rendering implementation are not copied.

## Workflows

The [workflow guide](../../skills/0-implement/references/verification-workflows.md) is linked from
Ship, its HTML package, workflow JSON and flow surface. It composes existing owners rather than
introducing another mode/router or an executable automation engine.

| ID | Ordered workflow | Outcome and stop condition |
|---|---|---|
| W-PS1 | Feature map → permitted project/browser check → coverage/drift reconciliation → owned teardown | Evidence by feature/entry point; prerequisites and unrun paths remain gaps; no automatic product repair |
| W-PS2 | State model → fixed formal check → permitted replay or unrun recipe → reconciliation | Property-specific result, bounds and model correspondence; a pass is not product-wide proof or release approval |
| W-PS3 | Frozen-run correction proposal → requested policy → authorized enforcement implementation → negative/clean controls | A proposal or tested mechanism; no automatic cleanup, exception approval, hook, commit or scheduling |

F-PS1 is used only when the requested outcome does not identify a workflow. Its branches include
Agent judgment. Selection preserves the inherited candidate, mode, permissions, output scope and
resource limits. A selected flow does not grant new execution, model-call, messaging or write authority.

## Integration gate

| Check | Result |
|---|---|
| Gap | Four independently useful outputs: historical rationale, runtime map, state model and formal-check evidence |
| Collision / merge | Impact and workflow observation remain with existing owners; model authoring and checker execution have explicit separate boundaries |
| Prev / next | Learn, Implement, Architecture and Review callers retained; no automatic lifecycle |
| Setup | No new hard dependency or runtime setup; missing verifier/browser tooling is a reported prerequisite |
| Thin / disclosure | Lean main bodies and linked contract references |
| Forbidden | No poteto-mode/help/setup promotion or alternate house router |
| Hub slot | Four depth-1 leaves under four existing domain hubs |
| Forks | F-R1 includes the formal-check option; F-PS1 is material-only and offers Agent judgment |
| Route surface | Descriptions, catalog metadata, matching identities, invocation policy and hub membership updated together |
| Skill lint | Gate PASS: zero critical findings and no new warnings |

## Static supply-chain review

Caller: `0-skill-manager`, using `2-skill-supply-chain-audit` criteria. This is a first selected
pstack import, not a comparison against a known-good executable release. Review scope: nine selected
skill bodies, four linked reference/example documents, two playbooks and plugin/license metadata.
All adopted source passages were read. Main-skill descriptions received capability-level screening.
The long README received orientation screening; the remainder of the plugin is not exhaustively audited.

Nineteen source files are preserved in a non-discoverable archive with SHA-256 hashes and original
names. They are provenance, not operative procedures. Executable code, tests, binary assets,
installers, JavaScript view modules, agents and Benny operational sources are not promoted or run.
The four new packages contain prose and invocation metadata only; no helper code is adopted.

Expected data flow: caller-approved repository/spec/history/model/result evidence → bounded local
artifact/proposal/report → actual caller. A future explicitly authorized checker run can execute
tool/model code; its inputs and output scope must be reviewed and bounded then. This import does
not contact models, read credentials, upload private data, attach to an app, or change hosted state.

| ID | Observed source evidence / implication | Adaptation |
|---|---|---|
| PS-1 | statechart's Run/Show sections install Java/TLC via mise and prescribe Pele installation; view modules contain executable JavaScript. High confidence, medium permission/toolchain expansion if transplanted without scope. | No bootstrap, helper or renderer adopted. Native Mermaid/existing tools only; checker execution requires a reviewed existing toolchain and exact authority. |
| PS-2 | statechart documents multiple runs with failed rules removed, state caps, projections and rules not checked. High confidence, medium evidence-interpretation risk if a final chart is mistaken for complete verification. | Preserve original property/config, per-property status, resource/abstraction limits, mixed states and hidden steps. Unchecked/incomplete is unknown, never green. |
| PS-3 | maintain-formal-verification treats some comments/tests/commit messages as evidence that a promise intentionally changed and supplies a fallback sync commit. High confidence, medium correctness risk if these are mistaken for approval or correspondence. | Resolve against the accepted contract/owner. History is an investigation clue; update sync evidence only after correspondence is established. |
| PS-4 | create-verification-skill says to fix a broken base first and can install/build launch prerequisites; maintenance requires live driving and may open a PR. High confidence, medium scope expansion outside a documentation request. | Map authoring and runtime execution are separate owners/phases; no implicit product repair, package install, PR or live interaction. Unrun recipes remain unverified. |
| PS-5 | The feature playbook requires delegates and model defaults, and says to commit liberally. runtime-forensics includes live instrumentation/hotfixing while calling its deliverable diagnosis. High confidence, medium authority and state-boundary risk in a house read-only flow. | Keep existing delegation policy, read-only browser semantics, edit/execute gates and Git authority. No mandatory model choice, live mutation or automatic commit imported. |
| PS-6 | correct promises to make mistakes impossible, applies fixed recurrence criteria, removes some instructions after enforcement and requests commits. High confidence, medium overclaim/scope risk. | Propose mechanisms from evidenced recurrence; distinguish syntactic enforcement from behavioral assurance; preserve useful rationale and require scoped implementation/negative controls. |
| PS-7 | blast-radius asks to execute proof code and parallel models as part of impact analysis. High confidence, medium mode/paid-execution expansion for the existing read-only owner. | Adopt explicit safety premises and evidence levels; supplied observations or a proposed falsifying check only, with unproven as a valid result. |

Recommendation: accept these adapted prose skills, two reference merges and three optional
workflow definitions for their stated scope. This is not certification of the full upstream plugin
or proof that its executable tools are safe/correct. Those components remain outside adoption.

## Behavior walkthroughs

These are manual specification checks, not real model/checker/app executions.

| Case | Intended result |
|---|---|
| A threshold exists in code but its PR discussion is unavailable | Rationale distinguishes current behavior from inferred original intent and preserves the missing history |
| A source-backed feature recipe has never been driven | Map labels it unrun, rather than verified |
| Two model states share a screen label but violate different rules | Chart preserves the distinction or mixed result and rule identity |
| A checker times out after checking only one property | Report that property’s evidence and mark unfinished claims unknown |
| A model counterexample uses a step the implementation cannot take | Investigate abstraction/drift before declaring a code defect |
| A user asks for a read-only impact analysis | Safety-premise guidance proposes a check without running it |
| A repeated correction suggests a lint rule | Observer returns a scoped proposal; W-PS3 implements it only with the corresponding authority |

## Change-set ledger

- Applied: four new live packages, manifests/licenses, three conditional contract references,
  two merged references and links from their existing skill bodies.
- Applied: four hub dispatch/metadata/workflow/HTML surfaces, flow membership, F-R1/F-PS1 updates,
  three optional workflow compositions, root/live READMEs, wiki index/log, lock/provenance and source archive.
- Applied: generated route projections when their inputs changed; no manual projection edits.
- Preserved: incumbent routers, approval boundaries, source snapshots, prior imports and unrelated dirty work.
- Not applied: plugin installation, runtime sync, background automation, Slack/tracker messages,
  scheduling, model calls, source execution, Java/TLC/renderer setup, commits, pushes or merges.

## Validation

- `rtk ./scripts/generate-route-index`: exit 0; regenerated both projections for 304 live skills
  (300 before this import). `rtk ./scripts/generate-route-index --check`: exit 0; projections current.
- `rtk ./scripts/lint-skills --format json`: exit 0, Gate PASS; 0 critical, 5 warnings,
  45 informational findings, matching the baseline. No new target warnings. Existing warnings
  concern inbox PR Explainer, browser-use and impeccable. The first run surfaced a lean-shape
  finding after Ship grew; kept the main body concise and used the preferred Process heading.
  No lint rule or gate was weakened.
- `rtk python3 scripts/test-routing.py`: exit 0; all 746 tests passed on the final skill bodies.
  Existing parity/link/fork tests cover the added routes; no test expectation or assertion changed.
- `rtk python3 /private/tmp/pstack-ingest-2026-11-15/check.py`: exit 0. Verified all 86 source-entry
  hashes, 560 file hashes and 19 archived copies; four new licenses/invocation policies/body hashes;
  21 local links; source/owner identity; lean bodies; and W-PS1/W-PS2/W-PS3 plus F-PS1 across the
  guide, workflow JSON, HTML and flow surfaces. All 2,026 pinned pre-existing paths remain unchanged
  outside the 23 owned paths, including generated projections. Original backups match the baseline.
  Incumbent hub JSON fields and lock provenance remain intact apart from scoped additions/hashes.
- `rtk proxy git diff --check`: exit 0. Reviewed incremental diffs against task-start copies to
  distinguish these edits from earlier uncommitted imports. The four new skills and two updated
  owners pass the manual structure/boundary/caller/disclosure check as well as catalog lint.

Evidence covers the final working tree, including earlier unrelated changes, at catalog HEAD
`5806c621ca8477b80e509f0f84ca567ce54a0f44`. No commit, application build, runtime model checker,
renderer, live browser, schedule or plugin activation was needed for prose/catalog integration.

Coverage limits: no real app feature map, historical investigation, state-model case or formal
checker was executed by this ingestion. No downstream savings, correctness, liveness, security,
translation of a model to code, or automation delivery is established by structural catalog checks.
