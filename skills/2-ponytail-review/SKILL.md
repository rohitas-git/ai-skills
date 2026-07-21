---
name: 2-ponytail-review
description: >
  Review focused only on over-engineering — what to delete. Use when asked for simplify
  review, over-engineering review, or /2-ponytail-review. Not for: full multi-axis review (1-code-review)
  or ponytail while coding (0-ponytail). Hub: /1-code-review. Triggers: over-engineering, what can we delete, simplify review.
disable-model-invocation: true
metadata:
  catalog:
    hub: 1-code-review
    role: cousin
    when:
      - "over-engineering-only review"
      - "find what to delete"
    not_when:
      - "full Spec/Standards review → 1-code-review"
      - "write lazy code → 0-ponytail"
    cousins: [1-code-review, 0-ponytail]
    triggers:
      - "over-engineering"
      - "what can we delete"
      - "simplify review"
      - "2-ponytail-review"
    requires_setup: false
---
## Process

1. Follow this skill's procedure.


Review diffs for unnecessary complexity. One line per finding: location, what
to cut, what replaces it. The diff's best outcome is getting shorter.

Before delete-without-reason: [references/chesterton-and-patterns.md](./references/chesterton-and-patterns.md). Full vendor simplification body: [references/vendor-simplification-full.md](./references/vendor-simplification-full.md).

## Format

`L<line>: <tag> <what>. <replacement>.`, or `<file>:L<line>: ...` for
multi-file diffs.

Tags:

- `delete:` dead code, unused flexibility, speculative feature. Replacement: nothing.
- `stdlib:` hand-rolled thing the standard library ships. Name the function.
- `native:` dependency or code doing what the platform already does. Name the feature.
- `yagni:` abstraction with one implementation, config nobody sets, layer with one caller.
- `shrink:` same logic, fewer lines. Show the shorter form.

## Examples

❌ "This EmailValidator class might be more complex than necessary, have you
considered whether all these validation rules are needed at this stage?"

✅ `L12-38: stdlib: 27-line validator class. "@" in email, 1 line, real validation is the confirmation mail.`

✅ `L4: native: moment.js imported for one format call. Intl.DateTimeFormat, 0 deps.`

✅ `repo.py:L88: yagni: AbstractRepository with one implementation. Inline it until a second one exists.`

✅ `L52-71: delete: retry wrapper around an idempotent local call. Nothing replaces it.`

✅ `L30-44: shrink: manual loop builds dict. dict(zip(keys, values)), 1 line.`

## Scoring

End with the only metric that matters: `net: -<N> lines possible.`

If there is nothing to cut, say `Lean already. Ship.` and stop.

## Boundaries

Scope: over-engineering and complexity only. Correctness bugs, security holes,
and performance are explicitly out of scope. Route them to a normal 0-review
pass, not this one. A single smoke test or `assert`-based
self-check is the 0-ponytail minimum, not bloat, never flag it for deletion.
Does not apply the fixes, only lists them.
"stop ponytail-review" or "normal mode": revert to verbose 0-review style.

## Don't use when

- Full multi-axis 0-review (Spec/Standards/Maintainability) → `/1-code-review`
- Mid-build self-verify → `/2-verify-work`
