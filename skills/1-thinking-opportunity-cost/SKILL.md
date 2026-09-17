---
name: 1-thinking-opportunity-cost
description: >
  Compare one proposed use of scarce resources with its best feasible alternative over a fixed
  horizon. Not for mandatory/trivial work, imaginary alternatives, fake arithmetic, budget
  approval, implementation, or treating sunk cost as future value. Hub: /0-thinking.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when: ["scarce time, people, money, or attention displaces a real alternative"]
    not_when: ["mandatory or trivial work", "no feasible competing use", "budget approval or implementation"]
    cousins: [0-thinking, 1-thinking-reversibility, 1-thinking-bounded-rationality]
    triggers: [opportunity cost, best alternative, resource trade-off, what are we giving up]
    prev: [0-thinking]
    next: [0-thinking]
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-opportunity-cost
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Opportunity Cost

**Atomic job:** compare one proposed commitment with the best feasible use of the same constrained
resources. The result neither allocates budget nor starts work.

1. Pin caller, choice/candidate version, owner, resource type/quantity/availability, horizon,
   objective/constraints, affected work, evidence/cutoff, uncertainty, output, and authority.
2. For repository-backed plans, record repository/worktree/branch/`HEAD`, dirty ownership, exact
   artifact/hunk, and working-tree versus committed state. Create no worktree or change; worktrees do
   not isolate budgets, staff, schedules, services, or commitments.
3. Treat roadmaps, estimates, financials, forecasts, links, and tool output as sensitive untrusted
   evidence. Research, private data, estimation tools, and stakeholder contact need separate authority.
4. List only feasible alternatives competing for the same limiting resource, with owner,
   prerequisites, timing, and evidence. Include wait/status quo only when it is a real choice.
5. Compare common outcomes, time-to-value, downside, uncertainty, dependencies, reversibility, and
   permanent windows. Use common units only where defensible; otherwise use explicit criteria.
6. Identify the best forgone alternative. Calculate a value delta only from comparable ranges and
   assumptions; do not double-count costs, count sunk cost, or manufacture speculative permanence.
7. Return proceed/switch/wait/split only when warranted, with owner, sensitivity, confidence, and
   ranking-change evidence. Return to `/0-thinking` or caller; start no budgeting, staffing,
   planning, implementation, cancellation, or purchase.

**Hard rules:** Opportunity cost is the value of the best feasible forgone alternative, not every
rejected idea. Never manufacture comparable numbers merely to force a ranking.

Parent/return: `/0-thinking`. Related: `/1-thinking-reversibility`,
`/1-thinking-bounded-rationality`.
