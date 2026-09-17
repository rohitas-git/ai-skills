# AI and LLM hardening

The [OWASP LLM risk list](https://genai.owasp.org/llm-top-10/) is a taxonomy, not a
permission model. Apply controls to the actual changed trust boundary; preserve
the user's requested functionality and the parent's scope.

- Treat retrieved text, tool results, files, memory and model output as untrusted
  data according to provenance. Prompt delimiters are not enforcement.
- Authorize consequential tools in trusted code: authenticated actor, permitted
  action, resource, tenant, destination and effect. Schema validity is only shape.
- Do not eval arbitrary model output as SQL, shell, code or HTML. Prefer bounded
  actions with sink-specific validation/encoding and narrow capabilities.
- Keep credentials and unauthorized cross-tenant records out of context. Minimize
  authorized sensitive data, protect logs and respect provider/data-sharing policy.
  Do not claim the system prompt can be kept outside the very model that uses it;
  assume it may leak and never make it the sole holder of secrets or permissions.
- Enforce retrieval authorization for documents/chunks in the requesting user's
  context. A tenant partition label or content filter alone does not prove isolation.
- Bound tool retries, concurrency, tokens and cost. Confirm material effects where
  required; avoid retrying an uncertain write without reconciliation/idempotency.
- Use inert local tests for indirect, stored and cross-agent injection paths.
  A prompt-injection test does not authorize executing a malicious payload.

For detailed boundary design/review use /2-prompt-injection-defense with the same
scope and mode, then return to the caller. Use /1-agent-evaluation for a requested
behavioral evaluation, not as an unconditional new pipeline. Do not duplicate an
existing specialist pass or automatically deploy a filter/service.
