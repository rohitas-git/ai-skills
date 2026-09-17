# Shipping and launch operative guide

Use after the main skill fixes the exact candidate, environment, mode, owner, and authority.
The complete upstream snapshot remains at
`archive/vendor/agent-skills/skills/shipping-and-launch/SKILL.md`. Its universal checklist,
fixed rollout percentages/windows/thresholds, executable deployment examples, and automatic
launch language are historical source material, not operative instructions.

## Readiness evidence

Select gates from actual risk and repository policy. A compact ledger is more truthful than a
generic checklist:

| Gate | Why applicable | Candidate/environment | Evidence | State | Owner/action |
|---|---|---|---|---|---|
| required checks | protected contract | source SHA | exact check suite/run | PASS | release owner |
| compatibility | old/new versions overlap | artifact digest + API version | contract/rehearsal | BLOCKED | resolve before go |
| data transition | writes change shape | migration set + DB target | local/disposable rehearsal | PASS | production execution separately authorized |
| observability | promotion gate needs signal | release cohort | named query/dashboard | SKIPPED | add before rollout |

Common areas to consider only when relevant:

- candidate build, provenance, signatures/SBOM, tests, review, and required checks;
- authentication, authorization, privacy, dependency and supply-chain risk;
- latency/capacity and resource limits supported by representative evidence;
- configuration/schema compatibility and presence of required secret *names* without revealing values;
- migrations, backfills, queues, cache/state, external integrations, and consumer ordering;
- support ownership, status/comms plan, maintenance window, and escalation;
- telemetry and recovery paths capable of evaluating each decision gate.

Do not mutate production merely to complete a readiness checkbox. Missing evidence is BLOCKED or
SKIPPED with an owner and next action.

## Rollout model

Choose the least risky mechanism supported by the system:

| Pattern | Useful when | Key constraint |
|---|---|---|
| direct | tiny, reversible, low-blast-radius change | strong health evidence and fast recovery |
| rolling | instances can safely run mixed versions | compatibility during overlap |
| blue/green | environments and traffic switch are trustworthy | state/schema compatibility and switchback |
| canary/cohort | representative exposure can be isolated and compared | unbiased allocation and enough signal |
| feature flag | deployment and user exposure should be separated | both-state behavior, kill path, debt ownership |

Stages are explicit tuples: candidate, environment, cohort/capacity, entry condition, observation
condition, promotion/hold/recovery thresholds, decision owner, and authorized action. Do not copy
5/25/50/100 percentages or 24-hour windows without traffic, risk, and signal evidence.

## Decision gates

For every gate record:

- user or dependent-system impact signal, plus technical diagnostic signals;
- baseline or SLO/error-budget source and comparison method;
- threshold, evaluation window, freshness/completeness checks, and minimum sample where relevant;
- exact dashboard/query and expected dimensions;
- promote, hold, rollback, forward-fix, or incident action and its human owner.

Absence of new errors is not enough when telemetry is missing, delayed, or sampled incorrectly.
When data integrity or security may be affected, stop exposure and route to the relevant specialist;
the appropriate response might be containment or forward recovery rather than rollback.

## Recovery decision tree

1. Confirm the target and deployed artifact identity; stop if they differ from the plan.
2. Determine whether traffic/exposure can be halted without changing data.
3. Classify compatibility and state effects: code-only, schema, backfill/data, queue/event, cache,
   external side effect, infrastructure, or mixed.
4. Select the pre-validated response: disable exposure, switch traffic, redeploy pinned artifact,
   apply an authorized forward fix, or enter incident response.
5. Verify user-visible recovery and target identity, not merely command success.
6. Record what remains: partial rollout, data reconciliation, flags, queued work, communications,
   monitoring window, and ownership.

Never use a generic `git revert && push` or framework “migration rollback” as a production plan.
Repository history is not necessarily the deployed artifact, and destructive down-migrations may
lose data or break mixed-version compatibility.

## Execution evidence

Plan/advice and readiness review stop before remote mutation. Read-only observation uses the exact
environment and candidate and records timestamps/freshness. For authorized execution:

- name one action and target at a time;
- re-read state immediately before the action;
- preserve command/output or provider event identity;
- check the gate after that stage before any promotion;
- stop on drift, ambiguity, failed/blocked evidence, lost telemetry, or surprising side effects;
- never infer approval for the next stage from approval for the current one.

Return to the actual Ship or DevOps caller. CI/CD authoring, telemetry implementation, candidate
repair, branch integration, incident handling, and post-launch cleanup remain separate actions.
