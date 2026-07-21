---
name: 1-karpathy-guidelines
description: >
  Behavioral guidelines that cut common LLM coding mistakes: surface assumptions,
  simplicity first, surgical diffs, goal-driven verification.
  Use when: writing, reviewing, or refactoring code; avoiding overcomplication;
  making minimal diffs; needing verifiable success criteria.
  Not for: active YAGNI lazy mode (0-ponytail), style/naming standards
  (1-coding-standards), claim-done evidence subagent (2-verify-work).
  Hub: /0-implement. Triggers: karpathy, surgical changes, simplicity first.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "write/review/refactor with process hygiene"
      - "avoid overcomplication; surgical diffs; verifiable goals"
    not_when:
      - "lazy YAGNI mode → 0-ponytail"
      - "naming/modularity style → 1-coding-standards"
      - "evidence-before-done gate → 2-verify-work"
    cousins: [0-ponytail, 1-coding-standards, 2-verify-work]
    triggers:
      - "karpathy"
      - "surgical changes"
      - "simplicity first"
      - "think before coding"
    requires_setup: false
---

# Karpathy Guidelines

Behavioral guidelines to reduce common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## Process

1. Apply the four rules below while writing, reviewing, or refactoring.
2. If the job is pure YAGNI/lazy mode, style standards, or evidence-before-done, redirect via Boundary.

## Boundary

| Need | Skill |
|------|--------|
| LLM coding process hygiene (this checklist) | **1-karpathy-guidelines** (this) |
| Active YAGNI / lazy ladder mode | `/0-ponytail` |
| Over-engineering-only review | `/2-ponytail-review` |
| Naming / modularity / comments while coding | `/1-coding-standards` |
| Evidence-before-done subagent gate | `/2-verify-work` |
| High-stakes adversarial CLAIM→DOUBT | `/1-doubt-driven-development` |

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## Related

Soft under `/0-implement`. Cousins: `/0-ponytail`, `/1-coding-standards`, `/2-verify-work`.
