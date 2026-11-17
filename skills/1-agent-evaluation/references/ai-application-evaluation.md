# AI feature evaluation

Load for single-call features, extraction/classification, RAG or an AI integration as well as agents.
Use the parent's fixed candidate, selected mode, protocol and checker qualification. No provider call is
implicit in designing cases or reading supplied results.

| Claim | Suitable evidence |
|---|---|
| Software contract | Deterministic parsing, business validation, permission and state-transition checks |
| Model component | Task-specific semantic labels/rubric for extraction, classification, answer or tool selection |
| Retrieval | Relevant permitted evidence retrieved, missing facts, ranking and freshness |
| End-to-end outcome | Supported user task completes with correct persisted or external effects |
| Production behavior | Actual cohorts, outcome slices, correction burden, latency, errors and costs |

Keep these layers separate. Valid JSON can contain a wrong value; a grounded answer can cite irrelevant
evidence; a successful unit test does not establish an end-to-end user outcome. Record false-positive and
false-negative costs, unsupported/no-answer cases, refusals, timeouts and invalid results in denominators.
Protect holdout data from prompt tuning, include difficult/adversarial and permission slices, and qualify
automated scoring against known failures and clean controls. Preserve disagreement with human/domain review.

Version code/model/parameters/prompts/tools/policy/corpus/index/memory/cache/runtime as relevant. A changed
component triggers the fitting regression checks, not a blanket reuse of prior scores. Explain statistical
and practical uncertainty; model quality, operational reliability and release approval are different claims.

[Research basis](../../../guidelines/catalog/research-ai-app-engineering-2026-11-17.md): S3, S6, S8–S10, S12–S13.
