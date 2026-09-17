---
name: 1-performance-optimization
description: >
  Run one controlled optimization experiment against a measured bottleneck and an
  explicit performance claim. Use when a budget, trace, profile, query plan, or repeatable
  benchmark identifies a slow or resource-heavy path. Not for unexplained failures,
  speculative tuning, durable telemetry design, or database advice without a measured query.
  Primary hub: /0-diagnosing-bugs; shared with /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-diagnosing-bugs
    role: soft
    when:
      - "a repeatable benchmark, trace, profile, query plan, field metric, or budget identifies one bottleneck"
      - "running one controlled optimization experiment with before-and-after evidence"
    not_when:
      - "performance symptom has no reproducible measurement loop → 0-diagnosing-bugs"
      - "greenfield or speculative tuning without a performance claim → 0-implement"
      - "add durable telemetry, SLOs, or alerts → 1-observability-and-instrumentation"
      - "general Postgres design or tuning → 1-supabase-postgres-best-practices"
    prev: [0-diagnosing-bugs, 0-implement]
    next: [0-diagnosing-bugs, 0-implement, 1-observability-and-instrumentation, 1-browser-testing-with-devtools, 1-playwright-browser-testing, 1-supabase-postgres-best-practices, 1-ci-cd-and-automation]
    cousins: [0-diagnosing-bugs, 1-observability-and-instrumentation, 1-supabase-postgres-best-practices]
    triggers:
      - "1-performance-optimization"
      - "optimize this measured bottleneck"
      - "improve this benchmark"
      - "reduce this profiled latency"
      - "fix this measured Core Web Vitals regression"
      - "optimize this query plan"
    requires_setup: false
---

# Performance Optimization

Run **one controlled experiment** that attempts to improve one pinned performance claim
without weakening correctness, security, accessibility, durability, or compatibility. Modes
are plan/advice, read-only measurement/analysis, or authorized repository edit.

## Boundary

| Need | Route |
|---|---|
| Improve one measured bottleneck and compare results | **this skill** |
| Build the first reproducible loop or diagnose an unknown cause | `/0-diagnosing-bugs` |
| Add durable production signals or budgets | `/1-observability-and-instrumentation` |
| Improve PostgreSQL broadly or author schema/index changes | `/1-supabase-postgres-best-practices` plus schema workflow |
| Investigate browser behavior only | `/1-browser-testing-with-devtools` |

## Input and workspace contract

Inherit caller, mode, requested outcome/exclusions, exact repository/worktree/branch/HEAD,
owned and protected files, performance claim and acceptance budget, workload/data fixture,
measurement command/tool/version/config, machine/runtime/network/environment identity, warm/cold
state, repetition/sample limits, correctness checks, benchmark-artifact ownership, and allowed
local, Git, remote, production, load, dependency, schema, and service effects.

Plan and read-only analysis create no worktree. Authorized edits reuse the caller's matching
owned worktree or conditionally route through `/1-git-worktrees`, then return. Store generated
profiles/reports in a task-owned ignored or temporary location unless repository policy says
otherwise. A worktree does not isolate CPUs, networks, browsers, databases, caches, queues,
ports, load generators, or hosted datasets.

## Process

1. **Pin the claim.** Name the user/system behavior, primary metric and unit, target or regression
   comparison, exact candidate, workload, environment, and correctness invariants. If no repeatable
   red-capable measurement exists, return to Diagnose rather than optimizing a hunch.
2. **Establish a comparable baseline.** Run the approved protocol enough to expose variability;
   record raw samples and summary, warm/cold state, machine/load, fixture, tool versions, time,
   and confounders. Field and synthetic data answer different questions; do not substitute one.
3. **Localize the bottleneck.** Use the narrowest fitting trace/profile/plan/counter and rank
   evidence-backed causes. Attribute waiting, execution, I/O, allocation, rendering, transfer, or
   contention before choosing a fix. Do not treat correlation or a single aggregate as causation.
4. **Define one experiment.** State hypothesis, predicted metric movement, allowed code/config
   surface, guard metrics, stop condition, and rollback/disposition. Change one causal variable
   when possible; if coupled changes are inseparable, disclose the attribution limit.
5. **Edit within authority.** Preserve behavior and policy; inspect cache keys/staleness, query and
   write costs, concurrency/backpressure, resource ceilings, accessibility, and failure modes as
   applicable. New dependencies, indexes/migrations, infrastructure, or hosted configuration use
   their owner workflows and return here with evidence.
6. **Re-measure fairly.** Use the same protocol and candidate identity, randomize/interleave when
   drift matters, compare the effect with noise and guard metrics, and explain uncertainty. A local
   result does not prove field or production improvement.
7. **Decide explicitly.** Keep, revise, or recommend removal based on the predeclared claim and
   trade-offs. Do not silently revert user work or keep complexity solely because it was written.
   A statistically visible change can still be operationally irrelevant; a trade-off can be valid
   only when the caller accepts it.
8. **Guard only when justified.** Propose or add the smallest stable regression signal supported by
   repository policy. Noisy microbenchmarks, mutable external services, and hardware-sensitive
   numbers may belong in trend monitoring rather than a required CI gate.
9. **Return.** Provide caller, candidate/worktree, protocol, raw/summary before-after evidence,
   variability and confounders, correctness results, kept/revised/removal disposition, generated
   artifacts, residual risk, and BLOCKED/SKIPPED field or remote validation.

## Hard rules

- Never win by dropping required work, weakening safeguards, changing the workload, or comparing
  unlike candidates/environments without disclosing it.
- Do not invent performance targets, field results, query plans, production load, or significance.
- Do not commit, push, merge, install tools, run load against shared/remote systems, alter schemas,
  deploy, or mutate remote/production state without separate authority.

## References

- Operative: [experiment guide](./references/full-guide.md), [evidence checklist](./references/performance-checklist.md)
- Provenance: [vendor source](./references/vendor-source.md)
