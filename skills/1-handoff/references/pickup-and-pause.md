# Pickup and explicit pause

## Pickup one task

Read the named existing capsule/trail or canonical project task record first. For the default
`.scratch/<task>/continuation.json`, follow the [project lifecycle](../../0-implement/references/project-continuity.md)
and inspect declared workspace drift before choosing the resume point. Start with metadata and recent
state, then the decision
points relevant to the next action. Treat the old transcript as evidence, never fresh authority. Keep
reads within the authorized workspace/thread; do not scan all project histories.

Reconstruct repository/worktree/branch/HEAD, local dirty ownership, landed/published work, open todos,
in-flight operations, services and accepted decisions. Compare done with pending and name one resume
point. Preserve useful prior reasoning and evidence instead of automatically repeating a full repro.
Revalidate exact identity and any claim whose candidate/environment changed or whose receipts are
missing. An old self-report is not proof, and patch-id alone does not establish current runtime state.

The handoff operation returns this resume point/capsule. Continuing the substantive task belongs to
the authorized caller, not an automatic consequence of reading a note. A cross-thread working brief
belongs to `/1-working-context`; same-chat status belongs to `/1-session-catchup`.

## Explicit pause

Pause only when the user requests it; an unattended keep-going request is not a pause. Stop starting
new work and reach an owned safe checkpoint. Account for delegated writers/processes within actual
control authority; do not abandon a mutable operation mid-step or conceal unreported output.

Preserve current files and original user changes. A pause does not require a WIP commit, stash, push,
PR, reset or cleanup. Those effects need the caller's existing authorization and repository rules.
If durability is requested, write a new non-overwriting handoff at the explicit or known project-task
path, using an approved temporary path only when project identity is unavailable. The active execution
owner separately refreshes its canonical checkpoint only within its existing artifact/edit authority. Record unsafe/incomplete state and the first resume action honestly.

Point to the canonical log/spec rather than duplicating it. Include what is durable on disk, what is
verified, what remains in flight or unknown, the actual authority boundary and retained state. Report
a pause as a pause; never mark the underlying objective complete to end the interaction.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
