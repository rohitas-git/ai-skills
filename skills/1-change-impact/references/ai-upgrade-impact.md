# AI change and upgrade impact

Load for model, prompt, context, retrieval, tool, memory or policy changes. Keep this analysis read-only.

## Identify the changed candidate

Compare old/new code, provider/model/version and parameters, instructions/examples, tool schemas and
implementations, policy, corpus/data snapshot, parser/chunking, embedding/ranker/index, memory/cache and
runtime. Unknown versions or mutable aliases limit the comparison. API compatibility is not proof of
unchanged model behavior. Do not copy a stale benchmark across candidates.

## Trace effects beyond the SDK call

- Output semantics, refusals, formats and business validation; downstream stored outputs and consumers.
- Tool selection, permissions, action parameters, idempotency, cancellation and partial completion.
- Context relevance, citations, freshness, missing answers, document access and revocation/deletion.
- Conversations, memory, embeddings/index compatibility and cache namespace/invalidation.
- Error/retry/fallback behavior, latency, cost per accepted result, rate limits and data handling.
- User expectations and language, accessibility, oversight, telemetry and operational ownership.

For each affected claim, map prior evidence to valid, invalidated or unknown with a reason and the
smallest representative recheck. Keep deterministic compatibility tests, model-quality evaluations,
adversarial cases and production observation separate. A favorable average can hide a new severe slice failure.

## Transition obligations

Recommend the fitting replay/shadow/cohort comparison without executing it. Shadow requests must suppress
or safely simulate consequential effects and respect private-data permissions and spend limits.
Identify dual-version state, re-embedding/reindexing and recovery constraints. Code/model rollback may not
reverse new stored outputs, memory, index changes or external writes. Send cutover and release decisions
to existing owners; the impact report approves neither execution nor release.

[Research basis](../../../guidelines/catalog/research-ai-app-engineering-2026-11-17.md): S6–S10, S12–S13.
