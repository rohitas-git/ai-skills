---
name: 1-code-comments
description: >
  Write clear, professional API and surface documentation using the convention for the
  language in context (JSDoc for JS/TS, docstrings for Python, GoDoc, rustdoc, etc.).
  Prefer intention-revealing names. Comment why, not what. Never write execution-flow or
  step-by-step walkthrough comments unless the user invokes execution-flow-comments. Use
  when writing or reviewing public/exported docs and contracts. For one-line comments
  above internal code blocks, use inline-comments. For numbered Execution Flow trees,
  use execution-flow-comments. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "writing or reviewing public/exported docs and contracts"
    triggers:
      - "1-code-comments"
      - "code comments"
    requires_setup: false
---

# Code Comments

## Process

1. Follow the steps and hard rules in this skill.
2. Load linked `references/` only when the branch needs them.


Apply **Clean Code** discipline with **language-native professional conventions** for **API / surface docs**. Comments support readers; they must not narrate the code.

**Boundary**

| Need | Skill |
|------|--------|
| JSDoc / docstrings / GoDoc / public contracts | **code-comments** (this skill) |
| One-line notes above internal blocks | **inline-comments** |
| Numbered steps + `└─` Execution Flow trees | **execution-flow-comments** |

## Core Rules

1. **Match the language’s professional convention**  
   Use the docs/comment style that professionals use for that language (see below). Do not invent a custom format or mix styles in one codebase.

2. **Code first, comments second**  
   Prefer better names, smaller functions, and clearer structure. If a name needs a comment to explain it, rename.

3. **Comment why, not what**  
   Explain intent, business rules, trade-offs, constraints, and non-obvious consequences. Do not restate what the signature or body already says.

4. **No execution-flow in this skill**  
   Numbered steps, ASCII trees (`└─`), and “Execution Flow” blocks belong to **execution-flow-comments** only when that skill is active.

5. **Keep docs accurate and lean**  
   Only document what a reader cannot 0-learn quickly from names and types. Delete outdated, redundant, or dead comments. No commented-out code.

## Language Conventions (use the one in context)

Detect language from file extension, project tooling, or surrounding code. Prefer the **project’s existing style** when it already follows a professional standard.

| Language | Professional form | Typical use |
|----------|-------------------|-------------|
| **JavaScript / TypeScript** | **JSDoc** (`/** ... */`, `@param`, `@returns`, `@throws`, `@typedef`, …) | Exported modules, public functions/classes, non-obvious contracts. TS: prefer types in code; JSDoc for runtime/export docs and JS files. |
| **Python** | **Docstrings** (PEP 257; Google/NumPy/Sphinx style if the repo already uses one) | Modules, classes, public functions. |
| **Go** | **GoDoc** (`// Name ...` on exported symbols) | Exported packages, types, funcs. |
| **Rust** | **rustdoc** (`///`, `//!`, crate/module docs) | Public items and modules. |
| **Java / Kotlin** | **Javadoc / KDoc** | Public APIs and non-obvious contracts. |
| **C / C++** | Doxygen-style or project-standard block comments | Headers and public APIs. |
| **C#** | XML doc comments (`/// <summary>`) | Public APIs. |
| **Swift** | DocC (`///`) | Public APIs. |
| **Shell** | Brief `#` headers | Scripts, non-obvious flags/side effects. |
| **SQL** | Brief `--` notes | Non-obvious constraints, migrations, dangerous ops. |

Inline `//` or `#` inside bodies: only brief local why (warnings, invariants)—never as a substitute for the language’s API doc form on public symbols. Placement and density of those line comments are covered by **`1-inline-comments`**.

## When to Document

| Kind | When |
|------|------|
| Language-native API docs | Exported/public symbols; non-trivial contracts (params, returns, errors, side effects) |
| Intent / why | Business rule, invariant, or design choice names can’t carry |
| Warning | Thread-safety, order sensitivity, irreversible or costly ops |
| TODO | Temporary debt with a clear follow-up (prefer ticket link) |

## When Not to Comment

- Restating the name, types, or next line of code
- Narrating every step of a function
- Custom “Purpose / Args / Returns / Flow” blocks that ignore language conventions
- Noise markers, end-of-block labels, journal history, HTML in comments
- Anything a good name, type, or extract-method would make obvious

## Examples

### JavaScript / TypeScript (JSDoc)

```js
/**
 * Captures a settled payment hold.
 * Call only after the hold settles; double-billing is not recoverable.
 *
 * @param {string} holdId - Provider hold id (also used as idempotency key).
 * @param {number} amount - Amount in minor units.
 * @returns {Promise<Charge>} Created charge.
 * @throws {Error} If the hold is still pending or already captured.
 */
async function capturePayment(holdId, amount) {
  // Same idempotency key as hold create — required by the provider.
  return stripe.charges.create({ amount, /* ... */ }, { idempotencyKey: holdId });
}
```

TypeScript: put types in the type system; use JSDoc for exported JS-interop, runtime notes, and `@deprecated` / warnings. Avoid duplicating every `@param` type already in the signature.

### Python (docstring)

```python
def capture_payment(hold_id: str, amount: int) -> Charge:
    """Capture a settled payment hold.

    Call only after the hold settles; double-billing is not recoverable.

    Args:
        hold_id: Provider hold id (also used as idempotency key).
        amount: Amount in minor units.

    Returns:
        The created charge.

    Raises:
        ValueError: If the hold is still pending or already captured.
    """
    # Provider requires the same idempotency key as hold create.
    ...
```

### Go (GoDoc)

```go
// CapturePayment captures a settled payment hold.
// Call only after the hold settles; double-billing is not recoverable.
func CapturePayment(holdID string, amount int64) (*Charge, error) {
    // Provider requires the same idempotency key as hold create.
    ...
}
```

## Refactoring Existing Comments

- Wrong format for the language → rewrite in the professional convention (e.g. plain `//` above a public JS function → JSDoc).
- Redundant *what* but useful *why/where* → keep the why; drop the rest.
- Execution-flow / narrative blocks → hand off to **execution-flow-comments** if the user wants that style; otherwise replace with language-native docs + short why, or remove.
- Align with `1-clean-craftsmanship`: comments that only restate the code are a smell.

## Enforcement

- Detect the language (and project style) before choosing a comment form.
- Apply when writing, editing, or reviewing code comments.
- Prefer renaming and types over prose.
- Do not introduce a non-standard comment format when the language already has one.
