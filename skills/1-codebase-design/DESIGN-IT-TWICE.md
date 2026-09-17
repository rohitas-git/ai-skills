# Design It Twice

When the user wants to explore alternative interfaces for a chosen candidate, compare at least
two materially different designs. Generate them in the current agent by default. Use parallel
sub-agents only when the user explicitly requests delegation and the alternatives can be explored
independently without shared writes.

Uses the vocabulary in [SKILL.md](SKILL.md) — **module**, **interface**, **seam**, **adapter**, **leverage**.

## Process

### 1. Frame the problem space

Before spawning sub-agents, write a user-facing explanation of the problem space for the chosen candidate:

- The constraints any new interface would need to satisfy
- The dependencies it would rely on, and which category they fall into (see [DEEPENING.md](DEEPENING.md))
- A rough illustrative code sketch to ground the constraints — not a proposal, just a way to make the constraints concrete

Use the frame as the common evidence boundary for every alternative.

### 2. Generate alternatives

Produce two or three meaningfully different interfaces. More options are not automatically better;
stop when another design would not expose a new trade-off. If the user explicitly authorized
sub-agents, assign one read-only design brief per independent alternative and keep all code edits
with the owning caller/worktree.

Use the same evidence and a different design constraint for each alternative:

- Minimize caller-visible concepts while covering required use cases.
- Optimize the common caller path without hiding important failure or effect semantics.
- Preserve likely variation or ownership boundaries with the least justified extension surface.
- When applicable, isolate a remote or privileged dependency without inventing a generic port.

Use [SKILL.md](./SKILL.md) vocabulary only where helpful and preserve the project's domain language.

Each alternative includes:

1. Interface (types, methods, params — plus invariants, ordering, error modes)
2. Usage example showing how callers use it
3. What the implementation hides behind the seam
4. Dependency strategy and adapters (see [DEEPENING.md](DEEPENING.md))
5. Trade-offs — where leverage is high, where it's thin

### 3. Present and compare

Present designs sequentially so the user can absorb each one, then compare them in prose. Contrast by **depth** (leverage at the interface), **locality** (where change concentrates), and **seam placement**.

After comparing, give your own recommendation: which design you think is strongest and why. If elements from different designs would combine well, propose a hybrid. Be opinionated — the user wants a strong read, not a menu.
