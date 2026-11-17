# Catalog wiring and workflow audit

Objective: for each skill, improve wiring, pipeline and worktree connections, and other
aspects that affect correct use. Scope is all live skills, their operative references,
hub workflows, flows, generated routing, and verification tooling.

Status: **complete**. Final inventory on 2026-09-12: **232 live skills; 232 reviewed**.
Structural lint passing is not proof that skill behavior and routing are correct.
The current dirty worktree contains extensive pre-existing changes; preserve them.

## Completion requirements

For every skill, verify purpose and atomic boundary; usable triggers and exclusions;
actual parent membership and dispatch; conditional next/caller-return behavior;
workspace applicability, path/branch identity and ownership; input/output evidence;
authority and side effects; operative reference consistency and usable local links.
Non-coding/read-only skills need an explicit audit decision, not a forced worktree step.
Fix material defects found, preserve meaningful specialist boundaries, and record evidence.

Catalog-wide completion also requires consistent flows/workflow/route-index surfaces,
regression coverage of routing failure modes, and a final inventory reconciliation.
Review relevant instructions and references fully before editing their procedures.
Do not mark the goal complete while semantic review remains pending.

## Completed first batch

- Generated index now includes explicit triggers even when `when` exists, retains
  complete next targets, escapes table pipes, and stops catalog parsing at scalar siblings.
- Architecture has an explicit API/module/system decision route (F-ARCH1).
- Implementation/plan entry now verifies workspace, resumes the caller, and reviews
  the scoped diff before requested finishing.
- Worktree setup checks task fit, conditionally configures local services, and
  returns provenance and verification evidence to its actual caller.
- Finish branch uses ownership evidence for cleanup, preserves shared services,
  honors previously selected outcomes, and removes obsolete menu instructions.
- Linter now detects a declared parent that does not actually own the skill.
- Five routing regression tests passed; full catalog lint: 0 critical, 0 warnings,
  61 informational findings. `git diff --check` passed.
- No commit, push, merge, or host sync performed.

These are targeted improvements, not completed semantic audits of the entire catalog.

## Workspace and plan-execution batch

Four more skills reviewed: `1-git-worktrees`, `1-finish-branch`, `1-execute-plan`,
and `1-subagent-implement`. Task-matching workspaces, conditional lifecycle handoffs,
resumable evidence, sequential writer authority and complete review inputs now agree
across their main bodies and operative references. Three existing SDD helpers are
hardened; 7 routing/reference checks and 11 disposable helper tests pass.
Evidence and limits: [workspace audit](./wiring-audit-workspaces.md).
**189 of 227** skills have individual review evidence; final catalog sweep pending.

## UI/UX pure-router and complete-child-surface batch

The UI/UX hub was reviewed; [evidence](./wiring-audit-ui-ux-hub.md) records all twelve real child routes, Butler and
adjacent-domain boundaries, direct routing with material-only F-UI1, exact caller/candidate/authority and optional
worktree/runtime/deployment identity, shared browser/server/design/cloud/participant state, untrusted UI/research
inputs, project brand authority, no hub tools or verification, removal of automatic multi-leaf chaining, symmetric
workflow/flow/HTML text, clickable children, and corrected package-relative navigation.

## Impeccable current-install and effect-class batch

Impeccable was reviewed; [evidence](./wiring-audit-impeccable.md) records one explicit installed command on one
immutable target, current installed path/version authority rather than stale archived execution, exact caller/
target/worktree/server/effect identity, shared package/browser/hook/account state, untrusted browser/context inputs,
repository-brand precedence, no implicit `npx`/download/update, strict read-only-versus-edit/config separation,
bounded proof, and return without automatically implementing findings or starting another command.

## Hatch Pet operation atomization batch

Hatch Pet plus four new focused children were reviewed; [evidence](./wiring-audit-hatch-pet.md) records a pure
operation router, F-PET1, new-candidate build, one-defect repair, read-only validation, and explicit hash-bound local
installation. The split removes implicit research, installation, cleanup, and mandatory workers; pins exact caller,
candidate, rights, authority, destination and optional worktree; exposes global Codex/provider state; restores the
true `review` animation-row name; adds helper containment/collision/revision rules; and retires the 925-line mega-guide.

## XLSX source-preserving recalculation and type-safety batch

XLSX was reviewed; [evidence](./wiring-audit-xlsx.md) records one immutable source/data-set operation, exact
caller/range/schema/lineage/authority and optional worktree identity, shared office/profile/cloud state,
untrusted formulas/links/macros, explicit types and financial conventions, separate analysis/edit/recalc/refresh
effects, and bounded verification. The unsafe global-macro/in-place recalculation helper now uses separate paths,
an isolated disposable profile, trust assertion, hazard/alias/collision/revision gates, source hashing, atomic
promotion, and honest engine/formula limits. The 289-line guide is now 30 compatibility lines.

## PPTX one-operation and evidence-based QA batch

PPTX was reviewed; [evidence](./wiring-audit-pptx.md) records one immutable source/content-set operation,
exact caller/slide/output/authority and optional worktree identity, shared office/font/asset/cloud state,
untrusted package/external content, source/unknown-part preservation, separate edit/cleanup/export effects,
revision-safe writes, package/content/render/viewer proof, and caller return. Its former 855-line universal
workflow is now 69 lines of selective compatibility notes without forced aesthetics, subagents, defect cycles,
stale paths, or install recipes.

## JSON Canvas stable-identity and inert-reference batch

JSON Canvas was reviewed; [evidence](./wiring-audit-json-canvas.md) records one create/bounded-edit operation,
exact caller/candidate/consumer/authority and worktree identity, shared Obsidian/sync/cloud state, inert untrusted
file/URL references, preservation of unknown fields and stable IDs, evidence-labeled relationships, concurrency-
safe writes, structural versus visual proof, and actual-caller return without hidden app, vault, link, sharing, or
publication work. Its former 572 lines of guide/examples are now 75 lines of compatibility material.

## DOCX one-operation and compatibility batch

DOCX was reviewed; [evidence](./wiring-audit-docx.md) records one immutable source-set operation, exact caller/
source/output/author/authority and optional worktree identity, shared office/cloud/font state, untrusted OOXML
handling, source and unknown-part preservation, revision-safe writes, separate semantic transformations, layered
structure/content/render verification, partial-effect return, and no implicit conversion/publication. Its former
588-line universal tool recipe is now a short version-sensitive compatibility reference without stale install,
path, author, font, or paper-size mandates.

## Diagram artifact evidence and no-design batch

Diagram Maker was reviewed; [evidence](./wiring-audit-diagram-maker.md) records one evidence-bounded diagram
artifact, exact caller/source/format/destination/authority and optional worktree identity, shared visual-tool
state, untrusted imported content, node/edge evidence labels, separate architecture decisions, result-driven
layout, revision-safe writes, syntax and visual verification, non-authorizing templates, and actual-caller return
without automatic sharing, upload, conversion, presentation, or revision.

## PDF one-operation and source-preservation batch

PDF was reviewed; [evidence](./wiring-audit-pdf.md) records one operation on one immutable source set, exact
caller/source/output/authority and optional worktree identity, source preservation, untrusted active-content
handling, verified sandbox requirements, target-specific overwrite/signing authority, true-redaction and
independent verification standards, revision-safe promotion, partial-effect reporting, and caller return.
The imported mega-workflow is provenance only and the OpenAI entry now uses the live skill ID.

## Office extraction and internal-communication batch

Defuddle and Internal Communications were reviewed; [evidence](./wiring-audit-office-text-leaves.md) records
one version-observed, rights-aware HTML-to-Markdown extraction and one audience/evidence-cutoff-bound internal
draft. Both pin exact caller/source/result/authority and optional worktree identity, treat inputs as sensitive
untrusted data, distinguish Git isolation from shared services/accounts/documents/recipients, verify their own
bounded result without overstating coverage, and return before any research, summary, Vault ingest, browser,
incident operation, document conversion, send, schedule, or publication. Defuddle's stale package/executable
recipe was corrected against its current official CLI documentation.

## Office and media hub batch

Office was reviewed; [evidence](./wiring-audit-office-hub.md) records a pure one-artifact router covering
all ten live Office children, with strategic HTML presentations kept as an explicit UI/UX cross-route.
It pins caller, immutable source/output identities, optional exact worktree, sensitivity, rights,
overwrite/publication rules, allowed tools, and effect authority; treats artifact content as untrusted;
distinguishes Git isolation from shared desktop/browser/cloud/account state; prevents automatic conversion
or publication chains; and returns verified artifact provenance and effects to the actual caller. Domain,
fork, path, navigation, manifest, index, flow-chart, wiki, README, and generated-route surfaces now agree.

## Triage atomization batch

Triage and its three extracted children were reviewed; [evidence](./wiring-audit-triage.md) records a pure
one-operation hub, one bounded read-only attention snapshot, one read-only candidate assessment, and one
approved transition applier. They preserve exact candidate/query revision, optional worktree versus shared
tracker state, privacy, taxonomy, disclosure, and effect authority; exclude generated tickets by provenance;
keep PR assessments in scope; return specialist handoffs without running them; verify real multiline tracker
effects; preserve rejection history; and never treat ready state as implementation authority.

## Wayfinder atomization batch

Wayfinder and its two extracted children were reviewed; [evidence](./wiring-audit-wayfinder.md) records a
pure one-operation hub, one new map-set artifact leaf, and one existing map's single decision-ticket cycle.
They preserve exact caller/candidate/evidence/authority and conditional worktree identity, distinguish
Git isolation from shared tracker/service state, gate every tracker effect, return specialist handoffs
without starting them, safely resume with supplied resolutions, report partial effects without duplicates,
and route settled snapshots only to separately requested To Spec—never directly to implementation.

## Ticket-set batch

To Tickets was reviewed; [evidence](./wiring-audit-to-tickets.md) records one immutable approved spec to
one draft/local/tracker ticket-set result, exact caller/destination/authority and conditional worktree
identity, evidence-based slice sizing, bidirectional requirement coverage, an acyclic dependency graph,
shared-resource-aware parallel eligibility, conditional tracker setup, duplicate-safe partial-publication
reporting, and no automatic triage, execution, delegation, Git, or issue-closure effects.

## Specification artifact batch

To Spec was reviewed; [evidence](./wiring-audit-to-spec.md) records one immutable settled source and
one draft/local-write/tracker-publish artifact, exact caller/evidence/destination/authority plus conditional
worktree identity, requirement-to-acceptance traceability, gap-ledger return instead of guessing, conditional
tracker setup, revision-safe writes, and no automatic labels, tickets, planning, implementation, Git, or
publication follow-ons. Its former multi-phase vendor workflow is provenance only.

## Grilling hub batch

The full Grilling parent was reviewed; [hub evidence](./wiring-audit-grilling-hub.md) records one
consent-respecting interview on one immutable candidate, optional exact worktree provenance, one
neutral decision-changing question at a time, delegation/deferral/stopping, ordinary clear approval,
direct specialist routing, separately accepted evidence detours, and actual-caller return. Ideation and
all delivery work are separate; obsolete confidence/prediction rituals, the Ship fork, automatic
follow-ons, stale paths, and incomplete navigation were removed.

## Visual-plan effect-boundary batch

Visual Plan was reviewed; [visual-plan evidence](./wiring-audit-visual-plan.md) records one explicit
draft/create/update operation, immutable source-plan and worktree identity, smallest-useful-surface
selection, private-by-default persistence, fresh-revision targeted updates, effect-specific connector/
browser/share authority, no automatic implementation, and Grilling/caller return. The imported vendor
workflow remains provenance rather than live authority.

## Grilling interview, brainstorm, and domain-artifact batch

Four Design children were reviewed; [Grilling-child evidence](./wiring-audit-grilling-design-children.md)
records distinct no-docs and pinned-worktree read-only interview entries, one proposal-only design-options
memo, one accepted domain artifact per invocation, sensitive untrusted inputs, exact caller/candidate/
authority returns, and separately requested specification, visualization, prototype, planning, or
implementation routes. Brainstorm's automatic browser/server, spec write/review, delegation, commit,
and implementation sequence was demoted to non-operative provenance.

## Thinking hub batch

The full Thinking parent was reviewed; [hub evidence](./wiring-audit-thinking-hub.md) records exact
33-child parity across metadata, workflow JSON, HTML, and Butler flows; direct-match-first one-leaf
routing; immutable candidate/evidence/authority/worktree handoff; material-only forks; `NONE` as a
valid disposition; separately bounded model composition and plan arbitration; actual-caller return;
and no automatic analysis or action. Stale Steel-Manning ownership and risk/execution labels were
corrected, and the hub now meets the lean line target.

## Scientific, causal, comparative, systemic, reality, domain, and question-frame batch

Seven Thinking diagnostic leaves were reviewed; [diagnostic-frame evidence](./wiring-audit-thinking-diagnostic-frames.md)
records immutable symptom/request/candidate sets, optional repository/worktree identity, explicit
evidence-versus-inference boundaries, proposal-only observations and interventions, descriptive-versus-
normative map handling, provisional Cynefin classifications, one-question Socratic scope, separate
tool/production/action authority, no automatic follow-ons, and Thinking/caller returns. Targeted
Thinking metadata and HTML now expose every diagnostic leaf; the parent hub remains pending.

## Presentation-mode batch

Four Butler leaves were reviewed; [presentation evidence](./wiring-audit-presentation-modes.md)
records explicit activation, one-request overlays, caller returns, immutable task/evidence/
authority boundaries, no-worktree decisions, truthful status semantics, and historical
source isolation. Other Butler session-meta leaves remain pending.

## Butler help and session-continuity batch

Four more Butler leaves were reviewed; [continuity evidence](./wiring-audit-session-continuity.md)
records Grok-local evidence and host-state authority, truthful context assessment,
host-neutral same-session capsules, safe-boundary gates, and a verified non-overwriting
durable handoff with Butler-primary/Grilling-detour returns.

## Butler autonomy, retrieval, app, and project-adapter batch

Four remaining Butler leaves were reviewed; [satellite evidence](./wiring-audit-butler-satellites.md)
records authority-preserving autonomous continuation, bounded private Rewind retrieval,
external WebMCP operation/readback safety, and a lean pi_agent_rust adapter that routes
to general engineering workflows with current-checkout and shared-resource provenance.

## Learn hub and Tutor atomization batch

The Learn parent and new Tutor leaf were reviewed; [Learn evidence](./wiring-audit-learn-hub.md)
records direct one-leaf routing, material-only forks, detail-versus-distillation safety,
complete workflow/HTML/flow parity, and the promotion of hidden tutor behavior into one
integrity-bounded, no-worktree interactive-practice skill.

## Concept-learning pipeline batch

Five Learn operations were reviewed; [concept-learning evidence](./wiring-audit-concept-learning.md)
records one-leaf routing, minimal non-demographic diagnostics, truth-preserving audience
adaptation, predictive/bounded models, one-layer deep dives, caller returns, no-worktree
decisions, and a complete rewrite of dogmatic or stale shared teaching references.

## Selected-material and code-explanation batch

Two object-specific Learn leaves were reviewed; [object-explanation evidence](./wiring-audit-object-explanation.md)
records exact `???` selection, untrusted embedded content, causal/evidence preservation,
code candidate/worktree/dirty-state provenance, observed-versus-runtime distinctions,
no-worktree/no-mutation decisions, and clean returns to separate teaching, diagnosis,
review, tutoring, or Ship workflows.

## Teaching-workspace batch

Five durable-course operations were reviewed; [teaching-workspace evidence](./wiring-audit-teaching-workspace.md)
records the atomization of the old multi-job Teach behavior into a pure router plus
workspace, lesson, append-only progress, and one-term glossary leaves. Exact workspace/
worktree provenance, non-overwrite rules, caller returns, evidence-kind distinctions,
source authority, history preservation, and complete Learn workflow/HTML/flow wiring now
agree across the skills and their four shared schemas.

## Narrative and resource-distillation batch

Two Learn leaves were reviewed; [narrative/resource evidence](./wiring-audit-narrative-resources.md)
records one-result boundaries, exact source and optional worktree provenance, claim/evidence/
coverage preservation, copyright and untrusted-content handling, caller returns, and removal
of fixed pedagogy, size, format, and automatic-chaining rules. Story Teacher's old Clean-books
summary is now a non-operative historical note; Vault Ingest requests summaries by evidence
need rather than line-count thresholds.

## Vault Concept explanation bridge batch

One Vault-primary/Learn-on-ramp skill was reviewed; [Vault Explain evidence](./wiring-audit-vault-explain.md)
records exact safe note resolution, optional Git/worktree candidate identity, private and
untrusted note handling, one bounded evidence packet, one Learning Explainer call, grounded
return to the actual caller, and strict no-neighbor/no-write/no-follow-on behavior. Targeted
Vault parent surfaces and the resource-profile gate were corrected without counting the
unreviewed parent as complete.

## Personal Vault hub batch

The Vault parent and all nine references were reviewed; [Vault hub evidence](./wiring-audit-vault-hub.md)
records one-operation direct routing, F11/F-D2 material-only forks, exact root/candidate/
worktree/authority handoffs, private-untrusted data handling, no hidden chaining, and complete
metadata/workflow/HTML/flow parity. Duplicated child workflows and stale numeric, language,
plugin, link, cleanup, path, and host-install rules were replaced by lean shared contracts.

## Vault Inbox capture batch

One Vault leaf was reviewed; [Inbox evidence](./wiring-audit-vault-inbox.md) records one
supplied-item/create-only operation, canonical root and optional worktree identity,
case-insensitive collision safety, filename/path hardening, privacy/redaction boundaries,
truthful minimal metadata, exact-payload verification, and explicit parent/optional-later-
ingest returns without automatic processing.

## Vault Ingest reconciliation batch

One Vault pipeline leaf and all five references were reviewed; [Ingest evidence](./wiring-audit-vault-ingest.md)
records a fixed source snapshot, bounded overlap retrieval, source/user/existing/synthesis
evidence ledger, explicit multi-file effect ledger, conflict/destructive/privacy gates,
canonical root and optional worktree identity, last-moment race checks, honest partial-write
recovery, and symmetric source/parent/follow-on returns without automatic archive/consume/
index/lint/explain behavior.

## Vault lint and one-finding repair batch

The former audit-plus-fix leaf was split into two reviewed skills; [Lint/Repair evidence](./wiring-audit-vault-lint-repair.md)
records a read-only snapshot/coverage/finding ledger and a separately authorized one-finding
repair with current-evidence revalidation. Exact optional worktree candidates, private-data
limits, sampling honesty, active-schema check definitions, stale/conflict dispositions,
high-impact mutation gates, targeted verification, and caller returns now agree across the
Vault metadata/workflow/HTML/flow surfaces.

## Vault query evidence and authority batch

One Vault leaf and all four references were reviewed; [Query evidence](./wiring-audit-wiki-query.md)
records one fixed question against one pinned snapshot, exact optional Git/worktree identity,
private/untrusted bounded retrieval, claim-level locators and conflict/coverage status, credential
non-disclosure, stale-evidence handling, and read-only caller returns. Automatic Query-page/MOC/
index/log writes and fixed registry/MOC/page-count rituals were replaced by a separately selected
Vault Ingest handoff carrying the verified answer packet.

## Obsidian primitive target and side-effect batch

Three Vault primitives and all five references were reviewed; [Obsidian evidence](./wiring-audit-obsidian-primitives.md)
records one-file Markdown syntax, one-command CLI, and one-file/named-view Bases boundaries.
Each now pins exact root/target and optional Git/worktree identity, treats vault/app output as
private untrusted data, preserves shared app/sync/plugin authority, and returns verified effects.
The CLI's broad plugin-debug workflow was removed, Bases' 671-line version-sensitive manual was
reduced to a local-version contract, and Markdown's generic syntax dump became a minimal exact-hunk
procedure with compatibility-only references.

## Agent Engineering direct-router batch

The Agent Engineering hub and all hub surfaces were reviewed; [hub evidence](./wiring-audit-agent-engineering-hub.md)
records complete nine-child parity, direct one-leaf routing, material-only F-AE1, exact candidate/
worktree/trust/privacy/authority handoffs, shared-provider/service boundaries, and caller returns.
The misleading mandatory lifecycle was removed. Child metadata received targeted parent-return
repairs but the unaudited child bodies/references remain pending and are not counted here.

## Agent Evaluation candidate and decision batch

One Agent Engineering leaf, all three references/config surfaces, and its local aggregator were
reviewed; [evaluation evidence](./wiring-audit-agent-evaluation.md) records one decision, fixed
candidate/protocol identity, design/analysis/execution mode separation, representative-source and
checker qualification, private/untrusted evaluation data, explicit provider/tool authority,
descriptive uncertainty, symmetric specialist returns, and helper regression coverage.

## Human oversight policy and authority batch

One Agent Engineering leaf, its full guidance/template/entry package, and policy validator were
reviewed; [oversight evidence](./wiring-audit-human-in-the-loop.md) records one workflow/action-
family policy, design/review/edit separation, exact optional worktree candidate, owner-policy and
stable-subject boundaries, immutable approval binding, protected-action non-execution, explicit
conservative-profile semantics, bounded validator input, symmetric returns, and regression tests.

## MCP server surface, protocol, and authority batch

One Agent Engineering leaf, its full reference/template/entry package, and manifest validator were
reviewed; [MCP evidence](./wiring-audit-mcp-server-building.md) records one bounded server surface,
design/review/implementation mode separation, exact optional worktree candidate, pinned protocol/
SDK/client/transport identity, untrusted protocol-content handling, separate conformance and
business-authorization controls, revision-aware compatibility, shared runtime-resource authority,
an explicit non-standard manifest profile, bounded validator input, symmetric specialist returns,
and regression tests.

## Agent workflow retrospective and proposal boundary batch

One Agent Engineering leaf and all parent route surfaces were reviewed; [observer evidence](./wiring-audit-agent-workflow-observer.md)
records one fixed completed/paused run snapshot, observed/inferred/unknown evidence labels, exact
optional Git/worktree/local/remote/CI provenance, private/untrusted run-data handling, shared-resource
limits, existing-home and recurrence checks, reversible experiment design, proposal-only authority,
actual-caller return, and regression coverage. Misleading live-watch and automatic catalog-authoring
routes were removed.

## DevOps direct-router and operational-authority batch

The DevOps hub, both shared references, and all route surfaces were reviewed; [DevOps evidence](./wiring-audit-devops-hub.md)
records complete 17-child parity, direct one-specialist routing, a material-only F-O1 fork, exact
environment/candidate/worktree/authority handoffs, untrusted operational evidence, shared-resource
limits, effect-specific approval, recovery-as-operation, truthful state/verification reporting, and
complete HTML links. The misleading mandatory lifecycle was removed. Child bodies were still
independently pending at that checkpoint. Subsequent audited batches now cover every listed child; the
subtree was reconciled at audit 121/218 against the tracker, 218-skill route index, 395-test suite,
and zero-warning lint gate.

## AI platform candidate, data, and effect boundary batch

One DevOps leaf was reviewed; [AI-platform evidence](./wiring-audit-ai-platform-operations.md)
records one design/assessment/authorized operation, exact platform and served-candidate identity,
optional worktree versus shared runtime separation, untrusted model/RAG/telemetry data, provenance/
consent/retention and tenant-isolation gates, infrastructure-versus-quality evidence boundaries,
effect-specific deployment/data/cache/index/GPU authority, truthful convergence reporting, and
direct parent return without automatic adjacent operations.

## IaC, cloud, and container operation boundaries batch

Three DevOps leaves were reviewed; [infrastructure-operation evidence](./wiring-audit-infrastructure-operations.md)
records distinct IaC-source, provider-resource, and container-platform jobs; design/read-only/edit or
operation modes; exact candidate/environment/worktree identity; backend/provider/daemon/registry/
cluster shared-state limits; sensitive untrusted plans/state/images/manifests/output; controller
ownership and reconciliation; effect-specific local/remote authority; stale-plan and mutable-tag
defenses; truthful convergence proof; and direct DevOps returns without applying IaC or starting
adjacent workflows.

## Data/storage, network/edge, and server/fleet boundaries batch

Three stateful DevOps leaves were reviewed; [stateful-operation evidence](./wiring-audit-stateful-operations.md)
records distinct data-service/storage, network/edge, and host/fleet jobs; exact target/environment/
worktree identities; shared data/control-plane/host state; sensitive untrusted operational evidence;
backup-versus-restore proof, vantage/propagation limits, controller reconciliation, canary/fleet
coverage, effect-specific authority, and truthful attempted/accepted/converged reporting without
automatic restoration, scanning, expansion, cleanup, or adjacent workflows.

## Internal platform and identity/secret authority batch

Two DevOps leaves were reviewed; [platform/identity evidence](./wiring-audit-platform-identity.md)
records one repository-owned internal-platform capability versus one control-plane identity/secret
operation, explicit modes and parent returns, exact candidate/environment/worktree identity,
shared portal/registry/IdP/KMS/Vault/consumer boundaries, untrusted templates and identity evidence,
honest adoption limits, immutable subject/policy/approval binding, staged credential rotation,
consumer-by-consumer proof, and no automatic publication, access change, revocation, or follow-on.

## Incident stabilization and resilience-exercise boundary batch

Two DevOps leaves and their parent/caller route surfaces were reviewed; [incident/resilience evidence](./wiring-audit-incident-resilience.md)
records one active incident through stable handoff versus one pre-incident failure-scenario plan or
exercise, exact candidate/environment/worktree identity, private untrusted evidence and append-only
decision/action history, per-action communication/containment/recovery authority, explicit stability
proof, exercise containment, measured RTO/RPO semantics, tabletop/backup evidence limits, and no
automatic postmortem, recovery exercise, cleanup, remediation, or resolution claim.

## Compliance evidence and PostgreSQL read-only boundary batch

Two DevOps leaves and PostgreSQL's provenance note were reviewed; [compliance/Postgres evidence](./wiring-audit-compliance-postgres.md)
records one pinned control/evidence package versus one bounded database question, exact optional
worktree and external candidate identity, sensitive untrusted evidence/data, legal/applicability and
control-effectiveness claim limits, immutable traceability, non-writing/non-`BYPASSRLS` database
roles, unsafe routine/FDW/query-shape defenses, bounded result handling, and direct DevOps returns
without remediation, certification, administration, migration, performance, or external follow-ons.

## Grilling response-mode evidence and caller-return batch

Three Grilling leaves and Critique's operative guide were reviewed; [response-mode evidence](./wiring-audit-grilling-response-modes.md)
records separate evidence-before-agreement, interpersonal reflection, and fixed-candidate critique
jobs; explicit activation; exact optional artifact/worktree identity; private/untrusted evidence;
earned agreement and humane safety boundaries; no false balance, diagnosis, or discomfort-as-rigor;
no tools, worktree creation, research, memory retrieval, action, or automatic follow-on; and direct
caller returns. Targeted Grilling metadata/workflow/HTML/flow surfaces were repaired without counting
the still-pending full parent audit.

## Perspective lens and representation boundary batch

One Thinking leaf and its operative Six Thinking Hats guide were reviewed; [perspective evidence](./wiring-audit-perspective-analysis.md)
records one fixed decision, exact optional artifact/worktree provenance, sensitive untrusted inputs,
strict separation of observations from attributed or hypothetical views, persona research limits,
power and trade-off ownership, no stereotype/consensus/vote fabrication, optional evidence-aware
thinking modes, no tools or automatic research/action, and direct Thinking/caller return. Targeted
Thinking metadata and HTML were repaired without counting the still-pending parent audit.

## Ethical, strategic, and competitive decision boundary batch

Three Thinking leaves and Ethical Thinking's operative guide were reviewed; [decision-analysis evidence](./wiring-audit-ethical-strategy-competition.md)
records distinct normative, strategic-framework, and named-competitor jobs; fixed decisions,
candidate/as-of/worktree identity, sensitive untrusted evidence, representation/consent/legal limits,
framework-versus-fact and current-versus-forecast distinctions, dated claim ledgers, collection and
account/contact authority, no unsupported market claims, no automatic adjacent work, and symmetric
Thinking/caller returns. Targeted Thinking metadata/HTML were repaired without counting the parent.

## Mental-model composition and shared-evidence batch

One Thinking satellite was reviewed; [model-combination evidence](./wiring-audit-thinking-model-combination.md)
records one fixed question, a required material gap after a primary lens, exact optional artifact/
worktree identity, sensitive untrusted shared evidence, non-independent agreement, distinct lens
roles, predeclared conflict handling, a three-lens boundary, no invented weights/model soup/tools/
automatic action, and direct Thinking/caller return. Targeted Thinking metadata/HTML were repaired
without counting the parent; Plan Arbiter remains separately audited.

## Decision-frame evidence, precision, and no-action batch

Four Thinking leaves were reviewed; [decision-frame evidence](./wiring-audit-thinking-decision-frames.md)
records fixed decision/candidate/worktree identity, sensitive untrusted evidence, separately
authorized research/probes/actions, concrete undo-path truth, feasible opportunity alternatives,
calibrated-versus-structured estimates, correlated-evidence handling, mechanism-bounded downstream
chains, removal of false numeric/depth rituals, no automatic action, and Thinking/caller returns.
Targeted Thinking metadata/HTML were repaired without counting the parent.

## Thinking sufficiency, competence, durability, and opposition batch

Four Thinking/Grilling leaves and Steel-Manning's full reference package were reviewed;
[evidence-boundary evidence](./wiring-audit-thinking-evidence-boundaries.md) records predeclared
sufficiency without premature stopping, claim-grounding without automatic fetch, qualitative Lindy
survival without lifetime arithmetic, faithful opposition without forced synthesis, exact optional
artifact/worktree identity, sensitive untrusted inputs, separate tool/action authority, no automatic
follow-ons, and caller returns. Targeted parent metadata/HTML were repaired without counting hubs.

## First-principles, lateral, TRIZ, and subtraction boundary batch

Four Thinking create leaves and Lateral Thinking's operative guide were reviewed;
[creative-frame evidence](./wiring-audit-thinking-creative-frames.md) records verified-constraint
preservation, nonliteral provenance, genuine parameter contradictions, honest residual trade-offs,
recommendation-only subtraction, exact optional artifact/worktree identity, untrusted evidence,
separate tool/action authority, no automatic follow-ons, and Thinking/caller returns. Targeted
Thinking metadata/HTML were repaired without counting the parent.

## Counterfactual, user-job, and effectuation boundary batch

Three remaining Thinking create leaves were reviewed; [applied-creative evidence](./wiring-audit-thinking-applied-creative.md)
records counterfactual-as-hypothesis limits, supplied-user-evidence and segment divergence,
owner-set affordable loss, exact optional artifact/worktree identity, sensitive untrusted inputs,
separate research/tool/experiment/contact authority, no automatic product or external actions, and
Thinking/caller returns. Targeted Thinking metadata/HTML were repaired without counting the parent.

## Pre-mortem, red-team, margin, constraint, and OODA boundary batch

Five Thinking risk leaves were reviewed; [risk-frame evidence](./wiring-audit-thinking-risk-frames.md)
records immutable plan candidates, hypothetical-not-realized attack paths, evidence-derived buffers,
constraint-existence classification, owner-executed OODA cycles, exact optional artifact/worktree
identity, sensitive untrusted inputs, separate tool/production/action authority, no automatic
follow-ons, and Thinking/caller returns. Targeted Thinking metadata/HTML were repaired and compacted,
restoring zero-warning lint without counting the parent hub.

## Planning and coordination batch

Five additional skills reviewed; [planning evidence](./wiring-audit-planning.md)
records corrected parent routes, workspace/authority boundaries and verification.
Parent hubs received targeted updates and still require their own full audits.

## Review and verification batch

Six more skills reviewed; [review evidence](./wiring-audit-review.md) records the
actual-candidate contract, scoped/read-only caller returns, verification evidence
rules and aligned hub routes. Security Auditor received a targeted differential
mode correction; its complete reference tree is still pending.

## Security audit and dependency-review batch

Two more skills reviewed; [security evidence](./wiring-audit-security.md) records
the completed Security Auditor reference audit, dependency-review methodology,
schema/helper repairs and regression coverage. Other security specialists remain
pending; reviewing their main files alone does not count as completion.

## Security hardening batch

One more skill reviewed; [hardening evidence](./wiring-audit-hardening.md) records
scoped implementation/workspace returns, consolidated references, corrected security
examples and reference-graph lint regression tests. Prompt-injection and package-audit
specialists were pending at this checkpoint.

## Prompt-injection defense batch

One more skill reviewed; [prompt-injection evidence](./wiring-audit-prompt-defense.md)
records caller-preserving parent routes, read-only assessment versus authorized edits,
historical-source adaptation, corrected manifest validation and bounded/redacted input
handling. The package supply-chain specialist was pending at this checkpoint.

## Package supply-chain audit batch

One more skill reviewed; [package-audit evidence](./wiring-audit-package-security.md)
records recommendation-only parent/ingest returns, fixed-snapshot and sandbox/worktree
boundaries, complete source adaptation, scanner coverage/budget/privacy repairs,
permission/link-aware comparison and create-only reports. Other domains remain pending.

## Tool-schema design batch

One more skill reviewed; [tool-schema evidence](./wiring-audit-tool-schema.md) records
design/review/edit modes, parent and specialist caller returns, conditional workspace
use, external authority versus JSON shape, historical-source adaptation, and a bounded,
redacted validator that rejects ambiguous hostile input. Other Agent Engineering
children and their complete references remain pending.

## Error-handling batch

One newly added skill reviewed; [error-handling evidence](./wiring-audit-error-handling.md)
records its atomic failure-policy boundary, Architecture ownership, conditional Ship and
Review caller returns, pinned review candidate, and worktree/authority behavior. Its full
reference package and source ledger were reviewed; other Architecture children remain
pending.

## API and interface design batch

One more Architecture leaf reviewed; [API/interface evidence](./wiring-audit-api-interface.md)
records its consumer-contract boundary, formal Ship caller, conditional workspace/return
behavior, and corrections to compatibility, validation, pagination, update, idempotency, and
external-effect guidance. Other Architecture children remain pending.

## Codebase-design batch

One more Architecture leaf reviewed; [codebase-design evidence](./wiring-audit-codebase-design.md)
records its lean vocabulary disclosure, evidence-based seam/depth heuristics, conditional Ship
return, coverage-preserving test migration, and explicit-only sub-agent exploration. Other
Architecture children remain pending.

## Deprecation and migration batch

One more Architecture leaf reviewed; [deprecation evidence](./wiring-audit-deprecation.md)
records its consumer/evidence ledger, separately authorized removal gate, conditional Ship
worktree return, and strict database-specialist boundary. Other Architecture children remain
pending.

## Architecture hub batch

The Architecture parent is now reviewed; [hub evidence](./wiring-audit-architecture-hub.md)
records complete child dispatch, bounded read-only scan/worktree behavior, explicit-only
delegation, static local report safety, caller returns, and repaired HTML/workflow/flow surfaces.
Several remaining Architecture children are still pending.

## Clean-craftsmanship batch

One more Architecture leaf reviewed; [craftsmanship evidence](./wiring-audit-clean-craftsmanship.md)
records its lean advice-only boundary, context-sensitive operative principles, historical/non-
operative book distillation, F-C1 route, and explicit no-worktree/no-edit return. Other
Architecture children remain pending.

## Coding-standards batch

One more Architecture/Ship leaf reviewed; [coding-standards evidence](./wiring-audit-coding-standards.md)
records its scoped candidate contract, repository-authority precedence, explicit no-worktree/no-review-
mutation behavior, bounded verification, and F-C1 route. Other Architecture and Ship children remain
pending.

## Go-best-practices batch

One more Architecture/Ship/Review leaf reviewed; [Go evidence](./wiring-audit-go-best-practices.md)
records repaired three-parent dispatch, caller/worktree/read-only preservation, repository toolchain
authority, contextual interface/error/concurrency guidance, and bounded verification. Other children
of those parents remain pending.

## Graphify batch

One more Architecture satellite reviewed; [Graphify evidence](./wiring-audit-graphify.md) records
its corrected extract/query command surface, pinned corpus/worktree/output ownership, per-worktree
artifact isolation, local code-only default, non-persistent reads, and source-verification boundary.
Other Architecture children remain pending.

## Project-wiki-manager batch

One more Architecture documentation leaf reviewed; [project-wiki evidence](./wiring-audit-project-wiki.md)
records declared-source and exact-worktree provenance, read-only query/audit modes, scoped write
authority, repository-native layout, code-evidence support, flexible grounding/templates, and a
substantially leaner reference package. Other Architecture children remain pending.

## Living-documentation-governor batch

One more Architecture/Ship documentation leaf reviewed; [living-doc evidence](./wiring-audit-living-documentation.md)
records exact-candidate/worktree provenance, read-only assessment versus scoped update, truthful
trigger obligations, required-check presence, shared-worktree hook safety, repository-native
placement, and a leaner adapted reference package. Other Architecture/Ship children remain pending.

## Software-architect batch

One Architecture/Review specialist reviewed; [software-architect evidence](./wiring-audit-software-architect.md)
records reconciled domain-entry versus depth ownership, three-parent dispatch, pinned read-only
candidate/worktree behavior, viable non-forced alternatives, evidence-backed quantitative claims,
conditional recommendations, and specialist returns. Other Review/Ship children remain pending.

## Implement-hub batch

The Ship parent is now reviewed; [implement-hub evidence](./wiring-audit-implement-hub.md) records
clear-request entry, exact workspace/candidate/authority inheritance, conditional worktree isolation,
explicit-only delegation, behavior-selected evidence, bounded review/repair convergence, separately
authorized Git/external effects, lean operative references, and complete metadata/workflow/HTML/flow
surface parity. Its remaining children still require their own semantic audits.

## Karpathy-guidelines batch

One Ship process leaf is now reviewed; [Karpathy evidence](./wiring-audit-karpathy-guidelines.md)
records explicit opt-in triggering, a single caller-preserving checklist job, exact candidate/worktree/
authority inheritance, load-bearing assumption handling, safety-preserving simplicity, a surgical
scope ledger, behavior-selected falsifying evidence, and return to Ship without Git/external effects.
Other Ship children remain pending.

## CI/CD and automation batch

One Ship/DevOps leaf is now reviewed; [CI/CD evidence](./wiring-audit-ci-cd.md) records
its single workflow/check-contract boundary, dual-parent caller return, exact candidate/
worktree/authority identity, required-context honesty, root-versus-downstream failure
ownership, conditional workspace use, secure artifact-oriented design, and separately
authorized remote effects. Other Ship and DevOps children remain pending.

## Observability and instrumentation batch

One Ship/DevOps/Agent Engineering leaf is now reviewed; [observability evidence](./wiring-audit-observability.md)
records its one-behavior question-to-signal boundary, three-parent caller return, exact candidate/
worktree/environment/authority identity, conditional signal selection, cardinality and content-privacy
controls, and separately authorized hosted verification and operations. Other children of those
parents remain pending.

## Shipping and launch batch

One Ship/DevOps lifecycle leaf is now reviewed; [shipping evidence](./wiring-audit-shipping.md)
records its immutable release-candidate boundary, plan/read-only/authorized-execution modes,
two-parent caller returns, exact artifact/environment/worktree/authority identity, risk-derived
readiness ledger, evidence-driven stage gates, state-aware recovery, and separately authorized
Git/remote/production effects. Other Ship and DevOps children remain pending.

## Frontend UI engineering batch

One Ship/UI-UX implementation leaf is now reviewed; [frontend UI evidence](./wiring-audit-frontend-ui.md)
records its bounded interaction-surface job, corrected Ship-primary ownership, two-parent caller
returns, exact candidate/worktree/service authority, repository-native architecture, applicable
interaction/accessibility state contract, and fresh rendered/runtime evidence requirements. Other
Ship and UI/UX children remain pending.

## Performance optimization batch

One Diagnose/Ship specialist is now reviewed; [performance evidence](./wiring-audit-performance.md)
records its one-experiment boundary, dual-parent caller return, exact candidate/worktree/protocol/
shared-resource authority, comparable baseline and raw-sample evidence, causal hypothesis and
explicit disposition, database/cache/load safety, and conditional regression guards. Other
Diagnose and Ship children remain pending.

## Browser DevTools evidence batch

One Diagnose runtime-evidence leaf is now reviewed; [browser evidence](./wiring-audit-browser-devtools.md)
records its read-only session boundary, exact candidate/server/profile/fixture and interaction
authority, Diagnose/Frontend UI/Performance returns, untrusted browser-data handling, narrow
redacted capture, and claim-specific evidence limits. Other Diagnose children remain pending.

## Playwright browser testing batch

One Diagnose regression-test leaf is now reviewed; [Playwright evidence](./wiring-audit-playwright.md)
records its one-check author/repair/run boundary, exact candidate/worktree/server/fixture and
interaction authority, Diagnose/DevTools/Frontend UI/Performance returns, non-mutating preflight,
contract reconciliation, stable locator and flake rules, untrusted-data handling, narrow artifacts,
and scenario-bounded verdict. Other Diagnose children remain pending.

## Diagnosing bugs hub batch

The Diagnose parent is now reviewed; [Diagnose evidence](./wiring-audit-diagnosing-bugs.md)
records its diagnosis-only boundary and authorized Ship exit, removal from Setup, specific
triggers, exact candidate/worktree/environment/evidence/probe authority, F-DIAG1 specialist
selection, reproduce-or-observe honesty, calibrated conclusions, safe historical-source and
HITL handling, and aligned metadata/workflow/HTML/flow surfaces. Its remaining children still
require their own semantic audits.

## TDD batch

The core Ship/Diagnose TDD pipeline is now reviewed; [TDD evidence](./wiring-audit-tdd.md)
records its one-slice red→green boundary, F-TDD1 fit gate, grounded independent oracle,
Ship/Diagnose/plan-execution returns, removal from Setup, exact candidate/worktree/service
ownership, user-work preservation, honest red/green dispositions, proportional verification,
contextual test/mocking/portfolio guidance, and historical-source isolation. Remaining Ship
and Diagnose children still require their own semantic audits.

## Setup hub batch

The Setup parent is now reviewed; [Setup evidence](./wiring-audit-setup-rohitas-skills.md)
records its one-child router boundary, exact consumer-repository/worktree/authority
handoff, read-only hub behavior, F-S1-only selection, removal of unrelated legacy
children/forks, template-side-effect limits, multiline issue-body safety, and aligned
metadata/workflow/HTML/flow paths. The [issue-tracker child](./wiring-audit-setup-issue-tracker.md)
is also reviewed: local SSOT/pointer writes, evidence-based tracker selection,
idempotent verification, explicit parent return, and strict separation from remote
tracker authority. The [domain-doc](./wiring-audit-setup-domain-docs.md),
[vault-root](./wiring-audit-setup-vault-root.md), and
[triage-label](./wiring-audit-setup-triage-labels.md) children now share the same
candidate/worktree/authority and idempotent return contract while preserving their
distinct content, privacy, and remote-state boundaries. The full Setup cluster is
individually reviewed; final cross-catalog reconciliation remains pending.

## Action-first output batch

One Butler session-mode leaf is now reviewed;
[action-first evidence](./wiring-audit-action-first-output.md) records explicit-only
activation, caller return, scope/authority neutrality, non-medical framing, honest
host-session persistence, required-detail preservation, and the decision that
worktrees/tools are inapplicable to presentation-only mode changes.

## Butler routing-apex batch

The routing apex is now reviewed; [Butler evidence](./wiring-audit-butler.md)
records direct-skill-first selection, F7-only material ambiguity, all 32 real exits,
removal of the stale Setup detour, live-file authority over generated projections,
read-only/worktree-inapplicable behavior, corrected hub/manifest links, and safe
route-index truncation. Remaining child semantics still require individual audits.

## Catalog governance batch

Nine catalog-governance skills are now reviewed; [governance evidence](./wiring-audit-catalog-governance.md)
records one pinned catalog change-set, one body-candidate authoring operation, a true create wrapper,
read-only discovery/reflection/lint modes, one-cluster atomization, fixed-corpus private authoring,
proportional evaluation, revision-safe worktree/dirty ownership, and separately gated installation,
sync, commit, push, publication, and external/global effects. The redundant F-A3/F10 confirmation forks
and hidden npx/subagent/viewer/deploy workflows were removed; operative source mega-guides are now lean
provenance adaptations. Individual semantic coverage was **224 of 232** live skills at that checkpoint.

## Final eight-skill batch

The remaining eight skills are now reviewed; [final-eight evidence](./wiring-audit-final-eight.md) records one-artifact
creative leaves, a read-only risk-based codebase-review plan, an external-customer evidence audit, one-pass adversarial
claim review, diagnose-versus-fix text normalization, one-answer research, and one self-contained HTML deck. Imported
mega-workflows and stale automatic network/install/batch/staging/follow-on paths were removed. Parent route, caller
return, candidate/worktree/shared-state, effect-authority, and operative-reference contracts now agree. Individual
semantic coverage is **232 of 232** live skills; final inventory and verification remain below.

## Final reconciliation

- Live disk and tracker agree: 232 skill packages, 232 tracker rows, no missing/extra/pending row.
- Generated route index contains 232 skills; hub membership reports 234 memberships and zero orphans.
- Routing regression suite: 726 tests passed, including 11 final-eight tests.
- Other catalog validators: 69 tests passed across boundary manifests, human-in-the-loop policy, MCP/tool manifests,
  SDD helpers, security findings, package audit, and evaluation aggregation.
- Catalog lint: 0 critical, 0 warnings, 44 informational topology/lean notes; gate passed.
- All changed files in the final batch pass targeted `git diff --check`; four affected workflow JSON files parse.
- No install, host sync, commit, push, merge, deployment, publication, browser action, or remote service mutation ran.

## Per-skill coverage

All rows received the structural lint and declared-parent comparison on 2026-09-11.
“Targeted updates” means a first pass only; it does not count as full semantic completion.

| Skill | Semantic audit status | Evidence / remaining work |
|---|---|---|
| `0-agent-engineering` | Reviewed; final catalog sweep pending | Pure one-operation router with complete nine-child parity, F-AE1 material-only selection, candidate/worktree/trust/privacy/authority handoff, shared provider/service boundaries, no hub effects, and Butler/leaf returns; [evidence](./wiring-audit-agent-engineering-hub.md) |
| `0-butler` | Reviewed; final catalog sweep pending | Direct-skill-first routing, F7-only material ambiguity, complete 32-exit parity, no Setup detour or execution effects, current hub/manifest paths, and token-safe route-index generation; [evidence](./wiring-audit-butler.md) |
| `0-devops` | Reviewed; final catalog sweep pending | Complete 17-child metadata/workflow/HTML/flow parity, direct one-specialist routing, material-only F-O1, exact environment/candidate/worktree/authority handoff, shared-resource boundaries, effect-specific approval, recovery-as-operation, and actual-caller return; [evidence](./wiring-audit-devops-hub.md) |
| `0-diagnosing-bugs` | Reviewed; final catalog sweep pending | Diagnosis-only causal-evidence return, Setup membership removed, specific triggers, exact candidate/worktree/environment/probe authority, F-DIAG1, calibrated non-reproduction, safe HITL/sources, and aligned hub surfaces; [evidence](./wiring-audit-diagnosing-bugs.md) |
| `0-git` | Reviewed; final catalog sweep pending | Normalization dispatch, F-G2, conditional caller returns; SKILL/JSON/flows/HTML aligned; see [Git evidence](./wiring-audit-git.md) |
| `0-grilling` | Reviewed | Consent-respecting one-candidate interview; exact caller/evidence/authority and optional worktree identity; direct specialist routes; no confidence ritual or automatic delivery |
| `0-implement` | Reviewed; final catalog sweep pending | Clear-request entry, conditional worktree isolation, caller/authority inheritance, explicit-only delegation, claim-based verification, review/repair convergence, separately authorized closure, and aligned parent surfaces; [evidence](./wiring-audit-implement-hub.md) |
| `0-improve-codebase-architecture` | Reviewed; final catalog sweep pending | Complete child dispatch, bounded read-only scan, explicit-only delegation, safe static report, Ship return, and aligned hub surfaces; [evidence](./wiring-audit-architecture-hub.md) |
| `0-learn` | Reviewed; final catalog sweep pending | Read-only direct one-leaf router, material-only F-L1/F-L2, exact child/caller payload, complete workflow/HTML/flow parity, no worktree/effects, and live Tutor route; [evidence](./wiring-audit-learn-hub.md) |
| `0-office` | Reviewed | [Office hub evidence](./wiring-audit-office-hub.md): one-artifact router, exact caller/source/output/authority and optional worktree, shared-state warning, ten leaves plus explicit HTML-slides cross-route, no hidden conversion/publication chain |
| `0-ponytail` | Reviewed | Explicit coding-only overlay/direct-child router; comprehension before ladder; caller candidate/worktree/authority inheritance; acceptance/safety/repository/test/reporting invariants; Ultra oversight; no implicit child/review/Git chain; [evidence](./wiring-audit-ponytail.md) |
| `0-review` | Reviewed; final catalog sweep pending | Actual candidate, bounded evidence, read-only caller return and aligned parent routes; see [review evidence](./wiring-audit-review.md) |
| `0-rohitas-vault-wiki` | Reviewed; final catalog sweep pending | One-operation read-only router, complete Vault/Obsidian/on-ramp dispatch, exact root/candidate/worktree/authority handoff, private-untrusted data and shared-state boundaries, lean nine-reference schema package, and Butler return; [evidence](./wiring-audit-vault-hub.md) |
| `0-setup-rohitas-skills` | Reviewed; final catalog sweep pending | One-child setup router, exact consumer repository/worktree/authority return, F-S1-only selection, template/external-effect boundaries, stale membership removal, and aligned hub artifacts; [evidence](./wiring-audit-setup-rohitas-skills.md) |
| `0-skill-creator` | Reviewed | One pinned body candidate in draft/update/trigger-eval/output-eval mode; proportional evidence; no automatic placement/install/sync/Git/publication; [evidence](./wiring-audit-catalog-governance.md) |
| `0-skill-manager` | Reviewed | One explicit bounded catalog change-set, revision-safe dirty-worktree ledger, affected projections and lint, separately gated destructive/external/global effects; [evidence](./wiring-audit-catalog-governance.md) |
| `0-thinking` | Reviewed; final catalog sweep pending | Pure direct-match-first one-leaf router with exact 33-child parity, material-only F-T1/F-T2, immutable candidate/evidence/authority and optional worktree handoff, NONE disposition, no automatic composition/diagnosis/action, corrected Grilling/risk-response labels, and actual-caller return; [evidence](./wiring-audit-thinking-hub.md) |
| `0-triage` | Reviewed | Pure inbox/assess/apply router; exact tracker/candidate revision and optional worktree; configured taxonomy/privacy/authority; generated-ticket exclusion; F-TR1; no hub effects or automatic implementation; [evidence](./wiring-audit-triage.md) |
| `0-ui-ux` | Reviewed | [UI/UX hub evidence](./wiring-audit-ui-ux-hub.md): pure one-specialist router, complete twelve-child surface, material-only F-UI1, exact candidate/authority/worktree/runtime handoff, shared UI-system state, no auto pipeline, repaired package links |
| `0-wayfinder` | Reviewed | Pure chart/advance/settled-spec router; immutable map candidate, optional exact worktree, shared-state and authority handoff; material F-W1/F-W2/F8; no hub effects or direct implementation; [evidence](./wiring-audit-wayfinder.md) |
| `1-action-first-output` | Reviewed; final catalog sweep pending | Explicit presentation-only session mode, Butler return, scope/authority neutrality, honest persistence, no file/tool/worktree effects, and override by newer requirements; [evidence](./wiring-audit-action-first-output.md) |
| `1-agent-evaluation` | Reviewed; final catalog sweep pending | One decision and fixed baseline/candidate set, design/analysis/execution modes, exact optional worktree/protocol identity, source/privacy/contamination ledger, qualified graders, external-effect authority, honest uncertainty and parent/specialist returns; [evidence](./wiring-audit-agent-evaluation.md) |
| `1-agent-pr-review` | Reviewed; final catalog sweep pending | Actual candidate, bounded evidence, read-only caller return and aligned parent routes; see [review evidence](./wiring-audit-review.md) |
| `1-agent-workflow-observer` | Reviewed; final catalog sweep pending | One fixed completed/paused run snapshot, observed/inferred/unknown evidence, exact optional worktree plus local/remote/CI provenance, private/untrusted data limits, existing-home and recurrence checks, proposal-only authority, no live supervision/application, and parent return; [evidence](./wiring-audit-agent-workflow-observer.md) |
| `1-ai-platform-operations` | Reviewed; final catalog sweep pending | One bounded design/assessment/authorized platform operation, exact served candidate/environment and optional worktree, shared endpoint/data/cache/GPU authority, untrusted model/RAG evidence, provenance/tenant gates, infrastructure-versus-quality separation, effect-specific mutation authority, truthful convergence, and DevOps return; [evidence](./wiring-audit-ai-platform-operations.md) |
| `1-anti-sycophancy` | Reviewed; final catalog sweep pending | Explicit evidence-before-agreement overlay, one-request scope, earned agreement, exact optional artifact/worktree identity, no false balance/tools/effects, and Grilling/caller return; [evidence](./wiring-audit-grilling-response-modes.md) |
| `1-api-and-interface-design` | Reviewed; final catalog sweep pending | Consumer-visible contract boundary, Architecture/Ship routes, conditional workspace/caller return, and complete adapted-guide review; [evidence](./wiring-audit-api-interface.md) |
| `1-atomic-git-commits` | Reviewed; final catalog sweep pending | Staged ownership, candidate verification, caller return; historical guide non-operative; helper argument validation; see [Git evidence](./wiring-audit-git.md) |
| `1-banner-design` | Reviewed | One promotional artifact; exact brief/dimensions/source/output/effect authority; no forced export, variants, browser research, or publication; [evidence](./wiring-audit-final-eight.md) |
| `1-brainstorm` | Reviewed; final catalog sweep pending | One design-options memo, optional exact worktree candidate, evidence/assumption separation, viable alternatives without quotas, no invented product facts or automatic visual/spec/subagent/Git/implementation effects, and Grilling/caller return; [evidence](./wiring-audit-grilling-design-children.md) |
| `1-brand` | Reviewed | Pure guideline/review/context-extraction sub-hub, material-only F-BR1, exact source/candidate/worktree/privacy/authority state, shared design/approval/publication boundary, no router effects or token/asset pipeline, and UI/UX/caller return; [evidence](./wiring-audit-brand.md) |
| `1-bro` | Reviewed; final catalog sweep pending | One identified prior reply, exact-meaning re-expression, direct new-topic routing, style-only examples, no tools/worktree/effects, and Butler return; [evidence](./wiring-audit-presentation-modes.md) |
| `1-browser-testing-with-devtools` | Reviewed; final catalog sweep pending | One read-only browser evidence session, exact candidate/server/profile/fixture authority, Diagnose/Frontend UI/Performance returns, untrusted-data handling, narrow capture, and claim-specific evidence limits; [evidence](./wiring-audit-browser-devtools.md) |
| `1-caveman` | Reviewed; final catalog sweep pending | Explicit ultra-terse overlay, critical-meaning preservation, ordinary brevity boundary, no tools/worktree/effects, and Butler return; [evidence](./wiring-audit-presentation-modes.md) |
| `1-ci-cd-and-automation` | Reviewed; final catalog sweep pending | Workflow/check-contract boundary, dual-parent returns, exact candidate/worktree/authority, truthful required contexts, failure ownership, secure artifact design, conditional worktrees, and separately authorized remote effects; [evidence](./wiring-audit-ci-cd.md) |
| `1-clean-craftsmanship` | Reviewed; final catalog sweep pending | Lean principle-level advice, context-sensitive operative guide, historical source boundary, F-C1, and no-worktree/no-edit caller return; [evidence](./wiring-audit-clean-craftsmanship.md) |
| `1-cloud-platform-operations` | Reviewed; final catalog sweep pending | One provider-resource design/assessment/authorized operation, exact resource/environment and optional worktree, shared account/API/billing/data authority, controller ownership, IaC-drift prevention, effect-specific mutation gates, convergence proof, and DevOps return; [evidence](./wiring-audit-infrastructure-operations.md) |
| `1-code-comments` | Reviewed | One public/exported doc surface in assessment/edit mode; exact worktree/candidate/symbol/convention/authority; untrusted evidence and contract grounding; generated-source ownership; bounded doc proof; no behavior/refactor/review/Git chain; [evidence](./wiring-audit-code-comments-layout.md) |
| `1-code-explainer` | Reviewed; final catalog sweep pending | One exact code candidate, worktree/HEAD/dirty provenance, adjacent-read bounds, observed/inferred/runtime separation, no fixed audience/depth ritual, no mutation, and Learn return; [evidence](./wiring-audit-object-explanation.md) |
| `1-code-review` | Reviewed; final catalog sweep pending | Actual candidate, bounded evidence, read-only caller return and aligned parent routes; see [review evidence](./wiring-audit-review.md) |
| `1-codebase-design` | Reviewed; final catalog sweep pending | Lean module-design router, Architecture/Ship routes, evidence-based seam heuristics, caller/worktree return, and explicit-only alternatives delegation; [evidence](./wiring-audit-codebase-design.md) |
| `1-codebase-review-strategy` | Reviewed | One read-only risk-based coverage plan; exact repo/worktree/candidate/evidence boundary; no fixed tiers, installs, broad scans, or review execution; [evidence](./wiring-audit-final-eight.md) |
| `1-coding-standards` | Reviewed; final catalog sweep pending | Scoped repository conventions, Architecture/Ship routes, no-worktree/read-only preservation, bounded verification, and F-C1; [evidence](./wiring-audit-coding-standards.md) |
| `1-competitive-analysis` | Reviewed; final catalog sweep pending | One fixed named-competitor/market decision, exact as-of and optional artifact/worktree identity, current cited claim ledger, untrusted-source and collection/account/contact limits, no unsupported market/roadmap claims or automatic action, and Thinking/caller return; [evidence](./wiring-audit-ethical-strategy-competition.md) |
| `1-complete-pr-review` | Reviewed; final catalog sweep pending | Actual candidate, bounded evidence, read-only caller return and aligned parent routes; see [review evidence](./wiring-audit-review.md) |
| `1-compliance-engineering` | Reviewed; final catalog sweep pending | One pinned requirement/control evidence package in design/assessment/repository mode, exact source/scope/period/population/candidate/worktree, private untrusted evidence, traceable control ledger, design-versus-operating-effectiveness limits, no legal/certification/risk authority, and DevOps return; [evidence](./wiring-audit-compliance-postgres.md) |
| `1-constraint-driven-development` | Reviewed; final catalog sweep pending | Proposed/measured/enforced quality contract; read-only assessment, safe floor semantics and conditional automation; see [planning evidence](./wiring-audit-planning.md) |
| `1-container-platform-operations` | Reviewed; final catalog sweep pending | One image/registry/runtime/orchestrator operation, exact digest/controller/environment and optional worktree, shared daemon/cache/registry/cluster boundaries, untrusted artifact handling, GitOps reconciliation, differentiated validation/build/run/push/apply effects, and DevOps return; [evidence](./wiring-audit-infrastructure-operations.md) |
| `1-context-monitor` | Reviewed; final catalog sweep pending | Evidence-backed continue/compact/handoff disposition, no invented telemetry, safe checkpointing, immutable task state, no tools/worktree/effects, and Butler return; [evidence](./wiring-audit-session-continuity.md) |
| `1-create-skill` | Reviewed | True one-body authoring wrapper; returns creator candidate and never auto-places or installs; [evidence](./wiring-audit-catalog-governance.md) |
| `1-critique` | Reviewed; final catalog sweep pending | One explicitly fixed candidate, untrusted evidence and repository/worktree provenance, issue/falsifier/mitigation ledger, preserved strengths, optional non-dogmatic guide, no automatic research/action, and Grilling/caller return; [evidence](./wiring-audit-grilling-response-modes.md) |
| `1-customer-experience-audit` | Reviewed | One read-only external-customer backlog; pinned runtime/account/evidence state; no browser, participant, analytics, redesign, or implementation effects; [evidence](./wiring-audit-final-eight.md) |
| `1-database-and-storage-operations` | Reviewed; final catalog sweep pending | One data-service/storage design/assessment/authorized operation, exact topology/resource/environment and optional worktree, sensitive data/backup controls, backup-versus-restore evidence, lock/replication/client boundaries, isolated restore authority, convergence proof, and DevOps return; [evidence](./wiring-audit-stateful-operations.md) |
| `1-defuddle` | Reviewed | [Office text-leaf evidence](./wiring-audit-office-text-leaves.md): one immutable HTML source/result, official CLI contract, explicit network/read/write authority, optional exact worktree, no install/crawl/research/publish chain |
| `1-deprecation-and-migration` | Reviewed; final catalog sweep pending | Consumer/evidence ledger, explicit removal gate, Architecture/Ship routes, conditional worktree return, and database-specialist boundary; [evidence](./wiring-audit-deprecation.md) |
| `1-design` | Reviewed | One logo/icon/social/identity artifact; exact rights/provider/output authority; no implicit secrets, provider call, batch, CIP, report, or install; [evidence](./wiring-audit-final-eight.md) |
| `1-design-system` | Reviewed | One draft/applied versioned contract set, exact consumer/source/destination/worktree/ownership identity, evidence-based layering, untrusted defaults, bounded helpers and proof, slide-route separation, no implicit UI/brand/publish effects, and UI/UX/caller return; [evidence](./wiring-audit-design-system.md) |
| `1-diagram-maker` | Reviewed | [Diagram evidence](./wiring-audit-diagram-maker.md): one evidence-bounded artifact, no hidden architecture decisions, exact caller/format/destination/authority and optional worktree, shared visual state, untrusted inputs, syntax/visual proof, no publish chain |
| `1-discover-skills` | Reviewed | Read-only fixed-snapshot external discovery, fit/license/maintenance/permission evidence, no popularity shortcut or npx/install execution, supply-chain/manager handoff; [evidence](./wiring-audit-catalog-governance.md) |
| `1-docx` | Reviewed | [DOCX evidence](./wiring-audit-docx.md): one immutable source-set operation, exact caller/output/author/authority and optional worktree, untrusted OOXML, source preservation, revision-safe writes, layered verification, lean compatibility guide |
| `1-domain-modeling` | Reviewed; final catalog sweep pending | Exactly one accepted context-language change set or ADR in draft/apply mode, pinned authorized worktree and exact target, collision/generated/conflict safeguards, no second artifact/Git/implementation effects, and Grilling/caller return; [evidence](./wiring-audit-grilling-design-children.md) |
| `1-doubt-driven-development` | Reviewed | One read-only claim disposition; immutable evidence/worktree candidate; no fresh-agent, cross-model, repeated-loop, or fix effects; [evidence](./wiring-audit-final-eight.md) |
| `1-error-handling` | Reviewed; final catalog sweep pending | Atomic failure behavior, three parent routes, pinned read-only candidate, conditional workspace and caller return; [evidence](./wiring-audit-error-handling.md) |
| `1-execute-plan` | Reviewed; final catalog sweep pending | Direct execution, resume evidence, conditional helpers and caller return; see [workspace evidence](./wiring-audit-workspaces.md) |
| `1-execution-flow-comments` | Reviewed | One explicitly requested function flow block in assessment/edit mode; exact worktree/function/revision; real path and untrusted-evidence checks; no fixed quota or invented branches; bounded reconciliation; no implementation/other-function/review/Git chain; [evidence](./wiring-audit-code-comments-layout.md) |
| `1-explain-with-example` | Reviewed; final catalog sweep pending | Exact `???` object boundary, qualifier/evidence preservation, untrusted embedded instructions, non-upgraded causal/remedy claims, one grounded example, no worktree/tools, and Learn return; [evidence](./wiring-audit-object-explanation.md) |
| `1-finish-branch` | Reviewed; final catalog sweep pending | Honored prior choice, detached menu, candidate verification and owned cleanup; see [workspace evidence](./wiring-audit-workspaces.md) |
| `1-frontend-ui-engineering` | Reviewed; final catalog sweep pending | Bounded interaction surface, Ship-primary/UI-UX caller returns, exact candidate/worktree/service authority, repository-native architecture, applicable accessibility states, and fresh runtime evidence; [evidence](./wiring-audit-frontend-ui.md) |
| `1-git-changelog` | Reviewed; final catalog sweep pending | Pinned local range, read-only workspace applicability and conditional release handoff; see [Git evidence](./wiring-audit-git.md) |
| `1-git-text-normalization` | Reviewed | One diagnose or authorized exact-path fix; explicit index/blob/worktree state; no stage-to-preview, broad renormalization, commit, or remote effect; [evidence](./wiring-audit-final-eight.md) |
| `1-git-worktrees` | Reviewed; final catalog sweep pending | Task-fit checkout, explicit start, local-service ownership and caller evidence; see [workspace evidence](./wiring-audit-workspaces.md) |
| `1-github-cli` | Reviewed; final catalog sweep pending | Create/edit IDs, multiline preservation, uncertain-result reconciliation and caller return; see [Git evidence](./wiring-audit-git.md) |
| `1-github-pr-comment-intake` | Reviewed; final catalog sweep pending | Paginated read-only queue, coverage gaps and source IDs; no repair trigger; see [Git evidence](./wiring-audit-git.md) |
| `1-go-best-practices` | Reviewed; final catalog sweep pending | Architecture/Ship/Review routes, scoped caller/worktree contract, repository toolchain authority, contextual Go guidance, and bounded verification; [evidence](./wiring-audit-go-best-practices.md) |
| `1-graphify` | Reviewed; final catalog sweep pending | Explicit Architecture satellite, corrected CLI surface, pinned corpus/worktree/output, per-worktree artifacts, local-only extraction, and source-verification return; [evidence](./wiring-audit-graphify.md) |
| `1-grill-me` | Reviewed; final catalog sweep pending | One supplied-candidate interactive interview wrapper, explicitly no repository/tools/writes, delegation preserved, no automatic downstream work, and Grilling/caller return; [evidence](./wiring-audit-grilling-design-children.md) |
| `1-grill-with-docs` | Reviewed; final catalog sweep pending | One read-only repository-grounded interview, exact worktree/HEAD/dirty/deployment provenance, bounded untrusted evidence, user-only decisions, separate domain-artifact apply authority, and Grilling/caller return; [evidence](./wiring-audit-grilling-design-children.md) |
| `1-grok-help` | Reviewed; final catalog sweep pending | One Grok-specific local-evidence question, secret-minimized config reads, explicit edit authority, host-shared state, Skill Manager boundary, and Butler return; [evidence](./wiring-audit-session-continuity.md) |
| `1-handoff` | Reviewed; final catalog sweep pending | Butler-primary/Grilling-detour ownership, safe boundary, one redacted non-overwriting verified artifact, exact candidate/worktree/authority state, and caller return without execution; [evidence](./wiring-audit-session-continuity.md) |
| `1-hatch-pet` | Reviewed | [Hatch Pet evidence](./wiring-audit-hatch-pet.md): pure build/repair/validate/install sub-hub, F-PET1, no router effects, exact authority/worktree/global-state boundary, and lean live references |
| `2-hatch-pet-build` | Reviewed | [Hatch Pet evidence](./wiring-audit-hatch-pet.md): one fresh run-owned validated candidate, one Imagine call per job, canonical identity, no research/install/cleanup/mandatory delegation |
| `2-hatch-pet-repair` | Reviewed | [Hatch Pet evidence](./wiring-audit-hatch-pet.md): one verified defect class in a copied candidate, protected design scope, packaging-eligible row repair, affected-gate proof, no installed-pet mutation |
| `2-hatch-pet-validate` | Reviewed | [Hatch Pet evidence](./wiring-audit-hatch-pet.md): read-only hash-pinned contract assessment, structural/visual evidence separation, honest coverage, no repair/install authority |
| `2-hatch-pet-install` | Reviewed | [Hatch Pet evidence](./wiring-audit-hatch-pet.md): explicit hash-bound local install, exact destination/collision/recovery authority, atomic pair staging, no activation/sync/cleanup |
| `1-honest-advisor` | Reviewed; final catalog sweep pending | One supplied interpersonal event/decision, observation/interpretation/motive separation, privacy and location-aware safety stop, no false balance/diagnosis/retrieval/tools, one reversible suggestion, and Grilling/caller return; [evidence](./wiring-audit-grilling-response-modes.md) |
| `1-human-in-the-loop` | Reviewed; final catalog sweep pending | One workflow/action-family policy, design/review/edit modes, optional exact worktree candidate, owner policy/stable identity and immutable approval binding, current-authority/protected-effect separation, explicit conservative validator profile, and symmetric specialist returns; [evidence](./wiring-audit-human-in-the-loop.md) |
| `1-identity-and-secrets-management` | Reviewed; final catalog sweep pending | One identity/access/secret design/assessment/authorized operation, immutable principal/resource/policy and optional worktree identity, shared IdP/KMS/Vault/session/consumer state, secret non-disclosure, assessment-without-remediation, approval binding, staged rotation and consumer proof, and DevOps return; [evidence](./wiring-audit-platform-identity.md) |
| `1-imagine` | Reviewed | [Imagine evidence](./wiring-audit-imagine.md): one raster result, current host contract, exact caller/reference/privacy/authority/worktree boundary, untrusted media, deterministic-content routes, and no hidden search/video/publication/variant effects |
| `1-impeccable` | Reviewed | [Impeccable evidence](./wiring-audit-impeccable.md): one current-installed command, exact target/authority/worktree/server identity, shared package/browser/config state, stale archive excluded, no implicit install/edit/hooks/pins/doctor/publication |
| `1-incident-response` | Reviewed; final catalog sweep pending | One identified active incident through evidence-backed stable handoff, DevOps/Observability/Shipping caller returns, exact deployed/worktree/remote candidate, private untrusted evidence and append-only action ledger, per-action authority, explicit observation-window stability, and no automatic postmortem/resilience/cleanup; [evidence](./wiring-audit-incident-resilience.md) |
| `1-infrastructure-as-code` | Reviewed; final catalog sweep pending | One design/review/repository-edit IaC change with no apply, exact module/tool/backend/target/worktree identity, sensitive state/plan handling, remote init/validate/refresh/plan effects, immutable plan evidence binding, and DevOps return; [evidence](./wiring-audit-infrastructure-operations.md) |
| `1-inline-comments` | Reviewed | One internal why/constraint block in assessment/edit mode; exact worktree/block/revision; zero-comment default; no invented claims/refactor; machine-directive protection; bounded truth check; no neighboring-comment/review/Git chain; [evidence](./wiring-audit-code-comments-layout.md) |
| `1-internal-comms` | Reviewed | [Office text-leaf evidence](./wiring-audit-office-text-leaves.md): one evidence-bound internal draft, audience/classification/authority pinned, optional exact worktree, no invented facts/send/publish/convert/incident-operation chain |
| `1-json-canvas` | Reviewed | [JSON Canvas evidence](./wiring-audit-json-canvas.md): one create/bounded edit, stable IDs/unknown fields, exact consumer/authority/worktree, inert linked content, fresh-revision write, structural/visual proof boundary, lean references |
| `1-karpathy-guidelines` | Reviewed; final catalog sweep pending | Explicit Ship-only process checklist, exact candidate/worktree/authority inheritance and return, safety-preserving simplicity, scoped diff ledger, fitting evidence loop, and no independent mutations; [evidence](./wiring-audit-karpathy-guidelines.md) |
| `1-learning-diagnostic` | Reviewed; final catalog sweep pending | Minimal evidence-labeled learner profile, no demographic inference/re-asking/persistence, one material question at a time, no worktree/tools, and Learn caller return; [evidence](./wiring-audit-concept-learning.md) |
| `1-learning-explainer` | Reviewed; final catalog sweep pending | One concept-operation router, Learn/Vault caller identity, F-L3 only when material, evidence/authority preservation, no worktree/tools, and one-leaf return; [evidence](./wiring-audit-concept-learning.md) |
| `1-learning-glossary` | Reviewed; final catalog sweep pending | One evidence-grounded term operation, glossary-only mutation, collision/alias/history preservation, exact workspace provenance, idempotence, and Learn/Teach caller returns; [evidence](./wiring-audit-teaching-workspace.md) |
| `1-learning-progress-record` | Reviewed; final catalog sweep pending | One append-only decision-grade record, explicit evidence kinds, privacy minimization, new-record supersession, exact workspace provenance, and Learn/Teach caller returns; [evidence](./wiring-audit-teaching-workspace.md) |
| `1-lesson-authoring` | Reviewed; final catalog sweep pending | One new mission-linked lesson, non-overwrite/rescan behavior, exact workspace/candidate provenance, separated research, scoped verification, and Learn/Teach return; [evidence](./wiring-audit-teaching-workspace.md) |
| `1-level-explainer` | Reviewed; final catalog sweep pending | One first explanation at one evidenced audience, truth/source/safety invariants, conditional example/limitation, lean level guides, no worktree/tools, and Learn return; [evidence](./wiring-audit-concept-learning.md) |
| `1-living-documentation-governor` | Reviewed; final catalog sweep pending | Architecture/Ship routes, exact candidate/worktree, assessment versus update authority, honest trigger obligations, shared-hook safety, and contextual docs/ADR placement; [evidence](./wiring-audit-living-documentation.md) |
| `1-mcp-server-building` | Reviewed; final catalog sweep pending | One bounded server surface, design/review/implementation modes, exact optional worktree candidate, pinned protocol/SDK/client/transport, separate conformance/authorization controls, revision-aware compatibility, shared runtime-resource authority, explicit local manifest profile, and symmetric specialist returns; [evidence](./wiring-audit-mcp-server-building.md) |
| `1-mental-model-builder` | Reviewed; final catalog sweep pending | One relation-focused model with explicit mapping, prediction/use, breaking point, rendered-artifact boundary, no worktree/tools, and Learn return; [evidence](./wiring-audit-concept-learning.md) |
| `1-network-and-edge-operations` | Reviewed; final catalog sweep pending | One network/edge design/assessment/config/remote operation, exact source/destination/vantage/control-plane/certificate and optional worktree identity, private topology/traffic handling, bounded probe authority, propagation limits, distinct DNS/TLS/traffic effects, and DevOps return; [evidence](./wiring-audit-stateful-operations.md) |
| `1-observability-and-instrumentation` | Reviewed; final catalog sweep pending | One-behavior question-to-signal contract, three-parent returns, exact candidate/worktree/environment/authority, conditional signal selection, cardinality/content privacy, and separately authorized hosted verification; [evidence](./wiring-audit-observability.md) |
| `1-obsidian-bases` | Reviewed; final catalog sweep pending | One exact `.base` candidate/named view, active-version schema, optional worktree identity, bounded population/privacy, smallest hunk, static proof and separately authorized CLI runtime return; [evidence](./wiring-audit-obsidian-primitives.md) |
| `1-obsidian-cli` | Reviewed; final catalog sweep pending | One exact vault/target/command, local version-matched help, effect classification and action authority, argv/newline safety, targeted readback, shared app/sync/plugin state and parent return; [evidence](./wiring-audit-obsidian-primitives.md) |
| `1-obsidian-markdown` | Reviewed; final catalog sweep pending | One exact Markdown syntax hunk, configured root and optional worktree candidate, private/untrusted no-traversal input, active-schema preservation, literal/static verification and no app/runtime claims; [evidence](./wiring-audit-obsidian-primitives.md) |
| `1-parallel-agents` | Reviewed; final catalog sweep pending | Independent outputs, worktree/service ownership, actual live handles and verified caller-return synthesis; see [planning evidence](./wiring-audit-planning.md) |
| `1-pdf` | Reviewed | [PDF evidence](./wiring-audit-pdf.md): one immutable source-set operation, source preservation, optional exact worktree, untrusted sandbox boundary, overwrite/signing/redaction authority, independent verification and partial-effect return |
| `1-pending-migration-hygiene` | Reviewed | One cleanup candidate; exact worktree/version/hash/local-stack identity; rewrite proof only from complete observed provenance or exact human attestation; negative evidence cannot prove absence; no remote-ledger inspection; reference/collision/DDL-DML checks; safe no-op and caller return; [evidence](./wiring-audit-supabase.md) |
| `1-performance-optimization` | Reviewed; final catalog sweep pending | One measured experiment, Diagnose/Ship caller returns, exact candidate/worktree/protocol/shared-resource authority, comparable evidence, explicit disposition, and database/cache/load safety; [evidence](./wiring-audit-performance.md) |
| `1-perspective-analysis` | Reviewed; final catalog sweep pending | One fixed multi-lens decision, exact optional artifact/worktree identity, untrusted evidence and representation limits, no stereotypes/fake consensus, optional evidence-aware hats, no tools/automatic action, and Thinking/caller return; [evidence](./wiring-audit-perspective-analysis.md) |
| `1-pi-agent-rust` | Reviewed; final catalog sweep pending | Lean current-checkout adapter, exact worktree/dirty/shared-resource provenance, candidate commands only, and explicit Diagnose/Ship/Review/CI routes; [evidence](./wiring-audit-butler-satellites.md) |
| `1-plan-arbiter` | Reviewed; final catalog sweep pending | Grounded adopt/hybrid/revise decision, actual parent dispatch and no implicit execution; see [planning evidence](./wiring-audit-planning.md) |
| `1-platform-engineering` | Reviewed; final catalog sweep pending | One internal-platform design/review/repository implementation, exact user-job/matrix/candidate/worktree identity, untrusted template/dependency handling, shared build/portal/registry boundaries, versioned contract and owner-safe generation, representative-consumer proof without adoption claims, and DevOps return; [evidence](./wiring-audit-platform-identity.md) |
| `1-playwright-browser-testing` | Reviewed; final catalog sweep pending | One durable browser check, exact candidate/worktree/server authority, four caller returns, non-mutating preflight, contract/locator/flake discipline, and bounded artifacts/verdict; [evidence](./wiring-audit-playwright.md) |
| `1-plow-ahead` | Reviewed; final catalog sweep pending | Explicit authority-preserving overlay, inherited exact workflow/worktree state, routine reversible assumptions, no implicit delegation/Git/external effects, and caller return; [evidence](./wiring-audit-butler-satellites.md) |
| `1-ponytail-audit` | Reviewed | Read-only one-snapshot repository audit; exact worktree/candidate/root/classes/cutoff; untrusted-static boundary; enumerated or labeled sampled coverage; Chesterton evidence; risk/confidence ranking and estimated reductions; no repair/runtime/Git chain; [evidence](./wiring-audit-ponytail.md) |
| `1-ponytail-debt` | Reviewed | Read-only bounded marker ledger; exact worktree/candidate/root/grammar/cutoff; `rg`-first anchored scan; untrusted marker contents; no inferred owners/ceilings/triggers; honest zero coverage; no persistence/edit/issue chain; [evidence](./wiring-audit-ponytail.md) |
| `1-ponytail-gain` | Reviewed | One pinned upstream agentic benchmark card; corrected aggregate and predecessor disclosure; exact date/setup/sample; safety-floor and transfer limits; no repo measurement/prediction/fetch/mode/write effects; [evidence](./wiring-audit-ponytail.md) |
| `1-ponytail-help` | Reviewed | One-shot catalog-accurate levels/children card; coding/non-coding boundary; explicit activation and host-dependent persistence; removed nonexistent env/config/hook instructions; no mode/config/review effects; [evidence](./wiring-audit-ponytail.md) |
| `1-postgres-read-only` | Reviewed; final catalog sweep pending | One fixed question/snapshot and reviewed query, exact database/role/data/result and optional source-worktree identity, shared DB limits, non-writing/non-BYPASSRLS role, SELECT/routine/FDW and parser defenses, transaction/time/row/byte/privacy bounds, historical vendor note, and DevOps return; [evidence](./wiring-audit-compliance-postgres.md) |
| `1-pptx` | Reviewed | [PPTX evidence](./wiring-audit-pptx.md): one immutable source/content operation, exact slide/output/authority/worktree, untrusted package/assets, source preservation, separate edit/export effects, layered QA, lean references |
| `1-pr-comment-drafter` | Reviewed; final catalog sweep pending | Grounded draft and intended target; literal escapes preserved; conditional publication; see [Git evidence](./wiring-audit-git.md) |
| `1-pr-repair` | Reviewed; final catalog sweep pending | Shared workspace/scope/contract/CI checkpoints; head vs merge provenance and conditional rebase; see [Git evidence](./wiring-audit-git.md) |
| `1-pr-review-and-repair` | Reviewed; final catalog sweep pending | Shared checkpoints preserve one-at-a-time scope loop and review intent; see [Git evidence](./wiring-audit-git.md) |
| `1-pr-summarizer` | Reviewed; final catalog sweep pending | Pinned final diff/verification, local/remote distinction, conditional publication and corrected evals; see [Git evidence](./wiring-audit-git.md) |
| `1-progressive-deep-dive` | Reviewed; final catalog sweep pending | One identified prior target and one requested layer, preserved audience/evidence, explicit Research return, no automatic continuation/worktree/tools, and Learn caller return; [evidence](./wiring-audit-concept-learning.md) |
| `1-project-wiki-manager` | Reviewed; final catalog sweep pending | Declared sources, exact-worktree provenance, read-only query/audit, scoped writes, repository-native layout, contextual grounding/templates, and lean references; [evidence](./wiring-audit-project-wiki.md) |
| `1-prototype` | Reviewed; final catalog sweep pending | Bounded logic/UI experiment, F-P1, local-state evidence and no automatic promotion or cleanup; see [planning evidence](./wiring-audit-planning.md) |
| `1-quick-recap` | Reviewed; final catalog sweep pending | Evidence-driven display status without task-state mutation, required-final-structure precedence, historical-source isolation, no tools/worktree/effects, and Butler return; [evidence](./wiring-audit-presentation-modes.md) |
| `1-receive-review` | Reviewed; final catalog sweep pending | Assessment-only dispositions and authorized repair; no recursive PR loop; see [Git evidence](./wiring-audit-git.md) |
| `1-research` | Reviewed | One bounded cited answer plus optional requested persistence; source/version/cutoff and optional worktree identity; no background-agent, fetched-code, plan, or implementation chain; [evidence](./wiring-audit-final-eight.md) |
| `1-resilience-and-disaster-recovery` | Reviewed; final catalog sweep pending | One pre-incident plan/review/authorized exercise for one failure scenario, exact runbook/worktree/deployed target, shared service/data/region authority, private recovery material, containment revalidation, measured RTO/RPO, tabletop/backup proof limits, and DevOps return without live incident or cleanup; [evidence](./wiring-audit-incident-resilience.md) |
| `1-resolving-merge-conflicts` | Reviewed; final catalog sweep pending | Operation checkout, exact resolved-path staging, sequencer continuation and caller return; see [Git evidence](./wiring-audit-git.md) |
| `1-resource-summarizer` | Reviewed; final catalog sweep pending | One supplied source/slice and requested result, claim/provenance/coverage fidelity, exact optional worktree candidate, untrusted-content/copyright boundaries, no hidden fetch/write/chaining, and Learn/Vault returns; [evidence](./wiring-audit-narrative-resources.md) |
| `1-response-effort-calibrator` | Reviewed; final catalog sweep pending | Explicit one-request depth overlay, qualitative effort levels, invariant scope/evidence/authority, no tool/worktree effects, and Butler caller return; [evidence](./wiring-audit-presentation-modes.md) |
| `1-rewind` | Reviewed; final catalog sweep pending | One bounded local screen-memory question, privacy minimization, untrusted recovered content, no implicit setup/upload/action, no worktree isolation, and Butler/Handoff return; [evidence](./wiring-audit-butler-satellites.md) |
| `1-security-auditor` | Reviewed; final catalog sweep pending | Scoped six-phase audit, read-only caller return, artifact/schema consistency and tested validator; see [security evidence](./wiring-audit-security.md) |
| `1-server-and-fleet-operations` | Reviewed; final catalog sweep pending | One host/fleet design/assessment/config/remote operation, inventory/machine/management-plane and optional worktree identity, shared host/session/package state, untrusted output, controller reconciliation, self-lockout/canary/batch controls, exact fleet coverage, and DevOps return; [evidence](./wiring-audit-stateful-operations.md) |
| `1-session-skill-reflect` | Reviewed | Read-only bounded-run reflection with observed/inferred/unknown evidence, recurrence discipline, one proposed change-set, and no backup/edit/automation/Git effects; [evidence](./wiring-audit-catalog-governance.md) |
| `1-setup-domain-docs` | Reviewed; final catalog sweep pending | Local discovery SSOT plus pointer, exact worktree/authority, evidence-based layout, no domain/ADR authoring, idempotent verification, and Setup return; [evidence](./wiring-audit-setup-domain-docs.md) |
| `1-setup-issue-tracker` | Reviewed; final catalog sweep pending | Local tracker SSOT plus one pointer, evidence-based selection, exact worktree/authority, idempotent diff verification, no remote tracker actions, and explicit Setup return; [evidence](./wiring-audit-setup-issue-tracker.md) |
| `1-setup-triage-labels` | Reviewed; final catalog sweep pending | Five-role local mapping plus pointer, exact worktree/authority, no remote label/triage actions, idempotent validation, and Setup return; [evidence](./wiring-audit-setup-triage-labels.md) |
| `1-setup-vault-root` | Reviewed; final catalog sweep pending | One supplied path plus pointer, exact worktree/authority, no vault enumeration/operation, tracked-path privacy gate, idempotent validation, and Setup return; [evidence](./wiring-audit-setup-vault-root.md) |
| `1-shipping-and-launch` | Reviewed; final catalog sweep pending | Immutable release candidate, plan/read-only/authorized-execution modes, two-parent returns, exact artifact/environment/worktree/authority, evidence-driven gates, state-aware recovery, and separately authorized remote effects; [evidence](./wiring-audit-shipping.md) |
| `1-skill-atomize` | Reviewed | One pinned overlap cluster in assess/apply mode, smallest boundary-first resolution, material-only identity forks, revision-safe route updates, and manager return; [evidence](./wiring-audit-catalog-governance.md) |
| `1-skill-linter` | Reviewed | Read-only pinned skill/hub/diff/catalog report, tool version/exit/truncation evidence, enumerated coverage and projection freshness, structural-proof limits, manager return; [evidence](./wiring-audit-catalog-governance.md) |
| `1-slides` | Reviewed | One self-contained HTML deck; evidence/output/runtime/rights authority; no mandatory CDN, invented claims, conversion, presentation, or publication; [evidence](./wiring-audit-final-eight.md) |
| `1-source-backed-skill` | Reviewed | One private candidate from an authorized fixed corpus; exact hashes/destination/worktree, copyright/PII and execution boundaries, no automatic placement/publication; [evidence](./wiring-audit-catalog-governance.md) |
| `1-stacked-pr-repair` | Reviewed; final catalog sweep pending | Repair-only mode, immediate-parent/worktree mapping and scoped history/CI evidence; see [Git evidence](./wiring-audit-git.md) |
| `1-stacked-pr-review-and-repair` | Reviewed; final catalog sweep pending | Stack review mode, immediate-parent evidence and descendant invalidation; see [Git evidence](./wiring-audit-git.md) |
| `1-stepdown-rule` | Reviewed | One-file order assessment/edit; exact worktree/hash/language/tooling/authority; initialization/binding/reflection/generated constraints; repository-over-universal convention; smallest behavior-independent permutation; moved-text plus fitting checks; no logic/module/review/Git chain; [evidence](./wiring-audit-code-comments-layout.md) |
| `1-story-teacher` | Reviewed; final catalog sweep pending | One original narrative, internal source/fidelity ledger, optional explicit/implicit teaching and story form, protected-expression boundary, no auto-summary/continuation/write, and Learn return; [evidence](./wiring-audit-narrative-resources.md) |
| `1-strategic-analysis` | Reviewed; final catalog sweep pending | One fixed strategic decision/horizon, exact optional artifact/worktree provenance, framework-not-evidence discipline, current/forecast/scenario separation, common option criteria, no fabricated precision or automatic research/action, and Thinking/caller return; [evidence](./wiring-audit-ethical-strategy-competition.md) |
| `1-strategic-compact` | Reviewed; final catalog sweep pending | Host-neutral same-session capsule, safe checkpoint, exact continuation state, no assumed commands/hooks/worktree/effects, historical-source isolation, and Butler/Handoff returns; [evidence](./wiring-audit-session-continuity.md) |
| `1-subagent-implement` | Reviewed; final catalog sweep pending | Sequential writer/authority contracts, complete candidate review, safe artifact helpers and conditional finish; see [workspace evidence](./wiring-audit-workspaces.md) |
| `1-supabase` | Reviewed | One product-integration concern; exact project/local-stack/candidate/worktree/authority; shared-state and untrusted-data boundaries; current official docs; distinct local/hosted/repository effects; RLS/claim/privileged-function proof; no automatic schema/remote/Git chain; [evidence](./wiring-audit-supabase.md) |
| `1-supabase-postgres-best-practices` | Reviewed | One measured concern; exact database/workload/candidate/worktree identity; shared DB state; sensitive evidence; `EXPLAIN` versus executing `EXPLAIN ANALYZE`; one attributable recommendation/edit; schema handoff and no hosted/load/Git effects; [evidence](./wiring-audit-supabase.md) |
| `1-supabase-schema-migration` | Reviewed | One application-owned schema concept; exact worktree/version/local-stack ownership; cross-worktree collision checks; append-only uncertainty rule; DDL/DML and compatibility boundaries; safe locks/RLS; destructive-local reset gate; function/security/CI evidence; no remote application; [evidence](./wiring-audit-supabase.md) |
| `1-tdd` | Reviewed; final catalog sweep pending | One fitting red→green slice, F-TDD1, grounded oracle, Ship/Diagnose/plan returns, Setup removal, exact candidate/worktree/service ownership, honest red/green evidence, and historical-source isolation; [evidence](./wiring-audit-tdd.md) |
| `1-tutor` | Reviewed; final catalog sweep pending | One bounded interactive problem, progressive help, learner-response waits, transfer evidence, assessment integrity, no worktree/persistence, and Learn caller return; [evidence](./wiring-audit-learn-hub.md) |
| `1-teach` | Reviewed; final catalog sweep pending | Pure one-operation durable-course router, exact workspace/worktree/authority handoff, complete four-leaf dispatch, no hidden execution, and actual caller return; [evidence](./wiring-audit-teaching-workspace.md) |
| `1-teaching-workspace` | Reviewed; final catalog sweep pending | Exact root and dirty ownership, minimal mission-only setup, explicit replacement confirmation, optional source ledger, no empty scaffolding/research/Git effects, and Teach return; [evidence](./wiring-audit-teaching-workspace.md) |
| `1-thinking-bounded-rationality` | Reviewed; final catalog sweep pending | One evidence-based sufficiency/stop rule, optional artifact/worktree identity, mandatory gates and cheap material checks preserved, no threshold movement/research/execution, and Thinking/caller return; [evidence](./wiring-audit-thinking-evidence-boundaries.md) |
| `1-thinking-circle-of-competence` | Reviewed; final catalog sweep pending | One claim grounding disposition, optional repository/worktree/runtime identity, evidence-kind/currentness/coverage boundaries, no automatic fetch or familiarity-as-proof, and Thinking/caller return; [evidence](./wiring-audit-thinking-evidence-boundaries.md) |
| `1-thinking-cynefin` | Reviewed; final catalog sweep pending | One provisional situation classification, optional artifact/worktree identity, evidence-based domain and response-mode proposal, chaos-without-production-authority, no probes/stabilization/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-diagnostic-frames.md) |
| `1-thinking-effectuation` | Reviewed; final catalog sweep pending | One means-based learning option under owner-set affordable loss, optional artifact/worktree identity, resource/privacy/commitment boundaries, no automatic contact/spend/experiment/goal change, and Thinking/caller return; [evidence](./wiring-audit-thinking-applied-creative.md) |
| `1-thinking-ethical` | Reviewed; final catalog sweep pending | One fixed normative decision, exact optional artifact/worktree identity, evidence/value/prediction separation, rights/power/consent/burden safeguards, no invented representation/legal/compliance/risk authority, and Thinking/caller return; [evidence](./wiring-audit-ethical-strategy-competition.md) |
| `1-thinking-first-principles` | Reviewed; final catalog sweep pending | One challenged constraint and derived candidate, optional artifact/worktree identity, verified-limit and evidence classification, standard-option comparison, no automatic research/design/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-creative-frames.md) |
| `1-thinking-five-whys-plus` | Reviewed; final catalog sweep pending | One localized-fault causal/prevention memo, optional artifact/worktree identity, evidence-stopped branches, necessary/sufficient/contributing distinctions, no forced five levels/blame/remediation, and Thinking/caller return; [evidence](./wiring-audit-thinking-diagnostic-frames.md) |
| `1-thinking-jobs-to-be-done` | Reviewed; final catalog sweep pending | One evidence-backed segment/circumstance job hypothesis, optional behavior/artifact/worktree identity, no invented users/quotes/primary job, divergent segments and coverage limits, no automatic research/product action, and Thinking/caller return; [evidence](./wiring-audit-thinking-applied-creative.md) |
| `1-thinking-kepner-tregoe` | Reviewed; final catalog sweep pending | One immutable candidate set in exactly one problem- or decision-analysis mode, optional artifact/worktree identity, defensible contrasts/criteria/weights, no fabricated winner/tool/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-diagnostic-frames.md) |
| `1-thinking-lateral` | Reviewed; final catalog sweep pending | One evidenced stuck frame and nonliteral move, optional artifact/worktree identity, preserved constraints and provenance-isolated guide, candidates-not-evidence, no automatic test/research/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-creative-frames.md) |
| `1-thinking-lindy-effect` | Reviewed; final catalog sweep pending | One durability-sensitive comparison, optional artifact/worktree identity, qualitative survival prior with selection/drift/current-fit checks, no lifetime equation/age verdict/research/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-evidence-boundaries.md) |
| `1-thinking-map-territory` | Reviewed; final catalog sweep pending | One map-claim/territory-observation reconciliation, optional artifact/worktree identity, descriptive-versus-normative authority, provenance/freshness/version classification, no inspection/edit/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-diagnostic-frames.md) |
| `1-thinking-margin-of-safety` | Reviewed; final catalog sweep pending | One evidence-derived buffer, optional artifact/worktree identity, estimate/tail/breach/adjustment/cost factors, no canned multipliers/provisioning/monitoring/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-risk-frames.md) |
| `1-thinking-model-combination` | Reviewed; final catalog sweep pending | One fixed question after a named primary-frame gap, exact optional artifact/worktree identity, shared-evidence/non-independence accounting, distinct lens roles and predeclared conflicts, three-lens scope, no tools/automatic follow-on, and Thinking/caller return; [evidence](./wiring-audit-thinking-model-combination.md) |
| `1-thinking-ooda` | Reviewed; final catalog sweep pending | One current-state decision packet, optional artifact/worktree identity, no universal confidence or invented execution/re-observation, operational-owner handoff, no commands/mitigation/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-risk-frames.md) |
| `1-thinking-opportunity-cost` | Reviewed; final catalog sweep pending | One fixed resource commitment versus its best feasible alternative, optional artifact/worktree identity, common-unit or explicit-criteria comparison, no sunk cost/fantasy option/fake arithmetic/automatic action, and Thinking/caller return; [evidence](./wiring-audit-thinking-decision-frames.md) |
| `1-thinking-pre-mortem` | Reviewed; final catalog sweep pending | One immutable plan risk memo, optional plan/worktree identity, causal risk/evidence/control-effectiveness boundaries, proposed-only plan deltas, no forced scoring/edit/launch/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-risk-frames.md) |
| `1-thinking-probabilistic` | Reviewed; final catalog sweep pending | One checkable uncertainty, optional artifact/worktree identity, measurement/reference-class/calibration discipline, correlated evidence and sensitivity, no invented probability/precision/research/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-decision-frames.md) |
| `1-thinking-red-team` | Reviewed; final catalog sweep pending | One authorized read-only attack-path hypothesis, optional candidate/worktree identity, observed-versus-plausible finding boundary, secret/payload minimization, no active probe/remediation/disclosure/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-risk-frames.md) |
| `1-thinking-reversibility` | Reviewed; final catalog sweep pending | One fixed decision's concrete undo path, optional artifact/worktree identity, irreversible core and acting/waiting costs, correctness/safety preservation, no implicit experiment/rollback/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-decision-frames.md) |
| `1-thinking-scientific-method` | Reviewed; final catalog sweep pending | One immutable symptom differential, optional artifact/worktree identity, falsifiers and cheapest permitted observation proposal, parsimony-after-fit, no test/probe/repair/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-diagnostic-frames.md) |
| `1-thinking-second-order` | Reviewed; final catalog sweep pending | One fixed change's credible decision-changing downstream mechanisms, optional artifact/worktree identity, evidence-kind and horizon/scale separation, no forced depth/multiplier/probability or automatic action, and Thinking/caller return; [evidence](./wiring-audit-thinking-decision-frames.md) |
| `1-thinking-socratic` | Reviewed; final catalog sweep pending | One load-bearing ambiguity, optional artifact/worktree identity, self-resolution or one neutral question, no user-fact outsourcing/interview/scope expansion/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-diagnostic-frames.md) |
| `1-thinking-steel-manning` | Reviewed; final catalog sweep pending | One strongest faithful opposing case, exact optional artifact/worktree identity, no invented representation/false defense, optional engagement/synthesis, lean provenance-isolated guides, and Grilling/Thinking/caller returns; [evidence](./wiring-audit-thinking-evidence-boundaries.md) |
| `1-thinking-systems` | Reviewed; final catalog sweep pending | One bounded system map and leverage-test proposal, optional artifact/worktree identity, observed/inferred/alternate-map separation, boundary and archetype humility, no intervention/implementation/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-diagnostic-frames.md) |
| `1-thinking-theory-of-constraints` | Reviewed; final catalog sweep pending | One measured flow snapshot, optional artifact/worktree identity, stable/interacting/shifting/demand-bound classification, system-effect intervention proposal, no assumed bottleneck/profiling/capacity/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-risk-frames.md) |
| `1-thinking-thought-experiment` | Reviewed; final catalog sweep pending | One bounded counterfactual chain, optional artifact/worktree identity, explicit controls/assumptions/mechanisms, imagination-not-evidence and implication limits, no automatic test/research/action, and Thinking/caller return; [evidence](./wiring-audit-thinking-applied-creative.md) |
| `1-thinking-triz` | Reviewed; final catalog sweep pending | One genuine technical parameter contradiction, optional artifact/worktree identity, separation/transform evidence and honest residual trade-off, no forced invention/prototype/implementation, and Thinking/caller return; [evidence](./wiring-audit-thinking-creative-frames.md) |
| `1-thinking-via-negativa` | Reviewed; final catalog sweep pending | One addition-versus-subtraction analysis, optional artifact/worktree identity, dependent/control/reversibility evidence, recommendation-only deletion boundary, protected do-not-touch controls, and Thinking/caller return; [evidence](./wiring-audit-thinking-creative-frames.md) |
| `1-triage-apply` | Reviewed | One still-current approved transition; exact tracker/worktree targets and exhaustive effect ledger; stable multiline bodies; verified readback and partial-state reporting; ready is not implementation authority; [evidence](./wiring-audit-triage.md) |
| `1-triage-assess` | Reviewed | One immutable issue/external-PR read-only assessment; candidate/worktree provenance; claims/facts/gaps; bounded specialist handoffs; PR-scope ledger; no tracker/file effects; [evidence](./wiring-audit-triage.md) |
| `1-triage-inbox` | Reviewed | One cutoff-bounded read-only attention snapshot; exact tracker/local-worktree query; private minimal fields; generated-ticket provenance exclusion; no assessment, polling, or mutation; [evidence](./wiring-audit-triage.md) |
| `1-to-spec` | Reviewed | One settled source to one draft/local/tracker spec artifact; exact caller/evidence/destination/authority and optional worktree; gap ledger instead of interview/guess; conditional tracker setup; revision-safe write/publish; no automatic downstream effects; [evidence](./wiring-audit-to-spec.md) |
| `1-to-tickets` | Reviewed | One approved spec to one draft/local/tracker ticket set; exact caller/destination/authority and optional worktree; evidence-based slicing and bidirectional traceability; shared-resource-aware DAG/frontier; duplicate-safe publication; no automatic execution; [evidence](./wiring-audit-to-tickets.md) |
| `1-tool-schema-design` | Reviewed; final catalog sweep pending | Design/review/edit modes, parent/MCP/oversight/security returns, conditional worktree, complete references and bounded validator; [evidence](./wiring-audit-tool-schema.md) |
| `1-ui-styling` | Reviewed | One presentation-only visual delta, protected behavior/content/data contracts, exact caller/candidate/worktree and shared UI state, untrusted versioned inputs, repository-native stack detection, no implicit setup/install/config/font/helper/browser/Git effects, honest visual/runtime proof, and symmetric UI/UX/Ship/Frontend returns; [evidence](./wiring-audit-ui-styling.md) |
| `1-ui-ux-pro-max` | Reviewed | One read-only design-direction packet, exact caller/candidate/worktree/evidence identity, shared UI-state boundary, untrusted snapshot corpus, smallest explicit search, no persistence/implementation pipeline, and UI/UX/caller return; [evidence](./wiring-audit-ui-ux-pro-max.md) |
| `1-user-research` | Reviewed | Pure plan-versus-synthesis sub-hub, one material F-UR1, exact caller/decision/source/privacy/authority/worktree pass-through, external research-state boundary, no evidence reads or participant/product effects, and UI/UX/caller return; [evidence](./wiring-audit-user-research.md) |
| `2-user-research-plan` | Reviewed | One decision-linked protocol, fixed hypothesis/alternative, evidence-based method/sample and neutral tasks, privacy/consent/accessibility/safety/data/incentive plan, revision-safe optional local write, no recruitment/contact/execution/payment/synthesis/publication; [evidence](./wiring-audit-user-research.md) |
| `2-user-research-synthesis` | Reviewed | One fixed evidence-set/cutoff synthesis, exact provenance and evidence-kind separation, dissent/cohort/bias/missingness/privacy preservation, revision-safe optional redacted report, no new collection/persona invention/prioritization/implementation/publication; [evidence](./wiring-audit-user-research.md) |
| `1-wayfinder-advance` | Reviewed | One existing map and one frontier decision-ticket cycle; exact candidate/worktree/tracker revisions; one specialist handoff or resumed resolution recording; race/partial-effect controls; no next ticket or implementation; [evidence](./wiring-audit-wayfinder.md) |
| `1-wayfinder-chart` | Reviewed | One accepted destination to one draft/local/tracker map set; exact candidate/worktree/destination/authority; sharp decisions versus coarse fog; handoff labels only; duplicate-safe verified publication; [evidence](./wiring-audit-wayfinder.md) |
| `1-vault-explain` | Reviewed; final catalog sweep pending | One safely resolved private Concept and one bounded Learn packet, exact optional Git/worktree version, no body-wide search/neighbor traversal/write, source-versus-inference preservation, and Vault/Learn caller returns; [evidence](./wiring-audit-vault-explain.md) |
| `1-vault-inbox` | Reviewed; final catalog sweep pending | One supplied create-only capture, canonical root and optional Git/worktree candidate, privacy/redaction and untrusted-content handling, collision-safe filename/write, truthful minimal metadata, exact verification, and Vault/later-Ingest returns; [evidence](./wiring-audit-vault-inbox.md) |
| `1-vault-ingest` | Reviewed; final catalog sweep pending | One fixed source snapshot and explicit change-set ledger, bounded claim-level reconciliation, conflict/destructive/privacy gates, canonical optional Git/worktree candidate, safe URL/summary returns, race/partial-write evidence, and no automatic archive/consume/lint/explain; [evidence](./wiring-audit-vault-ingest.md) |
| `1-vault-lint` | Reviewed; final catalog sweep pending | Read-only pinned snapshot/scope, exact optional Git/worktree candidate, private/untrusted bounded reads, evidence-defined findings, honest sample coverage/staleness, no writes/follow-ons, and Vault/Repair returns; [evidence](./wiring-audit-vault-lint-repair.md) |
| `1-vault-repair` | Reviewed; final catalog sweep pending | One accepted finding, revalidated current evidence, exact files/hunks and optional worktree, stale/conflict/no-evidence no-op, high-impact action gates, targeted proof without clean-vault claim, and Lint/Vault/Ingest returns; [evidence](./wiring-audit-vault-lint-repair.md) |
| `1-visual-edit` | Reviewed | Exactly one open/inspect/preview/apply operation, installed-contract resolution instead of archived execution, exact Design/runtime/source/worktree identities, shared bridge/browser/account/pending-state boundary, untrusted content and secret containment, human consent plus revision-checked apply, mode-specific proof, no setup/mode/Git/publication chain, and UI/UX/adjacent returns; [evidence](./wiring-audit-visual-edit.md) |
| `1-visual-plan` | Reviewed; final catalog sweep pending | One explicit draft/create/update visual-plan operation, exact source/worktree/revision identity, smallest useful surface, private-by-default persistence and readback, no automatic connector/browser/share/subagent/implementation effects, and Grilling/caller return; [evidence](./wiring-audit-visual-plan.md) |
| `1-visual-recap` | Reviewed | One explicit draft/create/update for one immutable change candidate, exact diff/worktree/source/destination/visibility/authority identity, shared Plan/connector/browser/PR state, untrusted-input redaction, current-renderer authority, evidence-based visual density, distinct persistence/publication effects, bounded proof, and no feedback/Git/repair chain; [evidence](./wiring-audit-visual-recap.md) |
| `1-webmcp` | Reviewed; final catalog sweep pending | Exact external target/authority checkout, open/read/write separation, page-tool preference, uncertain-write handling, targeted readback, high-impact confirmation, and no worktree illusion; [evidence](./wiring-audit-butler-satellites.md) |
| `1-wiki-query` | Reviewed; final catalog sweep pending | One fixed question and pinned vault snapshot, bounded private/untrusted retrieval, exact note/claim locators, conflict/coverage/staleness honesty, credential non-disclosure, no writes or automatic follow-ons, and symmetric Vault/Ingest returns; [evidence](./wiring-audit-wiki-query.md) |
| `1-write-plan` | Reviewed; final catalog sweep pending | Source-grounded tasks, suitable verification, F-SP mode selection and planning-only return; see [planning evidence](./wiring-audit-planning.md) |
| `1-writing-great-skills` | Reviewed | One-body craft contract, positive boundaries, proportional evaluation, explicit worktree/effect guidance, and lean non-operative source adaptations; [evidence](./wiring-audit-catalog-governance.md) |
| `1-xlsx` | Reviewed | [XLSX evidence](./wiring-audit-xlsx.md): one immutable source/data operation, exact range/schema/authority/worktree, untrusted formulas/links, separate effects, isolated source-preserving recalc, hazard/alias/revision gates, bounded proof |
| `2-dependency-security` | Reviewed; final catalog sweep pending | Comparable advisory/candidate evidence, identity-based ratchet, policy/authority boundaries and caller return; see [security evidence](./wiring-audit-security.md) |
| `2-brand-context-extract` | Reviewed | One source-supported minimal brand packet for one consumer, exact source/worktree/privacy identity, untrusted parser output, no prompt injection/write/downstream execution, and Brand/caller return; [evidence](./wiring-audit-brand.md) |
| `2-brand-guidelines` | Reviewed | One draft or revision-safe applied brand contract, evidence-classified rules, exact target/worktree/authority, no invented defaults or downstream sync/asset/approval effects, and Brand/caller return; [evidence](./wiring-audit-brand.md) |
| `2-brand-review` | Reviewed | One read-only candidate-versus-contract review, exact revisions/worktree/evidence limits, helper-proof boundaries, no approval/remediation/asset effects, and Brand/caller return; [evidence](./wiring-audit-brand.md) |
| `2-ponytail-review` | Reviewed | Read-only one immutable PR/diff candidate; exact three-parent/worktree/dirty-scope identity; untrusted inputs; Chesterton/caller/contract evidence; safety and test preservation; optional estimated reduction; no fix/test/Git chain; lean operative/provenance references; [evidence](./wiring-audit-ponytail.md) |
| `2-prompt-injection-defense` | Reviewed; final catalog sweep pending | Read-only/design/implementation modes, dual-parent caller returns, conditional workspaces, complete references and bounded manifest checker; [evidence](./wiring-audit-prompt-defense.md) |
| `2-security-and-hardening` | Reviewed; final catalog sweep pending | Scoped authorized fixes, worktree/caller returns, consolidated references and corrected examples; see [hardening evidence](./wiring-audit-hardening.md) |
| `2-skill-supply-chain-audit` | Reviewed; final catalog sweep pending | Read-only fixed-snapshot audit, parent/ingest returns, worktree versus sandbox boundary, full package/reference/helper audit and honest coverage; [evidence](./wiring-audit-package-security.md) |
| `2-software-architect` | Reviewed; final catalog sweep pending | Architecture domain entry with Review-subhub depth, three-parent routes, read-only candidate/worktree contract, viable alternatives, conditional recommendation, and specialist returns; [evidence](./wiring-audit-software-architect.md) |
| `2-thermo-nuclear-code-quality-review` | Reviewed; final catalog sweep pending | Actual candidate, bounded evidence, read-only caller return and aligned parent routes; see [review evidence](./wiring-audit-review.md) |
| `2-verify-work` | Reviewed; final catalog sweep pending | Actual candidate, bounded evidence, read-only caller return and aligned parent routes; see [review evidence](./wiring-audit-review.md) |
