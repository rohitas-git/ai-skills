---
name: 1-stepdown-rule
description: >
  Enforce top-down file layout using the newspaper metaphor and stepdown rule
  (callers above callees, high abstraction first, low-level helpers last).
  Language-aware for JS/TS, Python, Go, Rust, Java/Kotlin, C/C++, C#, Swift,
  Shell, and SQL. Use when writing, reorganizing, or reviewing source file
  structure, function order, module layout, or when the user mentions stepdown,
  newspaper layout, call hierarchy order, or /1-stepdown-rule.
disable-model-invocation: true
---

# Stepdown Rule (Newspaper Metaphor)

Source files must read like a **top-down newspaper story**: headline and lead first, details later. Abstraction descends as you scroll.

## Universal order (all languages)

Within a single source file, prefer this vertical order:

| Zone | What goes here | Abstraction |
|------|----------------|-------------|
| **1. Imports / includes / package** | Dependencies, `use` / `import` / `require`, feature flags from env | Module edge |
| **2. Module config & constants** | Shared types/interfaces, enums, constants, registries, module-scope caches | Shared vocabulary |
| **3. Public surface (Level 1)** | Exported entry points, constructors, orchestrators, handlers callers hit first | High — what this file does |
| **4. Mid-level coordinators (Level 2)** | Private helpers that arrange steps, load config, compose lower helpers | Medium — how the story unfolds |
| **5. Low-level details (Level 3)** | Parsers, validators, coercers, pure utilities, DB/query primitives, formatters | Low — how the machinery works |

**Call hierarchy order (stepdown):** If `A` calls `B`, place `A` **above** `B` so a top-to-bottom reader meets the call before the definition. Apply within a type's methods when the language and team style allow reordering (see language notes).

**Related concepts cluster:** Keep tightly related helpers adjacent; do not scatter one feature's detail functions across the file.

**One abstraction level per function:** A high-level orchestrator should mostly call named mid-level steps — not mix orchestration with deep parsing/IO in the same body.

## Language notes

Same newspaper shape; adapt to how the language declares and binds symbols.

| Language | Layout notes | Call-order / declaration constraint |
|----------|--------------|-------------------------------------|
| **JavaScript** | Imports → constants/config → exported orchestrators → private helpers | Prefer **`function name() {}`** (hoisted) for same-file helpers so callers can sit above callees. Avoid module-scope `const fn = () => {}` for those helpers (TDZ breaks stepdown order). Arrows OK for inline callbacks. |
| **TypeScript** | Same as JS; shared types in zone 2 (or co-located if file-private) | Same as JS. Prefer types in the type system; exported types with the public surface. |
| **Python** | Imports → constants → public API → private `_helpers` | Module `def`s resolve at **call** time, so public functions may sit above helpers they call. Do not call helpers at **import** time before definition. Scripts: keep `if __name__ == "__main__"` at the bottom. |
| **Go** | `package` → imports → const/var → exported API → unexported helpers | No hoisting issues. Prefer **type-centric clusters** (methods next to their type); primary method first within a type. |
| **Rust** | `use` → const/static → `pub` items → private `fn` | Public API first; private helpers below. In `impl` blocks, primary API methods first. |
| **Java / Kotlin** | package/imports → type → fields → public methods → private methods | Public methods above private; primary entry methods first in the public group. |
| **C / C++** | Includes → macros/constants → public API → `static` helpers | In `.c`/`.cc`, public functions first, file-local `static` helpers last. Headers: public API only. |
| **C#** | usings → namespace → type → fields/properties → public methods → private methods | Public API first; private methods below. Do not invent `#region` noise unless the team already uses it. |
| **Swift** | imports → types → public API → private helpers | Public API first; `private` / `fileprivate` helpers lower in the type. |
| **Shell** | shebang → `set`/config → helpers (high→low) → thin `main` → invoke `main` | Bash has no hoisting: **define helpers before** the top-level call. Order helpers by descending abstraction; end with a short `main` invocation. |
| **SQL** | Named CTEs in intent order → final `SELECT` | Top-down narrative via `WITH` steps; push details into later CTEs or subqueries. |

## JavaScript / TypeScript (implementation constraint)

For same-module helpers that appear **below** their callers (newspaper order):

```js
// Level 1 — public orchestration (top)
export function getRuntimeOps(env) {
  const config = loadRuntimeConfig(env);
  return buildOps(config);
}

// Level 2 — mid-level
function loadRuntimeConfig(env) {
  return validateAndCoerceKnob(env.KNOB);
}

// Level 3 — detail (bottom)
function validateAndCoerceKnob(raw) {
  /* ... */
}
```

- Use **`function name() {}`** for these helpers (hoisted), not `const name = () => {}` at module scope, so call-before-define in source order stays safe.
- Arrow functions are fine for **inline** callbacks (`map`, short lambdas) and for values that must close over locals.
- In TypeScript, same rule; put shared types in zone 2 or co-locate file-private types with their only consumer.

## Python (module load semantics)

Module-level `def` bodies run at **call** time, so this stepdown order is valid:

```python
def get_runtime_ops(env: Mapping[str, str]) -> RuntimeOps:
    config = load_runtime_config(env)
    return build_ops(config)

def load_runtime_config(env: Mapping[str, str]) -> RuntimeConfig:
    return validate_and_coerce_knob(env.get("KNOB"))

def validate_and_coerce_knob(raw: str | None) -> Knob:
    ...
```

Keep public functions first; `_private` helpers last. Avoid calling helpers at **import** time before they are defined.

## Go (type-centric newspaper)

```go
// Public API first
func GetRuntimeOps(env Env) (Ops, error) { /* ... */ }

// Unexported helpers below
func loadRuntimeConfig(env Env) (Config, error) { /* ... */ }

func validateAndCoerceKnob(raw string) (Knob, error) { /* ... */ }
```

Prefer grouping methods with their type; within the file, exported entry points before unexported helpers.

## When to bend the rule

- **Language idioms win** when they conflict (e.g. Go method sets, Python `if __name__ == "__main__"`, React component file with component first then local helpers).
- **Generated code** — do not reformat generated files.
- **Very small files** (< ~40 lines) — strict zoning is optional if the story is already obvious.
- **Legacy files** — apply stepdown to **new** code and regions you touch (Boy Scout Rule); do not force a whole-file reshuffle unless asked.
- **Circular conceptual needs** — split into another module instead of breaking readability with forward-reference soup.

## Enforcement

- Apply when writing or reorganizing code in a file.
- On review, flag files where low-level helpers sit above public orchestrators without a language reason.
- Prefer extracting a module over inventing awkward forward references.
