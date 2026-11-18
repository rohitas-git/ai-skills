# Data shape before branching

Trace producers, consumers, access patterns and effects before choosing a shape. Name the domain
states and the one owner of each mutable fact. A state machine can replace booleans that must remain
in sync; a tagged union can separate variants; a table/registry can concentrate repeated policy; a
queue or index can match an actual access pattern. Keep clear local branching when a new structure
would add more indirection than it removes.

For a consequential uncertain seam, sketch meaningfully different types, signatures and caller usage
before choosing one. Start from the same small caller example for each candidate. Include the normal
path and one representative failure or retry so the example exposes decisions the caller must own.
Compare what each caller must know, which state can change and where, and what
compatibility it preserves. Use `/1-competing-solutions` when selecting/synthesizing multiple complete
artifacts is the requested job; two local sketches need no automatic delegation or tool installation.

Ask what you would build if the new requirement were present initially, then deliver the justified
change incrementally. Repeated workarounds are evidence to revisit ownership; they do not authorize
a whole-system rewrite. Trace changed names through code, serialization, examples, docs and consumers.

Parse untrusted input at its real boundary and keep framework/transport types from leaking into a
domain interface without purpose. A validated value may later become stale or mutable; retain checks
at authorization, persistence, concurrency and other genuine boundaries. Pure calculations are useful
where they reduce effects, but an operation whose purpose is I/O need not acquire a pass-through shell.

Use types to reject invalid combinations and semantically mixed primitives when the compiler can
express that property. Verify guards and constructors at runtime; a predicate annotation can lie.
For TypeScript details use `/1-typescript-best-practices`. Prefer one authoritative schema to three
hand-maintained copies. Preserve required dynamic checks and compatibility rather than trusting a
type assertion as evidence.

Treat the consuming engineer and future maintainer as users. Explain which tasks become easier and
which implementation details they no longer need to know. An interface earns its place by hiding
necessary complexity, not by satisfying a method-count or one-implementation rule.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
