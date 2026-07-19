---
name: execution-flow-comments
description: >
  Write structured Execution Flow comments with numbered steps and ASCII branch
  trees (Input, Output, Variable, Branch, Logic, Call, Side effect) above
  multi-step functions. Use when the user asks for execution flow, step-by-step
  flow comments, ASCII └─ trees, or /execution-flow-comments. Do not use for
  API docs (code-comments) or single-line block notes (inline-comments).
disable-model-invocation: true
---

# Execution Flow Comments

Document **how a multi-step function runs** with a fixed block above the function: numbered steps plus `└─` detail lines. This is intentional implementation narrative — not Clean Code API docs.

**Boundary**

| Need | Skill |
|------|--------|
| JSDoc / docstrings / public contracts | **code-comments** |
| One-line note above a small internal block | **inline-comments** |
| Numbered steps + `└─` trees for multi-step logic | **execution-flow-comments** (this skill) |

## When to use

- Multi-step handlers, middleware, orchestrators, pipelines (≈3+ sequential decisions or transforms)
- User or project explicitly wants execution-flow / walkthrough comments
- Onboarding-heavy modules where the control path is the point

**Skip** for trivial one-liners, pure getters, or when the user wants lean why-only comments.

## Required format

Place a block comment **immediately above** the function (language-native block style: `/** … */`, `/* … */`, or equivalent). Keep optional Purpose/Args/Returns short; the **Execution Flow** section is mandatory when this skill applies.

```js
/**
 * authenticateRequest - Verify auth token and attach user to the request.
 * Purpose: Gate protected routes; reject missing/invalid tokens early.
 * Args:
 *   request (Request): Incoming HTTP request
 *   next (Function): Express-style continuation
 * Returns:
 *   void: Calls next() with or without error
 *
 * Execution Flow:
 * 1. Extract token from request headers.
 *    └─ Input: request.header("auth-token")
 *    └─ Branch: If token is missing → pass UnauthorizedError to next() and exit.
 * 2. Verify token signature against JWT_SECRET_KEY using HS256.
 *    └─ Variable: decoded — { Object } decrypted JWT payload
 *    └─ Branch: Catch verification exceptions → log warning and pass error to next().
 * 3. Extract and validate user ID from decoded payload.
 *    └─ Variable: userId — { string } user database ID
 *    └─ Logic: Confirm validity of string or MongoId format (in non-test environments).
 *    └─ Branch: If invalid/missing → pass UnauthorizedError to next().
 * 4. Attach user context details to the request object and trigger next().
 *    └─ Side effect: Assigns request.user = { userId, _id: userId }
 *    └─ Output: Calls next() callback.
 */
function authenticateRequest(request, next) {
  // implementation
}
```

### Structure rules

1. **Numbered main steps** — `1.`, `2.`, … sequential happy-path story; early exits called out as **Branch** under the step that decides them.
2. **One primary action per step** — verb-led, present tense (“Extract…”, “Verify…”, “Attach…”).
3. **Detail lines** — indent with `└─` (and nested `└─` only when a call has clear sub-structure).
4. **Tag vocabulary** (use consistently; omit tags that add nothing):

| Tag | Meaning |
|-----|---------|
| `Input:` | Values read at this step (source expression or shape) |
| `Output:` | Value returned or callback fired |
| `Variable:` | Important local — `name — { Type } brief role` |
| `Branch:` | Conditional path / early exit / catch |
| `Logic:` | Non-obvious rule or validation not obvious from the step title |
| `Call:` | External/helper invocation; may nest Input/Output under it |
| `Side effect:` | Mutation, I/O, logging, request decoration |

5. **Keep shapes light** — prefer `{ Object }`, `{ string }`, short field lists; avoid pasting whole schemas.
6. **Length** — typically **4–12 steps** or fewer; detail lines only where they clarify. Prefer 6–25 total flow lines for most functions; trim for simple ones.
7. **Stay true to the code** — update the flow whenever the implementation changes; delete stale branches.

### Optional header (when useful)

Above `Execution Flow:`, a short metadata block is allowed:

```text
 * name - One-line summary.
 * Purpose: High-level intent.
 * Args:
 *   param (type): Role
 * Returns:
 *   type: Role
```

Do not expand Args/Returns into a second novel. Prefer types in the language (TS) when already present; metadata is for readers of the comment, not a substitute for real types.

## Language forms

| Language | Block style |
|----------|-------------|
| **JS / TS / Java / C / C++ / Rust** | `/** … */` or `/* … */` above the function |
| **Python** | Module/function docstring **or** a `#` block immediately above `def` using the same numbering and `└─` lines (prefer a triple-quoted block only if it is not competing with a public API docstring — for public APIs, put Purpose in the docstring and Execution Flow in a `#` block above, or a clearly separated section if the team allows) |
| **Go** | Multi-line `//` block above the func (GoDoc-style leading lines + Execution Flow) |
| **Shell** | `#` lines above the function |

Match project comment conventions; keep the **Execution Flow** skeleton identical.

### Python example

```python
def authenticate_request(request, next_):
    # Execution Flow:
    # 1. Extract token from request headers.
    #    └─ Input: request.headers.get("auth-token")
    #    └─ Branch: If missing → next_(UnauthorizedError) and return.
    # 2. Verify JWT with HS256 and secret.
    #    └─ Variable: decoded — { dict } payload
    #    └─ Branch: On JWTError → log warning, next_(error), return.
    # 3. Validate user id from payload.
    #    └─ Variable: user_id — { str }
    #    └─ Branch: If invalid → next_(UnauthorizedError), return.
    # 4. Attach user and continue.
    #    └─ Side effect: request.user = { "userId": user_id, "_id": user_id }
    #    └─ Output: next_()
    ...
```

## Quality bar

- **Accurate** — every Branch/Call exists in the code; no fictional steps
- **Ordered** — matches real control order (including short-circuits)
- **Scannable** — step titles alone tell the story; `└─` lines are optional detail
- **Stable labels** — use real identifier names from the code (`decoded`, `userId`)
- **No noise** — do not tag every assignment; only Inputs/Variables/Branches that matter

## Do not

- Use this skill for exported API docs alone → **code-comments**
- Replace a single non-obvious line with a full flow tree → **inline-comments**
- Invent “Purpose / Args / Returns / Flow” that ignore the template above
- Leave flow comments behind after a large refactor without updating them
- Comment every private one-liner with a 10-step tree

## Enforcement

- When this skill is active (user request or project mandate), apply to **new and modified** multi-step functions.
- When touching a function that already has Execution Flow, update or remove the block — never leave it lying.
- If the project defaults to lean comments, only apply when explicitly asked.
