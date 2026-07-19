---
name: coding-standards
description: >
  Enforce lean coding standards for naming, modularity, error handling, and
  comments. Use whenever generating, editing, or reviewing code. For file layout
  and function order (newspaper / stepdown), use stepdown-rule. For API docs use
  code-comments; for one-line block comments use inline-comments; for numbered
  Execution Flow trees use execution-flow-comments.
---

# Coding Standards

**Mandatory for all code contributions**

## 1. Commenting

- **API / surface docs** → **code-comments** (JSDoc, docstrings, GoDoc, etc.)
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

Follow **stepdown-rule** (newspaper metaphor): public/high-level first, helpers last; callers above callees where the language allows. Do not duplicate that skill here — load **stepdown-rule** when structuring or reviewing file order.

## 3. General standards

- **Clear, descriptive naming**: Self-explanatory functions, variables, files (e.g. `resetTransientFields`).
  - Prefer full semantic names (`request` not `req`, `response` not `res`, `error` not `err`, `isProduction` not `isProd`).
- **Modular & readable**: Small, single-responsibility functions.
- **State management**: Mutations easy to follow via structure and naming.
- **Error handling**: Key error paths clear; short comments only when control flow is non-obvious.

## 4. Enforcement

- Apply to **all new and modified code**.
- On review: naming, comments, modularity, and (via **stepdown-rule**) top-down layout.
- Boy Scout Rule: improve layout/comments in regions you touch; do not force whole-file reshuffles unless asked.
