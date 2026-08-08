---
name: 1-thinking-five-whys-plus
description: >
  When a fault is localized and the proximate cause is known but the systemic root is not, chain evidence-linked whys with a counterfactual stop and a countermeasure.
  Use when: When a fault is localized and the proximate cause is known but the systemic root is not, chain evidence-linked whys with a counterfactual stop and a countermeasure.
  Not for: live bug pipeline (0-diagnosing-bugs).
  Hub: /0-thinking. Triggers: thinking five whys plus, five-whys-plus.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "When a fault is localized and the proximate cause is known but the systemic root is not, chain evidence-linked whys w…"
    not_when:
      - "live bug pipeline → 0-diagnosing-bugs"
      - "Fault is not localized or multiple candidate causes remain"
      - "Root is evidenced and actionable"
      - "No evidence can answer the next \"why\""
    cousins:
      - "0-diagnosing-bugs"
    triggers:
      - "1-thinking-five-whys-plus"
      - "thinking five whys plus"
      - "five whys plus"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-five-whys-plus
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Five Whys Plus

Build an evidence-linked causal chain from a known proximate fault to an actionable systemic root, then prescribe a countermeasure that would have blocked it.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Five Whys Plus (this) | **1-thinking-five-whys-plus** (this) |
| live bug pipeline | `/0-diagnosing-bugs` |
| House routing (which domain) | `/0-butler` |

## When to Use

- A fault is already localized to a component, path, or subsystem.
- The proximate cause is known, but recurrence or systemic root is not.
- Prior symptom-only fixes failed and the failure returned.
- You need prevention that addresses why the proximate cause was possible.

## When NOT to Use

- Fault is not localized or multiple candidate causes remain — discriminate first.
- Root is evidenced and actionable — fix it.
- No evidence can answer the next "why" — gather evidence.
- One-off error without a process, tooling, or design enabler.
- Selective defect needing IS/IS-NOT analysis.
- Forward failure forecasting before commitment.

## Process

1. **State the localized problem.** Record the observable symptom, confirmed component/path, time window, scope, and impact. Stop if localization is missing.
2. **Chain why with evidence.** Make the prior answer the new effect; propose a cause; cite logs, code, config, metrics, or witnesses; name and rule out alternatives. Stop on speculation.
3. **Branch before descending.** Ask what else could produce the same effect; keep every evidenced independent pathway. Treat the retained branches as a causal set rather than forcing one root.
4. **Counterfactually test each pathway and the set.** For each candidate ask, "Would removing this cause block this pathway?" Then ask, "Would removing the retained set block the observed failure?" Retain independently sufficient branches whose removal blocks their own pathway; do not reject them merely because another branch could still cause the failure.
5. **Enforce stop criteria per branch.** Stop a branch only when its cause is evidenced, controllable, actionable, recurrence-preventing, non-blame (not merely "someone erred"), and counterfactual-positive for that pathway. If it hits human error, ask why the error was possible.
6. **Prescribe a countermeasure for every retained root.** Name the systemic fix, owner-capable action, and how recurrence will be checked. Prefer removing enabling conditions over only patching the proximate symptom.
7. **Stop when verified or blocked.** Halt when stop criteria pass and a countermeasure is specified, or when further steps lack evidence. Do not pad by habit.

## Output

```text
Problem: <localized symptom + component>
Chain:
  Why1: <cause> | Evidence: <...> | Ruled out: <...>
  WhyN: ...
Causal set check: would removing all retained roots block the failure? yes/no
Roots:
  - <systemic cause> | Pathway counterfactual: <...>
    Countermeasure: <action that removes the enabling condition>
    Verification: <how to confirm this pathway is blocked>
```

## Verification

- Falsify the chain if any step lacks evidence, if alternatives were never considered, if a retained root does not pass its pathway counterfactual, or if the full causal set does not explain the failure.
- Stop applying this skill once the root is fixed and verified, or when the problem is still pre-localization.
- Over-application guard: skip a full chain for a single known one-line defect; do not end at blame; do not invent depth without data.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-five-whys-plus/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
