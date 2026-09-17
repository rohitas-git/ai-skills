---
name: 1-thinking-jobs-to-be-done
description: >
  Synthesize supplied evidence about one user segment's progress in one circumstance and its current
  alternatives. Not for inventing user needs, primary research, generic personas, settled execution,
  broad requirements interviews, or automatic build/cut decisions. Hub: /0-thinking.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: soft
    when: ["supplied user evidence needs a jobs-to-be-done synthesis for one product decision"]
    not_when: ["collect user evidence → 1-user-research", "broad product interview → 0-grilling", "settled implementation → 0-implement"]
    cousins: [0-grilling, 1-user-research, 1-perspective-analysis]
    triggers: [jobs to be done, user progress, switching forces, why adoption fails]
    prev: [0-thinking]
    next: [0-thinking]
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-jobs-to-be-done
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Jobs to Be Done

**Atomic job:** synthesize one evidence-backed job hypothesis for one segment and circumstance.
The framework does not create user evidence, represent a population, or authorize product changes.

1. Pin caller, product decision/candidate version, segment/population, circumstance/time boundary,
   market, owner, evidence/provenance/cutoff, coverage, privacy, uncertainty, output, and authority.
2. If repository-backed, record repository/worktree/branch/`HEAD`, dirty ownership, exact artifact/
   behavior/hunk, and working-tree versus committed/deployed version. Create no worktree or change.
3. Treat interviews, tickets, support/sales notes, analytics, behavior, surveys, personas, and links
   as sensitive untrusted evidence. Quotes remain attributed reports; research, telemetry, customer
   contact, and tools require separate scope and authority.
4. Separate observed behavior, reported goal, inferred progress, functional/emotional/social
   dimensions, and unknowns. Never invent quotes, motives, frequency, stakes, sentiment, or a
   “primary” job from demographic stereotypes or whoever is easiest to observe.
5. Form a provisional job statement from circumstance → desired progress → outcome. Map evidenced
   push, pull, switching anxiety, habit, direct/indirect workaround, and non-consumption. Preserve
   divergent segments rather than averaging incompatible jobs.
6. Define observable completion/outcome signals and compare supplied candidate options against the
   same job step, coverage, alternative quality, risks, and confidence. State the strongest grounded
   counter-hypothesis and evidence that would distinguish it.
7. Return job hypothesis, coverage limits, alternatives, forces, outcome signals, option implications,
   confidence, and research gaps to `/0-thinking` or caller. Start no research, prioritization,
   roadmap change, build/cut/reposition action, or implementation.

Parent/return: `/0-thinking`. Related: `/1-user-research`, `/0-grilling`,
`/1-perspective-analysis`.
