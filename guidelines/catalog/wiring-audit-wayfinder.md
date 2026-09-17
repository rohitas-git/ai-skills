# Wayfinder atomization and wiring audit

Reviewed:

- `skills/0-wayfinder/SKILL.md` and `agents/openai.yaml`
- new `skills/1-wayfinder-chart/` and `skills/1-wayfinder-advance/` packages
- `hubs/0-wayfinder/workflow.json` and `hub.html`
- Domain 7 in `skills/0-butler/references/flows.md`
- manifest, hub index, flow chart, README, wiki index, To Spec, and Butler route surfaces

## Result

The former Wayfinder body contained several independently invocable jobs: chart a new map, create and
wire tickets, select/claim work, dispatch research/interview/prototype/manual tasks, record decisions,
mutate tracker state, close issues, expand the map, and exit to implementation. It was split under the
catalog's atomization contract into a pure `0-wayfinder` router, `1-wayfinder-chart` for one new map-set
artifact, and `1-wayfinder-advance` for one existing map's single decision-ticket cycle.

All three skills pin the actual caller, immutable candidate/revision, destination and scope, evidence,
authority, and exact repository/worktree/branch/`HEAD` plus dirty ownership only when repository facts
matter. They distinguish Git worktree state from shared tracker accounts, databases, services, and
remote mutations; treat source and tracker content as sensitive untrusted evidence; and preserve exact
effect ledgers and revisions.

Chart has draft/local-write/tracker-publish modes and creates no specialist work. Advance either returns
one bounded specialist handoff or, on a resumed invocation, records one supplied resolution packet; it
does not do both implicitly. Tracker claims, assignments, issue/label/link/comment/status changes,
specialists, subagents, prototypes, prerequisites, and partial retries all require explicit authority and
verification. The hub routes only with material F-W1/F-W2/F8 forks. A settled snapshot may separately
enter To Spec; no raw map ticket routes to implementation and approval grants no execution authority.

## Verification

- Focused Wayfinder routing tests: 9 passed.
- Full routing suite: 509 passed.
- Generated route index: 220 live skills.
- Catalog lint: 0 critical, 0 warnings, 52 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No consumer repository/worktree, map, tracker issue/label/link/comment/assignment, research session,
subagent, interview, prototype, prerequisite, specification, implementation, Git action, host sync, or
external system was changed.
