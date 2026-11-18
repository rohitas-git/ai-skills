# Behavior oracles that can fail

Start from a requirement, accepted contract or independently established bug example. Drive the
public interface with concrete inputs and assert observable values, caller-visible errors or real
effects at an existing external boundary. A mock recording an internal helper call is not the user's
outcome. A fake external receiver can be valid evidence for what the application sends to it.

Ask two questions: would this test fail if the user-visible behavior were broken, and would it survive
a harmless internal restructure? Wrong literal outputs, omitted/doubled effects and a reordered unsafe
operation are useful counterexamples. An expected value computed with the same implementation or an
assertion on data the test itself built can keep passing through a defect.

Pair never-happens claims with a case where that outcome does happen. Assert the stable error type
or structured field callers use; pin message wording only when it is the accepted interface. Retain
focused internal algorithm/invariant tests when they provide distinct useful evidence rather than
deleting every internal test by rule.

When a mutation/negative control is needed, use an authorized disposable fixture or repository-native
runner and restore only owned changes. Never alter user-owned production code, install a runner or
manufacture a red state merely to demonstrate discipline. Preserve meaningful red-before/green-after
evidence and distinguish a behavioral failure from a broken harness. Test-first requires a settled
deterministic seam; a prototype or probabilistic evaluation uses its own evidence contract.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
