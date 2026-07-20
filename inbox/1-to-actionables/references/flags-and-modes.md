# Flags and modes

## Parsing

Accept flags in any of these shapes (case-insensitive values):

```text
--mode actionables
--mode=pseudocode
mode: actionables
```

```text
--scope ticket
--scope=set
scope: set
```

Natural language maps:

| User says | Parse as |
|-----------|----------|
| "file-level", "checklist", "steps", "actionables" | `--mode actionables` |
| "pseudocode", "walkthrough", "narrative plan" | `--mode pseudocode` |
| "this ticket", "one ticket", a single path/URL | `--scope ticket` |
| "all tickets", "the whole set", "every issue" | `--scope set` |

If both a flag and natural language appear and conflict, **flags win**. If still ambiguous after one parse pass, ask once with the four discrete choices (two modes × two scopes), then proceed.

## Defaults

| Flag | Default | When to override |
|------|---------|------------------|
| `--mode` | `actionables` | User wants design understanding before typing → `pseudocode` |
| `--scope` | `ticket` | User finished `/1-to-tickets` and wants plans for the batch → `set` |

## Mode comparison

| | `actionables` | `pseudocode` |
|--|---------------|--------------|
| Best for | Sitting down to type immediately | Understanding flow before typing |
| Unit of work | Numbered step (file + find + change) | Narrative unit (behaviour + pseudocode) |
| Code detail | Short sketches (≤15 lines), optional | Function-level pseudocode, optional real signatures |
| File paths | On every step | On each unit’s touch list + when critical mid-prose |
| Risk | Over-prescriptive if tree moves | Under-specific for junior coders |

You may regenerate the same ticket in the other mode later; write a **new** file with the other `--mode` suffix rather than overwriting unless the user asks to replace.

## Scope comparison

| | `ticket` | `set` |
|--|----------|-------|
| Input | One ticket path/URL/number/body | Feature issues dir or parent + children |
| Output | One actionables file | One file per ticket |
| Depth | Full deep-dive | Full deep-dive per ticket; mark blocked tickets with “do not start until …” |
| Chat summary | Focused | Index table (ticket → file path → blocked-by) + open the frontier first |

## Invocation examples

```text
/1-to-actionables --mode actionables --scope ticket .scratch/checkout-retry/issues/03-retry-banner.md
```

```text
/1-to-actionables --mode pseudocode --scope ticket 1842
```

```text
/1-to-actionables --mode actionables --scope set .scratch/checkout-retry/issues/
```

```text
Break ticket 03 into file-level coding steps I can do myself
→ --mode actionables --scope ticket
```

```text
Pseudocode walkthrough for all tickets under this feature
→ --mode pseudocode --scope set
```

## Missing inputs

| Situation | Action |
|-----------|--------|
| No ticket and `--scope ticket` | Ask for path/URL/number |
| Empty issues dir and `--scope set` | Ask for feature slug or parent issue |
| Spec missing | Proceed from ticket alone; note “no parent spec loaded” |
| Codebase unexplored | Always explore before writing paths |
