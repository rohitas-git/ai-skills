# Skills and evaluation

Use the selected section within the [playbook handoff and tool contract](../playbooks.md#handoff-and-tool-selection).

## authoring-a-skill

1. Use [Skill Creator](../../../0-skill-creator/SKILL.md) to define one job, trigger, exclusions and representative outcomes. Apply *Encode Lessons in Structure* via [recurring corrections](../../../1-agent-workflow-observer/references/recurring-corrections.md) when a repeated error can be prevented by a check or existing contract.
2. Link exact live owners, specify any tool prerequisite and describe how a missing capability affects the result. For a requested project-local runtime verifier, use [runtime verification authoring and maintenance](../../../0-implement/references/runtime-verification-maintenance.md). For a formal property, use [model and check](../../../0-implement/references/verification-workflows.md#w-ps2--model-check-and-reconcile) and [maintain model correspondence](../../../1-formal-verification/references/rerun-and-maintain.md).
3. Validate structure with [Skill Linter](../../../1-skill-linter/SKILL.md). Use [Eval](#eval) for claims about behavior. Report which checks actually ran and send requested catalog placement to [Skill Manager](../../../0-skill-manager/SKILL.md).

## eval

1. Apply *Prove It Works* by freezing representative cases, acceptance criteria, permissions and a baseline before testing. [Skill Creator](../../../0-skill-creator/SKILL.md) owns skill evaluations. [Agent Evaluation](../../../1-agent-evaluation/SKILL.md) owns app/model evaluation design.
2. For supported skill cases, use the [catalog evaluation harness](../../../../scripts/evaluate-skills). Schema validation checks the case file. Authorized trials produce behavior evidence. For comparative review, the [packet helper](../../../0-skill-creator/scripts/blind-packets.py) strips metadata and randomizes labels. Check the exported content for remaining identity clues before judging.
3. Report rubric results alongside raw outcomes and failures, including missing trials and limitations of the comparison. Model behavior claims need executed cases or directly observed evidence.
