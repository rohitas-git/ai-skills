# Feature verification contract

Use the project's current format. The following fields are a checklist, not a required new schema.

| Field | Evidence to preserve |
|---|---|
| Identity and scope | Stable feature ID, user goal, supported surface/role and source revision |
| Entry points | Menu, route, shortcut, CLI/API action; distinguish equivalent and untested paths |
| Preconditions | Seeded data, auth/entitlement, platform, relevant state and exact instance identity |
| Launch and health | Existing command, readiness condition, expected build, owned port/profile/data |
| Drive | Ordered real user actions and existing tool commands/handles |
| Observe | Expected visible result and permitted second view of persisted effects |
| Evidence | Action plus resulting state, matching candidate/time, artifact path and privacy limits |
| Cleanup | Only run-owned fixtures/processes; preserve evidence outside disposable state |
| Coverage | Source-backed / runtime observed / failed / blocked / not run, by entry point |
| Gotchas | Focus, timing, permissions, cancellation, known gaps and unsafe external effects |

Prefer stable accessible names/roles and repository-supported identifiers to coordinates or
positional selectors. Wait for a meaningful state, not a fixed sleep. A status toast alone may not
prove persistence; reopening the saved item through a permitted second view can distinguish it.

For example, a fictional “Create note” map can distinguish toolbar, keyboard and CLI entries;
canceling a draft must not save it. This does not establish real commands, fixtures or app behavior.

Use supplied runtime evidence from the actual served build. A clean source review cannot close a
live coverage gap. If startup, health, auth or data prerequisites fail, record the blocker instead
of simplifying the recipe. Never double-drive a shared instance or kill a process by name.

Modified from pstack create/maintain-verification guidance and feature-map examples, MIT.
[Source and review](../../../guidelines/catalog/ingest-pstack-2026-11-15.md).
