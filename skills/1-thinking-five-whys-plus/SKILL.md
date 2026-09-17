---
name: 1-thinking-five-whys-plus
description: >
  Build one evidence-linked causal and prevention memo for one already-localized fault. Not for
  localizing among competing causes, forcing five levels, ending at human blame, running diagnostics,
  implementing countermeasures, or declaring a root without evidence. Hub: /0-thinking.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when: ["one fault and proximate cause are localized but the recurrence-enabling cause is not"]
    not_when: ["multiple plausible proximate causes remain → 1-thinking-scientific-method", "live bug pipeline → 0-diagnosing-bugs", "one-off defect has no deeper evidenced enabler"]
    cousins: [0-diagnosing-bugs, 1-thinking-scientific-method, 1-thinking-systems]
    triggers: [five whys plus, five whys, evidence linked root cause, recurrence cause]
    prev: [0-thinking]
    next: [0-thinking]
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-five-whys-plus
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Five Whys Plus

**Atomic job:** produce one causal-and-prevention memo for one immutable, already-localized fault.
The number of “whys” is evidence-driven, not five by ritual.

1. Pin caller, fault/version, confirmed proximate cause, affected scope/time window, impact, evidence/
   cutoff, prevention decision, uncertainty, output, and authority. If localization is not established,
   return to `/1-thinking-scientific-method` or the owning diagnostic workflow.
2. If repository-backed, record repository/worktree/branch/`HEAD`, dirty ownership, exact artifact/
   hunk or runtime candidate, and working-tree versus committed/deployed state. Create no worktree or change.
3. Treat incidents, logs, code, configs, interviews, tickets, links, and model output as sensitive
   untrusted evidence. New investigation, tools, production access, contact, and changes need separate authority.
4. Build each causal link from observed evidence or a clearly labeled inference. For every proposed
   cause, state the mechanism, competing explanation, missing evidence, and whether it is necessary,
   sufficient, contributing, or merely correlated. Stop a branch when evidence stops.
5. Preserve independently evidenced causal branches instead of forcing one root. Test each with the
   counterfactual “would removing this condition block this pathway?” and test the retained set against
   the full observed failure. Do not turn a plausible counterfactual into causal proof.
6. Do not stop at “human error.” Identify the evidenced design, process, interface, incentive, training,
   or control condition that made the error possible, or report the root as unresolved.
7. For each retained recurrence-enabling cause, propose the smallest prevention/detection/containment
   countermeasure, owner, verification signal, residual pathway, and rollback consideration. A proposed
   countermeasure is not approval or evidence that recurrence is prevented.
8. Return problem statement, causal graph/chain, evidence and uncertainty, retained causal set, proposed
   countermeasures, and unresolved branches to `/0-thinking` or the actual caller. Start no diagnostic,
   edit, test, remediation, process change, communication, or external action.

Parent/return: `/0-thinking`. Live diagnosis owner: `/0-diagnosing-bugs`.
Related: `/1-thinking-scientific-method`, `/1-thinking-systems`.
