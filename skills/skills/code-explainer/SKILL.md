---
name: code-explainer
description: >
  Explain source code (lines, blocks, functions, files, modules) at audience
  levels (Noob, Learner, Junior, Senior) and depths (Brief, Standard, Deep).
  Trigger on "explain this code", "what does this function do", "break down this
  file". Not general concept teaching (/learning-explainer), Socratic tutoring
  (/learn tutor-mode), or vault Concepts (/vault-explain). Soft under /learn.
disable-model-invocation: true
---

# Code Explainer

**Atomic job:** audience-adapted walkthrough of **code**, not abstract topics.

## Boundary

| Need | Skill |
|------|--------|
| Explain code (line → module) | **code-explainer** (this) |
| Explain a concept (no code focus) | `/learning-explainer` (via `/learn` F-L1) |
| Socratic practice / quiz | `/learn` tutor-mode |
| Route learning intent | `/learn` |
| Vault `[[Note]]` | `/vault-explain` |

## Hard redirect

If there is **no code** under discussion (pure concept, theory, non-code ELI5): ask **F-L1** with recommended `/learning-explainer`, wait, then load that skill.

If the user wants to **solve a problem themselves** under guidance: ask once → `/learn` tutor-mode.

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

- **Parent hub (soft):** `/learn` — F-L1 code walkthrough branch
- **Cousins:** `/learning-explainer` · tutor-mode · `/vault-explain`
