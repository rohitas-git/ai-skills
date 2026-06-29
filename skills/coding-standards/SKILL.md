---
name: coding-standards
description: Enforce coding standards including structured step-by-step execution flow comments with ASCII branches for ALL new functions. Use whenever generating, editing, or reviewing code.
---

# Coding Standards

**Mandatory for all code contributions**

## 1. Function Documentation (Strict Rule)

**Every new and modified function** — public, private, arrow functions, reducers, helpers, tests, utilities, graph nodes — **must** begin with a structured metadata block (Purpose, Args, Returns) and, if it contains multi-step logic, a step-by-step execution flow comment.

### Required Format

```js
/**
 * functionName - Brief description.
 * Purpose: High-level intent of the function.
 * Args:
 *   paramName (type): Description.
 * Returns:
 *   type: Description.
 *
 * Execution Flow:
 * 1. [High-level step 1 description]
 *    └─ Input: { dataShape } (Keep root input references simple)
 *    └─ Logic: key decision, transformation, or call
 * 2. [High-level step 2 description]
 *    └─ Call: helperFunction()
 *       └─ Input: { intermediateShape } — description of intermediate parameters
 *       └─ Output: { intermediateResult } — description of returned result
 * 3. [High-level step 3 description]
 *    └─ Output: { returnShape } (Keep root output references simple)
 *    └─ Branch: if condition → alternative path
 */
function functionName(params) {
  // implementation
}
```

### Guidelines
- **Always include** the metadata block. Include the execution flow steps for any function containing multi-step logic.
- Use numbered steps for the main sequence.
- Root inputs/outputs (the function's arguments and return value) should remain lightweight in the Execution Flow (e.g., simple type annotations like `{ dataShape }`) to avoid repeating descriptions already in the `Args` and `Returns` blocks.
- Intermediate inputs/outputs (for steps calling other functions, DB operations, or APIs) **can be fully described** to clarify intermediate data shapes and integration logic.
- Keep comments **concise yet informative** (typically 8–20 lines).
- Update the flow comment whenever logic changes meaningfully.
- This serves as pseudo-code + explanation for maintainability in complex agentic systems.

## 2. General Coding Standards

- **Clear, descriptive naming**: Functions, variables, and files must be self-explanatory (e.g. `resetTransientFields`, `assembleCreativeOutput`).
  - **Avoid Abbreviations**: Do not use short-hand abbreviations for standard variables/parameters. Always use full semantic names (e.g., `request` instead of `req`, `response` instead of `res`, `error` instead of `err`, `isProduction` instead of `isProd`).
- **Modular & readable**: Prefer small, single-responsibility functions.
- **State Management**: Explicitly document any state mutations in the flow comment.
- **Error Handling**: Always handle and document key error paths in Execution Flow.
- **Comments**: Use JSDoc for public APIs/entry points (routes, controllers, exports) in addition to the execution flow. Always preserve JSDoc parameters (like `@route`, `@param`) to document the static interface, while the Execution Flow documents the dynamic implementation logic.
- **Inline Comments**: For complicated code blocks inside a function, write brief inline comments to explain the logic.


## 3. Enforcement

- Apply these standards to **all new and modified code**.
- When modifying any existing function, always review its `Execution Flow` comment block and update it to accurately reflect your changes.
- When reviewing PRs or generated code, verify compliance.
- Existing code should be gradually updated when touched.

This skill integrates the stricter `code-flow-comments` rule into the broader Antigravity development workflow.
