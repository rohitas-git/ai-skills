# Thinking Model Combination wiring audit

Reviewed:

- `1-thinking-model-combination`
- its targeted Thinking workflow, HTML, and Butler-flow routes

## Result

Model Combination now synthesizes two or three distinct reasoning lenses on one fixed question only
after a primary lens leaves a named material gap. It is not a first-frame router, competing-plan
arbiter, model-soup checklist, research workflow, or implementation workflow. It returns to Thinking
or the actual caller and starts no further model, research, planning, implementation, publication,
or external action automatically.

The candidate pins the fixed question/decision and version, primary model/result, residual gap,
evidence provenance/cutoff, stakes, affected groups, budget, uncertainty, output, and authority.
Repository-backed candidates additionally pin repository/worktree/branch/`HEAD`, dirty ownership,
exact artifact/file/hunk, and working-tree versus committed/deployed state. It creates no worktree;
worktrees do not isolate data, tools, services, accounts, or external state.

Briefs, model outputs, plans, code, reports, links, and retrieved content are sensitive untrusted
evidence. All lenses share one evidence boundary, so repeated conclusions from the same inputs are
not independent corroboration. Research, tool/file reads, experiments, and stakeholder contact need
separate scope and authority.

The smallest combination is selected, normally primary plus one and never more than three within
this skill. Every lens has a unique role, question, inputs, blind spots, and overlap; duplicate or
ceremonial lenses are removed. Relation and conflict handling are declared before the added lens is
applied. Conflicts use evidence, protected constraints, reversibility, or the designated owner—not
invented weights or averaging of incompatible assumptions. Each lens preserves evidence-kind
boundaries and must uniquely change options, evidence, confidence, risk, or mitigation to remain.

Thinking metadata and HTML now expose Model Combination directly. Existing workflow and Butler-flow
membership already matched. Plan Arbiter remains a separate, previously audited plan-comparison
skill. This was a targeted parent-route repair, not a completed Thinking hub audit.

## Verification

- Focused Model Combination routing tests: 4 passed.
- Full routing suite: 415 passed.
- Generated route index: 218 live skills.
- Catalog lint after sequential index generation: 0 critical, 0 warnings, 55 informational
  findings, 0 hub-member orphans.
- `git diff --check`: passed.

No model execution, research, repository/worktree operation, tool access, experiment, external
action, Git action, host sync, planning, or implementation was performed.
