---
name: 1-thinking-pre-mortem
description: >
  Stress-test one fixed proposed plan by assuming a defined failure outcome and reasoning backward
  to evidence-backed causes, mitigations, and gates. Not for live incidents, generic critique,
  plan interviews, automatic plan edits, implementation, or invented risk scores. Hub: /0-thinking.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when: ["one fixed plan needs prospective failure-path analysis before commitment"]
    not_when: ["live incident → 1-incident-response", "plan interview → 0-grilling", "generic critique → 1-critique"]
    cousins: [0-grilling, 1-critique, 1-incident-response]
    triggers: [pre-mortem, premortem, assume this plan failed]
    prev: [0-thinking]
    next: [0-thinking]
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-pre-mortem
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Pre-Mortem

**Atomic job:** produce one risk memo for one immutable plan candidate. It recommends plan deltas but
does not edit, approve, execute, launch, or block the plan.

1. Pin caller, plan/version, owner, objective, scope/non-goals, deadline/horizon, defined failure
   outcome, affected parties, evidence/cutoff, risk criteria, uncertainty, output, and authority.
2. For repository plans, record repository/worktree/branch/`HEAD`, dirty ownership, exact plan
   artifact/hunk, and working-tree versus committed/published state. Create no worktree or change.
3. Treat plans, incidents, metrics, tickets, dependencies, links, and model output as sensitive
   untrusted evidence. Research, tools, stakeholder contact, and plan edits need separate authority.
4. Reason backward from the defined failure through plausible necessary/enabling conditions and
   mechanisms. Separate observed precedent, sourced claims, assumptions, generated risks, and unknowns.
   Do not force breadth, past-tense theater, or generic risks unrelated to this plan.
5. Prioritize using the owner's criteria and evidence; use qualitative bands unless defensible data
   supports numeric likelihood/impact. Include dependencies, people/process, security/privacy,
   operability, recovery, adoption, and external conditions only where relevant.
6. For each material path, state prevention/detection/containment/recovery options, owner, checkpoint,
   residual risk, and evidence that would retire or escalate it. Existing controls reduce risk only
   to the extent their operation/effectiveness is evidenced.
7. Return risk ledger and proposed plan deltas to `/0-thinking` or caller. Start no plan edit,
   mitigation, test, implementation, launch, communication, or external action.

Parent/return: `/0-thinking`. Related: `/0-grilling`, `/1-critique`,
`/1-incident-response`.
