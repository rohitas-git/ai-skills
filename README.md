# AI-Skills Catalog

**Catalog version:** see [`catalog.yaml`](./catalog.yaml) · **Feature log:** [`docs/FEATURE-LOG.md`](./docs/FEATURE-LOG.md) · **ADRs:** [`docs/adr/`](./docs/adr/)

A comprehensive, depth-organized catalog of Claude agent skills for software engineering, code review, system design, documentation, and project management. Skills are hierarchically organized (0-hubs, 1-skills, 2-specialized), discoverable, and symlink-installable into any Claude agent environment.

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
```
Validates catalog structure: SKILL.md presence, depth-prefix, hub membership, **route surface** (`metadata.catalog`, no top-level route keys), lean/sprawl. Prints **`catalog.yaml` version**. Gate PASS = 0 critical. Reports-only; use `/0-skill-manager` to fix.

### `generate-route-index` — Butler skim
```bash
./scripts/generate-route-index
```
Rebuilds `skills/0-butler/references/route-index.md` from live skill `metadata.catalog` (fallback: description + hub membership). Run after place/ingest/organize.

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
→ /1-codebase-review-strategy → /1-code-review
  ├─ Tier the repo (SMALL/MED/LARGE)
  ├─ Focused review per tier
  ├─ Technical debt ranking
  └─ Refactoring roadmap
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

| Name | Description |
|------|-------------|
| **0-butler** | Hub of hubs — navigation for the entire catalog. Use when lost or need orientation. |
| **0-diagnosing-bugs** | Systematic diagnosis loop for hard bugs and performance regressions. |
| **0-grilling** | Relentlessly stress-test a plan, decision, or idea. |
| **0-implement** | Implement a piece of work based on a spec or set of tickets. |
| **0-improve-codebase-architecture** | Scan codebase for deepening opportunities with visual HTML report. |
| **0-learn** | Domain hub for learning — how/why something works (not shipping code). |
| **0-office** | Domain hub for office/media tools (Word, slides, sheets, diagrams, canvas). |
| **0-ponytail** | Force the laziest, shortest, most minimal solution that works. |
| **0-review** | Domain hub for verification (code review, security audit, architecture review). |
| **0-rohitas-vault-wiki** | Steward Rohitas's Notes Obsidian vault — Atlas hubs, Concepts, Inbox, Guides. |
| **0-setup-rohitas-skills** | Configure this repo for engineering skills — issue tracker, labels, docs. |
| **0-skill-creator** | Create, edit, and evaluate agent skills. |
| **0-skill-manager** | Catalog facilities: CRUD skills, organize hubs, place under workflows. |
| **0-triage** | Move issues/PRs through state machine — categorize, verify, grill, brief. |
| **0-wayfinder** | Plan huge work as shared map of decision tickets on issue tracker. |
| **1-anti-sycophancy** | Independent claim assessment; suppress praise/agreement bias; evidence-first. |
| **1-api-and-interface-design** | Design stable APIs and module boundaries (REST, GraphQL, types). |
| **1-browser-testing-with-devtools** | Runtime browser verification via Chrome DevTools MCP (DOM, console, network). |
| **1-ci-cd-and-automation** | Build/test/deploy pipelines and quality gates. |
| **1-clean-craftsmanship** | Q&A reference from Clean Code/Architecture (SOLID, Uncle Bob). |
| **1-code-comments** | Write clear API and surface documentation (JSDoc, docstrings, etc.). |
| **1-code-explainer** | Explain source code at multiple audience levels and depths. |
| **1-code-review** | Multi-axis review of changes — Spec, Standards, Maintainability. |
| **1-codebase-design** | Shared vocabulary for designing deep modules and interfaces. |
| **1-codebase-review-strategy** | Determine repo tier and select optimal review approach per size. |
| **1-coding-standards** | Always-on lean coding standards for naming, modularity, error handling. |
| **1-context-monitor** | Monitor context usage, warn at ~50%, suggest token optimizations. |
| **1-create-skill** | Thin entry for authoring skills (routes to skill-creator + skill-manager). |
| **1-critique** | Explicit rigorous critique / devil's advocate of ideas and reasoning. |
| **1-defuddle** | Extract clean markdown from web pages, removing clutter and navigation. |
| **1-deprecation-and-migration** | Sunset APIs/features and migrate callers safely. |
| **1-diagram-maker** | Create SVG/HTML or Excalidraw diagrams for concepts, flows, architecture. |
| **1-discover-skills** | Help users discover and install agent skills. |
| **1-docx** | Create, read, edit, or manipulate Word documents (.docx files). |
| **1-domain-modeling** | Build and sharpen project domain model — ubiquitous language. |
| **1-doubt-driven-development** | Fresh-context adversarial review of non-trivial decisions. |
| **1-execution-flow-comments** | Write structured Execution Flow comments with numbered steps and branches. |
| **1-frontend-ui-engineering** | Accessible, responsive, production-quality UI (not generic aesthetics). |
| **1-git-commit-helper** | Generate high-quality git commit messages from staged changes. |
| **1-grill-me** | Relentless interview to sharpen a plan or design. |
| **1-grill-with-docs** | Relentless interview that also creates ADRs and glossary as you go. |
| **1-grok-help** | Grok documentation and configuration help (setup, MCP, skills, keybindings). |
| **1-handoff** | Compact current conversation into a handoff document for another agent. |
| **1-hatch-pet** | Create and package Codex-compatible v2 animated pets from art/images. |
| **1-imagine** | How to use image_gen and image_edit in Claude Code (prompt-craft, reference). |
| **1-inline-comments** | Add concise one-line comments above non-obvious code blocks. |
| **1-json-canvas** | Create and edit JSON Canvas files (.canvas) with nodes and connections. |
| **1-karpathy-guidelines** | LLM coding process hygiene: think before coding, simplicity, surgical diffs, goals. |
| **1-learning-explainer** | Structured multi-level explanations with mental models and progressive deep-dive. |
| **1-living-documentation-governor** | Code-synced living documentation — drift checks, grounded Q&A. |
| **1-observability-and-instrumentation** | Logging, metrics, tracing, and alerting for diagnosable production behavior. |
| **1-obsidian-bases** | Create and edit Obsidian Bases (.base files) with views and formulas. |
| **1-obsidian-cli** | Interact with Obsidian vaults — read, search, manage notes and tasks. |
| **1-obsidian-markdown** | Create and edit Obsidian Flavored Markdown (wikilinks, embeds, callouts). |
| **1-performance-optimization** | Measure-first perf work (FE/BE/DB) — Core Web Vitals, N+1 queries, profiling. |
| **1-pi-agent-rust** | Speed up pi_agent_rust development and verification workflows. |
| **1-ponytail-audit** | Whole-repo audit for over-engineering — ranked list of what to delete. |
| **1-ponytail-debt** | Harvest every `0-ponytail:` comment into a debt ledger. |
| **1-ponytail-gain** | Show ponytail's impact — less code, less cost, more speed. |
| **1-ponytail-help** | Quick-reference card for all ponytail modes and commands. |
| **1-pptx** | Create, read, edit, or manipulate PowerPoint presentations (.pptx files). |
| **1-pr-summarizer** | Summarize changes, write PR descriptions, or draft PR comments. |
| **1-project-wiki-manager** | Karpathy-style in-repo project wiki — concept pages, grounded Q&A. |
| **1-prototype** | Build throwaway prototype to sanity-check state model or UI. |
| **1-research** | Investigate a question against high-trust sources; save findings as Markdown. |
| **1-resolving-merge-conflicts** | Resolve in-progress git merge/rebase conflicts. |
| **1-resource-summarizer** | Distill long resources (PDF, video, article) into learning-focused notes. |
| **1-response-effort-calibrator** | Guide response effort and depth based on prompt cues. |
| **1-security-auditor** | Multi-phase security auditor for codebases — OWASP, vulnerability review. |
| **1-session-skill-reflect** | Self-improving skill system — extract learnings, propose/update skill files. |
| **1-shipping-and-launch** | Pre-flight checklist, canary rollout, monitoring, rollback planning. |
| **1-skill-atomize** | Make catalog skills atomic — one job each, hard redirects. |
| **1-skill-linter** | Health-check agent skills for SKILL.md format and chaining. |
| **1-stepdown-rule** | Enforce top-down file layout — callers above callees. |
| **1-story-teacher** | Turn lessons/articles/transcripts into engaging stories that teach invisibly. |
| **1-strategic-compact** | Suggest manual context compaction at logical task intervals. |
| **1-tdd** | Test-driven development — red → green → refactor at agreed seams. |
| **1-teach** | Multi-session teaching workspace (MISSION.md, lessons, learning-records). |
| **1-thinking-steel-manning** | Build strongest version of opposing case before engaging. |
| **1-to-spec** | Turn conversation into spec and publish to issue tracker. |
| **1-to-tickets** | Break plan/spec into tracer-bullet tickets with blocking edges. |
| **1-vault-explain** | Explain a concept from Rohitas's Notes vault for learning. |
| **1-vault-inbox** | Fast-capture notes into Rohitas's Notes Inbox. |
| **1-vault-ingest** | Ingest knowledge into Rohitas's Notes — create/update Concepts. |
| **1-vault-lint** | Health-check vault — broken links, orphans, duplicates, drift. |
| **1-wiki-query** | Answer questions against personal LLM wiki / Obsidian vault. |
| **1-writing-great-skills** | Reference for writing and editing skills well. |
| **1-xlsx** | Create, read, edit, or manipulate spreadsheets (.xlsx, .csv, .tsv). |
| **2-ponytail-review** | Code review focused on over-engineering — what to delete. |
| **2-security-and-hardening** | Harden code against vulnerabilities while building or remediating. |
| **2-software-architect** | Grandmaster architect analysis — current state, trade-offs, impact. |
| **2-verify-work** | Verification subagent — diffs, builds, tests, correctness evaluation. |

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
2. /0-wayfinder (if >1 session: plan decision tickets)
   ↓
3. /1-tdd (red → green → refactor)
   ↓
4. /1-code-review (spec, standards, maintainability)
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
2. /1-codebase-review-strategy (tier the repo, pick review approach)
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

This catalog works with any Claude agent environment that supports the Skill tool:

| Platform | Support | Notes |
|----------|---------|-------|
| **Claude Code (CLI)** | ✅ Full | Primary platform; all skills tested here |
| **Claude Code (VS Code)** | ✅ Full | Symlinks into `~/.claude/skills` |
| **Claude Code (Web)** | ✅ Full | Syncs from `~/.claude/skills` |
| **Cursor** | ✅ Full | Symlink into `~/.cursor/skills` |
| **Grok (Grok Build)** | ✅ Full | Symlink into `~/.grok/skills` |
| **Codex** | ✅ Partial | Symlink into `~/.codex/skills` |
| **Gemini (Antigravity)** | ✅ Partial | Symlink into `~/.gemini/antigravity/skills` |
| Custom agents | ✅ Yes | Symlink into your agent's skills directory |

**Installation:** Run `./scripts/setup.sh` and select targets during setup. Each agent uses its own symlinked copy, so changes in one don't affect others.

---

**Questions?** Start with `/0-butler` for navigation, or check [`skills/CLAUDE.md`](./skills/CLAUDE.md) for detailed invocation rules.
