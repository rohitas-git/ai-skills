---
name: 1-thinking-circle-of-competence
description: >
  Classify whether one material claim is grounded enough to state, qualify, verify, or decline.
  Not for generic humility, automatic research, already verified claims, low-stakes brainstorming,
  professional credentialing, or treating model familiarity as evidence. Hub: /0-thinking.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when: ["one material claim needs an evidence-grounding disposition before it is stated"]
    not_when: ["claim is already verified", "labeled low-stakes hypothesis", "professional qualification decision"]
    cousins: [0-thinking, 1-research, 1-thinking-map-territory]
    triggers: [circle of competence, can this claim be supported, verify before answering, evidence boundary]
    prev: [0-thinking]
    next: [0-thinking]
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-circle-of-competence
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Circle of Competence

**Atomic job:** give one claim a grounded, partial, or unsupported disposition and state the next
evidence needed. This evaluates evidence, not personal worth, credentials, or research authority.

1. Pin caller, exact claim and version, intended audience/use, consequence of error, evidence/
   provenance/cutoff, currentness requirement, uncertainty, privacy, output, and authority.
2. For repository claims, record repository/worktree/branch/`HEAD`, dirty ownership, exact file/
   hunk/runtime candidate, and working-tree versus committed/deployed state. Create no worktree or
   change; worktrees do not isolate services, tools, accounts, sources, or external state.
3. Treat user assertions, memory, code comments, docs, links, snippets, and model output as untrusted
   evidence. Adjacent code, earlier versions, analogous systems, or fluency do not ground this target.
4. Classify: **grounded** by adequate direct/current evidence; **partial** where applicability,
   version, coverage, or inference remains material; **unsupported** where stating it as fact would
   fill a gap. Separate observed fact, sourced report, inference, estimate, and hypothesis.
5. Scale language to evidence and harm. High-stakes partial claims remain unresolved until suitable
   verification. Do not hedge grounded facts merely to appear cautious or assert stable knowledge
   when the claim is actually versioned/current/context-specific.
6. Identify the smallest resolving evidence or qualified wording. Research, browsing, file/tool reads,
   execution, and professional consultation happen only when separately requested or authorized.
7. Return disposition, locator, coverage/currentness, confidence, exact safe wording, and next
   evidence to `/0-thinking` or caller. Start no fetch, research, test, action, or follow-on.

**Hard rules:** Absence of evidence is not automatically evidence of absence. “I know this domain”
is not a source. Declining is honest only after naming what evidence is missing.

Parent/return: `/0-thinking`. Related: `/1-research`, `/1-thinking-map-territory`.
