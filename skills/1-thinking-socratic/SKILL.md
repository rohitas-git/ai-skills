---
name: 1-thinking-socratic
description: >
  When a request is vague, assumption-laden, or "obvious," ask the few load-bearing questions that expose hidden requirements before building or committing.
  Use when: When a request is vague, assumption-laden, or "obvious," ask the few load-bearing questions that expose hidden requirements before building or committing.
  Not for: plan interview (0-grilling).
  Hub: /0-thinking. Triggers: thinking socratic, socratic.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "When a request is vague, assumption-laden, or \"obvious,\" ask the few load-bearing questions that expose hidden requir…"
    not_when:
      - "plan interview → 0-grilling"
      - "Spec is already clear and actionable"
      - "Ambiguity is resolvable by reading code, running a command, or checking docs"
      - "Mid-execution of an agreed plan"
    cousins:
      - "0-grilling"
    triggers:
      - "1-thinking-socratic"
      - "thinking socratic"
      - "socratic"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-socratic
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Socratic Questioning

**Core rule:** Surface the load-bearing assumption or undefined term before you build. Ask only what you cannot resolve yourself; stop when the next action is decision-ready.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Socratic Questioning (this) | **1-thinking-socratic** (this) |
| plan interview | `/0-grilling` |
| House routing (which domain) | `/0-butler` |

## When to Use

- Request is underspecified ("make it fast", "add a dashboard", "fix the bug") and a guess would misbuild.
- Claim rests on an unstated assumption that may be the real problem.
- Someone treats a premise as "obvious" or jumps to a solution before the problem is defined.
- Debugging a vague symptom that needs a checkable specific before investigation.

## When NOT to Use

- Spec is already clear and actionable — do the work; do not interrogate for theater.
- Ambiguity is resolvable by reading code, running a command, or checking docs — resolve it yourself.
- Mid-execution of an agreed plan — re-questioning every step is friction, not rigor.
- Emergency where one load-bearing fact is enough to act — clarify that fact, then act (prefer ooda).
- You need the strongest opposing case, not clarification — use steel-manning.
- You need causal chain depth on a defined failure — use five-whys-plus or scientific-method.

## Process

1. **Name the gap.** State what is undefined, assumed, or uncheckable. If you can fill it from tools/repo without the user, do that and stop.
2. **Ask the load-bearing question first.** Prefer one question whose answer most changes what you will build. Categories (use only what the gap needs):
   - Clarification — "What does X mean / for whom / success looks like?"
   - Assumption — "What must be true? What if it is false?"
   - Evidence — "What supports this? What would disprove it?"
   - Perspective — "Who is affected / who would disagree?"
   - Implication — "What follows if we do this?"
   - Meta — "Is this the right question?"
3. **Resolve or branch.** From the answer, either (a) write the clarified requirement/decision and proceed, or (b) ask at most one follow-up that still gates the work. Do not run all six categories by default.
4. **Make assumptions explicit.** Restate: "This assumes X; success means Y; out of scope is Z." Confirm only if still ambiguous after your restatement.
5. **Stop at decision-ready clarity.** When the next action no longer depends on a hidden premise, end questioning and act or hand off. Cap user-facing questions tightly; prefer batching the few that truly gate work.

## Output

```text
gap: <what was vague or assumed>
resolved_by: self | user | mixed
questions_asked:
  - <only questions actually needed>
assumptions_made_explicit:
  - <X must be true / success = Y>
clarified_requirement: <decision-ready statement>
next_action: <build | investigate | re-scope | stop>
stop_reason: clear_enough | self_resolved | blocked_on_<fact>
```

## Verification

- **Falsify / stop:** If answers do not change the plan, you asked non-load-bearing questions — stop interrogating. If the "clarification" is still a guess, do not build; name the remaining blocker.
- **Over-application guard:** Do not Socratic-interview a well-specified task. Do not outsource facts you can read or measure. Do not turn every step of execution into a new question round.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-socratic/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
