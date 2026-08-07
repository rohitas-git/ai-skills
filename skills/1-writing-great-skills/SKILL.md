---
name: 1-writing-great-skills
description: >
  Craft vocabulary and principles for predictable skills — invocation, information hierarchy,
  progressive disclosure, pruning, leading words. Use when: writing or editing a skill body,
  pruning sprawl/duplication/no-ops, choosing what to disclose, or improving a description.
  Not for: place/ingest (0-skill-manager), full create/eval automation (0-skill-creator).
  Hub: /0-skill-creator.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-creator
    role: craft
    when:
      - "write or edit skill body for predictability"
      - "prune sprawl, duplication, no-ops"
      - "choose progressive disclosure or leading words"
    not_when:
      - "place/ingest → 0-skill-manager"
      - "run eval harness / create loop → 0-skill-creator"
    next: [0-skill-creator]
    cousins: [0-skill-creator, 1-create-skill]
    triggers:
      - "writing great skills"
      - "skill craft"
      - "progressive disclosure"
      - "leading words"
    requires_setup: false
---

# Writing great skills

**Predictability** — same *process* every run, not the same tokens — is the root virtue. Every lever below serves it.

**Bold terms** → [`GLOSSARY.md`](GLOSSARY.md).

## Process

1. Name the job and **branches** (distinct invocation cases).
2. Choose **model-invoked** vs **user-invoked** (description cost vs human index).
3. Place content on the **information hierarchy** — steps first; disclose reference behind **context pointers** whose *wording* encodes when to load.
4. Write or edit the body; end each step on a checkable **completion criterion**.
5. **Prune:** single source of truth → relevance → no-ops (delete whole sentences that fail the no-op test).
6. Hunt **leading words** that collapse restated meaning into pretrained anchors.
7. If trigger accuracy or output quality needs measurement → `/0-skill-creator` (not this file).

## Invocation

| Kind | Pays | Reach |
|------|------|--------|
| **Model-invoked** | Permanent **context load** (description always in window) | Agent + human; other skills can name it |
| **User-invoked** | **Cognitive load** (human is the index); `disable-model-invocation: true` | Human typing only |

Use model-invocation only when the agent (or another skill) must discover it alone. Many user-invoked skills → one **router skill** that names them and when.

## Writing the description

A model-invoked **description** states the skill and lists **branches** that should fire it. Every word is **context load**:

- Front-load the **leading word** that does the invocation work.
- **One trigger per branch** — synonym restatements are **duplication**.
- Cut identity already in the body.

**Trigger-eval method** (near-miss set, train/val, anti-overfit): [agentskills-io-optimizing-descriptions.md](../0-skill-creator/references/agentskills-io-optimizing-descriptions.md). House automation: skill-creator [full-guide](../0-skill-creator/references/full-guide.md) § Description Optimization.

## Information hierarchy

Two content types — **steps** and **reference** — on one ladder:

1. **In-skill step** — ordered action; ends on a checkable (and often exhaustive) **completion criterion**. Vague criteria invite **premature completion**.
2. **In-skill reference** — on-demand rules/facts in `SKILL.md` (flat peer sets are fine).
3. **Disclosed / external reference** — sibling or out-of-skill file via **context pointer**, loaded only when the pointer fires.

**Progressive disclosure** moves reference down the ladder so the top stays legible. Inline what every branch needs; disclose what only some need. **Co-location:** keep a concept’s definition, rules, and caveats under one heading.

## When to split (**granularity**)

Each cut spends a load — only split when it earns:

- **By invocation** — distinct **leading word** needs its own model-invoked description.
- **By sequence** — **post-completion steps** pull the agent into **premature completion**; hide them across a real context boundary.

## Pruning

1. **Single source of truth** — one home per meaning.  
2. **Relevance** — still bears on the skill?  
3. **No-op** test per sentence — does it change behavior vs default? Fail → delete the sentence, don’t trim words.

## Leading words

A pretrained compact concept the agent *thinks with* (e.g. *tracer bullets*, *fog of war*). Anchors **execution** in the body and **invocation** in the description when the same word lives in prompts/docs. Collapse triads of restated quality into one strong word (*tight*, *red*) — fewer tokens, sharper hook.

## Failure modes

| Mode | Defence |
|------|---------|
| **Premature completion** | Sharpen completion criterion first; only then hide later steps |
| **Duplication** | One SSOT |
| **Sediment** | Prune on a schedule; adding is cheap, removing feels risky |
| **Sprawl** | Disclose reference; split by branch/sequence |
| **No-op** | Stronger leading word or delete |
| **Negation** | Prompt the **positive** target; ban only as last-resort guardrail + pair with what to do |

## Progressive disclosure (harvest)

| Load when | File |
|-----------|------|
| Upstream authoring patterns (gotchas, defaults, validation loops) | [references/agentskills-io-best-practices.md](./references/agentskills-io-best-practices.md) |
| TDD-for-docs / eval pressure (superpowers) | [references/superpowers-writing-skills-full.md](./references/superpowers-writing-skills-full.md) |
| Subagent testing | [references/superpowers/testing-skills-with-subagents.md](./references/superpowers/testing-skills-with-subagents.md) |
| Anthropic authoring mirror | [references/superpowers/anthropic-best-practices.md](./references/superpowers/anthropic-best-practices.md) |
| Persuasion principles | [references/superpowers/persuasion-principles.md](./references/superpowers/persuasion-principles.md) |
| Output evals / scripts / open format | `/0-skill-creator` → [evaluating](../0-skill-creator/references/agentskills-io-evaluating-skills.md) · [scripts](../0-skill-creator/references/agentskills-io-using-scripts.md) · [spec](../0-skill-creator/references/agentskills-io-specification.md) |

## Related

Parent: `/0-skill-creator` · place/ingest: `/0-skill-manager` · lint: `/1-skill-linter`.
