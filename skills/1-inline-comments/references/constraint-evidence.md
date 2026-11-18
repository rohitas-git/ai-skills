# Comments, constraints and enforcement

Read the containing code, actual contract and needed history before accepting or deleting a warning.
Classify narration, stale workaround, public contract, legal notice, tooling directive and a genuine
non-obvious constraint. Public API blocks belong to `/1-code-comments`; a broad multi-file pass needs
the caller's explicitly selected scope rather than expanding this one-block operation.

When a comment explains an awkward shape in our own code, propose a clearer name, type, ownership
or structure. A prose task does not authorize that refactor. Preserve a still-needed constraint until
an accepted implementation or other authoritative evidence makes it redundant. Ambiguity is not
permission to delete. Trace `do not remove` and similar warnings instead of treating them as proof.

Inspect a scoped suppression's actual rule and rationale. A faulty/style-only rule differs from a
correctness or safety warning, but neither conclusion alone grants removal authority. Preserve license,
generated/machine-significant comments, approved exceptions and public contracts. Confirm relevant
tool behavior before an authorized suppression change; never silence a new failure for appearance.

For an enforceable constraint, propose the cheapest fitting type, runtime guard, test or CI rule.
Run a known violation and a clean control if that implementation is authorized. Keep rationale that
still serves a reader. Do not claim the comment's deletion proves the underlying issue impossible.
Report retained/removed/proposed entries, evidence, enforcement limits and out-of-scope fixes.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
