# Qualify and maintain a formal check

Choose a property where the accepted harm and code mechanism justify verification cost, rather than
the easiest model to make green. Let the question choose state exploration, a code-level verifier or
a proof. Generated/property-based tests are valuable when no verifier fits, but do not rename them
formal proof. Keep source symbols, atomic actions, bounds, fairness and excluded behavior explicit.

A requested project-local verification skill is authored by `/0-skill-creator`, with coverage, real
commands, version/prerequisites, last evidenced correspondence and interpretation rules. It remains a
draft until authorized execution and a known violation show it can detect the claimed error. A real
baseline defect can remain a finding; do not manufacture a passing baseline by weakening a property.

On maintenance, preserve the old result before changing correspondence when a run is authorized.
Inspect changes to covered code from the last evidenced sync, including moves, splits and new writers
of guarded state. A last-edited commit is only a fallback investigation clue if sync evidence is absent.
Classify no semantic effect, model/harness drift, accepted promise change or possible product defect.

Model changes come from the current code and accepted contract, not the desired verdict. A changed
test/comment/commit message alone cannot authorize weakening the promise. Record old/new wording,
decision evidence, changed bounds and costs. Authoring a new state model returns to its owner.

After an authorized update, recheck source correspondence, a seeded violation and clean control in
disposable fixtures. Replay a counterexample only when permitted; an impossible step is a modeling
gap, not a proven product defect. A check can be both drift-reconciled and property-violated. A pass
on the old stale description does not validate current code. Never advance sync for a blocked check.

Report per-property correspondence and verdict separately, tool/config identities, bounds, actual
commands, known limitations and human-readable failing steps. Keep verification changes separate
from product fixes and use the caller's actual Git/publication authority.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
