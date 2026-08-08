---
name: 1-thinking-second-order
description: >
  When a change has effects past the immediate fix—incentives, scale, feedback—trace consequence chains with timing and probability before committing.
  Use when: When a change has effects past the immediate fix—incentives, scale, feedback—trace consequence chains with timing and probability before committing.
  Not for: Local reversible edit with no incentive or cross-component coupling—just ship and observe; Full system structure (stocks, many loops, leverage ranking) is the goal—use systems.
  Hub: /0-thinking. Triggers: thinking second order, second-order.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "When a change has effects past the immediate fix—incentives, scale, feedback—trace consequence chains with timing and…"
    not_when:
      - "Local reversible edit with no incentive or cross-component coupling—just ship and observe"
      - "Full system structure (stocks, many loops, leverage ranking) is the goal—use systems"
      - "Pre-mortem of failure modes for a plan already chosen—use pre-mortem"
      - "Pure mechanical changes (rename, format) with no behavioral effect"
    cousins:
      - "0-thinking"
    triggers:
      - "1-thinking-second-order"
      - "thinking second order"
      - "second order"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-second-order
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Second-Order Consequence Chains

Do not stop at the intended first effect. Trace what happens next across actors, time, and feedback until the chain stops changing the decision.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Second-Order Consequence Chains (this) | **1-thinking-second-order** (this) |
| House routing (which domain) | `/0-butler` |

## When to Use

- Strategic, policy, incentive, or architecture choices with lasting coupling.
- The obvious fix feels too easy or has known backfire patterns.
- Success or scale would create new problems (load, gaming, debt).
- Need to compare options by delayed effects, not only day-one benefit.

## When NOT to Use

- Local reversible edit with no incentive or cross-component coupling—just ship and observe.
- Full system structure (stocks, many loops, leverage ranking) is the goal—use systems.
- Pre-mortem of failure modes for a plan already chosen—use pre-mortem.
- Pure mechanical changes (rename, format) with no behavioral effect.

## Process

1. **State decision and first-order effect.** One sentence each: action and intended immediate result.
2. **Chain "and then what?"** At least two further orders. For each link record: effect, who responds, rough probability (high/med/low), timing (immediate / next cycle / at scale), and whether it feeds back into the original problem (reinforce or counteract).
3. **Expand affected parties.** Who else reacts (users, operators, other teams, attackers, markets)? What incentives does the change create or destroy?
4. **Scale test.** Ask what happens if everyone does this or usage grows 10x. Mark paths that only appear under scale or repetition.
5. **Prune and decide.** Drop speculative links that do not change the choice. Keep only effects that alter go/no-go, design, or mitigations. Revise the action or add guards where second-order harm exceeds first-order gain.

**Stop when** further "and then what?" no longer changes the decision, or the remaining chain is pure speculation without mechanism.

## Output

```text
decision: <action>
first_order: <intended immediate effect>
chain:
  - order: 2
    effect: <what>
    actors: <who>
    p: high|med|low
    when: immediate|next_cycle|at_scale
    feedback: none|reinforce|balance
  - order: 3
    ...
scale_if_universal: <one sentence or n/a>
revised_decision: <same | modified action | no-go>
mitigations: <guards for kept risks>
```

## Verification

- **Falsify:** If no credible second-order path changes the choice, first-order is enough—stop inventing cascades. If the core issue is multi-loop structure rather than one decision's trail, switch to systems.
- **Stop:** End at the first order that no longer affects the decision; do not pad to a fixed depth.
- **Over-application guard:** No low-probability sci-fi chains. No treating parameter tweaks as deep strategy. Probability and timing required on kept links; omit decoration without mechanism.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-second-order/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
