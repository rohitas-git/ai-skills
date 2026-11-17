# AI integration contract

Load when a consumer-visible interface adds or changes an AI feature. Preserve the parent's selected mode.
This reference defines one integration seam; it does not implement a complete agent or grant tool authority.

1. Establish current request/response, authentication, business rules, persisted data and error contracts.
   Keep a non-AI path or an explicit unavailable result where product requirements demand it.
2. Separate model input, output schema, semantic validation and trusted action execution. Treat generated
   fields as untrusted even when schema-valid. Never take actor/tenant credentials or approval from model text.
3. Define success, refusal, incomplete/invalid output, timeout, rate limit, unavailable provider, missing
   evidence and policy-denied outcomes. Make consumer behavior explicit for each; do not silently substitute
   a low-quality answer for failure or retry an irreversible action because generation timed out.
4. For streaming/background operations, distinguish partial text, proposed action, accepted job and confirmed
   completion. Define cancellation, disconnect, retry/idempotency and status lookup at the actual boundary.
   Aborting a stream does not necessarily undo an action or stop remote work.
5. Pin the model/prompt/tool/data contract and version persisted outputs. Check older clients, unknown fields,
   changed enums/statuses, conversation state and fallback compatibility. A stable HTTP schema can hide a
   changed semantic contract. Delegate detailed error mechanics to `/1-error-handling`.
6. Define checks for a correct-looking but invalid value, denial/wrong tenant, refusal/partial output,
   provider failure, repeated request and stale approval when relevant. Test runtime policy independently
   of model quality. `/1-agent-evaluation` handles the latter; selection alone triggers no paid execution.

Fictional example: an assistant drafts a refund proposal. A valid `amount` field does not establish that
the requester owns the order, that the refund is within policy, or that it has been approved or executed.
Return those states explicitly and keep execution in the authorized business service.

[Research basis](../../../guidelines/catalog/research-ai-app-engineering-2026-11-17.md): S8–S12.
