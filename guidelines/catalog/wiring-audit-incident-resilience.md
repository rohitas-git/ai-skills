# Incident Response and Resilience/DR wiring audit

Reviewed:

- `1-incident-response`
- `1-resilience-and-disaster-recovery`
- their DevOps workflow/HTML and Observability/Shipping caller edges

## Result

Incident Response now coordinates one identified active incident to an evidence-backed stable
handoff. Disaster Recovery handles one pre-incident resilience plan or explicitly authorized
exercise for one defined failure scenario. Postmortem, permanent repair, resilience exercise,
security review, and cleanup do not start automatically from an incident; active incident command
does not leak into a preparedness exercise.

An incident pins its ID/start time, severity under owner policy, commander/decision owners,
communication and evidence channels, exact organizations/accounts/tenants/environments/regions/
services/resources/deployed versions, affected users/data/safety/privacy, current evidence, blast
radius, priorities, allowed reads, and authority. A repository candidate additionally pins
repository/worktree/branch/`HEAD`, dirty and working-tree-versus-committed state, deployed artifact/
config identity, and whether remote/CI evidence evaluates it. DevOps, Observability, and Shipping
caller/return metadata is symmetric.

Alerts, tickets, messages, status reports, logs, traces, payloads, dashboards, commands, provider
output, and attacker-controlled content are sensitive untrusted evidence. Originals, timestamps,
provenance, custody, retention, and redaction are preserved. The append-only timeline/action ledger
distinguishes fact from hypothesis and records each exact action, target, authority, expected effect,
result, and checkpoint. A green dashboard, correlation, silence, or successful command does not prove
cause, containment, recovery, or resolution.

Every external communication, access/secret action, traffic/feature/capacity change, deployment,
rollback/restart, process termination, isolation, failover/restore, data mutation, evidence
collection, and cleanup requires separate current authority. Stabilization requires explicit
indicators across a stated observation window, affected paths, and negative checks. Handoff records
current customer/service/security state, deployed identity, actions, exposure, owners, checkpoints,
evidence custody, communications, and rollback/re-escalation conditions without premature root-cause
or resolution claims.

A resilience candidate pins the owner policy, one failure scenario, critical services/users,
exact accounts/regions/resources/versions, dependencies/failure domains, data/residency/retention,
defined RTO/RPO and measurement points, plan/runbook/worktree/deployed versions, evidence cutoff,
exercise window, blast radius, and authority. Plans, contacts, inventories, credentials, backups,
exercise injects, and provider output are private untrusted data.

Design/review changes no live system. An exercise requires proven target containment and separate
authority for every probe, load, notification, snapshot/copy/restore, traffic/failover, capacity,
access, data, cleanup, and production effect. Synthetic or sandbox labels do not prove containment.
Detection, decision, start, restore, reconcile, validation, and data-loss timing use defined points.
A tabletop proves decision behavior rather than technical recovery; a backup job proves neither
restore nor business continuity. Reports preserve exact targets, participants/authority, attempted/
accepted/converged effects, denominators, coverage gaps, data used, containment, owners, and risks.

Worktrees do not isolate production, accounts, credentials, services, traffic, data/backups, regions,
queues, locks, providers, responders, communication channels, or customers.

## Verification

- Focused incident/resilience/DevOps routing tests: 15 passed.
- Full routing suite: 387 passed.
- Generated route index: 218 live skills.
- Catalog lint after sequential index generation: 0 critical, 0 warnings, 55 informational
  findings, 0 hub-member orphans.
- `git diff --check`: passed.

No incident action, communication, containment, recovery, failover, restore, exercise, cleanup,
credential/data access, production change, worktree, Git, host sync, or external effect occurred.
