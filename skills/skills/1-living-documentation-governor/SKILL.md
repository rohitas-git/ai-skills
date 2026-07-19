---
name: 1-living-documentation-governor
description: >
  Code-synced living documentation: trigger maps, placement into guides/ADR/
  glossary/archive, drift checks, grounded Q&A from docs+code. Not a Karpathy
  concept wiki from docs/raw (/1-project-wiki-manager) or personal Obsidian vault
  (/0-rohitas-vault-wiki). Soft under Architecture domain.
disable-model-invocation: true
---

# Living Documentation Governor

## Boundary

| Need | Skill |
|------|--------|
| Living docs + triggers + code drift | **living-documentation-governor** (this) |
| In-repo concept wiki (`docs/raw` → `docs/wiki`) | `/1-project-wiki-manager` |
| Personal Rohitas’s Notes vault | `/0-rohitas-vault-wiki` |
| Active glossary/ADR while grilling design | `/1-domain-modeling` |

## Process

1. Read [references/full-guide.md](./references/full-guide.md) for full steps, templates, and detail.
2. Execute the procedure from that guide.
3. Stay within this skill's Boundary (above or in guide).

## Progressive disclosure

| Load when | File |
|-----------|------|
| Full workflow / detail | [references/full-guide.md](./references/full-guide.md) |
| Bare project README shape | [references/project-readme-skeleton.md](./references/project-readme-skeleton.md) |
| Full vendor docs+ADRs body | [references/vendor-docs-adrs-full.md](./references/vendor-docs-adrs-full.md) |
| Detail | [references/page-template.md](./references/page-template.md) |
| Detail | [references/trigger-enforcement.md](./references/trigger-enforcement.md) |
| Detail | [references/git-hooks-setup.md](./references/git-hooks-setup.md) |
| Detail | [references/knowledge-placement-examples.md](./references/knowledge-placement-examples.md) |
| Detail | [references/adr-criteria-examples.md](./references/adr-criteria-examples.md) |
| Detail | [references/qa-response-template.md](./references/qa-response-template.md) |

## Related

See Boundary table and hub membership in `skills/0-butler/references/flows.md`.
