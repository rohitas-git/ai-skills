---
name: coding-standards
description: Enforce coding standards including structured step-by-step execution flow comments with ASCII branches for ALL new functions. Use whenever generating, editing, or reviewing code.
---

# Coding Standards

**Mandatory for all code contributions**

## 1. Commenting Default

Unless the user explicitly asks for JSDoc, execution-flow comments, or another formal comment style, **do not add structured metadata blocks or execution-flow comments by default**.

Default behavior:
- Add **no comment** for obvious code that reads cleanly on its own.
- For non-trivial new or modified functions/callbacks, prefer a **brief 1-2 line comment above the function** explaining its purpose.
- Inside a function body, add **short comments only above genuinely complex blocks**.
- Keep comments lightweight and practical; avoid comment boilerplate that repeats the code.

### Default Format

```js
// Keep the draft selection in sync with the latest server payload.
function functionName(params) {
  // Reconcile optimistic rows with persisted rows before rendering.
  // implementation
}
```

### Guidelines
- Prefer code clarity first; comments should support readability, not compensate for weak naming.
- Use plain language and keep comments short.
- Only document behavior that is hard to infer quickly from the code itself.
- If the user or project explicitly requests JSDoc or structured flow comments, follow that request for the touched code.

## 2. General Coding Standards

- **Clear, descriptive naming**: Functions, variables, and files must be self-explanatory (e.g. `resetTransientFields`, `assembleCreativeOutput`).
  - **Avoid Abbreviations**: Do not use short-hand abbreviations for standard variables/parameters. Always use full semantic names (e.g., `request` instead of `req`, `response` instead of `res`, `error` instead of `err`, `isProduction` instead of `isProd`).
- **Modular & readable**: Prefer small, single-responsibility functions.
- **State Management**: Keep state mutations easy to follow in code structure and naming.
- **Error Handling**: Handle key error paths clearly in code; add short comments only where the control flow is non-obvious.
- **Comments**: Do not add JSDoc or execution-flow blocks unless the user or project explicitly asks for them.
- **Inline Comments**: For complicated code blocks inside a function, write brief inline comments to explain the logic.


## 3. Enforcement

- Apply these standards to **all new and modified code**.
- When modifying existing comments, simplify them unless the user has asked to preserve a more formal style.
- When reviewing PRs or generated code, verify compliance.
- Existing code should be gradually updated when touched.
