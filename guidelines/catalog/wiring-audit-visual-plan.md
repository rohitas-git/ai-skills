# Visual Plan wiring audit

Reviewed:

- `1-visual-plan`
- the complete imported BuilderIO `visual-plan` workflow used by the prior live body
- targeted Grilling metadata, workflow, HTML, and Butler-flow routes

## Result

Visual Plan now performs exactly one explicitly selected `draft`, `create`, or `update` operation for
one immutable source plan. It pins source-plan and repository/worktree/branch/`HEAD` versions, dirty
ownership, local-versus-hosted destination, sensitivity, visibility, review question, output, and
effect-specific authority. A visual artifact cannot silently change the checkout or plan version it
represents.

The smallest useful surface is required; text remains valid when no visual relationship improves
review. Draft mode has no write. Create mode writes one authorized private artifact. Update mode
requires a fresh revision, targeted change, concurrency fence where supported, and persisted readback.
Hosted visibility remains private/narrow by default.

The prior vendor defaults no longer govern the live skill. Selection does not authorize connector
installation/authentication, browser or server launch, hosted publication, public sharing, invitations,
feedback resolution/consumption, full replacement, subagents, export, source edits, or implementation.
Plan approval returns as evidence to the caller; it is not implementation permission.

## Verification

- Focused Grilling-child routing tests: 9 passed.
- Full routing suite: 478 passed.
- Generated route index: 218 live skills.
- Catalog lint: 0 critical, 0 warnings, 54 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No plan artifact, connector, server, browser, hosted/local write, share, export, feedback mutation,
subagent, implementation, Git action, or host sync occurred.
