# Deep-module vocabulary and heuristics

Use these terms where they improve precision; preserve established project and domain names.

- **Module:** a cohesive unit with one or more intentional caller-facing interfaces and a hidden implementation. It may be a function, type, package, subsystem, or vertical slice.
- **Interface:** everything a caller must know to use a module correctly: operations and types plus relevant invariants, ordering, failures, configuration, limits, and performance promises. A language `interface` is only one representation.
- **Implementation:** behavior hidden behind an interface.
- **Depth:** useful capability hidden per unit of caller-visible complexity. It is not a source-line ratio.
- **Seam:** a place where behavior or an implementation can vary without editing its callers.
- **Adapter:** an implementation that connects a module-facing contract to a concrete dependency or transport.
- **Leverage:** capability or policy reused by callers through the module.
- **Locality:** related knowledge, change, and verification concentrated under one owner.

## Heuristics, not verdicts

- Prefer a small, coherent interface when it still expresses the real use cases clearly.
- Hide implementation choices and repeated policy; expose constraints callers genuinely need.
- A pass-through can still be useful when it enforces policy, translates contracts, protects an ownership boundary, or isolates volatile infrastructure.
- Use the deletion test to reveal where complexity moves, not to decide automatically that a module should disappear.
- Treat the caller-visible interface as the primary behavioral test surface. Add focused internal tests when complex algorithms or invariants need faster, more diagnostic evidence.
- Dependency injection is useful at real seams but can be needless ceremony for stable local details. A seam may be justified by multiple implementations, ownership, volatility, security, process boundaries, or controllable tests.
- Side effects are sometimes the module's purpose. Make them explicit, bounded, and testable rather than forcing every operation to be pure.
- Measure locality through expected future changes and caller knowledge, not method counts alone.
