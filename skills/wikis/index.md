# Wiki Index

**Summary**: Categorized index of all live skills (project-wiki-manager index style).

**Last updated**: 2026-07-19

**Sources**: `skills/<name>/`; hub packages in `hubs/`; flows SSOT in `skills/butler/references/flows.md`.

---

## Project Overview

| Page | Description | Sources |
|------|-------------|---------|
| [[layout]] | Six-folder catalog layout | guidelines/layout.md |
| [[flows]] | Domain hubs, pipelines, forks | skills/butler/references/flows.md |
| [[hubs]] | Hub HTML/JSON packages | hubs/ |

## Hub: butler

| Page | Description | Sources |
|------|-------------|---------|
| [[butler]] | Hub of hubs for this skills catalog — real-life butler. Use when lost ("which skill?"), need orie… | `skills/butler` |

## Hub: code-review

| Page | Description | Sources |
|------|-------------|---------|
| [[verify-work]] | Check your work with a verification subagent that reviews diffs, runs builds and tests, and evalu… | `skills/verify-work` |
| [[code-review]] | Multi-axis review of changes since a fixed point: Spec (ticket/PRD fidelity), Standards (repo doc… | `skills/code-review` |
| [[ponytail-review]] | Code review focused exclusively on over-engineering. Finds what to delete: reinvented standard li… | `skills/ponytail-review` |
| [[security-and-hardening]] | Hardens code against vulnerabilities while building or remediating. Use when handling user input,… | `skills/security-and-hardening` |
| [[software-architect]] | Act as a Grandmaster software architect and system designer. Analyze codebases/projects for curre… | `skills/software-architect` |

## Hub: diagnosing-bugs

| Page | Description | Sources |
|------|-------------|---------|
| [[diagnosing-bugs]] | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debu… | `skills/diagnosing-bugs` |
| [[tdd]] | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentio… | `skills/tdd` |

## Hub: grilling

| Page | Description | Sources |
|------|-------------|---------|
| [[domain-modeling]] | Build and sharpen a project's domain model. Use when the user wants to pin down domain terminolog… | `skills/domain-modeling` |
| [[grill-me]] | A relentless interview to sharpen a plan or design. | `skills/grill-me` |
| [[grill-with-docs]] | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) … | `skills/grill-with-docs` |
| [[grilling]] | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-te… | `skills/grilling` |
| [[handoff]] | Compact the current conversation into a handoff document for another agent to pick up. | `skills/handoff` |
| [[prototype]] | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check … | `skills/prototype` |

## Hub: implement

| Page | Description | Sources |
|------|-------------|---------|
| [[implement]] | "Implement a piece of work based on a spec or set of tickets." | `skills/implement` |

## Hub: improve-codebase-architecture

| Page | Description | Sources |
|------|-------------|---------|
| [[clean-craftsmanship]] | Q&A / principle reference from Clean Code and Clean Architecture (why, trade-offs, SOLID, Uncle B… | `skills/clean-craftsmanship` |
| [[codebase-design]] | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a modu… | `skills/codebase-design` |
| [[coding-standards]] | Always-on lean coding standards for naming, modularity, error handling, and comments while genera… | `skills/coding-standards` |
| [[improve-codebase-architecture]] | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill thr… | `skills/improve-codebase-architecture` |
| [[living-documentation-governor]] | Code-synced living documentation: trigger maps, placement into guides/ADR/ glossary/archive, drif… | `skills/living-documentation-governor` |
| [[project-wiki-manager]] | Karpathy-style in-repo project wiki: docs/raw/ → docs/wiki/ concept pages, grounded Q&A, audit, c… | `skills/project-wiki-manager` |

## Hub: learn

| Page | Description | Sources |
|------|-------------|---------|
| [[code-explainer]] | Explain source code (lines, blocks, functions, files, modules) at audience levels (Noob, Learner,… | `skills/code-explainer` |
| [[learn]] | Domain hub for intellectual understanding — how/why something works, not shipping code or vault c… | `skills/learn` |
| [[learning-explainer]] | Structured multi-level explanations (child through frontier) with knowledge probe, mental models,… | `skills/learning-explainer` |
| [[resource-summarizer]] | Distills long resources (PDF, video/transcript, article, image) into learning-focused notes using… | `skills/resource-summarizer` |
| [[story-teacher]] | Use to turn any summary, lesson, educational text, article, book notes, video transcript, URL con… | `skills/story-teacher` |
| [[teach]] | Multi-session teaching workspace in the current directory (MISSION.md, lessons, learning-records)… | `skills/teach` |
| [[vault-explain]] | Explain a Rohitas's Notes Concept for learning — grounds in the vault note then redirects to lear… | `skills/vault-explain` |

## Hub: misc

| Page | Description | Sources |
|------|-------------|---------|
| [[defuddle]] | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation… | `skills/defuddle` |
| [[diagram-maker]] | Create SVG/HTML or Excalidraw diagrams for concepts, architecture, flows, and whiteboards. | `skills/diagram-maker` |
| [[docx]] | "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.doc… | `skills/docx` |
| [[hatch-pet]] | Create, repair, validate, visually QA, and package Codex-compatible v2 animated pets from charact… | `skills/hatch-pet` |
| [[imagine]] | How to use the image_gen and image_edit tool calls in Grok Build: when to build a visual with cod… | `skills/imagine` |
| [[json-canvas]] | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when … | `skills/json-canvas` |
| [[office]] | Hub for office/media and cross-cutting tool skills (docx, pptx, xlsx, diagrams, images, canvas, w… | `skills/office` |
| [[pptx]] | "Use this skill any time a .pptx file is involved in any way — as input, output, or both. This in… | `skills/pptx` |
| [[xlsx]] | "Use this skill any time a spreadsheet file is the primary input or output. This means any task w… | `skills/xlsx` |

## Hub: ponytail

| Page | Description | Sources |
|------|-------------|---------|
| [[ponytail]] | Forces the laziest solution that actually works, simplest, shortest, most minimal. Channels a sen… | `skills/ponytail` |
| [[ponytail-audit]] | Whole-repo audit for over-engineering. Like ponytail-review, but scans the entire codebase instea… | `skills/ponytail-audit` |
| [[ponytail-debt]] | Harvest every `ponytail:` comment in the codebase into a debt ledger, so the deliberate shortcuts… | `skills/ponytail-debt` |
| [[ponytail-gain]] | Show ponytail's measured impact as a compact scoreboard: less code, less cost, more speed, from t… | `skills/ponytail-gain` |
| [[ponytail-help]] | Quick-reference card for all ponytail modes, skills, and commands. One-shot display, not a persis… | `skills/ponytail-help` |

## Hub: review

| Page | Description | Sources |
|------|-------------|---------|
| [[codebase-review-strategy]] | Use when reviewing any codebase of unknown or varying size. Determines repo tier from measurable … | `skills/codebase-review-strategy` |
| [[review]] | Domain hub for verification modes — multi-axis change review, security audit, architecture review… | `skills/review` |

## Hub: rohitas-vault-wiki

| Page | Description | Sources |
|------|-------------|---------|
| [[obsidian-bases]] | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use wh… | `skills/obsidian-bases` |
| [[obsidian-cli]] | Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, t… | `skills/obsidian-cli` |
| [[obsidian-markdown]] | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and othe… | `skills/obsidian-markdown` |
| [[rohitas-vault-wiki]] | Steward Rohitas's Notes Obsidian vault — Atlas hubs, Concepts atoms, Inbox capture, Guides/Projec… | `skills/rohitas-vault-wiki` |
| [[vault-inbox]] | Fast-capture notes into Rohitas's Notes Inbox while using agentic AI — no full ingest, no Concept… | `skills/vault-inbox` |
| [[vault-ingest]] | Ingest knowledge into Rohitas's Notes: process chat text, Inbox files, or URLs; create or update … | `skills/vault-ingest` |
| [[vault-lint]] | Health-check Rohitas's Notes vault: broken wikilinks, orphans, misplaced hubs, frontmatter, contr… | `skills/vault-lint` |
| [[wiki-query]] | Answer questions against a personal LLM wiki / Obsidian vault using Karpathy-style query workflow… | `skills/wiki-query` |

## Hub: security-auditor

| Page | Description | Sources |
|------|-------------|---------|
| [[security-auditor]] | Multi-phase security and quality auditor for codebases and projects. Use for security audit, vuln… | `skills/security-auditor` |

## Hub: setup-rohitas-skills

| Page | Description | Sources |
|------|-------------|---------|
| [[setup-rohitas-skills]] | Configure this repo for Rohitas engineering skills — issue tracker, triage labels, domain docs, a… | `skills/setup-rohitas-skills` |
| [[to-tickets]] | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declari… | `skills/to-tickets` |

## Hub: skill-creator

| Page | Description | Sources |
|------|-------------|---------|
| [[create-skill]] | Thin entry for authoring skills. Loads skill-creator (body craft/eval), then skill-manager for ca… | `skills/create-skill` |
| [[skill-creator]] | Create new skills, modify and improve existing skills, and measure skill performance. Use when us… | `skills/skill-creator` |
| [[writing-great-skills]] | Reference for writing and editing skills well — the vocabulary and principles that make a skill p… | `skills/writing-great-skills` |

## Hub: skill-manager

| Page | Description | Sources |
|------|-------------|---------|
| [[skill-atomize]] | Make catalog skills atomic: one job each, Boundary tables, hard redirects, and ask-user forks for… | `skills/skill-atomize` |
| [[skill-linter]] | Health-check agent skills for Matt-style lean SKILL.md, chaining (prev/next/hub), references, hub… | `skills/skill-linter` |
| [[skill-manager]] | Catalog facilities manager: CRUD skills, place them under a domain hub workflow, create new hubs,… | `skills/skill-manager` |

## Hub: triage

| Page | Description | Sources |
|------|-------------|---------|
| [[triage]] | Move issues and external PRs through a state machine of triage roles — categorise, verify, grill … | `skills/triage` |

## Hub: wayfinder

| Page | Description | Sources |
|------|-------------|---------|
| [[to-spec]] | Turn the current conversation into a spec and publish it to the project issue tracker — no interv… | `skills/to-spec` |
| [[wayfinder]] | Plan a huge chunk of work — more than one agent session can hold — as a shared map of decision ti… | `skills/wayfinder` |

## Unassigned (place under a hub)

| Page | Description | Sources |
|------|-------------|---------|
| [[code-comments]] | Write clear, professional API and surface documentation using the convention for the language in … | `skills/code-comments` |
| [[context-monitor]] | Monitors conversation context usage, warns at ~50% of the limit, and provides actionable advice o… | `skills/context-monitor` |
| [[execution-flow-comments]] | Write structured Execution Flow comments with numbered steps and ASCII branch trees (Input, Outpu… | `skills/execution-flow-comments` |
| [[discover-skills]] | Helps users discover and install agent skills when they ask questions like "how do I do X", "find… | `skills/discover-skills` |
| [[git-commit-helper]] | Helps generate high-quality git commit messages by analyzing staged changes, untracked files, or … | `skills/git-commit-helper` |
| [[grok-help]] | Grok documentation and configuration help. Use when users ask about setup, configuration, MCP ser… | `skills/grok-help` |
| [[inline-comments]] | Add concise one-line comments immediately above non-obvious code blocks or slightly complex snipp… | `skills/inline-comments` |
| [[pi-agent-rust]] | >- | `skills/pi-agent-rust` |
| [[pr-summarizer]] | Summarize changes, write PR descriptions, or draft comments for pull requests. Trigger this skill… | `skills/pr-summarizer` |
| [[session-skill-reflect]] | Self-improving system for skills. Analyze session for corrections/approvals, extract learnings, p… | `skills/session-skill-reflect` |
| [[research]] | Investigate a question against high-trust primary sources and capture the findings as a Markdown … | `skills/research` |
| [[resolving-merge-conflicts]] | "Use when you need to resolve an in-progress git merge/rebase conflict." | `skills/resolving-merge-conflicts` |
| [[response-effort-calibrator]] | Guides the AI on response effort, depth, and style (brief, concise, balanced, detailed, exhaustiv… | `skills/response-effort-calibrator` |
| [[stepdown-rule]] | Enforce top-down file layout using the newspaper metaphor and stepdown rule (callers above callee… | `skills/stepdown-rule` |
| [[strategic-compact]] | Suggests manual context compaction at logical intervals to preserve context through task phases r… | `skills/strategic-compact` |
| [[thinking-steel-manning]] | Use before rejecting a proposal or when you're inclined to just agree with the user. Build the st… | `skills/thinking-steel-manning` |

## Archive (tombstones)

| Page | Description | Sources |
|------|-------------|---------|
| [[ask-matt]] | Tombstone | `archive/ask-matt` |
| [[code-review-v2]] | Tombstone | `archive/code-review-v2` |
| [[continuous-learning-v2]] | Tombstone | `archive/continuous-learning-v2` |
| [[obsidian-notes-manager]] | Tombstone | `archive/obsidian-notes-manager` |
| [[software-architecture]] | Tombstone | `archive/software-architecture` |
| [[task-observer]] | Tombstone | `archive/task-observer` |

_Live skills: **80**._
