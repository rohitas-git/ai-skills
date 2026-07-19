# Project README skeleton (harvested)

Source: archive vendor `documentation-and-adrs` (README Structure only).  
ADRs/glossary while designing → `/domain-modeling`. Living docs + drift → this skill’s full guide. Inline API docs → `/code-comments`. Do not peer-promote documentation-and-adrs.

Minimal README every project should have:

```markdown
# Project Name

One-paragraph description.

## Quick Start
1. Clone
2. Install deps
3. Env: copy `.env.example`
4. Dev server command

## Commands
| Command | Description |
|---------|-------------|
| … | … |

## Architecture
Brief structure + key decisions; link `docs/adr/` / CONTEXT.

## Contributing
Standards, PR process, how agents should load context.
```

Prefer linking durable decisions (ADRs) over restating code. Changelog for consumers lives under `/shipping-and-launch` versioning ref.
