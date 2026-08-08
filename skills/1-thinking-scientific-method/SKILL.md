---
name: 1-thinking-scientific-method
description: >
  When a symptom has several plausible causes, rank falsifiable hypotheses and run the cheapest discriminating observation first; prefer least-assumptive survivors only after evidence fit.
  Use when: When a symptom has several plausible causes, rank falsifiable hypotheses and run the cheapest discriminating observation first; prefer least-assumptive survivors only after evidence fit.
  Not for: live bug pipeline (0-diagnosing-bugs).
  Hub: /0-thinking. Triggers: thinking scientific method, scientific-method.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "When a symptom has several plausible causes, rank falsifiable hypotheses and run the cheapest discriminating observat…"
    not_when:
      - "live bug pipeline → 0-diagnosing-bugs"
      - "Cause is already obvious from a single stack, failing test, or recent diff"
      - "Only one plausible hypothesis exists"
      - "No observation is possible yet"
    cousins:
      - "0-diagnosing-bugs"
    triggers:
      - "1-thinking-scientific-method"
      - "thinking scientific method"
      - "scientific method"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-scientific-method
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Scientific Method (Hypothesis Differential)

When a symptom could come from several places, enumerate competing falsifiable hypotheses and spend the cheapest observation on the one that best discriminates among them. After each observation, keep only hypotheses that still fit, then prefer the survivor with the fewest unsupported assumptions as the working explanation.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Scientific Method (Hypothesis Differential) (this) | **1-thinking-scientific-method** (this) |
| live bug pipeline | `/0-diagnosing-bugs` |
| House routing (which domain) | `/0-butler` |

## When to Use

- A bug, incident, or anomaly has more than one plausible cause.
- You can observe code, logs, diffs, traces, tests, configs, or data now.
- You must localize the faulty file, function, branch, config, or invariant before fixing.
- Competing explanations fit the same surface facts and you need a discriminating check.

## When NOT to Use

- Cause is already obvious from a single stack, failing test, or recent diff — fix directly.
- Only one plausible hypothesis exists — test it; do not invent rivals for ritual.
- No observation is possible yet — obtain access first; do not speculate a localization.
- Multi-week experiments, product A/B tests, or policy trials — this skill is for agent-now checks.
- Fault is already localized and you need systemic root/prevention depth — use five-whys-plus.
- Selective "only these objects/times" defects better suited to IS/IS-NOT comparison — use Kepner-Tregoe.
- Representation (doc/dashboard) may be stale versus reality — verify territory with map-territory first, then resume hypotheses.

## Process

1. **State the symptom precisely.** Capture failing behavior, scope, timing, environment, and constraints. Separate observation from interpretation.
2. **Enumerate 2–5 competing hypotheses.** Name specific files, functions, configs, input conditions, or invariants. Reject vague buckets ("backend issue"). If no serious alternative remains after a deliberate check, exit this differential and test or fix the sole evidenced cause directly; never fabricate a rival to continue the procedure.
3. **Name falsifiers and cheap observations before looking.** For each hypothesis: what result drops it, and what read/grep/diff/log/test check can you run now. Prefer observations available immediately over deploys, canaries, or long waits.
4. **Rank observations by discrimination × cheapness.** Run the cheapest check that best separates the top contenders. Do not deep-dive the favorite first if a cheap cross-check would kill alternatives.
5. **Update after each observation.** Drop falsified hypotheses. Among survivors that still fit all evidence, prefer the one with the fewest independent unsupported assumptions (extra components, rare timing, external dependencies). Parsimony ranks survivors after fit; it never rescues a leaner hypothesis that evidence already contradicts. Escalate complexity only when simpler survivors are ruled out.
6. **Localize and stop.** When one hypothesis has direct supporting evidence and key alternatives are ruled out, name the file/function/config to change and the evidence that localizes it. Stop analyzing once localization is direct.

## Output

```text
Symptom: <specific failing behavior, scope, timing>
Hypotheses:
  H1: <specific cause> | Why plausible | Observation | Falsified if
  H2: ...
  H3: ...
Test order: <cheapest discriminating checks>
Results: <what each observation showed>
Survivors: <remaining Hs; least-assumptive working pick among fit>
Localized fault: <file/function/config + supporting evidence>
Ruled out: <Hs dropped and why>
```

## Verification

- Falsify the differential conclusion if you continued with fewer than two serious hypotheses, if no pre-stated falsifier existed, if a cheaper discriminating check was skipped, or if a "simpler" story was kept after evidence contradicted it.
- Stop when the fault is directly localized and alternatives that matter are ruled out; do not continue theorizing.
- Over-application guard: do not narrate observe→question without competing causes; do not treat fewest assumptions as proof; do not run this skill when a single obvious cause is already evidenced.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-scientific-method/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
