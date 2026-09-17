---
name: 1-writing-great-skills
description: >
  Apply concise skill-craft principles to one body candidate. Use when improving invocation,
  information hierarchy, progressive disclosure, completion criteria, or pruning. Not for executing
  a full author/eval operation (0-skill-creator) or catalog placement (0-skill-manager).
  Hub: /0-skill-creator.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-skill-creator
    role: craft
    when: [apply skill-craft principles to one body candidate]
    not_when:
      - "author or evaluate the package → 0-skill-creator"
      - "place or wire catalog → 0-skill-manager"
    prev: [0-skill-creator]
    next: [0-skill-creator]
    cousins: [0-skill-creator, 1-create-skill, 1-skill-atomize]
    triggers: [writing great skills, skill craft, progressive disclosure, leading words]
    requires_setup: false
---

# Writing Great Skills

**Predictability:** the same bounded process each run, with outputs allowed to vary.

## Process

1. Name the skill's one job, intended caller, output, and genuine invocation branches.
2. Choose model invocation only when automatic discovery earns its permanent description cost; otherwise keep a user-invoked entry behind a clear router.
3. Put every-run steps and safety boundaries in `SKILL.md`; disclose conditional reference behind a pointer that states exactly when to load it.
4. End each step with an observable completion condition. Split only when a distinct trigger or a real sequence boundary earns another skill.
5. Prune in order: duplicate meaning, stale/irrelevant material, then instructions that do not change default behavior.
6. Test the narrow uncertainty that matters—trigger accuracy, output shape, or rule adherence—using available, authorized evidence. Do not impose a universal TDD/subagent/evaluation ritual.
7. Return the craft recommendation or revision to `/0-skill-creator`.

## Craft contract

- Description: what/when plus enough negative boundary to distinguish cousins; keep body procedure out of it.
- Body: one default path, explicit effects and authority, exact candidate/worktree identity when files are involved, and honest coverage.
- References: one level deep where practical; every pointer names its load condition.
- Scripts: bundle only repeated deterministic work; inspect and verify locally before use.
- Language: positive target first. Absolute wording is reserved for genuine safety or correctness invariants and never overrides user authority.
- Evidence: observations, inferences, and unknowns stay distinct.

Full vocabulary: [glossary](./GLOSSARY.md).

## Source adaptations

These are provenance notes, not operative instructions. Load only when auditing how this house policy differs from its source:
[Agent Skills authoring](./references/agentskills-io-best-practices.md) ·
[Superpowers writing](./references/superpowers-writing-skills-full.md) ·
[Anthropic guidance](./references/superpowers/anthropic-best-practices.md) ·
[subagent testing](./references/superpowers/testing-skills-with-subagents.md) ·
[persuasion critique](./references/superpowers/persuasion-principles.md).

## Related

Parent/return: `/0-skill-creator` · placement: `/0-skill-manager` · structural report: `/1-skill-linter`.

