---
name: 1-thinking-theory-of-constraints
description: >
  When throughput or latency is pipeline-limited, identify the single binding constraint and exploit, subordinate, elevate, then recheck—ignore non-constraints.
  Use when: When throughput or latency is pipeline-limited, identify the single binding constraint and exploit, subordinate, elevate, then recheck—ignore non-constraints.
  Not for: Load is spread; no stage dominates—use systems for interactions; Problem is correctness/fault, not flow rate—debug the fault.
  Hub: /0-thinking. Triggers: thinking theory of constraints, theory-of-constraints.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "When throughput or latency is pipeline-limited, identify the single binding constraint and exploit, subordinate, elev…"
    not_when:
      - "Load is spread; no stage dominates—use systems for interactions"
      - "Problem is correctness/fault, not flow rate—debug the fault"
      - "Bottleneck hops every run due to coupling/contention without a stable stage—systems or …"
      - "Constraint already known and a cheap fix is ready—apply it without ceremony"
    cousins:
      - "0-thinking"
    triggers:
      - "1-thinking-theory-of-constraints"
      - "thinking theory of constraints"
      - "theory of constraints"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-theory-of-constraints
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Theory of Constraints

A throughput-limited system has one binding constraint. Improve only that constraint; local optimization of non-constraints wastes effort and often grows WIP.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Theory of Constraints (this) | **1-thinking-theory-of-constraints** (this) |
| House routing (which domain) | `/0-butler` |

## When to Use

- Latency or throughput goal where one stage dominates time or rate.
- Work piles up before one stage; downstream idles.
- Adding capacity/workers elsewhere does not raise end-to-end output.
- Need ordered plan: exploit cheaply before spending to elevate.

## When NOT to Use

- Load is spread; no stage dominates—use systems for interactions.
- Problem is correctness/fault, not flow rate—debug the fault.
- Bottleneck hops every run due to coupling/contention without a stable stage—systems or concurrency design, not five focusing steps.
- Constraint already known and a cheap fix is ready—apply it without ceremony.

## Process

1. **Define the flow and goal.** Name the unit of work (request, job, PR, record) and the metric that matters (end-to-end rate or latency).
2. **Identify the constraint with evidence.** Compare stages on utilization, queue/wait, and throughput. Constraint signals: near-100% use, longest queue, lowest stage rate, work piles here, more input does not raise system output. Prefer measured rates over opinions. If two candidates tie, pick the one whose improvement would raise system throughput first.
3. **Exploit (no major spend).** Maximize constraint output: cut idle, drop nonessential work on the constraint, reduce rework/setup, protect its time, improve quality at the constraint so output is not wasted. Estimate gain before spending.
4. **Subordinate non-constraints.** Pace upstream to constraint rate; do not flood WIP. Make other stages serve the constraint (readiness, clarity, immediate pull). Reject local utilization targets that grow queues before the constraint.
5. **Elevate only if still short.** After exploit is maxed, invest to raise constraint capacity (people, tooling, sharding, parallel path). Choose cheapest adequate elevation.
6. **Recheck (prevent inertia).** After elevation or large exploit, remeasure all stages—the constraint often moves. Return to step 2. Do not keep optimizing the old constraint.

**Stop when** constraint, evidence, exploit plan, subordination rules, and elevate-or-not decision are explicit—or when no single stage binds (exit to systems).

## Output

```text
system_goal: <throughput/latency objective>
flow: <stage sequence>
constraint: <stage or resource>
evidence: <utilization / queue / rate facts>
exploit: <actions, expected gain>
subordinate:
  - stage: <name>
    change: <how it serves the constraint>
elevate: <none | option + cost/gain>
next_constraint_watch: <what to remeasure after change>
```

## Verification

- **Falsify:** If raising the named stage cannot increase system throughput (another stage already caps), identification is wrong. If non-constraint optimizations change end-to-end rate, re-identify.
- **Stop:** Do not elevate before exploit is exhausted. Do not optimize multiple stages “just in case.”
- **Over-application guard:** One constraint at a time. Idle capacity upstream is not a problem to fill. Do not use TOC language for pure multi-loop emergence without a binding stage.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-theory-of-constraints/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
