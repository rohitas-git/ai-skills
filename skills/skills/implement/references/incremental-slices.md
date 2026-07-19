# Incremental implementation (merged from vendor)

Source: archive vendor `incremental-implementation`.

## Slice before you code

For multi-file work, cut **vertical slices** that each leave the system green:

1. **Risk-first** — hardest unknown or integration first when it unblocks the rest.
2. **Contract-first** — types/API seams before deep implementation when many callers depend on them.
3. **Tracer bullet** — one thin path through UI→API→storage beats horizontal "all models then all UI."

## Per-slice checklist

- [ ] Slice has a user-visible or testable outcome
- [ ] Tests via `/tdd` at agreed seams
- [ ] Typecheck / targeted tests green before next slice
- [ ] No drive-by refactors outside slice (ponytail/review later)

## Scope discipline

If the slice grows past one clear outcome, stop and re-slice. Prefer small PRs over mega-diffs (`/code-review` sizing).
