# Scripts agents can run (agentskills.io harvest)

> **Source:** [agentskills.io/skill-creation/using-scripts](https://agentskills.io/skill-creation/using-scripts) · fetched 2026-08-05  
> **Load when:** bundling helpers, writing one-off tool commands, or designing CLI for non-interactive agents.  
> **Cousins:** [specification](./agentskills-io-specification.md) (`scripts/`) · [evaluating-skills](./agentskills-io-evaluating-skills.md) (when traces show reinvention) · [best-practices](../../1-writing-great-skills/references/agentskills-io-best-practices.md).

**Leading word: agentic CLI** — scripts and one-offs that a non-interactive agent can finish without a human at the TTY.

## When to one-off vs bundle

| Situation | Move |
|-----------|------|
| Existing package, few flags | One-off in `SKILL.md` via runner (`uvx` / `npx` / …) |
| Command hard to get right first try | Tested file under `scripts/` |
| Same helper reinvented every eval run | Bundle once; instruct **run**, not re-author |

Pin versions. State prerequisites in body or `compatibility`. Paths are **relative to skill root**.

### Runners (pick default for the stack)

| Default | Stack |
|---------|--------|
| `uvx pkg@ver` / `uv run script` | Python |
| `npx pkg@ver` | Node |
| `bunx` / `deno run` / `go run` | Only when that runtime is the environment |

`pipx run` is a fine Python alternate when uv is missing.

### Point from SKILL.md

List scripts, then give exact commands (agent discovers by reading, not by guessing):

```markdown
## Available scripts
- `scripts/validate.sh` — config validation
- `scripts/process.py` — transform input

## Steps
1. `bash scripts/validate.sh "$INPUT_FILE"`
2. `python3 scripts/process.py --input results.json`
```

## Self-contained deps

Prefer scripts that install their own deps so the agent skips a separate setup step.

**Python (PEP 723)** — `# /// script` + `dependencies = […]`; run with `uv run scripts/extract.py`.

**Deno** — `npm:` / `jsr:` imports with versions.  
**Bun** — pin in import path; auto-install when no `node_modules`.  
**Ruby** — `bundler/inline` + explicit gem versions.

## Agentic CLI design

| Rule | Why |
|------|-----|
| **No interactive prompts** | Agent shells hang forever on TTY input — flags / env / stdin only |
| **`--help` is the interface doc** | Short description, flags, examples (context load) |
| **Errors that teach the next attempt** | What failed · expected set · received value |
| **Structured stdout** | JSON/CSV; diagnostics on **stderr** |
| **Idempotent create** | Create-if-absent beats fail-on-duplicate under retries |
| **Closed inputs** | Enums; reject ambiguity instead of guessing |
| **Destructive = explicit** | `--dry-run`; `--force` / `--confirm` when risk warrants |
| **Exit codes mean something** | Document in `--help` |
| **Bounded output** | Harnesses truncate; default summary / `--offset` / require `--output` for bulk |

**Completion criterion for a new script:** non-interactive happy path + clear error on bad flags + `--help` + agent can parse success from stdout alone.
