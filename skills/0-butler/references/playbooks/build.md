# Build and design

Use the selected section within the [playbook handoff and tool contract](../playbooks.md#handoff-and-tool-selection).

## feature-idea

1. Ground the idea in the current app with [Grilling](../../../0-grilling/SKILL.md). Name the user journey, expected outcome and unresolved choices. Write one observable acceptance example for each material behavior.
2. If evidence can settle a design choice, use [Prototype](#prototype). If several supplied approaches compete, [Competing Solutions](../../../1-competing-solutions/SKILL.md) compares them against the same acceptance criteria.
3. Record the accepted behavior and exclusions with [To Spec](../../../1-to-spec/SKILL.md) when a spec is requested. Use [Multi-phase Plan](#multi-phase-plan) for execution sequencing. Discovery finishes with decisions and open questions. Accepted implementation resumes at [Feature](#feature).

## feature

1. Pin acceptance criteria, dirty-work ownership and the first independently verifiable slice. Use [Codebase Design](../../../1-codebase-design/SKILL.md) when the change crosses a meaningful seam. Apply [Model the Domain](../../../1-codebase-design/references/data-shapes-and-ownership.md) by naming the data shape, legal states and owning module before changing behavior.
2. Use [Competing Solutions](../../../1-competing-solutions/SKILL.md) when materially different designs merit comparison. Build the chosen slice. Use [TDD](../../../1-tdd/SKILL.md) when a deterministic behavior and independent expected result are settled.
3. Apply *Prove It Works* on the affected surface. For a user journey, use the [runtime feature verification workflow](../../../0-implement/references/verification-workflows.md#w-ps1--runtime-feature-verification). For an in-scope invariant, use the [model and check workflow](../../../0-implement/references/verification-workflows.md#w-ps2--model-check-and-reconcile). [Review the actual change](../../../1-code-review/SKILL.md) and reconcile supported findings.
4. Record observed checks and gaps for the actual candidate. For multi-step work, save the next action through [project continuity](../../../0-implement/references/project-continuity.md). If a reusable app verifier is requested, [author or maintain one](../../../0-implement/references/runtime-verification-maintenance.md) and exercise its launch, readiness, drive, evidence and cleanup.

## refactoring

1. Capture an observable behavior baseline with a characterization test or equivalent output. Use [Behavioral Oracles](../../../1-tdd/references/behavioral-oracles.md) to keep the test independent of the structure being replaced.
2. Apply [Minimize Reader Load](../../../0-ponytail/references/reader-load.md) to the proposed shape. Use [Codebase Design](../../../1-codebase-design/SKILL.md) for a changed seam or [Coordinated Cutover](../../../1-deprecation-and-migration/references/coordinated-cutover.md) when callers need migration.
3. Run the same baseline check on the changed candidate. Compare output and side effects, then use [Code Review](../../../1-code-review/SKILL.md) for changed ownership and accidental behavior changes. Report which behaviors were checked.

## prototype

1. Name the decision and what would distinguish the options. Apply *Exhaust the Design Space* where several viable approaches merit trying. Use the [prototype procedure](../../../1-prototype/references/deciding-with-prototypes.md) to bound the experiment and isolate scratch work.
2. Choose a probe for the question. A permitted browser can exercise a UI variant. A timing experiment needs a reproducible workload and a comparable output. Use [Competing Solutions](../../../1-competing-solutions/SKILL.md) when supplied artifacts need a shared rubric.
3. Return observations per variant, the resulting choice or unresolved question, and which scratch artifacts remain. A production implementation starts under the accepted Feature scope.

## visual-parity

1. Pin baseline and candidate build, viewport, data, fonts, state and tolerance. Apply *Prove It Works* by preserving the baseline as an independent comparison.
2. Use the existing screenshot comparison harness. When a browser capability is available and permitted, [Browser Testing with DevTools](../../../1-browser-testing-with-devtools/SKILL.md) can collect matching captures. [Playwright Browser Testing](../../../1-playwright-browser-testing/SKILL.md) fits a requested durable browser check. Follow the [parity procedure](../../../1-frontend-ui-engineering/references/visual-parity-and-agent-controls.md) for repeatable capture conditions.
3. Record visual differences against the agreed tolerance. Verify relevant interaction and accessibility separately and report each covered state.

## multi-phase-plan

1. Use [Write Plan](../../../1-write-plan/SKILL.md) to turn a settled design into explicit dependencies. Apply [Sequence Work into Verifiable Units](../../../0-implement/references/rerunnable-changes.md) so each phase has a meaningful observable exit.
2. Name each phase owner, prerequisites, evidence and what blocks the next step. Reference the [project checkpoint](../../../0-implement/references/project-continuity.md) for multi-session execution.
3. Check that someone starting cold can identify the first unfinished dependency and its acceptance check. A requested execution uses [Execute Plan](../../../1-execute-plan/SKILL.md) with the accepted plan and authority.
