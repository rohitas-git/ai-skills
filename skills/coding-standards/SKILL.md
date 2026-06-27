---
name: coding-standards
description: Enforce coding standards including structured step-by-step execution flow comments with ASCII branches for ALL new functions. Use whenever generating, editing, or reviewing code.
---

# Coding Standards

**Mandatory for all code contributions**

## 1. Function Documentation (Strict Rule)

**Every new function** — public, private, arrow functions, reducers, helpers, tests, utilities, graph nodes — **must** begin with a structured step-by-step execution flow comment.

### Required Format

```js
/**
 * functionName - One-line clear purpose of the function.
 *
 * Execution Flow:
 * 1. [High-level step 1 description]
 *    └─ Input: { dataShape } — description of shape or purpose
 *    └─ Logic: key decision, transformation, or call
 * 2. [High-level step 2 description]
 *    └─ Variable: exampleVar — { type, purpose }
 *    └─ Side effect: what changes
 * 3. [High-level step 3 description]
 *    └─ Output: { returnShape } — what is returned
 *    └─ Branch: if condition → alternative path
 */
function functionName(params) {
  // implementation
}
```

### Guidelines
- **Always include** this comment, even for small functions.
- Use numbered steps for main sequence.
- Use `└─` ASCII branches to detail variables, data shapes, logic branches, external calls, and side effects.
- Keep comments **concise yet informative** (typically 8–20 lines).
- Update the flow comment whenever logic changes meaningfully.
- This serves as pseudo-code + explanation for maintainability in complex agentic systems.

## 2. General Coding Standards

- **Clear, descriptive naming**: Functions, variables, and files must be self-explanatory (e.g. `resetTransientFields`, `assembleCreativeOutput`).
- **Modular & readable**: Prefer small, single-responsibility functions.
- **State Management**: Explicitly document any state mutations in the flow comment.
- **Error Handling**: Always handle and document key error paths in Execution Flow.
- **Comments**: Use JSDoc for public APIs in addition to the execution flow.

## 3. Enforcement

- Apply these standards to **all new and modified code**.
- When reviewing PRs or generated code, verify compliance.
- Existing code should be gradually updated when touched.

This skill integrates the stricter `code-flow-comments` rule into the broader Antigravity development workflow.
