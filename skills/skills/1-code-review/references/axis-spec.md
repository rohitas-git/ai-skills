# Axis: Spec

Does the diff faithfully implement the originating issue / PRD / spec?

## When this axis is applicable

Runnable when a **spec source** exists (scan order):

1. Issue references in commit messages (`#123`, `Closes #45`, etc.) — fetch via `docs/agents/issue-tracker.md` (run `/0-setup-rohitas-skills` if missing)
2. Path the user passed
3. PRD/spec under `docs/`, `specs/`, or `.scratch/` matching branch/feature
4. Ticket/spec text already in the conversation (e.g. implement was fed a ticket)

If none: **soft-skip** and report `Spec: skipped — no spec source`.

## Sub-agent brief

Given the diff command, commit list, and spec contents, report under 400 words:

- (a) requirements asked for that are missing or partial (quote spec)
- (b) behaviour in the diff that wasn't asked for (scope creep)
- (c) requirements that look implemented but wrong (quote spec)

Do not judge coding style or maintainability here.
