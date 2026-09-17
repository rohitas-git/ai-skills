# Legacy spec-review prompt provenance

This imported prompt is not operative for `/1-brainstorm`. Brainstorm returns one design-options memo
and does not automatically write a spec or dispatch a reviewer.

If the user separately requests a durable specification, route the accepted thread to `/1-to-spec`.
If they request review of that artifact, use the applicable review workflow with explicit candidate,
worktree, scope, and delegation authority. Never infer permission to create a subagent from this file.

The useful retained criteria are: material completeness, internal consistency, implementation-changing
ambiguity, bounded scope, and unrequested complexity. Minor wording preferences are not blockers.
