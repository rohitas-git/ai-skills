# Observability review checklist

Apply only to the bounded behavior and candidate named by the main skill. “Not applicable” is a
valid result; this checklist does not require every signal type.

## Scope and provenance

- [ ] Caller, design/assessment/edit mode, behavior, operator question, and exclusions are named.
- [ ] Repository/worktree/branch/HEAD and target environment/evidence time are exact where relevant.
- [ ] Existing logger, metric, tracing, dashboard/runbook, and schema conventions were inspected.
- [ ] Allowed local, hosted, and production effects are explicit; shared service ownership is known.

## Question-to-signal contract

- [ ] Every proposed signal answers a stated question or existing obligation.
- [ ] Stable name, source boundary, fields/dimensions, propagation, owner, and verification are recorded.
- [ ] Data classification, access, retention, sampling, volume, and cost consequences are considered.
- [ ] Unknown SLOs or thresholds are identified as decisions rather than invented values.

## Events and logs, when applicable

- [ ] Output follows repository structure and stable event naming.
- [ ] Levels fit existing policy and actionable meaning.
- [ ] Correlation/run/trace identity is validated or generated and propagated only where needed.
- [ ] Shared sinks distinguish bounded entry points at their origin.
- [ ] Fields are allowlisted; secrets, authorization material, unnecessary personal/content data,
      full bodies, and raw third-party payloads are absent or policy-approved and redacted.

## Metrics, when applicable

- [ ] RED/USE or another selected model fits the target behavior/resource.
- [ ] Latency uses an appropriate distribution rather than relying only on an average.
- [ ] Dimensions come from small controlled sets; estimated combined series growth is acceptable.
- [ ] IDs, emails, tenants, raw URLs, free-form errors, prompts, and payloads are not dimensions.

## Traces and agent telemetry, when applicable

- [ ] Existing context propagation is preserved across the changed HTTP/RPC/queue/job seam.
- [ ] Manual spans have a specific operator purpose; auto-instrumentation exposure was assessed.
- [ ] Sampling and retention match policy and backend capability.
- [ ] Agent telemetry separates operational metadata from prompts, completions, retrieval content,
      memory, tool payloads/results, and feedback; sensitive content is omitted by default.
- [ ] Correctness claims route to evaluation/tests; trace presence alone is not treated as proof.

## Alerts and response artifacts, when applicable

- [ ] Alert maps to an actionable symptom, SLO/error budget, or measured baseline.
- [ ] Threshold/window/deduplication/severity use repository evidence or remain explicitly proposed.
- [ ] Owner, destination, dashboard, and response/runbook link are valid for the target environment.
- [ ] Creating or editing hosted alerts, dashboards, routes, and runbooks is separately authorized.

## Verification and return

- [ ] Success and safe failure paths were exercised at the narrowest authorized level.
- [ ] Actual emitted shape, redaction, dimensions, and changed-seam propagation were inspected.
- [ ] Hosted ingestion, queryability, rendering, notification, and production claims use exact remote
      evidence; local output is not substituted.
- [ ] No tool install, shared-service start, fault injection, alert firing, deploy, or remote mutation
      occurred without separate authority.
- [ ] Return includes candidate/worktree, ledger, PASS/FAIL/BLOCKED/SKIPPED checks, risks, proposed
      remote checks, and residual blind spots.
