# Visual Explainer ingestion

Date: 2026-11-12. Request: create and ingest a skill from `nicobailon/visual-explainer`.
Source: https://github.com/nicobailon/visual-explainer/tree/9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad
Pinned commit: `9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad`, upstream version 0.15.0.
License: MIT, Nico Bailon, 2025.
Catalog: `main` at `5806c621ca8477b80e509f0f84ca567ce54a0f44`, with pre-existing dirty work retained.

## Result and scope

Add `skills/1-visual-explainer` as a Learn leaf for one local, figure-led HTML explanation.
The new gap is a connected teaching page: overview, mechanisms, cases/comparisons, captions,
and optional local interaction. One standalone diagram remains `1-diagram-maker`'s job.

This is an adapted authoring skill, not installation of the upstream plugin/runtime.
No upstream source code, module loader, renderer, server, custom-element kit, or exporter is adopted.

| Upstream capability | Catalog disposition |
|---|---|
| Figure-led concept/system page | New `1-visual-explainer` |
| Source-backed comparison and project context recap | Supported within the new page's bounded evidence packet |
| Visual registers, matched cases, direct labels, concise captions | Adapted into local design/figure references |
| User-controlled stepper, replay, live parameter illustration | Adapted as optional native HTML/CSS/JS patterns with static fallback |
| One standalone diagram / editable whiteboard | Existing `1-diagram-maker` remains owner |
| Exact PR/diff orientation | Existing `1-visual-recap` remains owner; the chat/HTML PR drafts are also preserved |
| Visual implementation plan | Existing `1-visual-plan` remains owner |
| Correctness review / plan audit / fact investigation | Existing Review/research workflows; not a verdict from page rendering |
| HTML slide deck / PowerPoint | Existing `1-slides` / `1-pptx` remain owners |
| Imported code model execution and exhaustive walks | Excluded; a cited hand model is explicitly illustrative |
| Pi extension, MCP server, kit renderer, templates, plugin commands | Not installed or adopted |
| Video/narration/export utilities, CDN libraries, remote fonts | Outside this ingest; require separate selected tasks and dependency/effect review |
| Feedback runtime and automatic follow-on execution | Excluded; page choices do not grant implementation authority |

## Integration gate

| Check | Disposition |
|---|---|
| Gap | Connected multi-figure teaching page with optional interaction, distinct from a single diagram |
| Collision / merge | Explicit boundaries preserve diagram, PR, plan, slide, and UI owners; no generic review/router peer |
| Prev / next | Learn or actual caller → one page → caller; no automatic chaining |
| Setup | Soft; no upstream runtime, host configuration, API key, or mandatory onboarding |
| Thin / disclosure | Lean main process; design, figure, interaction, and source-adaptation references have load conditions |
| Forbidden | No whole vendor pack or second meta-router; only selected source evidence archived |
| Hub slot | `0-learn`, leaf, depth 1 |
| Forks | Clear HTML teaching request dispatches directly; existing F-L1 covers material learning-mode ambiguity and Agent judgment |
| Route surface | Use when / Not for / Hub, catalog metadata, explicit Claude/Codex invocation policy |
| Skill lint | Final results below; require zero critical findings |

## Static supply-chain assessment

Caller: `0-skill-manager`, using `2-skill-supply-chain-audit`'s static review contract.
Expected capability: bounded source inspection and local explanatory artifact authoring.
Proposed runtime permissions: existing tools only, explicit invocation, local artifact write.
No new account, credential, service, package, browser installation, or external state change.
Prior package baseline: none; first selected import, not an audited upstream update diff.

Reviewed all 11 selected source/metadata files: upstream `SKILL.md`; design, diagram, motion,
and machine references; generate-web-diagram, compare, and project-recap command texts;
root package metadata; plugin metadata; and MIT license. These bytes are retained with SHA-256
hashes in `archive/vendor/visual-explainer-2026-11-12/manifest.json`.
All are regular text files. No executable or active HTML template was imported or rendered.

The remaining renderer/kit/server/extension/exporter code, binaries/media, installers, evals,
and other commands were inventoried by path or outside scope, not exhaustively security reviewed.
No package installation, lifecycle script, model import, upstream check, MCP server, or renderer ran.
Do not interpret this recommendation as approval of those excluded components.

| Finding | Evidence / status | Treatment |
|---|---|---|
| Implicit effects and global output | Observed: upstream `SKILL.md` Deliver defaults to global output, rendering with opening, and table-triggered page conversion. Medium scope/authority concern if transplanted unchanged. | Default local workspace output, explicit invocation, no automatic browser launch or table conversion. |
| Source execution during rendering | Observed: `references/machines.md` imports repository code and runs a model in Node; its Trust section explicitly says this is not a sandbox. High-impact potential with untrusted code, not a demonstrated exploit. | No renderer/model walker adopted; inspect code read-only, cite transitions, label simulation limits. |
| External resources and host dependencies | Observed: main/diagram/motion instructions rely on kit tags and can use CDN libraries; metadata advertises server/export dependencies. Compatibility and network effects are conditional, not evidence of malice. | Native embedded HTML/CSS/SVG; no remote requests or dependency installation by default. |
| Certainty loss in simplification | Observed: upstream Words asks for no hedges. Medium evidence-integrity concern when sources are uncertain. | Preserve uncertainty, conditions, exceptions, and provenance; STE-inspired, not certified compliance. |
| Choice mistaken for authorization | Observed: project-recap command asks to start the picked next step. Authority depends on the original task. | Page controls are local illustrations; feedback is data, and follow-on work needs matching user authority. |
| Unavailable output proof | Observed: main instructs use of a kit-generated inspection sheet and forbids alternate browser checking. That pipeline is not adopted here. | Use available authorized browser/structural checks and report gaps; never claim unseen render results. |

Recommendation: accept the adapted text-only skill for explicit local authoring.
Residual risk: future generated HTML/JS needs artifact-level checking. Static skill review cannot
prove its output safe or factually complete. All model/data examples need source and assumption labels.

Data path: authorized source packet → evidence ledger → local HTML artifact → user.
Private content stays local by default. No telemetry, network submission, or credential access is introduced.

## Change ledger

- Applied: one new skill, four linked references, explicit invocation manifest, and MIT license.
- Applied: selected upstream snapshot and hashes; source-adaptation and assessment notes.
- Applied: Learn dispatch, workflow/HTML membership, flows, root/skill README, wiki index/log,
  new provenance lock entry, and generated route projections.
- Preserved: existing artifact owners, both PR explainer drafts, Matt Pocock additions, and unrelated dirty changes.
- Not applied: plugin/runtime install, host sync/activation, model execution, browser launch, commit, push, publication, or export.

## Validation

- `rtk ./scripts/lint-skills --format json`: exit 0, Gate PASS, 0 critical, 7 existing warnings,
  45 informational findings. No finding references the new skill. The warnings concern existing
  PR inbox drafts, browser-use, and impeccable, outside this change.
- `rtk python3 scripts/test-routing.py`: exit 0, all 746 tests passed, including Learn child parity
  across dispatch metadata, workflow, hub HTML, and flows.
- `rtk ./scripts/generate-route-index --check`: exit 0, projections current for 296 live skills.
- Read-only Python package check: exit 0. Verified all 11 selected source hashes, package YAML,
  explicit invocation policy, all relative Markdown links in the new package, lock hash, copied
  MIT license, and absence of adopted executable/runtime/template code.
- `rtk proxy git diff --check`: exit 0.
- Manual boundary/source review: figure-led teaching retains its own output; single diagrams,
  PR recaps, plans, slide decks, verdicts, and implementation retain their existing owners.

Coverage limits: no downstream explanation page was requested or generated during this ingest.
Browser rendering, generated interaction, and real-project output quality were not exercised.
No claim is made about safety or correctness of the excluded upstream runtime or exporters.
