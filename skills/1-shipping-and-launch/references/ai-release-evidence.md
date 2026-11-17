# AI release evidence

Load for an AI-enabled release. Keep the parent's readiness/plan/authorized-execution mode and owner.

| Gate | Candidate-specific evidence |
|---|---|
| Identity | Artifact plus model/provider/version, prompt, tools/policy, data/index, memory/cache and runtime |
| Software | Input/output/business validation, permission, denial, retry/idempotency and partial failure |
| AI quality | Representative held-out cases, difficult/adversarial slices, qualified scoring and baseline delta |
| Data/privacy | Authorized retrieval, tenant isolation, freshness, retention/deletion and trace-content limits |
| Experience | Draft/pending/completed states, useful fallback and appropriate correction/control |
| Operations | Latency/errors, budgets, cost per accepted outcome, bounded loops/retries and owner |
| Recovery | Last-known-good full candidate, persistent-state compatibility, disable path and recovery limits |

Set thresholds from actual product requirements and failure costs. Do not invent a universal pass rate,
traffic percentage, human gate or soak time. Sample size, missing outcomes and judge limitations remain visible.
An LLM judge does not establish authorization or replace deterministic checks for a business rule.

For shadow exposure, ensure duplicated traffic cannot send messages, spend, mutate accounts/data or run
jobs unexpectedly. Copying private inputs to another model/provider is a distinct data-handling effect.
For canary/cohort exposure, observe AI quality alongside system health and cost; a healthy endpoint does
not establish useful answers. Missing quality evidence is an explicit hold/gap under the governing policy.

Promote or recover only within the release owner's authority. Recheck affected evidence after a change
to any relevant candidate component. Return unknowns instead of equating local tests with deployed quality.

[Research basis](../../../guidelines/catalog/research-ai-app-engineering-2026-11-17.md): S8–S14.
