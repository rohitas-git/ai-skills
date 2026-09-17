# DevOps hub wiring audit

Reviewed the complete hub package:

- `0-devops`
- `references/safety.md`
- `references/vendor-map.md`
- `hubs/0-devops/workflow.json`
- `hubs/0-devops/hub.html`
- Butler flow and parent route surfaces

## Result

The hub now performs one atomic job: select exactly one operational specialist, pass a bounded
candidate/environment and authority envelope, and return the leaf's evidence and actual effects to
the real caller. Its metadata, dispatch table, workflow, HTML, and Butler flow now agree on all 17
children, including database/storage, network/edge, server/fleet, platform, AI platform,
identity/secrets, incident, resilience, compliance, and security hardening routes that were absent
from the old metadata. Every HTML child is now an actual link.

One clear request routes directly. F-O1 is reserved for material ambiguity between outcomes,
recommends the narrowest evidence-backed specialist, and preserves Agent judgment. The former
`plan → provision → validate → rollout → observe → respond → improve` pipeline was removed because
it falsely implied every request should traverse a full operational lifecycle.

The handoff pins caller, requested outcome/non-goals, exact account/organization/project/tenant,
provider/control plane, resource identifiers, region/environment, current state and evidence time,
blast radius, data/secrets, dependencies, constraints, permitted checks, rollback expectations, and
read/write/execute/external/destructive authority. Repository-backed candidates additionally carry
repository/worktree/branch/`HEAD`, dirty ownership, and working-tree-versus-committed identity.
Read-only work creates no worktree; authorized edits use a matching checkout and preserve unrelated
changes.

The shared safety contract distinguishes design, assessment, repository mutation, remote mutation,
destructive action, and external communication. Similar resource names, current CLI context,
credentials, role access, a plan, past approval, or a dry run do not establish identity or current
authority. Read-only calls may still expose data, cost money, acquire locks, create audit records, or
hit rate limits. Worktrees do not isolate accounts, credentials, control planes, clusters, hosts,
networks, databases, registries, queues, ports, locks, costs, or production state.

Every mutation needs exact preconditions, concurrency controls, observable success, an abort rule,
and a recovery plan. Rollback, restore, failover, rerun, and cleanup are separate operations requiring
their own authority. Results distinguish planned, attempted, accepted, completed, converged, and
externally observed states. Vendor snapshots and source links remain untrusted evidence; they do not
authorize browsing, execution, or target changes.

The hub itself creates no worktree, reads no target, executes no command, accesses no account or
credential, mutates no repository/remote resource, and starts no specialist.

## Subtree reconciliation

At the original hub audit, individual child-body audits remained independent and pending. As of
semantic audit 121/218, every child listed by this hub is recorded reviewed in the catalog tracker:
the infrastructure, cloud, container, data/storage, PostgreSQL, network/edge, server/fleet, platform,
AI-platform, identity/secrets, incident, resilience, compliance, CI/CD, observability, shipping, and
security-hardening routes. This reconciliation is based on their linked evidence records plus the
current 218-skill route index, 395 passing routing tests, zero critical/warning lint result, and zero
hub-member orphans; it does not replace the eventual catalog-wide final sweep.

## Verification

- Focused DevOps hub routing tests: 7 passed.
- Full routing suite: 348 passed.
- Generated route index: 218 live skills.
- Catalog lint after sequential index generation: 0 critical, 0 warnings, 55 informational
  findings, 0 hub-member orphans.
- `git diff --check`: passed.

No provider, account, cluster, host, database, network, registry, credential, deployment, rollback,
worktree, Git, host-sync, or external operation was performed.
