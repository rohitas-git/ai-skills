# AI system architecture decision

Load for one AI application or agent architecture choice. Keep the parent's read-only decision contract.

## Compare the relevant alternatives

Include ordinary code/search as a credible baseline. One model call, retrieval, tool use, a fixed workflow,
an autonomous loop, adaptation and multi-agent coordination are options for different failures, not stages
that every application must adopt. Use `/1-ai-suitability` when the user outcome or automation premise is
unsettled, and `/1-context-retrieval-design` for detailed source-to-context design; return to the actual caller.

| Decision driver | Evidence to compare |
|---|---|
| Benefit | Task success versus current workflow and unacceptable error classes |
| Model fit | Task/modalities, output constraints, context needs, measured quality and candidate versions |
| Knowledge | Static supplied context, current structured data, retrieval, source access and freshness |
| Control | Fixed control flow versus model-selected steps; iteration/time/spend bounds and stopping |
| State/effects | Trusted business rules, action permissions, state owner, duplicates and partial completion |
| Economics | Latency distribution, concurrency and cost per accepted outcome including retries/human correction |
| Operations | Data handling, provider limits/outages, fallback, observability, ownership and recovery |
| Change | Model/prompt/tool/index compatibility, persisted state, cutover and invalidated evidence |

Choose provider/model candidates by the task and observed constraints, not a universal leaderboard.
Verify current capabilities, versions, availability, pricing, data policies and region only when needed to
decide. Missing measurements produce a conditional recommendation and an unrun comparison protocol.
Do not call providers or install a framework in an architecture assessment.

## Preserve the deterministic boundary

The model may propose a classification, answer or action. Trusted application code validates domain rules,
identity, permission, limits and execution. Structured output shape does not prove truth or authorization.
Use one owner for consequential state and define retry/idempotency, approval, cancellation and recovery.
Diagram control/data flows only when helpful; label observations, desired design and unknown relationships.

## Decision packet

Return current design/non-AI baseline, viable options, explicit criteria, conditional choice, assumptions,
smallest falsifying experiment and migration/verification implications. Fine-tuning, GPU serving and
multimodal pipelines are specialist options when the task warrants them, not prerequisites for an AI feature.
Record compound candidate identity: code, provider/model, parameters, prompt, tools/policy, corpus/index/
embedding/ranker, memory/cache and runtime. A change in any relevant part can invalidate a comparison.

[Research basis](../../../guidelines/catalog/research-ai-app-engineering-2026-11-17.md): S1–S5, S8, S12–S14.
