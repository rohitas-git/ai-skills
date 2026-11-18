# TypeScript patterns and limits

## Represent legal states

Use one discriminator for exclusive cases, such as pending, success-with-value and failure-with-error.
Do not force an optional-field bag to encode mutual exclusion. An exhaustive switch can assign the
remaining value to `never`, so a new variant requires a deliberate handler.

Keep total operations total: a sum can accept an empty array. A function selecting the first item can
return an optional result or require `readonly [T, ...T[]]`. With strict indexed-access checking,
an arbitrary numeric index can still be undefined even on a nonempty tuple. `items[0]` and
`items[Math.floor(Math.random() * items.length)]` do not receive identical compiler guarantees.

## Parse once at the real boundary

Reuse the project's schema system and inference helpers. A hand-written predicate must validate every
field and constraint its claimed type requires; TypeScript trusts `value is User` even when its body
only checks that `id` exists. Test guards with wrong types, missing fields and invalid values.

Parsing establishes only what was checked at that point. It does not establish future authorization,
freshness, database integrity or the state of a shared mutable object. Retain checks at those boundaries.
Unknown-field handling is a protocol decision: accepting unknown keys may aid compatibility, but
security-sensitive commands may require rejection. Never set a universal ignore-unknown policy.

## Brands and numeric ranges

Use existing brand conventions. Brand semantic primitives where mixing otherwise-valid values causes
a real error. Validate format and ownership/meaning at the actual creation boundary; two UUID-shaped
strings can still refer to different domains. Avoid a cast that skips that check.

A representation with `start` and `durationMs: number` **still permits a negative duration**. A brand
does not make that value safe unless a controlled constructor rejects negative and nonfinite input.
The executable example in `../examples/contracts.ts` demonstrates checked construction and public
observation. It is a fixture, not a new dependency to import into applications.

## Narrowing and assertions

Prefer discriminant narrowing, `in`, `typeof` or `instanceof` as appropriate. `satisfies` validates
assignability without replacing the inferred expression type, but contextual typing can affect literal
inference. Use `as const` deliberately for readonly literal data when that matches the intended API.
Neither construct validates incoming runtime data.

An assertion may be justified for an established invariant the compiler cannot express or a foreign
library boundary. Keep it local, document the evidence when non-obvious, and test the boundary. Do
not replace one assertion with a lying guard. Use schema-derived `Pick`, `Omit`, `Parameters`,
`ReturnType`, `Awaited` or `typeof` where they express the real source of truth; do not contort a type
merely to avoid a clear domain declaration. Object arguments help avoid positional mixups, while
allocation-sensitive paths should follow measurements and the repository's established API.

Use existing structured diagnostics in applications. A CLI's specified stdout/stderr output is part
of its public contract; a blanket ban on console output would break that contract.

Adapted from pstack's TypeScript and type-system/boundary principles, MIT. Corrected the source's
unchecked numeric-range, predicate-trust and inference claims. [Review](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
