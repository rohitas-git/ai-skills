---
name: 1-critique
description: >
  Rigorous intellectual scrutiny: challenge assumptions, demand evidence, find
  logical gaps, question framing. Explicit request only (critique / devil's
  advocate / challenge my reasoning).
  Use when: user asks to critique, challenge, rigorously analyze, or be
  intellectually honest about an idea or argument.
  Not for: plan interview (0-grilling), steel-man only (1-thinking-steel-manning),
  praise-kill posture (1-anti-sycophancy), CLAIM→DOUBT (1-doubt-driven-development).
  Hub: /0-grilling. Triggers: critique, devil's advocate, challenge my reasoning.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-grilling
    role: soft
    when:
      - "explicit critique / challenge reasoning / devil's advocate"
    not_when:
      - "plan interview → 0-grilling"
      - "steel-man only → 1-thinking-steel-manning"
      - "praise-kill posture → 1-anti-sycophancy"
      - "CLAIM→DOUBT → 1-doubt-driven-development"
    cousins:
      - 0-grilling
      - 1-thinking-steel-manning
      - 1-anti-sycophancy
      - 1-doubt-driven-development
    triggers:
      - "critique"
      - "devil's advocate"
      - "challenge my reasoning"
      - "question my assumptions"
    requires_setup: false
---

# Critique

Rigorous intellectual scrutiny over supportive affirmation. Strengthen reasoning by challenging assumptions, evidence, and structure — not by encouraging or validating. **Invoke only when the user explicitly requests critique** (do not apply proactively).

## Process

1. Confirm an explicit critique request (critique / challenge / devil's advocate / intellectually honest). If not explicit, do not load this mode.
2. Restate the claim or argument in one sentence (steel-man understanding — not a strawman).
3. Challenge using the five principles (assumptions → evidence → logic → framing → depth). Prefer pointed questions and direct flaws over praise.
4. Load [references/full-guide.md](./references/full-guide.md) for techniques, success criteria, and full principle prompts.
5. End when reasoning is stronger, assumptions are exposed, or the user stops the mode. Acknowledge when reasoning holds up.

## Boundary

| Need | Skill |
|------|--------|
| Explicit critique / devil's advocate of an idea | **1-critique** (this) |
| Plan interview (one Q at a time) | `/0-grilling` · wrappers |
| Steel-man only before reject/agree | `/1-thinking-steel-manning` |
| Praise-kill / no agreement bias (posture) | `/1-anti-sycophancy` |
| High-stakes CLAIM→DOUBT decision review | `/1-doubt-driven-development` |

## Hard rules

**Do:**
- Question rather than affirm; demand evidence and specificity.
- Call out weak arguments and logical gaps directly.
- Challenge ideas and claims — not the person's character.
- Prefer truth over comfort; acknowledge when the argument survives scrutiny.

**Do not:**
- Apply proactively without an explicit request.
- Provide encouragement or validation as the default move.
- Soften critiques to avoid discomfort when reasoning is flawed.
- Attack the person; attack structure, evidence, and assumptions.

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full principles, techniques, success criteria | [references/full-guide.md](./references/full-guide.md) |

## Related

Soft under `/0-grilling`. Cousins: `/1-thinking-steel-manning`, `/1-anti-sycophancy`, `/1-doubt-driven-development`.
