---
name: 1-thinking-map-territory
description: >
  When a claim, doc, test, metric, or assumption conflicts with observed behavior, stop theorizing from the map and verify the live code or data; let territory overrule.
  Use when: When a claim, doc, test, metric, or assumption conflicts with observed behavior, stop theorizing from the map and verify the live code or data; let territory overrule.
  Not for: live bug pipeline (0-diagnosing-bugs).
  Hub: /0-thinking. Triggers: thinking map territory, map-territory.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "When a claim, doc, test, metric, or assumption conflicts with observed behavior, stop theorizing from the map and ver…"
    not_when:
      - "live bug pipeline → 0-diagnosing-bugs"
      - "The map is the artifact you are asked to edit (doc, diagram, spec)"
      - "Same path already verified this session"
      - "Map is authoritative and generative (codegen types, derived schema) with no claimed drift"
    cousins:
      - "0-diagnosing-bugs"
    triggers:
      - "1-thinking-map-territory"
      - "thinking map territory"
      - "map territory"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-map-territory
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Map Territory

Docs, tests, diagrams, metrics, comments, and mental models are maps. Running code and actual data are the territory. When they disagree, verify territory and update the model — never force reality to match the description.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Map Territory (this) | **1-thinking-map-territory** (this) |
| live bug pipeline | `/0-diagnosing-bugs` |
| House routing (which domain) | `/0-butler` |

## When to Use

- Observed behavior contradicts a doc, test expectation, diagram, comment, dashboard, or prior assumption.
- A claim about the system rests on a secondary source rather than current code or data.
- Tests pass but production or manual behavior is wrong.
- You are about to theorize why something happens before inspecting what happens.
- A decision depends on whether a model, schema, or metric is still current.

## When NOT to Use

- The map is the artifact you are asked to edit (doc, diagram, spec) — that artifact is the task territory.
- Same path already verified this session — reuse that observation.
- Map is authoritative and generative (codegen types, derived schema) with no claimed drift.
- The mismatch cannot change the decision — note and move on.
- Competing causal hypotheses after territory is confirmed — switch to scientific-method.
- Security exploit construction — use red-team; this skill only settles model-versus-observation.

## Process

1. **Name the map.** State the exact representation trusted: which doc, test, metric, diagram, comment, or assumption. Quote the claim, not a paraphrase.
2. **Name the territory check.** Specify the observation that would prove or disprove the claim: code path, runtime value, query, reproduction, recent change, or live metric.
3. **Verify source and freshness.** Confirm origin of the map (author, generator, last update) and whether it could be stale relative to deploy, config, or data change. Prefer primary current sources over summaries.
4. **Observe the territory.** Read the real code path, run or instrument it, query real data, or reproduce the behavior. Do not predict from signatures or names alone.
5. **Record the delta and update.** If territory contradicts the map, territory wins for shipped behavior. Document the gap, revise the model, then decide the fix (code, map, or both). Note unmapped paths — likely next failure sites.
6. **Stop when settled.** Once the claim is confirmed or overturned with a concrete observation, stop re-checking the same path.

## Output

```text
Map: <claim + source + freshness>
Territory check: <what was inspected/run/queried>
Observation: <concrete result, not interpretation>
Delta: <aligned | map wrong | territory incomplete>
Updated model: <corrected understanding>
Action: <fix code | update map | no decision impact>
Uncovered: <paths no map covers>
```

## Verification

- Falsify if you reasoned from the map without a territory observation, trusted a stale secondary source, or forced code to match a wrong doc without checking either.
- Stop when the contradiction is resolved or irrelevant to the decision.
- Over-application guard: do not re-verify the whole system when editing the map, when the map is the generative source of truth, or when the gap cannot change the next action.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-map-territory/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
