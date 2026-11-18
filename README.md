# AI-Skills Catalog

**Catalog version:** see [`catalog.yaml`](./catalog.yaml) · **Feature log:** [`docs/FEATURE-LOG.md`](./docs/FEATURE-LOG.md) · **ADRs:** [`docs/adr/`](./docs/adr/)

A comprehensive, depth-organized catalog of Codex and Claude agent skills for software engineering, code review, system design, documentation, and project management. Skills are hierarchically organized (0-hubs, 1-skills, 2-specialized), discoverable, and symlink-installable into supported agent environments.

## Table of contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Catalog Structure & Naming](#catalog-structure-naming)
  - [Depth-Based Organization](#depth-based-organization)
  - [Why This Naming Convention?](#why-this-naming-convention)
  - [Example Flow](#example-flow)
- [Scripts](#scripts)
  - [`setup.sh` — Interactive Installation](#setupsh-interactive-installation)
  - [`sync-skills-symlinks.sh` — Flatten & Link](#sync-skills-symlinkssh-flatten-link)
  - [`lint-skills` — Catalog Health Check](#lint-skills-catalog-health-check)
  - [`generate-route-index` — Butler skim](#generate-route-index-butler-skim)
  - [`evaluate-skills` — Cross-runtime evidence](#evaluate-skills-cross-runtime-evidence)
- [Useful Workflows for Engineers & PMs](#useful-workflows-for-engineers-pms)
  - [For Software Engineers](#for-software-engineers)
  - [For Technical Project Managers](#for-technical-project-managers)
- [All Skills (with Brief Descriptions)](#all-skills-with-brief-descriptions)
- [Quick Reference](#quick-reference)
  - [Common Commands](#common-commands)
  - [Most-Used Skills](#most-used-skills)
- [Example Workflows](#example-workflows)
  - [Feature Development (Happy Path)](#feature-development-happy-path)
  - [Bug Diagnosis & Fix](#bug-diagnosis-fix)
  - [Code Audit & Refactoring](#code-audit-refactoring)
  - [Project Triage & Routing](#project-triage-routing)
- [Configuration Reference](#configuration-reference)
  - [Default Config: `symlink-targets.local.json`](#default-config-symlink-targetslocaljson)
- [Contributing](#contributing)
  - [Creating a New Skill](#creating-a-new-skill)
  - [Editing Existing Skills](#editing-existing-skills)
  - [Testing Locally](#testing-locally)
- [Troubleshooting](#troubleshooting)
  - [Symlinks Not Appearing](#symlinks-not-appearing)
  - ["Config file not found"](#config-file-not-found)
  - [Skills Not Discoverable in Agent](#skills-not-discoverable-in-agent)
  - ["Skill name mismatch" from lint](#skill-name-mismatch-from-lint)
- [Related Resources](#related-resources)
  - [Documentation](#documentation)
  - [Skill Development](#skill-development)
  - [Navigation & Discovery](#navigation-discovery)
  - [Learning & Knowledge](#learning-knowledge)
- [Agent Compatibility](#agent-compatibility)


## Overview

**What this is:** A curated collection of reusable, battle-tested agent workflows and domain hubs that help you:
- Diagnose and fix bugs faster with systematic debugging
- Review code across multiple dimensions (correctness, maintainability, security)
- Design systems and architecture with expert guidance
- Manage projects, triage issues, and track work
- Automate skill discovery and installation across agent directories

**Organized as:**
- **0-level hubs**: Domain routers (learn, review, office, ponytail, etc.)
- **1-level skills**: Focused, single-job workflows (code-review, tdd, api-design, etc.)
- **2-level specialists**: Deep expertise for specific scenarios (security-hardening, software-architect, etc.)

Canonical catalog lives under [`skills/`](./skills/). See [`skills/README.md`](./skills/README.md) and [`skills/CLAUDE.md`](./skills/CLAUDE.md) for catalog structure and invocation details.

For common tasks, start with the [daily workflow guide](./guidelines/catalog/daily-workflows.md).
Use `?? show me the playbooks` to browse [Butler's playbooks](./skills/0-butler/references/playbooks.md)
and find the specialist, tool and verification steps for a specific task.
Its recipes are generated from one source and validated against live routes. Local helpers are documented
in [adopted pstack tooling](./guidelines/catalog/pstack-tooling.md).

## Getting Started

**One-time setup:**
```bash
./scripts/setup.sh
```
This interactive script:
1. Detects or clones the AI-Skills repo
2. Lets you select which skills to install
3. Picks target agent directories (`~/.claude/skills`, `~/.cursor/skills`, etc.)
4. Symlinks everything into place

**Then navigate via:**
- `/0-butler` — main hub of hubs (when lost or need orientation)
- `/0-wayfinder` — plan huge work (more than one session)
- `/0-triage` — move issues through a state machine
- `/0-skill-manager` — catalog CRUD and organization

## Catalog Structure & Naming

### Depth-Based Organization

The catalog organizes skills by **depth**: how specialized or meta they are.

**0-level (Hubs):**
- Domain routers and entry points
- "When should I use which skill?"
- Examples: `0-review` (all verification modes), `0-learn` (all learning workflows), `0-office` (all document tools)
- Act as **switchboards** — they route you to the right 1-level skill

**1-level (Core Skills):**
- Single, focused workflows
- "I want to do X" (code review, write TDD tests, design an API)
- 90+ skills: the workhorse catalog
- Reusable across projects, self-contained

**2-level (Specialists):**
- Deep expertise for high-stakes scenarios
- "I need expert judgment on X" (security hardening, software architecture, ponytail review)
- Small, high-leverage set

### Why This Naming Convention?

**Depth prefixes (`0-`, `1-`, `2-`) solve a real problem:**

1. **No overwhelm** — when you invoke `/0-butler`, you get routed to a domain (learn, review, office), not 150 skills at once
2. **Composable** — a 0-hub chains to the right 1-skills, which may chain to 2-specialists, building complexity as needed
3. **Discovery** — skills naturally sort (`ls /skills` shows 0-* first, then 1-*, then 2-*), matching how people think
4. **Metadata expressible** — chains (prev/next, hub membership) become checkable by lint
5. **Dual membership** — a skill like `1-code-review` can live under both `0-review` and be invoked standalone

### Example Flow

```
User: "Review this PR"
  ↓
/0-review (hub, asks: what kind? correctness? performance? security?)
  ↓
Routes to one or more:
  • /1-code-review (multi-axis: spec, standards, maintainability)
  • /1-security-auditor (security-focused audit)
  • /2-ponytail-review (over-engineering audit)
  • /1-performance-optimization (perf-focused)
  ↓
Each skill chains to sub-skills if deeper work needed
```

This prevents skill sprawl while keeping everything discoverable.

## Scripts

### `setup.sh` — Interactive Installation
```bash
./scripts/setup.sh
```
Detects existing clone, asks which skills to install, selects target directories, generates config, previews sync, and symlinks everything. Run once to configure your environment. Rerun to reconfigure.

**What it does:**
- Auto-detects repo root or prompts for path/clone destination
- Discovers all skills in `skills/` and `inbox/`
- Filters by your selection (all by default)
- Lets you deselect target directories or add custom ones
- Writes `scripts/symlink-targets.local.json` config
- Previews changes with `--dry-run`
- Confirms and runs actual symlink sync

### `sync-skills-symlinks.sh` — Flatten & Link
```bash
./scripts/sync-skills-symlinks.sh --config scripts/symlink-targets.local.json [--dry-run] [--verbose]
```
Reads config, discovers skills, and symlinks them into target agent directories. Used by `setup.sh` but can be run standalone to resync after catalog updates.

**Flags:**
- `--config FILE` — config JSON (required; see setup.sh output)
- `--dry-run` — show what would happen, don't change anything
- `--verbose` — print detailed operations

### `lint-skills` — Catalog Health Check
```bash
./scripts/lint-skills
./scripts/lint-skills --format json
```
Validates catalog structure: SKILL.md presence, depth-prefix, hub membership, **route surface** (`metadata.catalog`, no top-level route keys), lean/sprawl. Prints **`catalog.yaml` version**. Gate PASS = 0 critical. Reports-only; use `/0-skill-manager` to fix.

### `generate-route-index` — Butler skim
```bash
./scripts/generate-route-index
./scripts/generate-route-index --check
```
Rebuilds the model-facing `route-index.md` and tooling-facing `route-index.json` from live skill `metadata.catalog` (fallback: description + hub membership). Run after place/ingest/organize; use `--check` in verification.

### `evaluate-skills` — Cross-runtime evidence
```bash
./scripts/evaluate-skills validate guidelines/catalog/evals/ai-native-cases.json
```
Validates frozen routing and behavior cases without provider calls. Explicit `run --execute` commands use installed Codex or Claude against disposable fixtures and write raw evidence only under `.scratch/`; see [`guidelines/catalog/ai-native-evaluation.md`](./guidelines/catalog/ai-native-evaluation.md).

## Useful Workflows for Engineers & PMs

### For Software Engineers

**1. Bug Diagnosis & Fix**
```
User: "This endpoint times out randomly"
→ /0-diagnosing-bugs
  ├─ Systematically gather reproduction steps
  ├─ Isolate root cause (not symptom)
  ├─ Propose minimal fix
  └─ Verify with tests
```

**2. Feature Development (TDD)**
```
User: "Build login with OAuth"
→ /1-tdd
  ├─ Write failing test (red)
  ├─ Implement minimum to pass (green)
  ├─ Refactor (clean, optimize)
  └─ Verify production readiness
```

**3. Pull Request Review**
```
User: "Review this PR"
→ /1-code-review or /2-ponytail-review
  ├─ Spec fidelity (matches ticket/PRD)
  ├─ Standards (repo conventions, smell baseline)
  ├─ Maintainability (structure, complexity)
  ├─ Security & performance
  └─ Over-engineering / tech debt
```

**4. Architecture & System Design**
```
User: "Design the payment system"
→ /2-software-architect
  ├─ Current state analysis
  ├─ Core pillars vs. proposed design
  ├─ Trade-offs & risks
  ├─ Impact on scalability, latency, maintainability
  └─ Implementation strategy
```

**5. Performance Optimization**
```
User: "This page loads in 5 seconds"
→ /1-performance-optimization
  ├─ Profile (FE/BE/DB bottleneck?)
  ├─ Measure baseline
  ├─ Optimize targeted layer
  └─ Verify improvement
```

### For Technical Project Managers

**1. Issue Triage & Routing**
```
User: "We have 200 issues, no categorization"
→ /0-triage
  ├─ Categorize (bug, feature, tech-debt)
  ├─ Severity & effort estimate
  ├─ Grill stakeholders if unclear
  └─ Write agent-ready briefs & route to team
```

**2. Large Work Planning**
```
User: "We're rebuilding auth (3-month project)"
→ /0-wayfinder
  ├─ Break into decision tickets
  ├─ Map blocking edges
  ├─ Resolve one by one
  └─ Clear path to launch
```

**3. Spec to Tickets**
```
User: "Turn this Slack thread into work"
→ /1-to-tickets or /1-to-spec
  ├─ Synthesize conversation
  ├─ Create tracer-bullet tickets
  ├─ Declare blocking edges
  └─ Post to issue tracker (Linear, GitHub, etc.)
```

**4. Code Health Audit**
```
User: "Is this codebase maintainable?"
→ /1-codebase-review-strategy
  ├─ Pin the exact repository candidate and exclusions
  ├─ Build risk-based coverage and evidence plan
  ├─ Recommend the smallest review specialist
  └─ Run that review only when separately/originally authorized
```

**5. Shipping & Launch**
```
User: "We're ready to ship payment"
→ /1-shipping-and-launch
  ├─ Pre-flight checklist
  ├─ Canary rollout strategy
  ├─ Monitoring & alerts
  └─ Rollback plan
```

## All Skills (with Brief Descriptions)

Use the [generated skill index](./skills/0-butler/references/route-index.md) for current skills, owning domains, use cases, exclusions, and handoffs. Its entries come from live skill metadata and hub membership.

The [wiki index](./wikis/index.md) provides a domain view, and the [daily workflow guide](./guidelines/catalog/daily-workflows.md) provides task examples. These indexes replace a separately maintained skill table here.

## Quick Reference

### Common Commands

```bash
# Initial setup
./scripts/setup.sh

# Resync after catalog updates
./scripts/sync-skills-symlinks.sh --config scripts/symlink-targets.local.json

# Validate catalog structure
./scripts/lint-skills

# Preview symlink changes (dry-run)
./scripts/sync-skills-symlinks.sh --config scripts/symlink-targets.local.json --dry-run --verbose
```

### Most-Used Skills

| Scenario | Skill |
|----------|-------|
| Lost, need navigation | `/0-butler` |
| Fix a broken thing | `/0-diagnosing-bugs` |
| Review a PR | `/1-code-review` or `/2-ponytail-review` |
| Write feature (TDD) | `/1-tdd` |
| Design system/API | `/1-api-and-interface-design` or `/2-software-architect` |
| Categorize issues | `/0-triage` |
| Plan huge work | `/0-wayfinder` |
| Turn spec into tickets | `/1-to-tickets` or `/1-to-spec` |
| Audit codebase | `/1-codebase-review-strategy` |
| Ship & deploy | `/1-shipping-and-launch` |

## Example Workflows

### Feature Development (Happy Path)

```
1. User: "Build OAuth login"
   ↓
2. /0-wayfinder (if decision fog spans sessions: chart/advance one map operation)
   ↓
3. /1-to-spec → /1-to-tickets when the map is settled and delivery is separately requested
   ↓
4. /0-implement (choose the fitting evidence loop; /1-tdd only when suitable)
   ↓
5. /1-code-review (spec, standards, maintainability)
   ↓
5. /2-security-and-hardening (auth-specific hardening)
   ↓
6. /1-shipping-and-launch (rollout & monitoring)
```

### Bug Diagnosis & Fix

```
1. User: "Endpoint times out randomly"
   ↓
2. /0-diagnosing-bugs (systematic reproduction & root cause)
   ↓
3. /1-tdd (add failing test for bug)
   ↓
4. /0-ponytail (simplest fix, not symptom patch)
   ↓
5. /1-code-review or /2-ponytail-review (verify no regressions)
```

### Code Audit & Refactoring

```
1. User: "Is this codebase maintainable?"
   ↓
2. /1-codebase-review-strategy (pin the candidate and plan risk-based review coverage)
   ↓
3. /1-code-review (multi-axis review)
   ↓
4. /0-improve-codebase-architecture (visual report of deepening opportunities)
   ↓
5. /0-grilling (stress-test refactoring plan)
```

### Project Triage & Routing

```
1. User: "200 unorganized issues, help categorize"
   ↓
2. /0-triage (categorize, estimate, grill if unclear)
   ↓
3. /1-to-tickets (convert to agent-ready briefs)
   ↓
4. /0-skill-manager (organize into catalogs/inboxes)
```

## Configuration Reference

### Default Config: `symlink-targets.local.json`

After running `./scripts/setup.sh`, your config looks like:

```json
{
  "source": "/path/to/ai-skills/skills",
  "discoverPackages": ["skills", "inbox"],
  "neverDiscover": ["archive", "hubs", "guidelines", "wikis", "vendor", ".scratch", ".system", ".claude"],
  "nestedSkillRoots": [],
  "ingestDestination": "inbox",
  "include": [
    "0-butler",
    "1-code-review",
    "1-tdd"
  ],
  "targets": [
    "~/.claude/skills",
    "~/.cursor/skills"
  ]
}
```

**Fields:**
- `source` — path to `skills/` directory
- `discoverPackages` — where to look for skills (usually `["skills", "inbox"]`)
- `neverDiscover` — exclude archive/vendor/system dirs
- `nestedSkillRoots` — (unused; for future expansion)
- `ingestDestination` — where new skills land (inbox)
- `include` — specific skills (empty = all); set by setup.sh
- `targets` — where to symlink (e.g., `~/.claude/skills`, `~/.cursor/skills`)

Edit manually to add/remove targets or re-run `./scripts/setup.sh` to reconfigure.

## Contributing

### Creating a New Skill

```bash
cd skills/skills
mkdir 1-my-skill
cat > 1-my-skill/SKILL.md << 'EOF'
---
name: 1-my-skill
description: >
  What this skill does in one sentence. When to use it.
  Can span multiple lines.
prev: 1-related-skill
next: 1-next-skill
---
<skill body here>
EOF
```

Then:
1. Run `/1-create-skill` to refine the body
2. Run `/0-skill-manager` to place under a domain hub
3. Run `./scripts/lint-skills` to validate structure
4. Run `./scripts/sync-skills-symlinks.sh --dry-run` to preview

### Editing Existing Skills

```bash
# Edit skill metadata or body
vim skills/skills/1-my-skill/SKILL.md

# Lint for issues
./scripts/lint-skills

# Validate with /0-skill-manager or /1-skill-linter
```

### Testing Locally

```bash
# Validate catalog structure
./scripts/lint-skills

# Preview symlinks (without applying)
./scripts/sync-skills-symlinks.sh --config scripts/symlink-targets.local.json --dry-run --verbose

# Sync to test directories
./scripts/sync-skills-symlinks.sh --config scripts/symlink-targets.local.json
```

## Troubleshooting

### Symlinks Not Appearing

**Problem:** Ran `setup.sh` but skills don't show up in agent.

**Solution:**
1. Verify target directory exists: `ls ~/.claude/skills`
2. Check symlinks were created: `ls -la ~/.claude/skills | grep "^l"`
3. Run with `--verbose` to see what happened:
   ```bash
   ./scripts/sync-skills-symlinks.sh --config scripts/symlink-targets.local.json --verbose
   ```
4. Rerun setup: `./scripts/setup.sh`

### "Config file not found"

**Problem:** `sync-skills-symlinks.sh` says config doesn't exist.

**Solution:**
1. Run `./scripts/setup.sh` (generates `symlink-targets.local.json`)
2. Or manually create config (see Configuration Reference above)
3. Ensure path is correct: `ls scripts/symlink-targets.local.json`

### Skills Not Discoverable in Agent

**Problem:** Skills symlinked but agent doesn't see them.

**Solution:**
1. Restart your agent (CLI, VS Code, etc.) — agents cache skill directories on startup
2. Verify symlink points to correct directory: `ls -la ~/.claude/skills/0-butler`
3. Check skill name matches invocation: `/0-butler` (with dash, matches `0-butler/SKILL.md` name field)

### "Skill name mismatch" from lint

**Problem:** `./scripts/lint-skills` complains about skill naming.

**Solution:**
- Skill directory must match `name:` in SKILL.md frontmatter
- Depth prefix (`0-`, `1-`, `2-`) must match the directory structure
- Run `/0-skill-manager` to fix structurally; use `/1-skill-linter` for reports

## Related Resources

### Documentation
- **[`skills/README.md`](./skills/README.md)** — Detailed catalog structure, how skills are organized, depth/hub rules
- **[`skills/CLAUDE.md`](./skills/CLAUDE.md)** — Skill invocation rules, chaining patterns, hub membership

### Skill Development
- **[`0-skill-creator`](./skills/skills/0-skill-creator/SKILL.md)** — Author new skills from scratch
- **[`0-skill-manager`](./skills/skills/0-skill-manager/SKILL.md)** — Organize, place, ingest skills into catalog
- **[`1-skill-linter`](./skills/skills/1-skill-linter/SKILL.md)** — Validate skill health & structure
- **[`1-writing-great-skills`](./skills/skills/1-writing-great-skills/SKILL.md)** — Principles for readable, predictable skills

### Navigation & Discovery
- **[`0-butler`](./skills/skills/0-butler/SKILL.md)** — Main hub (when lost or need orientation)
- **[`1-discover-skills`](./skills/skills/1-discover-skills/SKILL.md)** — Find skills for a specific task

### Learning & Knowledge
- **[`0-rohitas-vault-wiki`](./skills/skills/0-rohitas-vault-wiki/SKILL.md)** — Rohitas's Notes Obsidian vault (concepts, guides, archives)
- **[`1-learning-explainer`](./skills/skills/1-learning-explainer/SKILL.md)** — Structured explanations at multiple levels

## Agent Compatibility

Primary invocation syntax is `$skill-name` in Codex and `/skill-name` in Claude Code. Invoke `/0-butler` only for genuine ambiguity or catalog orientation; direct tasks should load the smallest matching skill.

| Platform | Support | Notes |
|----------|---------|-------|
| **Codex CLI** | ✅ Verified primary | Ten frozen routing/behavior cases passed on 0.154.0 |
| **Claude Code CLI** | ✅ Verified primary | Ten frozen routing/behavior cases passed on 2.1.226 |
| **Claude Code integrations** | Installable | Uses `~/.claude/skills`; not covered by the CLI evaluation |
| **Cursor, Gemini, Grok, Kiro, Zcode** | Installable, unverified | Symlink targets exist; no runtime behavior claim is made |
| Custom agents | Format-compatible | Requires host support for Agent Skills-compatible packages |

Codex may shorten skill descriptions when the full catalog is installed because its skill-context budget is finite. If that warning appears, rerun setup and select only Butler plus the domains and specialist skills you actively use; the catalog source and route index remain complete.

**Installation:** Run `./scripts/setup.sh` and select targets during setup. Each agent uses its own symlinked copy, so changes in one don't affect others.

---

**Questions?** Start with `$0-butler` in Codex or `/0-butler` in Claude for navigation. Repository rules live in [`CLAUDE.md`](./CLAUDE.md).

Detailed pstack principles, functional skills and playbook adoption: [review and method guide](./guidelines/catalog/pstack-methods-review-2026-11-18.md). The live owners retain their existing routing and effect boundaries.
The [skill-by-skill follow-up](./guidelines/catalog/pstack-skill-by-skill-review.md) covers every skill at the pinned revision, including the three Benny automation recipes.
