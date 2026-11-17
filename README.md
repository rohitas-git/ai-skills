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

| Name | Description |
|------|-------------|
| **0-agent-engineering** | Route agent evaluations, tools, MCP servers, oversight, telemetry, and security. |
| **0-butler** | Hub of hubs — navigation for the entire catalog. Use when lost or need orientation. |
| **0-devops** | Route infrastructure, platform, delivery, reliability, incident, and compliance operations. |
| **0-marketing** | Route marketing strategy, research, conversion, content, search, paid media, lifecycle, growth, and sales work. |
| **0-diagnosing-bugs** | Systematic diagnosis loop for hard bugs and performance regressions. |
| **0-grilling** | Relentlessly stress-test a plan, decision, or idea. |
| **0-git** | Route safe Git workflows: worktrees, atomic commits, conflicts, and branch completion. |
| **0-implement** | Implement a piece of work based on a spec or set of tickets. |
| **0-improve-codebase-architecture** | Scan codebase for deepening opportunities with visual HTML report. |
| **0-learn** | Domain hub for learning — how/why something works (not shipping code). |
| **0-office** | Route one document, media, extraction, canvas, pet, or internal-communication artifact to one leaf. |
| **0-ponytail** | Explicit coding-only overlay for the smallest correct, repository-aligned solution. |
| **0-review** | Domain hub for verification (code review, security audit, architecture review). |
| **0-rohitas-vault-wiki** | Steward Rohitas's Notes Obsidian vault — Atlas hubs, Concepts, Inbox, Guides. |
| **0-setup-rohitas-skills** | Configure this repo for engineering skills — issue tracker, labels, docs. |
| **0-skill-creator** | Author or evaluate one pinned skill-body candidate; placement stays separate. |
| **0-skill-manager** | Apply one bounded catalog change-set or route a read-only catalog operation. |
| **0-triage** | Route one raw-intake snapshot, assessment, or approved transition. |
| **0-wayfinder** | Route one multi-session uncertainty-map operation. |
| **1-agent-evaluation** | Design evaluation sets, graders, baselines, and release gates for agents. |
| **1-ai-platform-operations** | Operate model serving, RAG, GPU, caching, registry, and LLMOps infrastructure. |
| **1-action-first-output** | Explicit, reversible session mode for action-first results, visible progress, and small next steps. |
| **1-anti-sycophancy** | Independent claim assessment; suppress praise/agreement bias; evidence-first. |
| **1-api-and-interface-design** | Design stable APIs and module boundaries (REST, GraphQL, types). |
| **1-bro** | Re-explain the last assistant reply in plain language (`/bro`). |
| **1-browser-testing-with-devtools** | Runtime browser verification via Chrome DevTools MCP (DOM, console, network). |
| **1-brand** | Route one brand request to guideline authoring, read-only review, or context extraction. |
| **2-brand-guidelines** | Draft or apply one evidence-backed brand-guideline contract. |
| **2-brand-review** | Read-only review one candidate against one approved brand contract. |
| **2-brand-context-extract** | Extract one minimal brand context packet for one named consumer. |
| **1-user-research** | Route one user-research request to study planning or completed-evidence synthesis. |
| **2-user-research-plan** | Author one decision-linked research protocol without executing the study. |
| **2-user-research-synthesis** | Synthesize one fixed participant-evidence set with provenance, dissent, and privacy limits. |
| **1-ci-cd-and-automation** | Build/test/deploy pipelines and quality gates. |
| **1-cloud-platform-operations** | Operate AWS, Azure, GCP, and Cloudflare managed resources. |
| **1-clean-craftsmanship** | Explain maintainability and Clean Code/Architecture principles with practical trade-offs. |
| **1-code-comments** | Assess or edit language-native documentation for one public/exported code surface. |
| **1-code-explainer** | Explain source code at multiple audience levels and depths. |
| **1-code-review** | Multi-axis review of changes — Spec, Standards, Maintainability. |
| **1-complete-pr-review** | Comprehensive, risk-weighted, read-only review of one fixed pull request. |
| **1-codebase-design** | Shared vocabulary for designing deep modules and interfaces. |
| **1-codebase-review-strategy** | Produce one risk-based coverage and evidence plan for an unfamiliar codebase. |
| **1-coding-standards** | Always-on lean coding standards for naming, modularity, and comments. |
| **1-error-handling** | Failure contracts, TS/JS errors, safe recovery, and cleanup. |
| **1-compliance-engineering** | Translate compliance obligations into technical controls and evidence. |
| **1-container-platform-operations** | Operate containers, registries, Kubernetes, Helm, Kustomize, and GitOps. |
| **1-context-monitor** | Monitor context usage, warn at ~50%, suggest token optimizations. |
| **1-constraint-driven-development** | Define measurable quality floors and detect attempts to weaken them. |
| **1-create-skill** | Thin entry that returns one new body candidate through skill-creator. |
| **1-critique** | Explicit rigorous critique / devil's advocate of ideas and reasoning. |
| **1-defuddle** | Extract clean markdown from web pages, removing clutter and navigation. |
| **1-deprecation-and-migration** | Sunset APIs/features and migrate callers safely. |
| **1-diagram-maker** | Create SVG/HTML or Excalidraw diagrams for concepts, flows, architecture. |
| **1-discover-skills** | Discover and vet external skill candidates without installing them. |
| **1-docx** | Create, read, edit, or manipulate Word documents (.docx files). |
| **1-domain-modeling** | Build and sharpen project domain model — ubiquitous language. |
| **1-doubt-driven-development** | One read-only adversarial pass over a consequential claim or decision. |
| **1-database-and-storage-operations** | Operate databases, durable storage, backups, and restore paths. |
| **1-execution-flow-comments** | Assess or edit one explicitly requested numbered flow block for one function. |
| **1-explain-with-example** | Explain selected material with grounded lenses, one example, and a non-executing dry run. |
| **1-frontend-ui-engineering** | Accessible, responsive, production-quality UI (not generic aesthetics). |
| **1-atomic-git-commits** | Partition changes into small, independently understandable and revertible verified commits. |
| **1-grill-me** | Relentless interview to sharpen a plan or design. |
| **1-grill-with-docs** | Relentless interview that also creates ADRs and glossary as you go. |
| **1-graphify** | Build or query an explicitly requested local Graphify codebase graph; no install or persistent behavior by default. |
| **1-grok-help** | Grok documentation and configuration help (setup, MCP, skills, keybindings). |
| **1-handoff** | Compact current conversation into a handoff document for another agent. |
| **1-hatch-pet** | Route one Codex v2 pet build, repair, validation, or local-install operation. |
| **2-hatch-pet-build** | Build one new validated v2 pet candidate without installation. |
| **2-hatch-pet-repair** | Repair one verified pet defect in a copied candidate. |
| **2-hatch-pet-validate** | Read-only validate one immutable v2 pet atlas or package. |
| **2-hatch-pet-install** | Explicitly install one already validated pet candidate locally. |
| **1-human-in-the-loop** | Design approval gates, escalation paths, and human oversight for agents. |
| **1-identity-and-secrets-management** | Operate IAM, SSO, access reviews, KMS, Vault, and secret lifecycle. |
| **1-imagine** | Generate or edit one raster result through the current host image capability. |
| **1-impeccable** | Run one explicit current-installed Impeccable command on one pinned UI surface. |
| **1-inline-comments** | Assess or edit one concise why/constraint comment for one internal block. |
| **1-infrastructure-as-code** | Design and verify Terraform, OpenTofu, CloudFormation, and Bicep. |
| **1-incident-response** | Coordinate active production incident containment, recovery, and evidence. |
| **1-json-canvas** | Create and edit JSON Canvas files (.canvas) with nodes and connections. |
| **1-karpathy-guidelines** | LLM coding process hygiene: think before coding, simplicity, surgical diffs, goals. |
| **1-learning-explainer** | Structured multi-level explanations with mental models and progressive deep-dive. |
| **1-living-documentation-governor** | Govern a pinned code↔canonical-doc contract: drift assessment, scoped updates, and honest trigger enforcement. |
| **1-mcp-server-building** | Design, implement, and validate MCP servers and tool manifests. |
| **1-marketing-ab-testing** | Plan and assess one marketing A/B experiment. |
| **1-marketing-ad-creative** | Draft and iterate paid-ad creative. |
| **1-marketing-ads** | Plan or audit one paid-advertising campaign. |
| **1-marketing-ai-seo** | Improve one site's visibility in AI-generated search answers. |
| **1-marketing-analytics** | Design or audit marketing tracking and measurement. |
| **1-marketing-aso** | Audit or improve one app-store listing. |
| **1-marketing-attribution** | Analyze which marketing activity drives conversion or revenue. |
| **1-marketing-churn-prevention** | Design one customer-retention or cancellation intervention. |
| **1-marketing-co-marketing** | Plan one co-marketing or partner campaign. |
| **1-marketing-cold-email** | Draft one B2B cold-email sequence. |
| **1-marketing-community-marketing** | Plan one community-led marketing program. |
| **1-marketing-competitor-profiling** | Build an evidence-backed marketing profile of named competitors. |
| **1-marketing-competitors** | Create one competitor-comparison or alternative-page plan. |
| **1-marketing-content-strategy** | Plan one marketing content portfolio or roadmap. |
| **1-marketing-copy-editing** | Edit one existing piece of marketing copy. |
| **1-marketing-copywriting** | Write one bounded marketing page or message. |
| **1-marketing-cro** | Audit or improve conversion on one marketing page or form. |
| **1-marketing-customer-research** | Conduct or synthesize customer research for a marketing decision. |
| **1-marketing-directory-submissions** | Prepare a bounded product-directory submission plan. |
| **1-marketing-emails** | Create or improve one lifecycle-email sequence. |
| **1-marketing-events** | Plan one marketing event, webinar, sponsorship, or speaking motion. |
| **1-marketing-free-tools** | Design one free tool as a marketing asset. |
| **1-marketing-image** | Specify or optimize one marketing-image asset. |
| **1-marketing-influencer-marketing** | Plan one influencer, creator, or ambassador program. |
| **1-marketing-launch** | Plan one product-marketing launch or announcement. |
| **1-marketing-lead-magnets** | Plan or improve one lead magnet. |
| **1-marketing-marketing-council** | Compare several named marketing perspectives on one question. |
| **1-marketing-marketing-ideas** | Generate and prioritize marketing tactics for a software product. |
| **1-marketing-marketing-loops** | Design one bounded recurring marketing workflow. |
| **1-marketing-marketing-plan** | Build one evidence-bounded marketing plan. |
| **1-marketing-marketing-psychology** | Apply behavioral principles to one marketing decision. |
| **1-marketing-offers** | Design or improve one commercial offer. |
| **1-marketing-onboarding** | Optimize one post-signup activation or onboarding flow. |
| **1-marketing-paywalls** | Optimize one in-product paywall or upgrade prompt. |
| **1-marketing-popups** | Optimize one marketing popup, modal, overlay, or banner. |
| **1-marketing-pricing** | Research or design one pricing and packaging decision. |
| **1-marketing-product-marketing** | Create or update one product-marketing context document. |
| **1-marketing-programmatic-seo** | Plan one template-and-data programmatic SEO system. |
| **1-marketing-prospecting** | Build an evidence-backed prospecting plan or shortlist. |
| **1-marketing-public-relations** | Plan one earned-media or public-relations motion. |
| **1-marketing-referrals** | Design one referral or affiliate program. |
| **1-marketing-revops** | Design one revenue-operations lifecycle, routing, or reporting change. |
| **1-marketing-sales-enablement** | Create one bounded sales-enablement asset. |
| **1-marketing-schema** | Design or audit website structured-data markup. |
| **1-marketing-seo-audit** | Audit one site's technical and on-page SEO. |
| **1-marketing-signup** | Optimize one signup, registration, or trial-start flow. |
| **1-marketing-site-architecture** | Plan one marketing-site hierarchy, navigation, and URL structure. |
| **1-marketing-sms** | Plan or draft one compliant SMS or MMS marketing sequence. |
| **1-marketing-social** | Plan or draft one social-media content program. |
| **1-marketing-video** | Plan one marketing-video concept, script, or production specification. |
| **1-network-and-edge-operations** | Operate DNS, load balancers, CDNs, proxies, meshes, firewalls, VPNs, and TLS. |
| **1-observability-and-instrumentation** | Logging, metrics, tracing, and alerting for diagnosable production behavior. |
| **1-obsidian-bases** | Create and edit Obsidian Bases (.base files) with views and formulas. |
| **1-obsidian-cli** | Interact with Obsidian vaults — read, search, manage notes and tasks. |
| **1-obsidian-markdown** | Create and edit Obsidian Flavored Markdown (wikilinks, embeds, callouts). |
| **1-performance-optimization** | Measure-first perf work (FE/BE/DB) — Core Web Vitals, N+1 queries, profiling. |
| **1-pdf** | Safely inspect, create, edit, and verify PDF files. |
| **1-pi-agent-rust** | Speed up pi_agent_rust development and verification workflows. |
| **1-plan-arbiter** | Compare competing plans and choose one executable direction. |
| **1-platform-engineering** | Build internal developer platforms, golden paths, and reproducible environments. |
| **1-plow-ahead** | Continue through routine ambiguity when the user explicitly requests autonomy. |
| **1-ponytail-audit** | Read-only audit of evidence-backed removable complexity in one bounded repository snapshot. |
| **1-ponytail-debt** | Return a bounded read-only ledger of exact `0-ponytail:` markers. |
| **1-ponytail-gain** | Show one pinned upstream agentic benchmark with its methodology and limitations. |
| **1-ponytail-help** | Catalog-accurate one-shot reference for Ponytail levels and child skills. |
| **1-pptx** | Create, read, edit, or manipulate PowerPoint presentations (.pptx files). |
| **1-pr-summarizer** | Summarize changes, write PR descriptions, or draft PR comments. |
| **1-pr-repair** | Repair known findings, CI failures, conflicts, and blockers on one PR without reviewing it. |
| **1-pr-review-and-repair** | Review, repair, rebase, push, and verify one PR until clean and green. |
| **1-project-wiki-manager** | Grounded in-repository concept wiki from declared sources; scoped ingest and read-only query/audit. |
| **1-prototype** | Build throwaway prototype to sanity-check state model or UI. |
| **1-quick-recap** | End work with a concise green, yellow, or red completion-state signal. |
| **1-research** | Answer one bounded question from current authoritative sources; persist only when requested. |
| **1-resilience-and-disaster-recovery** | Design and test backup, failover, disaster-recovery, and continuity plans. |
| **1-resolving-merge-conflicts** | Resolve in-progress git merge/rebase conflicts. |
| **1-resource-summarizer** | Distill long resources (PDF, video, article) into learning-focused notes. |
| **1-response-effort-calibrator** | Guide response effort and depth based on prompt cues. |
| **1-rewind** | Recover recent local screen context through Clips Rewind. |
| **1-security-auditor** | Multi-phase security auditor for codebases — OWASP, vulnerability review. |
| **1-server-and-fleet-operations** | Operate Linux/Windows hosts, services, SSH, patches, and managed devices. |
| **1-session-skill-reflect** | Read-only reflection that proposes one evidence-backed skill improvement. |
| **1-shipping-and-launch** | Pre-flight checklist, canary rollout, monitoring, rollback planning. |
| **1-skill-atomize** | Assess or repair one pinned cluster of overlapping live skills. |
| **1-skill-linter** | Report structural and routing health for one pinned catalog snapshot. |
| **1-stepdown-rule** | Assess or apply one behavior-independent top-down declaration reorder in one file. |
| **1-story-teacher** | Turn lessons/articles/transcripts into engaging stories that teach invisibly. |
| **1-strategic-compact** | Suggest manual context compaction at logical task intervals. |
| **1-stacked-pr-review-and-repair** | Review, repair, rebase, and verify every PR in a dependent stack. |
| **1-stacked-pr-repair** | Repair known findings, CI failures, conflicts, and blockers across a PR stack without reviewing it. |
| **1-tdd** | Test-driven development — red → green → refactor at agreed seams. |
| **1-tool-schema-design** | Design constrained, model-facing tool schemas and validate their safety surface. |
| **1-teach** | Multi-session teaching workspace (MISSION.md, lessons, learning-records). |
| **1-thinking-steel-manning** | Build strongest version of opposing case before engaging. |
| **1-thinking-ethical** | Map values, harms, power, and safeguards before a normative decision. |
| **1-thinking-lateral** | Escape a stuck framing with safe provocations and testable candidates. |
| **1-triage-inbox** | Read one cutoff-bounded snapshot of raw tracker items needing attention. |
| **1-triage-assess** | Assess one issue or external PR without applying tracker state. |
| **1-triage-apply** | Apply and verify one explicitly approved triage transition. |
| **1-to-spec** | Synthesize one settled source into one right-sized specification artifact. |
| **1-to-tickets** | Derive one dependency-aware ticket set from one approved specification. |
| **1-wayfinder-chart** | Produce one new uncertainty-map set from an accepted destination. |
| **1-wayfinder-advance** | Advance one existing map through one frontier decision-ticket cycle. |
| **1-vault-explain** | Explain a concept from Rohitas's Notes vault for learning. |
| **1-vault-inbox** | Fast-capture notes into Rohitas's Notes Inbox. |
| **1-vault-ingest** | Ingest knowledge into Rohitas's Notes — create/update Concepts. |
| **1-vault-lint** | Health-check vault — broken links, orphans, duplicates, drift. |
| **1-visual-edit** | Inspect or edit a running local app through Agent-Native Design. |
| **1-visual-plan** | Publish a plan as an interactive visual review artifact. |
| **1-visual-recap** | Draft, create, or update one private visual orientation artifact for one exact change candidate. |
| **1-webmcp** | Operate a user-specified web app through its MCP or WebMCP tools. |
| **1-wiki-query** | Answer questions against personal LLM wiki / Obsidian vault. |
| **1-source-backed-skill** | Author one private reference-skill candidate from an authorized fixed corpus. |
| **1-writing-great-skills** | Apply concise invocation, disclosure, completion, and pruning craft to one body. |
| **1-xlsx** | Create, read, edit, or manipulate spreadsheets (.xlsx, .csv, .tsv). |
| **2-ponytail-review** | Read-only review of one pinned diff solely for evidence-backed removable complexity. |
| **2-prompt-injection-defense** | Design and verify prompt-injection defenses at agent trust boundaries. |
| **2-skill-supply-chain-audit** | Audit third-party agent skills and packages for provenance and risky behavior. |
| **2-thermo-nuclear-code-quality-review** | Harsh maintainability-only review — code judo, giant files, spaghetti growth. |
| **2-security-and-hardening** | Harden code against vulnerabilities while building or remediating. |
| **2-software-architect** | Bounded, evidence-backed system decision analysis with viable alternatives, conditions, and migration/verification implications. |
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

## Available skill additions

| **1-ai-suitability** | Assess AI fit, non-AI alternatives and the level of automation. |
| **1-asd-ste100** | Rewrite agent-facing English with STE-inspired clarity and preserve meaning. |
