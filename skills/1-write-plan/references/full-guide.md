# Writing an executable plan

Use after the design/spec is sufficiently settled to plan implementation.
Planning is an artifact task, not authorization to implement, commit or publish.

## 1. Establish inputs and authority

Read the approved specification, relevant repository instructions, existing plans,
and the actual source/tests around the requested change. Record the repository,
branch/SHA and dirty-state context used for planning. Do not create a worktree
merely to read code or draft a response. A requested repository plan file is a
scoped documentation edit; preserve existing edits and honor its file location.

Use the project's plan convention or the user's path. Otherwise propose a clearly
named file such as `docs/superpowers/plans/YYYY-MM-DD-<feature>.md`; do not overwrite
an existing plan without establishing that it is the intended revision.

No settled requirements: name the specific unknown and return to the design caller
or `/0-grilling`/`/1-to-spec` as appropriate. Do not force a new brainstorm when
the supplied specification already answers the question.

## 2. Map requirements to bounded tasks

Map every acceptance criterion and explicit exclusion. Inspect real paths before
naming them; distinguish a proposed new file from one that exists. Use stable
symbol names and paths rather than relying solely on line numbers that will move.

Prefer vertical, verifiable slices. Group tightly coupled setup, code and tests
into the deliverable they enable; split only where a meaningful independent
acceptance boundary exists. Do not split by technical layer or introduce a file
reorganization solely to make the plan look neat.

For each task record dependencies, consumed/produced contracts and verification.
Order shared contracts, migrations, lockfiles and generated artifacts under one
owner. Parallel candidates require demonstrably independent inputs and side
effects, not just different filenames. Execution chooses actual checkouts through
`/1-git-worktrees`; the plan records isolation needs rather than inventing paths
or assuming local services already exist.

## 3. Specify enough to execute, without fabricating code

Use exact agreed values, interfaces and behavior. Provide targeted code examples
when they remove real ambiguity; a complete implementation pasted into every step
is not required and may become stale before execution. Label proposed APIs and
illustrative pseudocode. Never treat illustrative code as verified or working.

A runnable test or precise test case names inputs, expected behavior and the
independent acceptance source. Select the evidence loop per task:

- Known deterministic behavior: `/1-tdd` can use a behavior-level failing check
  followed by implementation and regression verification.
- Exploratory design: a bounded `/1-prototype` question before implementation.
- Probabilistic outputs: an evaluation rubric/dataset through `/1-agent-evaluation`.
- Configuration, docs and integration: their relevant validators and acceptance
  checks; do not fabricate a red-green cycle.

Do not claim future command output, timing, CI results or conflicts are known.
Write a discovery gate: what to inspect, the safe check, how its result informs the
next in-scope action, and which authority is still required. Missing runtime or
service readiness is an execution precondition, not evidence of a green result.

## Plan shape

Scale detail to risk and task size; avoid empty sections. A useful template:

```markdown
# <Feature> implementation plan

Status: draft | approved for the stated scope
Source: <spec/design and revision>
Repository context: <path, branch/SHA, relevant dirty-state assumptions>
Goal: <observable outcome>
Non-goals: <explicit exclusions>
Execution authority: <planning only, or actual granted operations>

## Global constraints
<Exact shared contracts, security/data rules and project quality requirements>

## Task 1: <verifiable deliverable>
- Depends on: <task IDs or none>
- Acceptance criteria: <requirement IDs and concrete outcomes>
- Files/symbols: <existing, new and protected paths>
- Interfaces: <consumes/produces and exact binding values>
- Workspace/services: <isolation and readiness requirements, not invented state>
- [ ] Inspect <named precondition/current-state evidence>.
- [ ] Implement <bounded behavior, including failure/edge cases>.
- [ ] Verify <actual project command or precise test cases and expected behavior>.
- [ ] Review <scope and evidence gate>.
- Evidence to record: <candidate identity, commands/results, remaining limits>
- Commit grouping: <logical group only; committing requires granted authority>

## Integration and handoff
<Cross-task checks, review scope, unresolved decisions and conditional next step>
```

Use numbered Task headings if the selected executor uses the catalog's task-brief
extractor. Global constraints must still accompany each extracted worker brief;
a task excerpt alone does not carry the entire specification.

## 4. Review the plan

Self-review requirement coverage, scope exclusions, dependency order, matching
interface names/types, executable verification and authority boundaries. Do not
interpret a TODO string in sample source as proof that the plan is incomplete;
flag actual missing decisions or behavior.

When an independent plan review is requested, use
[plan-document-reviewer-prompt.md](./plan-document-reviewer-prompt.md).
Recheck affected parts after a correction. A readable plan is not proof that its
implementation or tests pass.

## 5. Return or hand off

Return the plan path/text, source context, task/dependency summary, verification
strategy, unresolved gates and authority limits to the caller.

For planning-only requests, stop there. When execution is requested, honor an
already selected mode. If a choice remains, use **F-SP** from flows.md:

- Direct execution through `/1-execute-plan` (default unless delegation benefits
  the task), in the current or a new session.
- Requested sequential delegated tasks through `/1-subagent-implement`.
- **Agent judgment**, choosing a fitting mode without another question.

Tool availability alone is not a reason to select delegation. Genuinely concurrent
independent work uses `/1-parallel-agents` only within its authority and isolation
contract. Neither handing off a plan nor approving its design authorizes commits,
pushes, merges, migrations or cleanup by itself.
