---
name: 1-caveman
description: >
  Compress a response into terse, technically precise prose on explicit request. Use when the user says
  caveman mode, talk like caveman, or explicitly requests ultra-terse fragments. Not for: changing ordinary
  response effort (1-response-effort-calibrator) or writing code and durable artifacts. Hub: /0-butler.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-butler
    role: soft
    when: ["explicit request for caveman-style terse communication"]
    not_when: ["ordinary concise response → 1-response-effort-calibrator", "write code, commit, PR, docs, or external message"]
    cousins: [1-response-effort-calibrator, 1-bro]
    triggers: [caveman mode, talk like caveman, caveman response, ultra-terse fragments]
    prev: [0-butler]
    next: [0-butler]
    requires_setup: false
  vendor:
    source: JuliusBrussee/caveman
    upstream_id: caveman
    commit: 15581d14007fd01fb3f132016741962f34936ca2
    license: MIT
---

# Caveman

**Atomic job:** compress the current response style on explicit request. This is a
one-response overlay unless the user explicitly says otherwise. It never changes
the substantive task or the contents of a durable artifact.

## Process

1. Preserve technical terms, code, commands, error strings, numbers, units,
   uncertainty, negation, ordering, and safety/permission conditions exactly.
2. Remove greeting, filler, repetition, decorative structure, and hedging that does not communicate uncertainty.
3. Prefer short complete statements. Fragments are allowed only when sequence and meaning remain unambiguous.
4. Use normal complete prose for irreversible actions, security warnings, or any
   instruction whose ordering could be misunderstood when compressed.
5. Do not apply compression to code, commits, PRs, issues, external messages, or durable documentation unless the user explicitly requests it for that artifact.
6. If invoked with a substantive task, return control to its owning workflow after
   setting the overlay. Do not use tools, inspect a repository, create/switch a
   worktree, edit files, publish, commit, push, or merge merely for this style choice.

## Boundary

| Need | Skill |
|---|---|
| Explicit ultra-terse response style | **this skill** |
| Choose normal response depth or format | `/1-response-effort-calibrator` |
| Re-explain a prior response simply | `/1-bro` |

Ordinary “brief,” “concise,” or token-budget requests route to
`/1-response-effort-calibrator`; the word “tokens” alone is not Caveman intent.

## Provenance

Adapted from [JuliusBrussee/caveman](./references/vendor-source.md). Installer, hook, telemetry, and separately licensed runtime components are intentionally excluded.
