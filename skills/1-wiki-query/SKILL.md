---
name: 1-wiki-query
description: >
  Answer questions against personal vault/wiki with Karpathy-style query workflow and
  citations. Use for what do my notes say, query the wiki, answer from vault. Not for: invent without
  notes or generic web research. Hub: /0-rohitas-vault-wiki. Triggers: query wiki, notes say, answer from vault.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-rohitas-vault-wiki
    role: pipeline
    when:
      - "question against vault notes"
      - "query wiki / second brain"
    not_when:
      - "no vault / invent → research skills"
      - "structure vault → 0-rohitas-vault-wiki"
    triggers:
      - "query wiki"
      - "what do my notes say"
      - "answer from vault"
      - "1-wiki-query"
    requires_setup: false
---

# Wiki Query

Purpose router for **`/1-wiki-query`**. Full procedure: [references/full-guide.md](./references/full-guide.md).

## Process

1. Read [references/full-guide.md](./references/full-guide.md) for full steps, templates, and detail.
2. Execute the procedure from that guide.
3. Stay within this skill's Boundary (above or in guide).

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full workflow / detail | [references/full-guide.md](./references/full-guide.md) |

## Related

See Boundary table and hub membership in `skills/0-butler/references/flows.md`.


### Additional references

| Load when | File |
|-----------|------|
| karpathy query principles | [references/karpathy-query-principles.md](./references/karpathy-query-principles.md) |
| query page format | [references/query-page-format.md](./references/query-page-format.md) |
| vault map | [references/vault-map.md](./references/vault-map.md) |
