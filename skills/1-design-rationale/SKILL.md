---
name: 1-design-rationale
description: >
  Explain why one existing design or behavior was chosen from its decision history.
  Use when asking why a feature exists, a threshold was selected, or an alternative was rejected.
  Not for a runtime walkthrough, root-cause diagnosis, code review, or changing the design.
  Hub: /0-learn.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-learn
    role: leaf
    when: [explain the recorded rationale behind one existing design or behavior]
    not_when: [runtime code walkthrough, diagnose a failure, assess correctness, change the design]
    prev: [0-learn]
    next: [0-learn]
    cousins: [1-code-explainer, 1-code-review, 1-deprecation-and-migration]
    triggers: [why was this added, why did we choose this design, design rationale, why this threshold]
    requires_setup: false
  vendor:
    source: cursor/plugins
    upstream_id: pstack/skills/why
    commit: bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7
---

# Design Rationale

Return one cited explanation of a decision, its trade-offs and remaining relevance. Code shows
what happens; history may explain why. A plausible explanation is not evidence of author intent.

## Process

1. Pin caller, exact question and target, repository/worktree/branch/HEAD or supplied record,
   dirty ownership, historical interval, evidence cutoff and allowed read-only sources.
   Do not fetch private discussions, broaden access, or publish material merely to fill a gap.
2. Identify the introducing change and relevant later changes using scoped history, renames,
   commit messages, ADRs, linked issues and accessible PR discussion. Follow only evidence needed
   for this decision; record shallow, missing or rewritten history and inaccessible discussion.
3. Reconstruct the chronology: original problem, constraints, considered alternatives, selected
   option, later revisions and conditions that may no longer apply. Use the actual version of
   the dependency or interface involved. Commit order alone does not establish causation.
4. Attribute stated reasons to their records. Separate contemporaneous statements, current code
   facts, later recollection, your inference and unknowns. Preserve disagreements and qualifiers;
   do not invent consensus, rejected alternatives, benchmark evidence or approval.
5. Explain what purpose the change serves now and what removing it could undo only when supported.
   Distinguish recorded original intent from evidence of current necessity. A replacement or
   expired requirement may make removal reasonable; this explanation does not authorize it.
6. Return the answer, key decision trail with locators, trade-offs, confidence and unanswered
   questions to the caller. A small question may need one paragraph, not a full chronology.

## Boundary

| Need | Owner |
|---|---|
| Historical intent and trade-offs | **this skill** |
| How the current code behaves | `/1-code-explainer` |
| Whether it is correct or should change | `/1-code-review` or `/1-deprecation-and-migration` |

Stay read-only. No branch change, test execution, code/doc edit, commit or external message.
Source: [pstack ingestion and review](../../guidelines/catalog/ingest-pstack-2026-11-15.md), [MIT license](./LICENSE).
