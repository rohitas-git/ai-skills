---
name: 1-coding-standards
description: >
  Always-on lean coding standards for naming, modularity, error handling, and comments
  while generating or reviewing code. Not Clean Code/Architecture Q&A
  (/1-clean-craftsmanship). For file layout use 1-stepdown-rule; API docs →
  1-code-comments; one-line blocks → 1-inline-comments; numbered flow trees →
  execution-flow-comments. Soft under Ship / Architecture. Use when: Always-on lean
  coding standards for naming, modularity, error handling, and comments while generatin.
  Hub: /0-improve-codebase-architecture.
metadata:
  catalog:
    hub: 0-improve-codebase-architecture
    role: soft
    when:
      - "Always-on lean coding standards for naming, modularity, error handling, and comments while generatin"
    triggers:
      - "1-coding-standards"
      - "coding standards"
    requires_setup: false
---

# Coding Standards

## Process

1. Follow the steps and hard rules in this skill.
2. Load linked `references/` only when the branch needs them.


**Atomic job:** enforce lean standards **while writing or reviewing code**.

## Boundary

| Need | Skill |
|------|--------|
| Apply standards on this change | **coding-standards** (this) |
| Uncle Bob / SOLID / Clean Architecture *why* | `/1-clean-craftsmanship` |
| File order (newspaper / stepdown) | `/1-stepdown-rule` |
| API surface docs | `/1-code-comments` |
| One-line internal notes | `/1-inline-comments` |
| Numbered Execution Flow trees | `/1-execution-flow-comments` |
| Deep module seams | `/1-codebase-design` |

## Hard redirect / fork F-C1

**Enforce standards on code now, or discuss clean-code/architecture principles?**

- **Standards on code** (this) — **recommended** when editing or reviewing a diff
- **Principles Q&A** → `/1-clean-craftsmanship`
- **Agent judgment** — agent picks between standards vs principles and proceeds

Ask once if ambiguous; never replace mid-implement with a long craftsmanship essay. Always offer **Agent judgment**.

## 1. Commenting

- **API / surface docs** → **code-comments**
- **One-line notes above internal blocks** → **inline-comments**
- **Numbered steps + `└─` trees** → **execution-flow-comments** (only when requested or project-mandated)
- Prefer intention-revealing names over comments
- Default: comment **why**, not what — no execution-flow unless that skill is active
- No comment for obvious code

```js
/**
 * Keeps draft selection in sync with the latest server payload.
 * @param {DraftState} state
 * @param {ServerPayload} payload
 * @returns {DraftState}
 */
function reconcileDraftSelection(state, payload) {
  // Reconcile optimistic rows with persisted rows before rendering.
  // implementation
}
```

## 2. File layout

Follow **stepdown-rule** (newspaper metaphor). Do not duplicate that skill — load it when structuring or reviewing file order.

## 3. General standards

- **Clear, descriptive naming** — Self-explanatory functions, variables, files (e.g. `resetTransientFields`). Prefer full semantic names (`request` not `req`, `error` not `err`).
- **Modular & readable** — Small, single-responsibility functions.
- **State management** — Mutations easy to follow via structure and naming.
- **Error handling** — Key error paths clear; short comments only when control flow is non-obvious.

## 4. Enforcement

- Apply to **all new and modified code**.
- On 0-review: naming, comments, modularity, and (via **stepdown-rule**) top-down layout.
- Boy Scout Rule: improve layout/comments in regions you touch; do not force whole-file reshuffles unless asked.
