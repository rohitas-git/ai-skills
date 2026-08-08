---
name: 1-thinking-systems
description: >
  When behavior is emergent across components—fixes elsewhere break, loops/delays dominate—map boundary, stocks/flows, feedback, archetypes, then rank leverage.
  Use when: When behavior is emergent across components—fixes elsewhere break, loops/delays dominate—map boundary, stocks/flows, feedback, archetypes, then rank leverage.
  Not for: architecture deepen (0-improve-codebase-architecture).
  Hub: /0-thinking. Triggers: thinking systems, systems.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "When behavior is emergent across components—fixes elsewhere break, loops/delays dominate—map boundary, stocks/flows, …"
    not_when:
      - "architecture deepen → 0-improve-codebase-architecture"
      - "Single-component linear bug with clear stack/diff—trace and fix"
      - "Throughput limited by one obvious stage—use theory-of-constraints"
      - "Decision is a consequence chain of one proposed action—use second-order"
    cousins:
      - "0-improve-codebase-architecture"
    triggers:
      - "1-thinking-systems"
      - "thinking systems"
      - "systems"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-systems
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Systems Mapping and Leverage

Treat the problem as structure and interaction, not isolated parts. Map boundary, stocks/flows, loops/delays, and recurring patterns; intervene at the highest feasible leverage after a side-effect check.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Systems Mapping and Leverage (this) | **1-thinking-systems** (this) |
| architecture deepen | `/0-improve-codebase-architecture` |
| House routing (which domain) | `/0-butler` |

## When to Use

- Symptom spans services/components; single-stack fixes fail or bounce.
- A change in one place breaks another; behavior is emergent.
- Problem recurs despite local fixes (structure, not only symptom).
- Need to rank interventions when parameter/buffer tweaks do not stick.

## When NOT to Use

- Single-component linear bug with clear stack/diff—trace and fix.
- Throughput limited by one obvious stage—use theory-of-constraints.
- Decision is a consequence chain of one proposed action—use second-order.
- Approach selection (plan vs probe vs stabilize)—use cynefin first.

## Process

1. **Bound the system.** Name purpose, actors, boundary, and in/out flows. Exclude noise outside the decision horizon; include any path that can feed the symptom.
2. **Map stocks and flows.** List accumulating stocks (queue depth, debt, cache size, WIP) and the rates that fill/drain them. Note what changes slowly even when flows jump.
3. **Find feedback and delays.** For each candidate loop: classify reinforcing (amplifies) vs balancing (resists); mark same-direction (+) vs opposite (-) links; name delays (TTL, deploy lag, metric lag, ramp-up). Even count of opposite links → reinforcing; odd → balancing. Long delay + strong correction → overshoot risk.
4. **Match recurring structure when problems return.** Check only if recurrence or policy resistance is present; do not force a pattern:
   - Fixes That Fail — quick fix, delayed worse side effect
   - Shifting the Burden — workaround starves fundamental fix
   - Limits to Growth — growth hits a balancing constraint
   - Tragedy of the Commons — local optima deplete a shared stock
   - Escalation — mutual reaction spiral
   - Success to the Successful — advantage compounds via allocation
   - Growth and Underinvestment — capacity lags demand until crisis
   If none fits after a genuine pass, keep the from-scratch map.
5. **Trace symptom to structure.** Walk upstream along flows and loops; separate proximate symptom from structural driver (interaction, delay, wrong goal, missing info).
6. **Rank interventions by leverage, then side effects.** Prefer higher feasible class: goals/paradigm → rules/information → loop structure (gain, balancing add, delay shorten) → stock/flow topology → buffers/parameters. For each candidate: feasibility, blast radius, delayed reversal risk. Prefer moves that cut harmful reinforcing gain or strengthen needed balancing loops without creating a new commons/escalation.
7. **Stop.** Commit highest feasible intervention plus watch signals for loop/delay response. Re-map only if the structure changes or the intervention fails its watch.

**Stop when** boundary, key stocks/flows, dominant loop(s)+delay(s), optional archetype, and a ranked intervention with side-effect check are stated—or when the problem collapses to a single linear cause.

## Output

```text
boundary: <system purpose and edges>
stocks_flows: <stock → inflow/outflow list>
loops:
  - name: <loop>
    type: reinforcing | balancing
    delay: <where cause lags effect>
    links: <brief +/->
archetype: <name or none>
structural_driver: <one sentence>
interventions_ranked:
  - level: <goals|rules|loops|structure|params>
    action: <what>
    side_effects: <feedback/elsewhere/delay risk>
chosen: <highest feasible>
watch: <signals that confirm or falsify>
```

## Verification

- **Falsify:** If removing one component fully explains and fixes the issue with no cross-effects, systems mapping is wrong—drop to local debug. If utilization shows one fixed stage as the sole cap, switch to theory-of-constraints.
- **Stop:** Do not keep adding loops after the chosen intervention and watch are set.
- **Over-application guard:** No archetype without recurrence evidence. No low-leverage param tweak listed as primary when a feasible higher class exists. Do not recreate standalone archetype/feedback/leverage procedures—those checks live only inside this map.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-systems/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
