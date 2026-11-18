# Butler playbooks

Ask `?? show me the playbooks` to browse, `?? show me the feature playbook` to see one,
or `?? playbook bug-fix: checkout fails after applying a discount` for a route tailored to a task.
Butler returns the chosen playbook, its recipe link, one entry skill, the first action and any material constraints.
Open the linked recipe section only when selecting or inspecting that playbook.
If a named playbook conflicts with the requested outcome, explain the conflict and use the applicable route.

## Handoff and tool selection

The entry skill receives the recipe link, current phase, target candidate, requested outcome,
scope limits and evidence needed. The execution owner reads the selected recipe and calls each
specialist only when its step applies. It keeps the same scope and reconciles the results.
Butler's recommendation ends at the handoff.

- **Skills and principles.** Call a specialist for a concrete deliverable or question. Read the
  linked principle guidance when it changes the decision and state the resulting choice.
- **Plugins and local tools.** Identify the operation and surface before choosing a tool. Prefer a
  connected plugin when it supports the exact operation and target. Otherwise use the existing
  project harness or linked local helper if suitable. Check the required account, build, permissions
  and tooling before using either. A status reader and a provider write have distinct authority.
- **Verification.** Use a check that can disprove the claim on the relevant candidate. Record the
  command or action, candidate, observation and material gaps. Use PASS, FAIL, BLOCKED or NOT RUN
  for requested checks. If the available tool provides narrower evidence, report that scope.
- **Packaging.** These recipes link to live owner packages and catalog tools. When distributing
  a subset as a plugin, include its required references and resolve cross-skill links in the
  installed layout. Treat connector-backed steps as conditional and keep their local fallback
  or explicit blocked outcome visible. Installation and tool configuration are separate operations.

For example, a CSV-export Feature handoff can start with Codebase Design if ownership is unclear.
Once implemented, the runtime recipe drives the export through the available browser or existing
app harness and compares the file with the expected filtered rows and order. The project checkpoint
links the evidence and records the next unfinished step.

## Build and design

| Playbook | When and where to start | Steps and finish condition |
|---|---|---|
| **feature-idea** [Recipe](./playbooks/build.md#feature-idea) | You have a feature idea with unresolved behavior → [`/0-grilling`](../../0-grilling/SKILL.md). | Ground the idea in the app → resolve behavior and acceptance criteria → write the spec and plan when requested → hand an authorized build to Implement. Finish discovery with accepted decisions and open questions. |
| **feature** [Recipe](./playbooks/build.md#feature) | Behavior is agreed and implementation is requested → [`/0-implement`](../../0-implement/SKILL.md). | Pin scope and acceptance evidence → build a verifiable slice → test the behavior and review changes → checkpoint remaining work or completion. [Procedure](../../0-implement/references/feature-and-refactor.md) |
| **refactoring** [Recipe](./playbooks/build.md#refactoring) | Change structure while preserving observable behavior → [`/0-implement`](../../0-implement/SKILL.md). | Capture current behavior → change one structural concern → verify equivalence and review. [Procedure](../../0-implement/references/feature-and-refactor.md) |
| **prototype** [Recipe](./playbooks/build.md#prototype) | A runnable experiment can settle a design question → [`/1-prototype`](../../1-prototype/SKILL.md). | Name the uncertainty → build the smallest comparison → observe the result → report the decision and limits. [Procedure](../../1-prototype/references/deciding-with-prototypes.md) |
| **visual-parity** [Recipe](./playbooks/build.md#visual-parity) | Compare a UI change with an agreed visual baseline → [`/1-frontend-ui-engineering`](../../1-frontend-ui-engineering/SKILL.md). | Freeze baseline and capture conditions → compare the same states → report visual differences and check interaction/accessibility separately. [Procedure](../../1-frontend-ui-engineering/references/visual-parity-and-agent-controls.md) |
| **multi-phase-plan** [Recipe](./playbooks/build.md#multi-phase-plan) | A settled design needs an implementation plan → [`/1-write-plan`](../../1-write-plan/SKILL.md). | Map dependencies and evidence per phase → name exit gates and unresolved prerequisites → return a reviewable plan. [Procedure](../../1-write-plan/references/phase-evidence.md) |

## Investigate and improve

| Playbook | When and where to start | Steps and finish condition |
|---|---|---|
| **investigation** [Recipe](./playbooks/investigation.md#investigation) | Understand an existing subsystem → [`/1-code-explainer`](../../1-code-explainer/SKILL.md). | Trace inputs, state and effects → cite code and available rationale → return a read-only explanation and gaps. [Procedure](../../1-code-explainer/references/mechanism-and-rationale.md) |
| **bug-fix** [Recipe](./playbooks/investigation.md#bug-fix) | An unexplained failure needs diagnosis and a fix → [`/0-diagnosing-bugs`](../../0-diagnosing-bugs/SKILL.md). A known, accepted fix starts with Implement. | Preserve failing evidence → identify the cause → apply the smallest authorized fix → verify affected behavior. Diagnosis-only stops at findings. [Procedure](../../0-diagnosing-bugs/references/premises-and-forensics.md) |
| **runtime-forensics** [Recipe](./playbooks/investigation.md#runtime-forensics) | Diagnose a failure observed in a running app → [`/0-diagnosing-bugs`](../../0-diagnosing-bugs/SKILL.md). | Identify the running build and session → collect permitted observations → distinguish candidate causes → report evidence and blind spots. [Procedure](../../0-diagnosing-bugs/references/premises-and-forensics.md) |
| **trace-forensics** [Recipe](./playbooks/investigation.md#trace-forensics) | Diagnose from an existing trace → [`/0-diagnosing-bugs`](../../0-diagnosing-bugs/SKILL.md). | Pin the trace, revision and time window → reconstruct event order → check competing explanations → report what the trace establishes. [Procedure](../../0-diagnosing-bugs/references/premises-and-forensics.md) |
| **perf-issue** [Recipe](./playbooks/investigation.md#perf-issue) | A measured bottleneck needs investigation or tuning → [`/1-performance-optimization`](../../1-performance-optimization/SKILL.md). An unmeasured symptom starts with Diagnose. | Establish a comparable baseline → isolate the limiter → test one change → report work counts, correctness and meaningful improvement or uncertainty. [Procedure](../../1-performance-optimization/references/measurement-integrity.md) |
| **hillclimb** [Recipe](./playbooks/investigation.md#hillclimb) | The user requests iterative measured improvement → [`/1-performance-optimization`](../../1-performance-optimization/SKILL.md). | Freeze workload and correctness checks → test one change per iteration → keep improvements supported by evidence → stop at the target, budget or evidence limit. [Procedure](../../1-performance-optimization/references/hillclimb.md) |

## Skills and evaluation

| Playbook | When and where to start | Steps and finish condition |
|---|---|---|
| **authoring-a-skill** [Recipe](./playbooks/skills-and-evaluation.md#authoring-a-skill) | Draft or revise one skill body → [`/0-skill-creator`](../../0-skill-creator/SKILL.md). | Define its one job and trigger boundary → draft the body and conditional references → check representative outputs → return a candidate for any requested catalog placement. [Procedure](../../0-skill-creator/references/pstack-authoring-and-evaluation.md) |
| **eval** [Recipe](./playbooks/skills-and-evaluation.md#eval) | Evaluate one skill candidate → [`/0-skill-creator`](../../0-skill-creator/SKILL.md). An application or model evaluation uses [`/1-agent-evaluation`](../../1-agent-evaluation/SKILL.md). | Freeze cases, expected behavior and comparison conditions → run authorized trials → preserve attempts and failures → report results and limits. [Procedure](../../0-skill-creator/references/pstack-authoring-and-evaluation.md) |

## PRs and delivery

| Playbook | When and where to start | Steps and finish condition |
|---|---|---|
| **babysit** [Recipe](./playbooks/delivery.md#babysit) | Monitor an open PR and optionally address authorized blockers → [`/0-git`](../../0-git/SKILL.md). | Select status, threads-only or repair mode → inspect the current head and report or resolve issues within that mode → return check state and remaining blockers. [Procedure](../../0-git/references/babysit-modes.md) |
| **opening-a-pr** [Recipe](./playbooks/delivery.md#opening-a-pr) | Publish an implemented branch as a PR → [`/1-finish-branch`](../../1-finish-branch/SKILL.md). A description-only request uses [`/1-pr-summarizer`](../../1-pr-summarizer/SKILL.md). | Pin head/base and current evidence → prepare the title and description → open under existing authority → return the PR and head. [Procedure](../../1-finish-branch/references/verified-delivery.md) |
| **shipping** [Recipe](./playbooks/delivery.md#shipping) | Finish an authorized branch or PR stack → [`/1-finish-branch`](../../1-finish-branch/SKILL.md). A deployment uses [`/1-shipping-and-launch`](../../1-shipping-and-launch/SKILL.md). | Verify head/base and required checks → identify the contiguous verified stack prefix → apply the authorized finish action → distinguish queued from merged. [Procedure](../../1-finish-branch/references/verified-delivery.md) |
| **worktree-cleanup** [Recipe](./playbooks/delivery.md#worktree-cleanup) | Decide whether to remove completed worktrees → [`/1-finish-branch`](../../1-finish-branch/SKILL.md). For inventory only, use [`/1-git-worktrees`](../../1-git-worktrees/SKILL.md). | Audit exact paths, ownership, dirty and untracked files → confirm retention and disposition → remove only specifically authorized paths and report what remains. [Procedure](../../1-finish-branch/references/verified-delivery.md) |

## Long runs and continuity

| Playbook | When and where to start | Steps and finish condition |
|---|---|---|
| **autonomous-run** [Recipe](./playbooks/continuity.md#autonomous-run) | Continue one accepted task while the user is away → retain its active owner, commonly [`/0-implement`](../../0-implement/SKILL.md). | Set the done predicate, budget and stop conditions → verify units and checkpoint evidence → report completion or a concrete blocker. [Procedure](../../0-implement/references/bounded-runs.md) |
| **autopilot-full** [Recipe](./playbooks/continuity.md#autopilot-full) | Drive a queue of independent PR deliverables → [`/0-implement`](../../0-implement/SKILL.md). | Pin scope and per-operation grants → keep independent changes isolated → verify heads and bases → report each delivery disposition. Delegation requires its own authority. [Procedure](../../0-implement/references/bounded-runs.md) |
| **autopilot-stack** [Recipe](./playbooks/continuity.md#autopilot-stack) | Drive an ordered stack of dependent PRs → [`/0-implement`](../../0-implement/SKILL.md) for a build, [`/1-stacked-pr-repair`](../../1-stacked-pr-repair/SKILL.md) for known blockers, or [`/1-stacked-pr-review-and-repair`](../../1-stacked-pr-review-and-repair/SKILL.md) for fresh review and repair. | Verify dependency edges → work base-to-tip → reconcile changed evidence → report the verified prefix and outstanding work. [Procedure](../../0-implement/references/bounded-runs.md) |
| **session-pickup** [Recipe](./playbooks/continuity.md#session-pickup) | Resume a named task → its existing execution owner, or [`/1-execute-plan`](../../1-execute-plan/SKILL.md) for a written plan. Use [`/1-working-context`](../../1-working-context/SKILL.md) for reconstruction only. | Read the known checkpoint first → reconcile workspace, authority and evidence → name the first unfinished action → continue only within the request. [Procedure](../../0-implement/references/project-continuity.md) |
| **pause-safely** [Recipe](./playbooks/continuity.md#pause-safely) | Pause an active task → its active owner. A requested durable note uses [`/1-handoff`](../../1-handoff/SKILL.md). | Reach a safe boundary → preserve current work → refresh the owned checkpoint and write a handoff if requested → report where to resume. [Procedure](../../1-handoff/references/pickup-and-pause.md) |

The 22 pstack playbooks are mapped in the [source review](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
Feature Idea is a local entry for early app feature discovery. Read the selected skill and its procedure for operational detail.
