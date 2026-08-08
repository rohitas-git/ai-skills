---
name: 1-thinking-cynefin
description: >
  When the right response mode is unclear, classify the cause-effect domain first; decompose disorder.
  Use when: When the right response mode is unclear, classify the cause-effect domain first; decompose disorder.
  Not for: Domain and method are already agreed—execute; Task is finding a specific cause, not choosing an approach.
  Hub: /0-thinking. Triggers: thinking cynefin, cynefin.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "When the right response mode is unclear, classify the cause-effect domain first; decompose disorder."
    not_when:
      - "Domain and method are already agreed—execute"
      - "Task is finding a specific cause, not choosing an approach"
      - "Classification done; switch to the domain method—do not re-label endlessly"
      - "Pure mechanical edits with no approach uncertainty"
    cousins:
      - "0-thinking"
    triggers:
      - "1-thinking-cynefin"
      - "thinking cynefin"
      - "cynefin"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-cynefin
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Cynefin Classification

Classify by cause-effect, then use only the matching response mode. Wrong-domain method is the failure mode.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Cynefin Classification (this) | **1-thinking-cynefin** (this) |
| House routing (which domain) | `/0-butler` |

## When to Use

- Unsure whether to run a playbook, analyze, probe, or stabilize.
- A method keeps failing and domain mismatch is plausible.
- A novel or mixed problem needs approach selection before solution work.

## When NOT to Use

- Domain and method are already agreed—execute.
- Task is finding a specific cause, not choosing an approach.
- Classification done; switch to the domain method—do not re-label endlessly.
- Pure mechanical edits with no approach uncertainty.

## Process

1. **State the unit.** Name the decision, incident, or subsystem; if mixed, list separable parts.
2. **Probe cause-effect.** Is the link obvious, expert-analyzable, retrospective only, or imperceptible in turbulence? Check predictability, urgency, and probe safety.
3. **Assign one domain per unit:**
   - **Clear** — obvious → Sense → Categorize → Respond with a runbook.
   - **Complicated** — expert-analyzable → Sense → Analyze → Respond; several valid answers.
   - **Complex** — emergent → Probe → Sense → Respond with safe-to-fail probes; amplify/dampen signals.
   - **Chaotic** — no safe sensing time → Act → Sense → Respond; stabilize first.
   - **Disorder** — unknown → split and classify each part.
4. **Mismatch check.** Reject Clear if its runbook fails; Complicated if analysis cannot predict; Complex if probing is unsafe; Chaotic once safe probing becomes possible.
5. **Commit and stop.** Output domain + first actions. Re-classify only on evidence of domain shift.

**Stop when** every unit has one domain, first actions, and a falsifier—or disorder is decomposed.

## Output

```text
unit: <decision/incident/part>
domain: clear | complicated | complex | chaotic | disorder
evidence: <cause-effect basis>
response_mode: <Sense-Categorize-Respond | Sense-Analyze-Respond | Probe-Sense-Respond | Act-Sense-Respond | decompose>
first_actions: <1-3 concrete steps>
falsifier: <what forces reclassification>
parts: <only if disorder>
```

## Verification

- **Falsify:** Reliable prediction → not Complex. No safe probe → Chaotic. Working runbook → Clear.
- **Stop:** Stop classifying once the matched action is clear.
- **Over-application guard:** Do not call work Complex to avoid analysis or Complicated to avoid a standard fix. One label per unit; decompose multi-domain work.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-cynefin/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
