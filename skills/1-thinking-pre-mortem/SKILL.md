---
name: 1-thinking-pre-mortem
description: >
  Before committing to a plan or launch, assume it already failed and reason backward through concrete causes — convert failure paths into mitigations, gates, and stop checks.
  Use when: Before committing to a plan or launch, assume it already failed and reason backward through concrete causes — convert failure paths into mitigations, gates, and stop checks.
  Not for: plan interview (0-grilling); explicit critique mode (1-critique).
  Hub: /0-thinking. Triggers: thinking pre mortem, pre-mortem.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when:
      - "Before committing to a plan or launch, assume it already failed and reason backward through concrete causes — convert…"
    not_when:
      - "plan interview → 0-grilling"
      - "explicit critique mode → 1-critique"
      - "Work is small, local, and cheaply reversible"
      - "You are mid-incident under time pressure"
    cousins:
      - "0-grilling"
      - "1-critique"
    triggers:
      - "1-thinking-pre-mortem"
      - "thinking pre mortem"
      - "pre mortem"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-pre-mortem
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Pre-Mortem Analysis

**Core rule:** Prospective hindsight beats "what could go wrong?" Assume the plan has already failed (past tense), generate concrete failure paths, reverse them into prevention requirements, and bind each top path to a verifiable plan change.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model frame / which model? | `/0-thinking` (hub) |
| Pre-Mortem Analysis (this) | **1-thinking-pre-mortem** (this) |
| plan interview | `/0-grilling` |
| explicit critique mode | `/1-critique` |
| House routing (which domain) | `/0-butler` |

## When to Use

- Before kickoff, major technical commitment, high-risk sprint work, launch, or release.
- After a plan looks solid but before execution, especially when optimism or overconfidence is likely.
- When a decision is costly to reverse and risks are still implicit rather than enforced.

## When NOT to Use

- Work is small, local, and cheaply reversible — skip the ceremony.
- You are mid-incident under time pressure — act now (OODA / scientific method); pre-mortem is pre-execution.
- You would only emit generic risks ("scope creep", "requirements unclear") that do not bind to this plan.
- Risks are already enforced by live gates (CI, canary, rollback, alerts) with no residual unlisted path.
- A mature risk register already covers the same specific failure paths with owners and checks.

## Process

1. **Set the failure frame in past tense:** "It is [post-deadline date]. The plan failed: [rollback / data loss / no adoption / SLA breach]." Explaining a happened failure is required; predicting one is not enough.
2. **Generate failure reasons before filtering:** sweep technical, process, assumptions, dependencies/external, and people. Force a second pass: "What did the plan most need to be true that was not?" Collect breadth first (aim for many distinct reasons); do not rank mid-sweep.
3. **Prioritize:** group by theme; score likelihood × impact; keep the top 3–5 concrete risks (drop generics that do not bind).
4. **Failure-first reverse analysis (absorbed reverse path):** for each top risk, (a) restate the failed outcome in past tense, (b) list **necessary/enabling conditions** that had to be true for that failure, (c) **invert** each condition into a verifiable prevention requirement (avoid/require rule + check), (d) bind **owner, verification checkpoint, and ship/stage gate**.
5. **Mitigate and update the plan:** for each top risk, attach mitigation steps, spike/contingency if needed, and the reverse-analysis prevention requirements as explicit plan gates. A pre-mortem with no plan change is incomplete.
6. **Stop when** top risks each have a bound mitigation or prevention gate, or when further reasons are only generic restatements — then ship the updated plan, do not keep brainstorming.

## Output

1. **Failure scenario** — past-tense disaster frame with date and failed outcome.
2. **Failure reasons** — unfiltered list, then prioritized top 3–5 with likelihood × impact.
3. **Reverse paths** — for each top risk: necessary conditions → inverted prevention requirements.
4. **Mitigations** — owner, verification checkpoint, ship/stage gate per top risk.
5. **Plan deltas** — concrete tasks, spikes, contingencies, and gates added to the plan.

## Verification

- **Falsify/stop:** if no plan-specific failure path can be stated in past tense with necessary conditions, stop — you are generating theater, not risk. If a "mitigation" has no verification checkpoint, it is not done.
- **Over-application guard:** do not pre-mortem reversible chores, mid-incident firefighting, or systems that already enforce the same paths. Do not leave abstract risks as "mitigate later"; either invert them into gates or drop them as non-actionable.

## Related

Soft under `/0-thinking`. Vendor: `archive/vendor/cc-thinking-skills/skills/thinking-pre-mortem/`.
Route via hub when frame unclear; invoke this leaf when mechanism is known.
