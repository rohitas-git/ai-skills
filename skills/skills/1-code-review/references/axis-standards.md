# Axis: Standards

Does the diff conform to this repo's documented coding standards?

## When this axis is applicable

Runnable when **any** standards signal exists:

- `CODING_STANDARDS.md`, `CONTRIBUTING.md`, `.editorconfig` guidance docs
- Project `1-coding-standards` skill expectations if the catalog skill is the house bar
- `CONTEXT.md` / ADRs that constrain how code is written (not domain glossary alone)

If none: still run the **smell baseline** below as soft judgement calls, or soft-skip entirely if the scan finds zero signals *and* user prefers skip — default for implement: run baseline smells even without docs.

## Repo overrides

A documented repo standard always wins over the smell baseline.

## Smell baseline (Fowler, _Refactoring_ ch.3)

Always judgement calls unless the repo hard-bans them. Skip anything tooling already enforces.

- **Mysterious Name** — rename; if no honest name, design is murky
- **Duplicated Code** — extract shared shape
- **Feature Envy** — move method onto the data it envies
- **Data Clumps** — bundle into a type
- **Primitive Obsession** — give the concept a small type
- **Repeated Switches** — polymorphism or shared map
- **Shotgun Surgery** — gather what changes together
- **Divergent Change** — split module by reason to change
- **Speculative Generality** — delete unused abstraction
- **Message Chains** — hide walk behind one method
- **Middle Man** — cut pure delegation
- **Refused Bequest** — prefer composition

## Sub-agent brief

Given the diff, standards-source list, and smell baseline, report under 400 words:

- (a) documented-standard violations (cite file + rule) — may be hard
- (b) baseline smells (name + hunk) — judgement only
- Distinguish hard vs judgement; repo docs override baseline
