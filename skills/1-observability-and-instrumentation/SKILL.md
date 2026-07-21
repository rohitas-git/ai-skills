---
name: 1-observability-and-instrumentation
description: >
  Logging, metrics, tracing, and alerting so production behavior is diagnosable. Use
  when adding instrumentation, defining SLOs/alerts, or making on-call questions
  answerable from telemetry. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "adding instrumentation, defining SLOs/alerts, or making on-call questions answerable from telemetry"
    triggers:
      - "1-observability-and-instrumentation"
      - "observability and instrumentation"
    requires_setup: false
---

# Observability and Instrumentation

Lean catalog skill. **Full vendor body:** [references/full-guide.md](./references/full-guide.md).
Checklist: [references/observability-checklist.md](./references/observability-checklist.md). Pointer only: [references/vendor-source.md](./references/vendor-source.md).

## Process

1. List on-call questions this feature must answer (latency, errors, saturation).
2. Pick signals (RED/USE as appropriate); watch cardinality.
3. Add structured logs + correlation IDs at boundaries.
4. Define symptom-based alerts (not raw CPU noise).
5. Verify dashboards/alerts in non-prod before rely-on.

## Hard rules

- Prefer evidence and small reversible steps.
- Do not invent APIs, metrics, or CI status — verify in the repo/env.
- When overlapping another skill, load the specialist (see Related).

## Related

- Ship soft · pairs with `/1-shipping-and-launch` and `/0-diagnosing-bugs`
- Upstream harvest only; winner name is **`/1-observability-and-instrumentation`**
