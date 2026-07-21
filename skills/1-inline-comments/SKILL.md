---
name: 1-inline-comments
description: >
  Add concise one-line comments immediately above non-obvious code blocks or slightly
  complex snippets inside function bodies. Use when annotating implementation blocks,
  dense conditionals, multi-step pipelines, or non-obvious branches. Do not use for
  public API docs, JSDoc, docstrings, GoDoc, or language-native surface documentation
  (use 1-code-comments for those). Do not write execution-flow or step-by-step
  walkthrough comments (use 1-execution-flow-comments for those). Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "annotating implementation blocks, dense conditionals, multi-step pipelines, or non-obvious branches"
    triggers:
      - "1-inline-comments"
      - "inline comments"
    requires_setup: false
---

# Inline Comments

## Process

1. Follow the steps and hard rules in this skill.
2. Load linked `references/` only when the branch needs them.


Place **short line comments above code blocks**, not API docs. Scope is *inside* implementations: a branch, a few dense lines, a pipeline step.

**Boundary**

| Need | Skill |
|------|--------|
| JSDoc / docstrings / public contracts | **code-comments** |
| One-line notes above internal blocks | **inline-comments** (this skill) |
| Numbered steps + `└─` Execution Flow trees | **execution-flow-comments** |

## Rules

1. **One line, above the block** — Prefer a single `//` / `#` / `--` line immediately above the non-obvious block. Rarely two lines; never a narrative paragraph.
2. **Only where the code is slightly hard** — Dense logic, non-obvious order, a trap, a required side effect, or a multi-step chunk that isn’t self-explanatory from names alone.
3. **Why or constraint, not restatement** — Capture intent, invariant, or “why this order,” not “loop over items.”
4. **Do not comment every line** — Skip obvious assignments, returns, and self-explanatory calls.
5. **No execution-flow here** — Numbered steps / `└─` trees → **execution-flow-comments**.
6. **No API surface docs here** — Don’t put `@param` / docstrings / GoDoc on public symbols in this skill; defer to `1-code-comments`.

## When to add

| Place a line above… | Example intent |
|---------------------|----------------|
| Multi-step block in a body | “Normalize then validate before write” |
| Non-obvious branch | “Legacy clients omit currency; default to USD” |
| Order-sensitive sequence | “Flush buffer before closing the stream” |
| Subtle gotcha | “Must use same idempotency key as create” |
| Dense one-liner cluster | “Collapse retries into a single user-facing error” |

## When to skip

- The next line is obvious from names/types
- You’re documenting a public function contract → **`1-code-comments`**
- You’re tempted to narrate the whole function → rename/extract instead
- The comment would only repeat the code

## Format

Match the file’s line-comment syntax:

- JS/TS/Java/C/C++/Go/Rust: `// …`
- Python/Shell: `# …`
- SQL: `-- …`

Place it **tightly above** the block it describes (no blank-line gap if project style allows; otherwise one blank max).

```js
// Stripe requires the same key as hold create; double-capture is not recoverable.
return stripe.charges.create({ amount }, { idempotencyKey: holdId });
```

```js
// Reconcile optimistic rows with server rows before painting the list.
const merged = mergeById(localDrafts, serverRows);
const visible = merged.filter((row) => !row.archived);
```

```python
# Provider rejects empty tags; strip before the API call.
payload["tags"] = [t.strip() for t in tags if t and t.strip()]
```

## Quality bar

- **Concise** — roughly ≤ one short sentence
- **Stable** — won’t lie if a local variable is renamed
- **Local** — describes this block only, not the whole module
- **Prefer rename/extract** when a comment would only paper over messy structure

## Do not

- JSDoc / docstring / GoDoc / XML doc on symbols (→ `1-code-comments`)
- Comment every statement
- “// increment i”, “// return result”, “// call helper”
- Execution-flow or Purpose/Args/Returns/Flow blocks (→ **execution-flow-comments**)
