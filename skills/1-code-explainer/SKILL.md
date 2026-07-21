---
name: 1-code-explainer
description: >
  Explain source code at audience levels and depths. Use for "explain this code/function/file".
  Not for: general concepts (1-learning-explainer) or vault Concepts (1-vault-explain). Hub: /0-learn.
  Triggers: explain this code, what does this function do, break down this file.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: soft
    when:
      - "explain code blocks/files"
      - "code walkthrough by audience level"
    not_when:
      - "general concept → 1-learning-explainer"
      - "vault concept → 1-vault-explain"
    cousins: [1-learning-explainer]
    triggers:
      - "explain this code"
      - "what does this function"
      - "break down this file"
    requires_setup: false
---

# Code Explainer

**Atomic job:** audience-adapted walkthrough of **code**, not abstract topics.

## Boundary

| Need | Skill |
|------|--------|
| Explain code (line → module) | **code-explainer** (this) |
| Explain a concept (no code focus) | `/1-learning-explainer` (via `/0-learn` F-L1) |
| Socratic practice / quiz | `/0-learn` tutor-mode |
| Route learning intent | `/0-learn` |
| Vault `[[Note]]` | `/1-vault-explain` |

## Hard redirect

If there is **no code** under discussion (pure concept, theory, non-code ELI5): ask **F-L1** with recommended `/1-learning-explainer`, wait, then load that skill.

If the user wants to **solve a problem themselves** under guidance: ask once → `/0-learn` tutor-mode.

## Audience levels

- **Noob** — Never seen the language; analogies, no jargon.
- **Learner** — Language fundamentals, idioms, why this pattern.
- **Junior** — Edge cases, mistakes, performance, real-world fit.
- **Senior** — Purpose, architectural role, trade-offs, improvements.

## Depth modes

- **Plain Brief** — Simple + short request: purpose, meaning, key consequence only.
- **Brief** — ~1 min; high-signal summary.
- **Standard** — ~3–5 min; balanced (default + Junior if unspecified).
- **Deep** — 10+ min; models, alternatives, edge cases, related concepts.

## Process

1. **Identify scope** — line / block / function / file / module.
2. **Detect language** and relevant concepts.
3. **Apply levels & modes** — default Standard + Junior. Simple+short → Plain Brief.
4. **Structure**
   - Plain Brief: 1 short paragraph or 3–4 bullets (what, why it matters, main risk/outcome).
   - Else: **Overall Purpose** → labeled level/mode sections → snippets / ASCII diagrams → **Key Takeaways** (+ optional Further Learning).

## Best practices

- Accurate at every level; what → how → why.
- Highlight gotchas; prefer markdown structure.
- Combine levels (e.g. Noob + Senior) when asked.

## Related

- **Parent hub (soft):** `/0-learn` — F-L1 code walkthrough branch
- **Cousins:** `/1-learning-explainer` · tutor-mode · `/1-vault-explain`
