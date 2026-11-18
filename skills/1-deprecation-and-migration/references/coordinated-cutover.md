# Coordinated internal cutover

First establish who can consume the old API. A closed internal API with all callers owned and a
coordinated release can move callers and remove the old path in one authorized wave. An external,
offline or independently deployed consumer may require compatibility and observation phases.
Do not copy a universal no-shims rule across that distinction.

Pin the observable contract and target shape. Inventory call sites plus string references, serialized
forms, examples and documentation. Move all in-scope callers, update contract tests for an accepted
change, and remove obsolete implementation-detail tests only with coverage evidence and edit authority.
Keep tests that protect real behavior even when the implementation is being retired.

Avoid temporary compatibility machinery without a consumer or rollout reason. For an explicitly
planned disposable-branch phase, record where temporary breakage is acceptable and when the next
verifiable checkpoint must be reached. Never extend that permission to production, shared services,
published interfaces or unrelated work. Keep the final static/runtime checks and rollback obligations.

At each boundary prove the migrated behavior and consumer inventory. Removal still follows the
caller's exact scope and repository deletion policy. A plan, empty search or green typecheck does not
independently authorize deleting the legacy path or prove that no consumer remains.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
