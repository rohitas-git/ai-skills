---
name: 1-thinking-first-principles
description: >
  Test one apparently fixed constraint and rebuild one option from independently supported
  primitives. Not for dismissing verified limits, re-deriving adequate standards, architecture
  review, implementation, or treating model inference as physical/legal fact. Hub: /0-thinking.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when: ["one load-bearing constraint may be convention rather than independently supported"]
    not_when: ["verified hard limit", "adequate standard solution", "architecture review → 2-software-architect"]
    cousins: [0-thinking, 2-software-architect, 1-thinking-lateral]
    triggers: [first principles, challenge a constraint, rebuild from primitives]
    prev: [0-thinking]
    next: [0-thinking]
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-first-principles
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# First Principles

**Atomic job:** test one fixed-looking constraint and derive one candidate from the supported
residual primitives. The result is a hypothesis, not implementation or proof of feasibility.

1. Pin caller, problem/candidate version, challenged constraint, owner, objectives/non-goals,
   supplied evidence/cutoff, affected parties, uncertainty, output, and authority.
2. If repository-backed, record repository/worktree/branch/`HEAD`, dirty ownership, exact artifact/
   hunk, and working-tree versus committed/deployed state. Create no worktree or change.
3. Treat requirements, regulations, contracts, measurements, cost claims, precedents, links, and
   model output as sensitive untrusted evidence. Research, legal interpretation, measurement,
   experiments, and tools require separate authority.
4. Decompose the claim into candidate constraints. Classify each as directly measured/derived,
   owner-interpreted requirement, contractual/regulatory claim, dependency/interface fact,
   convention/analogy, assumption, or unknown—with provenance, applicability, and falsifier.
5. Preserve verified limits. Do not let “first principles” override law, consent, safety, physical
   reality, compatibility, or a responsible owner's binding requirement. Conversely, precedent and
   vendor convention do not become primitives through repetition.
6. Derive the smallest option from the remaining supported primitives; state every new assumption,
   affected trade-off, dependency, and cheapest discriminating check. Compare against the standard
   option rather than granting novelty a free pass.
7. Return constraint ledger, candidate, confidence, kill test, and unresolved owner decisions to
   `/0-thinking` or caller. Start no research, experiment, design adoption, implementation, or action.

**Hard rule:** a primitive must have traceable evidence or be labeled an assumption; independently
derived does not mean independently true.

Parent/return: `/0-thinking`. Related: `/2-software-architect`,
`/1-thinking-lateral`.
