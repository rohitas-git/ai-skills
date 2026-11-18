# Long runs and continuity

Use the selected section within the [playbook handoff and tool contract](../playbooks.md#handoff-and-tool-selection).

## autonomous-run

1. Keep the existing execution owner. Use [Plow Ahead](../../../1-plow-ahead/SKILL.md) for authorized persistence and [bounded runs](../../../0-implement/references/bounded-runs.md) for scope, budget, stop conditions and time or event checks.
2. Apply *Sequence Work into Verifiable Units*. Use the existing permitted status mechanism when waiting. At meaningful boundaries, refresh the [project checkpoint](../../../0-implement/references/project-continuity.md) and link any decision log.
3. Return the exit predicate and matching evidence, or the exact blocker and next action. A scheduled run or external write follows its own authorization.

## autopilot-full

1. Use [Implement](../../../0-implement/SKILL.md) to identify independent deliverables and per-operation grants. Apply [Separate Before Serializing Shared State](../../../1-parallel-agents/references/coverage-and-races.md) to mutable work. [Parallel Agents](../../../1-parallel-agents/SKILL.md) fits only when delegation is authorized and outputs can be isolated.
2. Checkpoint each deliverable with head, base and owner. Use [Verify Work](../../../2-verify-work/SKILL.md) to check the actual candidate and reconcile failed or stale evidence.
3. Return one disposition per deliverable. Use [Shipping](./delivery.md#shipping) only for the delivery effects already in scope.

## autopilot-stack

1. Use [Stacked PR Repair](../../../1-stacked-pr-repair/SKILL.md) for known blockers, [Stacked PR Review and Repair](../../../1-stacked-pr-review-and-repair/SKILL.md) for fresh review and fixes, or [Implement](../../../0-implement/SKILL.md) for building the slices. Pin real parent edges before starting.
2. Apply *Sequence Work into Verifiable Units* base-to-tip. Use the [checkpoint](../../../0-implement/references/project-continuity.md) for pending work and the [watcher](../../../1-pr-repair/scripts/watch-pr/watch-pr) for supported GitHub status. Refresh checks when rebasing changes what the evidence covers.
3. Return the contiguous verified prefix, gaps and exact head/base evidence. A request that ends at verified hands off that state. An authorized landing uses [Shipping](./delivery.md#shipping).

## session-pickup

1. Start with the named project checkpoint or handoff. Apply *Guard the Context Window* by using scoped project records and cited evidence. [Working Context](../../../1-working-context/SKILL.md) can reconstruct missing state when requested.
2. Use the [checkpoint helper](../../../0-implement/scripts/project-checkpoint.py) in read-only inspect mode where the project uses its schema. Reconcile drift and reverify affected receipts using the relevant project checks. A matching fingerprint confirms the inspected workspace scope.
3. Return the first unfinished action and any authority or prerequisite gap. When execution is requested, resume the owning skill or [Execute Plan](../../../1-execute-plan/SKILL.md) for a written plan.

## pause-safely

1. Use the active owner to reach a safe boundary. Preserve outstanding output and identify any process, service or recovery steps the next session needs.
2. Apply *Sequence Work into Verifiable Units* by recording the last completed evidence boundary and exact next step. Refresh the owned [project checkpoint](../../../0-implement/references/project-continuity.md). Use [Handoff](../../../1-handoff/SKILL.md) for a requested standalone note.
3. Read back the checkpoint or handoff and check its links against what exists on disk. Return what was preserved, what remains in flight and where to resume.
