---
name: coding-standards
description: >
  Always-on lean coding standards for naming, modularity, error handling, and
  comments while generating or reviewing code. Not Clean Code/Architecture Q&A
  (/clean-craftsmanship). For file layout use stepdown-rule; API docs → code-comments;
  one-line blocks → inline-comments; numbered flow trees → execution-flow-comments.
  Soft under Ship / Architecture.
---

# Coding Standards

**Atomic job:** enforce lean standards **while writing or reviewing code**.

## Boundary

| Need | Skill |
|------|--------|
| Apply standards on this change | **coding-standards** (this) |
| Uncle Bob / SOLID / Clean Architecture *why* | `/clean-craftsmanship` |
| File order (newspaper / stepdown) | `/stepdown-rule` |
| API surface docs | `/code-comments` |
| One-line internal notes | `/inline-comments` |
| Numbered Execution Flow trees | `/execution-flow-comments` |
| Deep module seams | `/codebase-design` |

## Hard redirect / fork F-C1

**Enforce standards on code now, or discuss clean-code/architecture principles?**

- **Standards on code** (this) — **recommended** when editing or reviewing a diff
- **Principles Q&A** → `/clean-craftsmanship`

Ask once if ambiguous; never replace mid-implement with a long craftsmanship essay.

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
- On review: naming, comments, modularity, and (via **stepdown-rule**) top-down layout.
- Boy Scout Rule: improve layout/comments in regions you touch; do not force whole-file reshuffles unless asked.
