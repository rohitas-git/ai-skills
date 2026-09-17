# Observability operative guide

Use this guide only after the main skill has fixed the caller, mode, candidate, behavior,
environment, data boundary, and allowed effects. The complete upstream snapshot remains at
`archive/vendor/agent-skills/skills/observability-and-instrumentation/SKILL.md`; its universal
requirements and executable examples are historical source material, not catalog authority.

## Start from a question

Write a small question-to-signal ledger before adding telemetry:

| Operator question | Signal | Stable dimensions | Sensitive data excluded | Verification |
|---|---|---|---|---|
| Why did this job fail? | structured terminal event | result class, attempt, entry point | payload, token, user content | exercise a safe failure and inspect output |
| Is this dependency degrading? | rate/error/duration metric | dependency, operation, result class | request ID, URL, error text | deterministic local load or recorded fixture |
| Where did this request wait? | trace/span continuity | service, operation, status | body, auth headers | follow one disposable request across the changed seam |

If a signal cannot answer a stated question or enforce an existing obligation, omit it.

## Signal choices

### Structured events

- Use the repository's logger and field conventions; JSON is common, not universally required.
- Choose stable event names and documented levels. Do not redefine severity globally in a
  feature-sized change.
- Put bounded classification fields in the event and high-detail diagnostics only where
  policy, access control, retention, and cost permit them.
- Validate inbound correlation values or generate new ones. Propagate request/run/trace identity
  only where it supports the path being observed; do not treat it as authentication.
- When multiple entry points share a sink, record a bounded entry-point identity at the origin
  and propagate it instead of inferring it later.

### Metrics

- RED (rate, errors, duration) fits request/dependency paths; USE (utilization, saturation,
  errors) fits resources. Neither is a mandate to instrument every endpoint or host.
- Prefer histograms or the platform's distribution type for latency. Select buckets/quantiles
  from the workload and backend rather than copying examples.
- Labels/tags must come from small controlled sets. IDs, emails, tenant names, raw URLs,
  free-form errors, prompts, and payloads do not belong in metric dimensions.
- Estimate series growth before adding labels: the Cartesian product, not each label alone,
  determines cardinality and cost.

### Traces

- Reuse the installed tracing/context mechanism. OpenTelemetry is a common interoperable option,
  not automatic permission to add packages or exporters.
- Add manual spans only around meaningful boundaries or unexplained work. Auto-instrumentation
  can expose data or add cost; inspect its defaults before enabling it.
- Propagate context across the specific HTTP, RPC, queue, or job handoff under review.
- Sampling is a reliability, privacy, and cost decision. Do not promise “all errors retained”
  unless the backend and policy actually implement it.

### Agent systems

- Prefer identifiers and aggregates for model, prompt-template version, tool, retrieval stage,
  latency, token use, cost estimate, retry, result class, and evaluation outcome.
- Treat prompts, completions, retrieved documents, tool arguments/results, memory, and feedback
  as potentially sensitive content. Redact or omit by default; content capture requires a named
  purpose, access/retention policy, and explicit authority.
- A trace shows execution, not correctness. Pair behavioral claims with `/1-agent-evaluation`.

## SLOs, alerts, dashboards, and runbooks

- Define an SLI from what users or dependent systems experience. Propose an SLO only when the
  owner and measurement window are known; otherwise return the missing decision.
- Alert on actionable symptoms or exhausted budgets when evidence supports the threshold.
  Infrastructure causes may still be appropriate warnings or investigation signals; avoid a
  universal “never page on causes” rule.
- Existing repository policy owns severity tiers and paging routes. Do not impose a two-tier
  scheme, destination, or response time from this skill.
- A dashboard should answer the fixed operator questions and link from the response path when
  the repository uses dashboards-as-code.
- Create or edit a runbook only when documentation changes are authorized and the repository has
  a canonical location. Minimum useful content: meaning, first safe checks, ownership/escalation,
  and rollback or containment boundaries where relevant.

## Verification ledger

For each claim record candidate, environment, method, time/fresh-run identity, result, and gap.

- Static/unit checks can validate names, schemas, redaction helpers, and bounded dimensions.
- Local/disposable runtime checks can validate emitted shape and seam propagation.
- Hosted ingestion/queryability, retention, dashboard rendering, notification delivery, and
  production behavior need evidence from that system and separate authority.
- Never lower a live threshold, inject a staging/production fault, page a channel, or deploy only
  to prove instrumentation. Provide a proposed command or procedure and mark the check blocked.

Return to the actual Ship, DevOps, or Agent Engineering caller after the bounded telemetry slice;
do not continue into incident response, optimization, rollout, or remote operation automatically.
