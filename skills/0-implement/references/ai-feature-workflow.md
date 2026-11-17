# Optional AI feature workflow

Use for an explicitly requested AI app, integration or upgrade. This is a composition reference, not a new
router or a mandatory sequence. `/0-implement` retains the task/workspace/candidate and selects only the
phase needed. Existing design, assessment, edit, execution, privacy and spend authority remains unchanged.

## Choose by the unresolved output

| Need | Owner | Return |
|---|---|---|
| Is AI useful; what should be automated? | `/1-ai-suitability` | Baseline, benefit/harms, assistance boundary and decision evidence |
| Which architecture fits? | `/2-software-architect` with its AI reference | Conditional alternatives and system decision |
| Which information should reach the model? | `/1-context-retrieval-design` | Source/access/freshness/memory contract |
| What does the application promise consumers? | `/1-api-and-interface-design` with its AI reference | Typed/semantic/effect/failure integration contract |
| How should the user interact with it? | `/1-frontend-ui-engineering` | Applicable AI interaction states and runtime evidence |
| Does the candidate perform the task? | `/1-agent-evaluation` | Fixed-case/checker/protocol results or unrun design |
| What did an upgrade invalidate? | `/1-change-impact` with its AI reference | Consumer/state/evidence impact ledger |
| Is this exact candidate ready for exposure? | `/1-shipping-and-launch` with its AI reference | Quality/operations/recovery readiness or authorized stage result |

## Delivery and evidence

1. Pin intended users/outcome, non-AI baseline, acceptance and harm criteria, scope, data permissions,
   candidate versions, protected work, required checks and allowed effects. Clear requests need no interview.
2. Resolve only load-bearing uncertainty. Read-only suitability/design returns proposals; running experiments,
   uploading data, installing dependencies or paying for models requires the corresponding task authority.
3. Implement one bounded slice using existing code and ordinary deterministic rules where appropriate.
   Reuse existing prompt, tool-schema, human-oversight, cost and security specialists when their outcome is needed.
4. Verify software contracts separately from model/retrieval quality and end-to-end behavior. Use existing
   project checks and `/1-dev-test` where applicable. Do not impose strict TDD on unsettled or
   probabilistic behavior; first define a specification, characterization or evaluation oracle.
5. Review the actual candidate; keep proposed action, authorization and executed result distinct. Final
   project readiness remains `/1-pre-merge`; AI quality evidence supplements its applicable gates.
6. Keep evidence tied to the compound candidate, including relevant model/prompt/tools/data/index/policy.
   Proposed examples and source-read recipes remain unrun; a demo alone does not establish product quality.
7. Return source/candidate, changed contracts, observed checks, uncertainty, effect and cost bounds, fallback,
   recovery and ownership. No automatic provider call, deployment, runtime sync, Git or merge follows.

## Fictional path

For a support draft assistant, compare ordinary search/status lookup with a grounded drafting feature.
Retrieve only permitted policy, look up live status through a bounded tool, validate structured results and
keep sending/refunds outside the draft's authority. Evaluate missing policy, denied orders, invalid values
and provider failure before drawing conclusions. A model upgrade needs affected-case replay and checks for
stored-output/tool behavior; a shadow replay cannot execute the original side effects again.

[Research basis](../../../guidelines/catalog/research-ai-app-engineering-2026-11-17.md).
