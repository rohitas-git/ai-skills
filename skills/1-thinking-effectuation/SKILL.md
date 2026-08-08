---
name: 1-thinking-effectuation
description: >
  Under genuine uncertainty with no reliable forecast, inventory means, cap downside at affordable loss, act for commitments, and let goals emerge from controllable moves.
  Use when: Under genuine uncertainty with no reliable forecast, inventory means, cap downside at affordable loss, act for commitments, and let goals emerge from controllable moves.
  Not for: The path is predictable: known market, knowable unit economics, established playbook → …; A single wrong step is ruinous or irreversible → de-risk first; do not treat affordable….
  Hub: /0-thinking. Triggers: thinking effectuation, effectuation.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "Under genuine uncertainty with no reliable forecast, inventory means, cap downside at affordable loss, act for commit…"
    not_when:
      - "The path is predictable: known market, knowable unit economics, established playbook → …"
      - "A single wrong step is ruinous or irreversible → de-risk first; do not treat affordable…"
      - "The goal is already fixed and resources are the only uncertainty → plan to the goal"
      - "Routine execution with settled requirements → act; do not re-inventory means"
    cousins:
      - "0-thinking"
    triggers:
      - "1-thinking-effectuation"
      - "thinking effectuation"
      - "effectuation"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-effectuation
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Effectuation

Under Knightian uncertainty, start from available means and affordable loss—not a fixed goal and predicted return. Create the path through controllable action and real commitments.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Effectuation (this) | **1-thinking-effectuation** (this) |
| House routing (which domain) | `/0-butler` |

## When to Use

- The market, technology, or problem is novel enough that outcome probabilities are not trustworthy.
- Means are clearer than the goal: identity, skills, assets, and network exist before a fixed target does.
- A small action can buy information or a partner commitment without risking ruin.
- Plans keep breaking because the environment shifts faster than forecasts.

## When NOT to Use

- The path is predictable: known market, knowable unit economics, established playbook → use causal planning.
- A single wrong step is ruinous or irreversible → de-risk first; do not treat affordable-loss steps as free.
- The goal is already fixed and resources are the only uncertainty → plan to the goal.
- Routine execution with settled requirements → act; do not re-inventory means.

## Process

1. **Inventory means only.** List who you are (skills, constraints, values), what you know (domain, tools, data), and who you know (reachable partners, users, resources). Reject "what would be needed for an ideal plan" as input.
2. **Cap affordable loss.** State the maximum time, money, reputation, and opportunity cost you can lose and still continue. If the proposed step exceeds any cap, redesign the step smaller or stop.
3. **Choose one controllable next action.** Prefer the smallest action that can yield either (a) a real commitment from someone else or (b) discriminating information. Act inside the loss cap; do not optimize expected return.
4. **Seek commitments, not opinions.** Share the working means-based offer. Anyone who commits resources, access, or work becomes a co-creator and may reshape the goal. Discard non-committing feedback as non-binding.
5. **Leverage contingencies.** Treat surprises as new means: failed hires, competitor moves, off-roadmap requests. Ask "how can this expand control?" not "how do we restore the old plan?"
6. **Update means and goal, then stop or loop.** Fold new means and commitments into the inventory; restate the emerging goal. Stop when a viable path is controlled enough to execute, the loss cap is exhausted without traction, or uncertainty collapses into a predictable plan (then switch to causal planning).

## Output

Emit an effectuation brief:

- `means`: identity / knowledge / network actually available now
- `affordable_loss`: hard caps (time, money, reputation, opportunity)
- `next_action`: one controllable step inside those caps
- `commitments_sought_or_won`: who must put skin in the game, and what changed if they did
- `contingencies_used`: surprises turned into means (or none)
- `emerging_goal`: current goal shaped by means and commitments (may differ from the starting wish)
- `stop_or_loop`: continue under effectuation, switch to causal planning, or halt

## Verification

- **Falsify means-first claims:** if the brief starts from a fixed goal and backfills resources, rewrite from means or abandon effectuation.
- **Loss-cap check:** every recommended action must fit inside stated affordable loss; if not, shrink or stop.
- **Commitment test:** progress that depends only on predictions or uncommitted interest is invalid—require at least one real commitment or a cheap information gain.
- **Over-application guard:** if a reliable forecast and known playbook exist, do not force effectuation; plan causally.
- **Stop:** after one means → loss-cap → action → commitment cycle with an explicit stop/loop decision; do not endless-explore under the effectuation label.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-effectuation/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
