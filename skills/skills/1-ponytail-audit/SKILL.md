---
name: 1-ponytail-audit
description: >
  Whole-repo audit for over-engineering. Like ponytail-review, but scans the
  entire codebase instead of a diff: a ranked list of what to delete, simplify,
  or replace with stdlib/native equivalents. Use when the user says "audit this
  codebase", "audit for over-engineering", "what can I delete from this repo",
  "find bloat", "1-ponytail-audit", or "/1-ponytail-audit". One-shot report, does
  not apply fixes.
disable-model-invocation: true
---

ponytail-review, repo-wide. Scan the whole tree instead of a diff. Rank
findings biggest cut first.

## Tags

Same as ponytail-review:

- `delete:` dead code, unused flexibility, speculative feature. Replacement: nothing.
- `stdlib:` hand-rolled thing the standard library ships. Name the function.
- `native:` dependency or code doing what the platform already does. Name the feature.
- `yagni:` abstraction with one implementation, config nobody sets, layer with one caller.
- `shrink:` same logic, fewer lines. Show the shorter form.

## Scope

Skip: tests, migrations, generated code, vendored deps, and anything the user
marks out-of-scope. Audit only the production src tree unless told otherwise.

## Output

Ranked list, biggest cut first. Same one-liner format as ponytail-review:
`<file>:L<line>: <tag> <what>. <replacement>.`

End with: `net: -<N> lines possible across <M> findings.`

Nothing to cut → `Lean already. Ship.`

## Boundaries

Reads and reports only, changes nothing. One-shot.
"stop ponytail-audit" or "normal mode": revert.
