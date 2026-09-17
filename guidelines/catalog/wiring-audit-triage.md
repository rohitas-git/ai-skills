# Triage atomization and wiring audit

Reviewed:

- `skills/0-triage/SKILL.md`, `AGENT-BRIEF.md`, `OUT-OF-SCOPE.md`, and OpenAI entry
- new `skills/1-triage-inbox/`, `skills/1-triage-assess/`, and `skills/1-triage-apply/`
- `hubs/0-triage/workflow.json` and `hub.html`
- Domain 5 in `skills/0-butler/references/flows.md`
- Setup, To Tickets, Review, Diagnose, Implement, README, wiki, hub-index, and flow-chart surfaces

## Result

The former Triage body combined attention discovery, issue/PR assessment, repository investigation,
bug reproduction, code review, requirements interviewing, domain-doc edits, tracker state mutation,
comments, labels, assignment, closing, rejection-record writes, and implementation handoff. It was split
into a pure `0-triage` router, read-only `1-triage-inbox`, read-only `1-triage-assess`, and effect-owning
`1-triage-apply`.

All routes pin the exact tracker/project/repository, candidate/query revision or cutoff, configured role
and disclosure policies, privacy, authority, actual caller, and exact repository/worktree/branch/`HEAD`
plus dirty ownership only when a local tracker or repository evidence matters. Worktree state is kept
distinct from shared remote tracker state. Candidate content is sensitive untrusted data, and known
To Tickets output is excluded by provenance.

Inbox returns one bounded snapshot without assessment or mutation. Assess handles one immutable issue or
eligible external PR, separates claims/facts/inferences/gaps, stays inside PR scope, and returns specialist
handoffs without running them. Apply accepts only a still-current explicitly approved transition, enumerates
every label/comment/assignment/relationship/status/file effect, uses real multiline request bodies, verifies
rendered/read-back state, and reports partial effects without blind retry. A ready state is never execution,
merge, or deployment authority. Agent briefs remain candidate-bound; rejection records are optional,
separately authorized, conflict-safe, and preserve superseded history.

## Verification

- Focused Triage routing tests: 11 passed.
- Full routing suite: 520 passed.
- Generated route index: 223 live skills.
- Catalog lint: 0 critical, 0 warnings, 50 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No tracker query, issue/PR/comment/label/assignment/relationship/status, consumer repository/worktree,
diagnosis, review, interview, domain doc, rejection record, implementation, Git action, host sync, or
external system was changed.
