# Plan document review brief

Use for an explicitly requested independent review, or as a self-review rubric.
Reviewing this template does not itself require spawning an agent.

## Inputs

- Plan path/text and revision.
- Authoritative specification/design and acceptance criteria.
- Repository context used by the plan, relevant instructions and scope exclusions.
- Granted implementation authority, if any.
- Known unresolved decisions and environment limitations.

## Review

Remain read-only. Compare each required outcome with an actionable task and check:

- Scope: no missing requirement, excluded feature or unrequested restructuring.
- Dependencies: feasible order; contracts agree across task boundaries.
- Workspace: task-matching checkout and service isolation are explicit where needed.
- Buildability: real paths/commands distinguished from proposed ones; future-state
  assumptions become discovery gates, not claims about unobserved results.
- Verification: behavior-level criteria, failure cases and cross-task checks;
  checks correspond to the chosen deterministic/prototype/evaluation workflow.
- Authority: no implicit commit, push, migration, deployment or cleanup permission.

Inspect relevant source when a concrete plan claim needs validation; do not review
the whole repository. Do not demand complete code listings or TDD for every step.
Report a missing source as missing evidence, not as a guessed approval.

## Output

- Status: ready for the stated scope | changes needed | blocked by missing evidence.
- Findings: task/step or source location, missing/contradictory criterion, practical
  consequence and focused correction.
- Evidence checked and unresolved preconditions.
- Advisory improvements clearly separated from blockers.

“Ready” is a plan-quality verdict, not permission to implement and not a claim
that the planned code works. Do not make unrelated edits or start execution.
