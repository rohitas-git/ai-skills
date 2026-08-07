# Authoring patterns (agentskills.io harvest)

> **Source:** [agentskills.io/skill-creation/best-practices](https://agentskills.io/skill-creation/best-practices) · fetched 2026-08-05  
> **Load when:** drafting body content, scoping a skill, or pruning after a real run.  
> **SSOT for vocabulary:** parent [SKILL.md](../SKILL.md) + [GLOSSARY.md](../GLOSSARY.md). Prefer house terms when both cover the same idea.  
> **Cousins:** [anthropic-best-practices.md](./superpowers/anthropic-best-practices.md) · eval/scripts/spec under `/0-skill-creator`.

**Leading test for every line you add:** would the agent get this wrong without it? If no → **no-op** — cut. If unsure → run a real task and watch the **transcript**, not only the final output.

## Ground in expertise (not generic “best practices”)

A skill earns its keep from *project* knowledge: your APIs, gotchas, recovery steps. Generic training prose is **sediment**.

| Source | What to harvest |
|--------|-----------------|
| Hands-on task with the agent | Steps that worked · corrections you made · I/O shapes · facts you had to supply |
| Project artifacts | Runbooks, schemas, review comments, fix patches, incident writeups |

**Completion criterion for a first draft:** every non-obvious project fact you used in the session is either in `SKILL.md` or behind a **context pointer** that names *when* to load it.

## Refine under eval pressure

One **execute → revise** pass beats three speculative edits. Read traces: vague steps (agent thrashing), dead branches (agent follows irrelevant instructions), menus without a **default**.

Structured loops: [agentskills-io-evaluating-skills.md](../../0-skill-creator/references/agentskills-io-evaluating-skills.md) · house ops in skill-creator [full-guide](../../0-skill-creator/references/full-guide.md).

## Spend **context load** on the ladder

Once activated, the body competes with the whole window. Same fight as house **information hierarchy**:

| Keep in `SKILL.md` | Disclose |
|--------------------|----------|
| Steps every run needs | Domain depth only some **branches** need |
| **Gotchas** the agent must see *before* the failure | Large schemas, rare edge catalogs |
| One default path + short escape | Alternate tools as equal menus |

- **Coherent unit** — one composable job (query+format may be one unit; +DBA is usually **sprawl**).  
- **Moderate detail** — stepwise + one worked example beats exhaustive edge catalogs.  
- **Progressive disclosure** — pointer wording is the trigger: `Read references/api-errors.md when the API returns non-200`, not “see references/”.

House ladder and disclosure mechanics: parent skill § Information hierarchy.

## Calibrate control (fragility)

| Fragility | Instruction style |
|-----------|-------------------|
| Low (many valid approaches) | Freedom + *why* — agent adapts |
| High (exact sequence, migrations) | Prescriptive command; fixed flags |

**Default, not menu** — one tool path; mention the alternate only when the default fails.  
**Procedure, not one-shot answer** — teach the class of problem; templates/constraints can still be specific.

## Patterns (use when they earn tokens)

| Pattern | When it pays |
|---------|----------------|
| **Gotchas** | Environment facts that defeat reasonable defaults — co-locate in `SKILL.md` if the agent must see them first |
| **Template** | Fixed output shape (inline if short; `assets/` if long/conditional) |
| **Checklist** | Multi-step with gates — each item is a **completion criterion** |
| **Validation loop** | Work → validate → fix until pass → then continue |
| **Plan-validate-execute** | Batch/destructive: structured plan file → script check against source of truth → execute |
| **Bundled script** | Same helper reinvented across runs → `scripts/` once — [using-scripts](../../0-skill-creator/references/agentskills-io-using-scripts.md) |

When a user correction recurs, add it as a **gotcha** (cheap iterative improve).

## Related

| Need | Where |
|------|--------|
| House craft vocabulary | [../SKILL.md](../SKILL.md) · [GLOSSARY.md](../GLOSSARY.md) |
| Description / trigger eval | [optimizing-descriptions](../../0-skill-creator/references/agentskills-io-optimizing-descriptions.md) |
| Output evals | [evaluating-skills](../../0-skill-creator/references/agentskills-io-evaluating-skills.md) |
| Format + house deltas | [specification](../../0-skill-creator/references/agentskills-io-specification.md) |
| Place / lint | `/0-skill-manager` · `/1-skill-linter` |
