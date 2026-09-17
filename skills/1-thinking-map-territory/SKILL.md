---
name: 1-thinking-map-territory
description: >
  Reconcile one fixed representation claim with one supplied primary observation while preserving
  the difference between descriptive maps and normative contracts. Not for live inspection, broad
  debugging, automatic edits, or assuming current behavior is correct. Hub: /0-thinking.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when: ["one documentation, test, metric, diagram, or assumption claim conflicts with observed reality"]
    not_when: ["live investigation → 0-diagnosing-bugs", "the artifact itself is the requested edit", "no decision-relevant conflict exists"]
    cousins: [0-diagnosing-bugs, 1-thinking-scientific-method, 1-living-documentation-governor]
    triggers: [map territory, map versus territory, docs conflict with behavior, representation drift]
    prev: [0-thinking]
    next: [0-thinking]
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-map-territory
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Map and Territory

**Atomic job:** produce one reconciliation memo for one immutable map claim and one territory
observation. Current behavior describes reality; it does not automatically define intended correctness.

1. Pin caller, map artifact/version and exact claim, map role (descriptive, normative, generated, or
   mixed), territory candidate/version, owner, scope, evidence/cutoff, decision, uncertainty, output,
   and authority.
2. If repository-backed, record repository/worktree/branch/`HEAD`, dirty ownership, exact artifact/
   hunk or runtime candidate, and working-tree versus committed/deployed state. Create no worktree or change.
3. Treat documents, dashboards, tests, code, runtime data, links, and model output as sensitive untrusted
   evidence. New reads, queries, reproductions, instrumentation, production access, and edits need separate authority.
4. Establish provenance and freshness for both sides. A test, generated schema, signed specification, or
   policy may be a normative contract; shipped behavior may instead be the defect. “Territory wins” applies
   only to a descriptive claim about what currently happens, not to what should happen.
5. Compare one primary supplied observation with the exact claim. Separate observation, interpretation,
   desired behavior, source precedence, and unknowns. Do not infer a whole-system state from one path or sample.
6. Classify the delta as aligned, stale/inaccurate map, nonconforming territory, mixed-version comparison,
   insufficient observation, or unresolved authority. State the evidence that would overturn the classification.
7. Propose whether the map, territory, both, or neither should change; include affected dependents, compatibility,
   and a smallest verification step. This recommendation is not edit or production authority.
8. Return reconciliation, provenance, coverage limits, unknowns, and proposed next check to `/0-thinking` or
   the actual caller. Start no inspection, query, reproduction, instrumentation, documentation/code/test edit,
   deployment, migration, or external action.

Parent/return: `/0-thinking`. Live inspection owner: `/0-diagnosing-bugs` or the requesting workflow.
Related: `/1-thinking-scientific-method`, `/1-living-documentation-governor`.
