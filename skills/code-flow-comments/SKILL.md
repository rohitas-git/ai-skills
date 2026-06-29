---
name: code-flow-comments
description: Enforce structured step-by-step execution flow comments with ASCII branches for ALL new functions in the codebase.
---

# Strict Code Flow Comments Standard

**Mandatory Rule:**  
**Every new and modified function** — including small helpers, private functions, arrow functions, reducers, node handlers, utilities, and tests — **must** begin with a structured metadata block (Purpose, Args, Returns) followed by an optional structured step-by-step execution flow comment if it has multi-step logic.

This applies to **all new and modified code**. Existing functions and their comments must be updated whenever they are touched.

### Required Format (Strict)

```js
/**
 * functionName - Brief description.
 * Purpose: High-level intent.
 * Args:
 *   paramName (type): Description.
 * Returns:
 *   type: Description.
 *
 * Execution Flow:
 * 1. [Step 1 description]
 *    └─ Input: { dataShape } (Keep root input references simple)
 *    └─ Logic: key decision or transformation
 * 2. [Step 2 description]
 *    └─ Call: externalFunction()
 *       └─ Input: { intermediateShape } — description of intermediate parameters
 *       └─ Output: { intermediateResult } — description of returned result
 * 3. [Step 3 description]
 *    └─ Side effects: state mutation, DB write, etc.
 * 4. Return / Early exit (Keep root output references simple)
 */
function functionName(params) {
  // implementation
}
```

### Enforcement Guidelines

- **Always include** the comment, even for very short functions (unless it's a one-liner trivial getter/setter — but prefer adding it anyway).
- Use **numbered steps** for the main sequence.
- Use **└─ branches** liberally to show:
  - Input/output data shapes (TypeScript-like inline notation)
  - Key variables being transformed
  - Decision branches
  - External calls (LLM, DB, tools, reducers)
  - State mutations
- Keep the comment **concise yet complete** — 6 to 25 lines recommended.
- Update the flow comment **every time** the function logic changes meaningfully.
- For complex functions, you may add a short pseudo-code style line under major steps.
- **Inline Comments**: For complicated code blocks inside a function, write brief inline comments to explain the logic.
- **JSDoc Coexistence**: Always preserve JSDoc parameters (e.g. `@route`, `@param`, `@typedef`) on public entry points (routes, controllers, exports) in addition to the Execution Flow. JSDoc documents the static interface contract (useful for IDEs and swagger), whereas the Execution Flow comment documents the implementation logic.


### Good Example

```js
/**
 * resetTransientFields - Prepares clean state for a new conversation turn
 *
 * Execution Flow:
 * 1. Deep clone the incoming state to avoid mutation
 *    └─ Input: Full ACE State object
 * 2. Reset all transient per-turn fields
 *    └─ textSections: []
 *    └─ currentTasks: []
 *    └─ plan: null
 * 3. Preserve persistent user context
 *    └─ artistProfile, conversationHistory, artForm, userId
 * 4. Return the cleaned state
 */
function resetTransientFields(state) {
  // ...
}
```