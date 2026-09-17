---
name: 1-thinking-thought-experiment
description: >
  Run one controlled counterfactual to expose mechanisms when a real test is unavailable,
  disproportionate, unsafe, or irreversible. Not for replacing cheap empirical checks, adversarial
  security testing, scenario sprawl, treating imagination as evidence, or implementation.
  Hub: /0-thinking.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when: ["one bounded counterfactual can expose a decision-relevant mechanism that cannot yet be tested"]
    not_when: ["cheap safe real check exists", "adversarial security work → 1-thinking-red-team", "vague scenario brainstorming"]
    cousins: [0-thinking, 1-thinking-scientific-method, 1-thinking-red-team]
    triggers: [thought experiment, controlled counterfactual, what if scenario]
    prev: [0-thinking]
    next: [0-thinking]
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-thought-experiment
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Thought Experiment

**Atomic job:** trace one explicit counterfactual far enough to expose a decision-relevant mechanism.
Its result is a hypothesis and test design, not observed evidence or permission to act.

1. Pin caller, question/decision and candidate version, control world, changed variable(s), owner,
   scope/non-goals, evidence/cutoff, uncertainty, safety, output, and authority.
2. If repository-backed, record repository/worktree/branch/`HEAD`, dirty ownership, exact artifact/
   hunk, and working-tree versus committed/deployed state. Create no worktree or change.
3. Treat diagrams, configs, policies, assumptions, links, and model output as sensitive untrusted
   evidence. Research, simulations, tests, tools, and external access need separate authority.
4. Prefer one isolated change. Allow a small declared interaction set only when the interaction is
   the question; do not pretend other conditions are fixed when they cannot be held constant.
5. Trace each causal step from supplied or explicitly assumed mechanisms. Label observations,
   sourced claims, assumptions, generated consequences, invariants, and unknowns. Drop steps with no
   credible mechanism instead of filling the story.
6. Identify the first material break point, affected parties, implication boundary, alternate path,
   and the cheapest safe discriminating observation. Never convert counterfactual consistency into
   probability, production behavior, safety proof, or causal validation.
7. Return the chain, confidence, invalidating assumptions, bounded implications, and proposed check
   to `/0-thinking` or caller. Start no experiment, simulation, research, implementation, or action.

Parent/return: `/0-thinking`. Related: `/1-thinking-scientific-method`,
`/1-thinking-red-team`.
