# Deepening

How to deepen a cluster of shallow modules safely, given its dependencies. Assumes the vocabulary in [SKILL.md](SKILL.md) — **module**, **interface**, **seam**, **adapter**.

## Dependency categories

When assessing a candidate for deepening, classify its dependencies. The category determines how the deepened module is tested across its seam.

### 1. In-process

Pure computation, in-memory state, no I/O. It may be safe to combine when responsibilities,
ownership, and change patterns are cohesive. No adapter is needed merely because tests exist.

### 2. Local-substitutable

Dependencies that have representative local test stand-ins (for example an embedded database
or temporary filesystem). A stand-in improves verification but does not itself justify merging.
Check semantic parity and retain real integration coverage where the stand-in differs.

### 3. Remote but owned (Ports & Adapters)

Your own services across a network boundary (microservices, internal APIs). A **port** and
transport **adapter** can isolate policy from HTTP/gRPC/queue details when that separation is
useful. Unit tests may use a controlled adapter, but contract and integration tests still verify
serialization, timeouts, compatibility, authentication, and real transport behavior.

Recommendation shape: *"Define the owned contract at the seam, implement the production
transport adapter, and use the smallest representative test double plus contract/integration
coverage so policy remains local without pretending the network is in-memory."*

### 4. True external (Mock)

Third-party services you do not control. Isolate their contract where volatility, ownership, or
testing needs justify it. Use recorded/sandbox/provider contract tests where authorized, and use
fakes or mocks only for behaviors they can faithfully establish.

## Seam discipline

- **Evidence justifies a seam.** Multiple implementations are strong evidence, but ownership,
  volatility, privilege, process boundaries, or controllable failure tests may justify a seam even
  with one current production adapter. Avoid indirection without a concrete benefit.
- **Internal seams vs external seams.** A deep module can have internal seams (private to its implementation, used by its own tests) as well as the external seam at its interface. Don't expose internal seams through the interface just because tests use them.

## Testing strategy: replace, don't layer

- Inventory the behavior each old test protects. Remove a test only after replacement evidence
  covers the same useful contract and the old test adds no distinct diagnostic or invariant value.
- Write new tests at the deepened module's interface. The **interface is the test surface**.
- Tests assert on observable outcomes through the interface, not internal state.
- Behavioral tests should usually survive internal refactors. Focused internal tests may change
  with an algorithm or invariant; keep them when their diagnostic speed or precision is valuable.
