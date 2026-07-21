---
name: 1-research
description: >
  Investigate a question against high-trust primary sources and capture the findings as
  a Markdown file in the repo. Use when the user wants a topic researched, docs or API
  facts gathered, or reading legwork delegated to a background agent. Hub: /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a bac"
    triggers:
      - "1-research"
      - "research"
    requires_setup: false
---
## Process

1. Follow this skill's procedure.


Spin up a **background agent** to do the research, so you keep working while it reads.

Its job:

1. Investigate the question against **primary sources** — official docs, source code, specs, first-party APIs — not a secondary write-up of them. Follow every claim back to the source that owns it. Version-pin and hierarchy: [references/source-driven.md](./references/source-driven.md). Full vendor body: [references/source-driven-full.md](./references/source-driven-full.md).
2. Write the findings to a single Markdown file, citing each claim's source.
3. Save it where the repo already keeps such notes; match the existing convention, and if there is none, put it somewhere sensible and say where.


## Related

**Next:** `/0-implement`. Parent hub: `/0-implement`.
