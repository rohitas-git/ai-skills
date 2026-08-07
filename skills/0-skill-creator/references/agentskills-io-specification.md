# Agent Skills format (agentskills.io harvest)

> **Source:** [agentskills.io/specification](https://agentskills.io/specification) · fetched 2026-08-05  
> **Load when:** drafting portable frontmatter/layout, or reconciling upstream docs with this catalog.  
> **House law wins:** depth-prefix · ADR 0009 route surface · hub membership · lean main — `/0-skill-manager`, `/1-skill-linter`.

Upstream defines the open package shape. This catalog **extends** it; do not place a live skill that only satisfies upstream.

## Package layout

```text
{name}/
├── SKILL.md       # required — frontmatter + body
├── scripts/       # optional — executables
├── references/    # optional — on-demand docs
├── assets/        # optional — templates, data
└── …
```

## Upstream frontmatter

| Field | Req | Rule |
|-------|-----|------|
| `name` | yes | ≤64; `[a-z0-9-]+`; no leading/trailing/double hyphen; **== directory name** |
| `description` | yes | ≤1024; what + when |
| `license` | no | Name or bundled file |
| `compatibility` | no | ≤500; env needs |
| `metadata` | no | string→string map (clients store extras) |
| `allowed-tools` | no | experimental space-separated tools |

Body: free markdown; entire file loads on activate → keep lean; one-level-deep relative links from `SKILL.md`.

**Progressive disclosure (upstream ladder):** metadata always → body on activate → resources on demand. Target body ≲500 lines / ~5k tokens.

Upstream check: `skills-ref validate ./my-skill`.

## House deltas (live `skills/`)

| Topic | Upstream | This catalog |
|-------|----------|--------------|
| Identity | bare kebab | **`{depth}-{slug}`** (`0-` hub … full tree depth) |
| Description | what + when | **Use when / Not for / Hub** contract |
| Route data | free `metadata` | **`metadata.catalog` only** (`hub`, `role`, `when`\|`triggers`, …) — never top-level route keys |
| Auto-invoke | client-defined | Prefer **`disable-model-invocation: true`** unless always-on |
| Membership | — | Hub child required (ADR 0006) |
| Lean | progressive disclosure | Thin router + disclosure map; lint `gate-lean` |
| Citizenship | install anywhere | **`/0-skill-manager` place/ingest** + **`/1-skill-linter` Gate PASS** |

Route surface detail: [skill-route-surface.md](../../0-skill-manager/references/skill-route-surface.md).  
Craft: `/1-writing-great-skills`. Eval ops: [full-guide.md](./full-guide.md).
