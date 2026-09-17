# Explicit delegation patterns

This reference applies only when the user or governing instructions explicitly request or authorize
delegation. Direct execution is the default; the mere availability of agents is not a reason to use
them. Route implementation delegation to `/1-subagent-implement` and independent parallel work to
`/1-parallel-agents`.

## Safe shapes

### Sequential delegated implementation

Use when tasks depend on prior edits/evidence or share files/state. One writer at a time owns the
confirmed worktree. Each task receives the current candidate, allowed paths, protected work,
acceptance evidence, and return contract. The caller verifies state after every handoff.

### Parallel independent outputs

Use only when subtasks can finish without reading another subtask's unpublished output and without
writing the same worktree, branch, files, database, service, ports, artifacts, or remote state. Safe
examples include disjoint read-only investigations or separately owned worktrees with isolated local
services. Merge/synthesis remains with the caller.

### Read-only research isolation

Use when a bounded read-heavy search would overwhelm the caller context and the returned digest is
substantially smaller. The request must pin repository/worktree/HEAD, scope, sources, exclusions, and
evidence format. The caller rechecks consequential claims before acting.

## Required handoff packet

- caller and task/slice ID;
- repository, exact worktree/branch/HEAD, and candidate/base;
- allowed paths and effects; protected/dirty ownership;
- acceptance criteria and checks permitted;
- local service/resource ownership;
- expected result and evidence/limits;
- explicit prohibition on commit/push/deploy/merge or other ungranted effects.

## Hard boundaries

- Never allow concurrent writers in one worktree or shared mutable environment.
- A child does not create/switch worktrees, stash user changes, install tools, start shared services,
  or broaden scope unless its assigned owner explicitly authorizes that action.
- Failed/partial agents return evidence; they do not silently restart, hand work to another agent, or
  claim completion.
- The caller re-reads current filesystem/Git/runtime state after agent completion. Summaries are not
  authoritative state.
- No harness-specific hooks, experimental team mode, global configuration, or persistent persona
  installation is part of this implementation workflow.
- More agents increase coordination cost and correlated-assumption risk. Use the smallest explicit
  composition that has a concrete latency/context/independence benefit.
