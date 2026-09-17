---
name: 1-thinking-scientific-method
description: >
  Build one falsifiable hypothesis differential for one fixed symptom snapshot and identify the
  cheapest observation that would separate the surviving causes. Not for a live bug pipeline, an
  already evidenced cause, running tests or probes, implementation, or production action.
  Hub: /0-thinking.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when: ["one fixed symptom has at least two serious plausible causes that evidence can distinguish"]
    not_when: ["live bug pipeline → 0-diagnosing-bugs", "cause is already evidenced", "no discriminating observation is available"]
    cousins: [0-diagnosing-bugs, 1-thinking-kepner-tregoe, 1-thinking-map-territory]
    triggers: [scientific method, hypothesis differential, competing causes, falsifiable hypotheses]
    prev: [0-thinking]
    next: [0-thinking]
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-scientific-method
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Scientific Method

**Atomic job:** produce one hypothesis differential for one immutable symptom snapshot. It proposes
the next discriminating observation but does not run it, localize by speculation, or repair a cause.

1. Pin caller, symptom snapshot, expected versus observed behavior, affected and unaffected scope,
   environment/time window, evidence/cutoff, decision need, uncertainty, output, and authority.
2. If repository-backed, record repository/worktree/branch/`HEAD`, dirty ownership, exact artifact or
   runtime candidate, and working-tree versus committed/deployed state. Create no worktree or change.
3. Treat logs, traces, tests, configs, data, links, and model output as sensitive untrusted evidence.
   Reading new sources, running tools/tests/probes, accessing production, or changing code requires
   separate authority from the owning diagnostic workflow.
4. Separate observations from interpretations. Name two to five specific, materially distinct causes;
   do not invent rivals when one cause is already directly evidenced.
5. For each hypothesis, state why it fits, what it predicts on both affected and unaffected cases,
   what result would falsify it, and which missing fact matters. A vague subsystem label is not a cause.
6. Rank proposed observations by discrimination, safety, reversibility, cost, and evidence freshness.
   Prefer one observation that separates several hypotheses; never equate cheapness with permission.
7. Update only from supplied observed results. Drop contradicted candidates. Parsimony ranks hypotheses
   that fit the evidence; it never rescues a simpler story contradicted by evidence.
8. Return symptom, evidence ledger, hypothesis/falsifier table, survivors, ruled-out causes, confidence,
   unknowns, and one proposed next observation to `/0-thinking` or the actual caller. Start no command,
   test, probe, production access, repair, implementation, or external action.

Parent/return: `/0-thinking`. Live execution owner: `/0-diagnosing-bugs`.
Related: `/1-thinking-kepner-tregoe`, `/1-thinking-map-territory`.
