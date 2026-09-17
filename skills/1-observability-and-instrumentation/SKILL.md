---
name: 1-observability-and-instrumentation
description: >
  Design, assess, or implement telemetry for one bounded production behavior so a
  stated operator question can be answered. Use for structured events, bounded
  metrics, trace continuity, SLO-derived alerts, or agent-system telemetry. Not for
  diagnosing an active failure, performance optimization, release execution, or a
  general privacy/security audit. Hubs: /0-implement, /0-devops, /0-agent-engineering.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "designing, assessing, or implementing telemetry for one bounded production behavior"
      - "making a stated operator question answerable with logs, metrics, traces, dashboards, or alerts"
      - "instrumenting model, tool, retrieval, token, cost, or agent-run behavior"
    not_when:
      - "diagnose or contain an active failure → 0-diagnosing-bugs / 1-incident-response"
      - "optimize measured latency or resource use → 1-performance-optimization"
      - "plan or execute a release → 1-shipping-and-launch"
      - "perform a general privacy or security audit → 1-security-auditor"
    prev: [0-implement, 0-devops, 0-agent-engineering]
    next: [0-implement, 0-devops, 0-agent-engineering, 0-diagnosing-bugs, 1-incident-response, 1-performance-optimization, 1-shipping-and-launch, 1-security-auditor, 1-agent-evaluation]
    triggers:
      - "1-observability-and-instrumentation"
      - "add telemetry for this behavior"
      - "design structured logging"
      - "define an SLO or alert"
      - "trace this request or job"
      - "instrument this agent workflow"
    requires_setup: false
---

# Observability and Instrumentation

Make **one bounded behavior** answer one or more stated operator questions. Work in
design/advice, read-only assessment, or authorized repository-edit mode; do not turn
instrumentation authoring into permission to operate a telemetry backend.

## Boundary

| Need | Route |
|---|---|
| Add or improve evidence emitted by a known behavior | **this skill** |
| Explain an observed failure from current evidence | `/0-diagnosing-bugs` |
| Contain or recover an active production incident | `/1-incident-response` |
| Optimize measured performance | `/1-performance-optimization` |
| Decide rollout, rollback, or launch monitoring | `/1-shipping-and-launch` |
| Audit telemetry privacy or security broadly | `/1-security-auditor` |

## Input contract

Inherit the caller, mode, requested outcome and exclusions; exact repository/worktree/
branch/HEAD when files are involved; target service/environment and evidence time; owned
and protected paths/services; data classifications and retention constraints; and allowed
local, remote, and production effects. Record the operator question and affected behavior.

Design and assessment create no worktree. An authorized edit reuses the caller's matching
owned worktree. Use `/1-git-worktrees` only when isolation is independently required, then
resume the original caller with returned provenance; a worktree does not isolate a shared
collector, dashboard, alert route, credential, port, or production tenant.

## Process

1. **Pin the slice.** State the behavior, user/operator impact, question, environment,
   candidate, and current evidence gap. Do not instrument an entire application by default.
2. **Inventory before choosing.** Inspect repository conventions, existing SDKs/exporters,
   schemas, dashboards/runbooks-as-code, and available local verification. Reuse them when
   fit; do not install an SDK, select a vendor, or create hosted resources without authority.
3. **Write a signal contract.** For each question record signal type, stable name, source
   boundary, allowed fields/labels, correlation/trace propagation, sampling or aggregation,
   retention/privacy constraints, owner, and how the signal will be falsified.
4. **Design minimally.** Use structured events for cases, bounded metrics for aggregates,
   and traces for cross-boundary paths. Apply RED/USE only where relevant. Prefer latency
   distributions over averages; never put unbounded or sensitive values in metric labels.
   Propagate a validated or generated correlation identity only across boundaries that need
   it. For agents, separate operational metadata from prompt, tool payload, retrieved content,
   and user data; capture content only when policy and explicit authority allow it.
5. **Define alerts from evidence.** Tie an alert to a user-visible symptom, SLO/error budget,
   or measured baseline; include owner, destination, deduplication/window, and a usable
   response link. Unknown thresholds stay proposed, not invented facts.
6. **Edit only within scope.** Change the minimum owned instrumentation, tests, and canonical
   docs/config required by the contract. Do not broaden product behavior merely to emit a
   signal. Route security, agent-evaluation, CI, or launch concerns to their specialist and
   return here only if telemetry work remains.
7. **Verify the candidate.** Prefer local or disposable evidence: exercise success and safe
   failure paths, inspect actual emitted shape, test redaction and bounded labels, and verify
   propagation at the changed seam. A hosted query, staging fault, alert test, dashboard
   change, or production probe requires its own authority. Report it as BLOCKED/SKIPPED when
   unavailable; do not invent remote evidence from local output.
8. **Return.** Give the caller the exact candidate/worktree, question-to-signal ledger,
   changed paths or recommendations, verification with PASS/FAIL/BLOCKED/SKIPPED, privacy/
   cardinality/retention risks, proposed remote checks, and residual blind spots.

## Hard rules

- Telemetry must not expose secrets, credentials, authorization material, or unnecessary
  personal/content data. Allowlist fields and verify redaction against actual output.
- Do not claim an SLO, threshold, dashboard, trace, alert delivery, or production signal was
  verified without evidence from the named environment and candidate.
- Do not commit, push, merge, install tools, start shared services, alter hosted telemetry,
  test-fire alerts, deploy, or mutate remote/production state without separate authority.

## References

- Operative: [adapted guide](./references/full-guide.md), [review checklist](./references/observability-checklist.md)
- Provenance: [vendor source](./references/vendor-source.md)
- Agent-specific source material: [archived agent-observability skill](../../archive/vendor/awesome-ai-agent-skills/agent-engineering/agent-observability/SKILL.md)
