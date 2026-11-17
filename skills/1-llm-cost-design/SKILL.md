---
name: 1-llm-cost-design
description: >
  Design one evidence-backed spending policy for an LLM workload, covering routing, retries,
  caching, and budget enforcement. Use when defining API cost controls or a cost-reduction proposal.
  Not for live billing administration, provider calls, implementation, or quality evaluation.
  Hub: /0-agent-engineering.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-agent-engineering
    role: leaf
    when: [design a spending policy or cost-reduction proposal for one LLM workload]
    not_when: [live billing changes, execute provider calls, implement a pipeline, run quality evaluation]
    prev: [0-agent-engineering]
    next: [0-agent-engineering]
    cousins: [1-agent-evaluation, 1-observability-and-instrumentation, 1-performance-optimization]
    triggers: [LLM cost policy, reduce LLM API spend, model routing budget, prompt caching strategy]
    requires_setup: false
  vendor:
    source: affaan-m/ECC
    upstream_id: cost-aware-llm-pipeline
    commit: d2ef2680594f9a17526a6e1a2e18b3d242c5d17b
---

# LLM Cost Design

Produce one policy/proposal in chat. Implementation, paid experiments, telemetry installation,
and live budget/account changes require their own scope. This skill performs no provider calls.

## Boundary

| Need | Owner |
|---|---|
| Define spending controls and compare cost options | **this skill** |
| Establish model/task quality or routing accuracy | `/1-agent-evaluation` |
| Implement a selected policy | `/0-implement` |
| Add production usage telemetry | `/1-observability-and-instrumentation` |
| Run a controlled latency/performance experiment | `/1-performance-optimization` |

## Process

1. Pin caller, workload, quality/failure requirements, data restrictions, provider/account/model/
   endpoint, traffic period, concurrency, current candidate, budget currency/scope, and design-only
   authority. Use supplied normalized usage or authorized read-only evidence; never expose secrets.
2. Establish the baseline: ordinary input, cache writes/reads, output, storage, tools, retries,
   failures, and latency. Verify current model availability, units, pricing, cache behavior and
   usage schema from official provider documentation before quoting numbers. Missing rates or
   usage remain unknown; label hypothetical scenarios and keep units consistent.
3. Compare the smallest fitting options. Use observed task quality to justify routing, not text
   length or a blanket cheapest-model rule. Include escalation, refusal, timeouts, invalid output,
   and fallback costs. A cheaper request can cost more per accepted result.
4. Specify enforcement before dispatch: conservative per-request/attempt bounds, atomic reservation
   for concurrent work, reconciliation to actual usage, cancellation, and a safe exhausted-budget
   result. Account for retries, fallbacks, streaming/tool charges, and uncertain failed-call billing.
   Post-call totals alone cannot enforce a hard cap. State where a strict bound is unavailable.
5. Define bounded retries for documented transient failures, with deadlines, jitter, provider limits,
   idempotency, and retry cost. Do not retry a consequential action just because a model call failed.
6. For repeated prompts, load [cache cost and privacy](./references/prompt-cache.md). Preserve task
   semantics, instruction order, access control, and quality while testing potential reuse.
7. Return baseline provenance, proposed rules, assumptions, cost scenarios, quality/latency guards,
   enforcement gaps, and a verification plan. Distinguish estimated savings from measured savings.
   Route requested execution or implementation to its owner without starting it automatically.

Source: [ECC adaptation and review](../../guidelines/catalog/ingest-ecc-2026-11-15.md), [MIT license](./LICENSE).
