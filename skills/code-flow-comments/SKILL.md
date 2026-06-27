---
name: code-flow-comments
description: Enforce structured step-by-step execution flow comments with ASCII branches for ALL new functions in the Antigravity/ACE codebase.
---

# Antigravity Strict Code Flow Comments Standard

**Mandatory Rule:**  
**Every new function** — including small helpers, private functions, arrow functions, reducers, node handlers, utilities, and tests — **must** begin with a structured step-by-step execution flow comment.

This applies to **all new code**. Existing functions should be updated when significantly modified.

### Required Format (Strict)

```js
/**
 * functionName - One-line clear purpose.
 *
 * Execution Flow:
 * 1. [Step 1 description]
 *    └─ Input: { dataShape }
 *    └─ Logic: key decision or transformation
 * 2. [Step 2 description]
 *    └─ Call: externalFunction() or LLM/tool
 *    └─ Output: { expectedShape }
 * 3. [Step 3 description]
 *    └─ Side effects: state mutation, DB write, etc.
 * 4. Return / Early exit
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