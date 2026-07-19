# Wiki Index

**Summary**: Live skills by domain hub. Physical path is always `skills/<name>/`.

**Last updated**: 2026-07-19

**Sources**: `skills/<name>`; hubs in `hubs/`; flows SSOT `skills/butler/references/flows.md`.

---

## Project Overview

| Page | Description | Sources |
|------|-------------|---------|
| [[layout]] | Six-folder catalog layout | guidelines/layout.md |
| [[flows]] | Domain hubs + forks | skills/butler/references/flows.md |
| [[hubs]] | Hub packages | hubs/ |

## Hub: butler

| Page | Description | Sources |
|------|-------------|---------|
| [[butler]] | Hub of hubs for this skills catalog — real-life butler. Use when lost ("which skill?"), need orienta… | `skills/butler` |
| [[context-monitor]] | Monitors conversation context usage, warns at ~50% of the limit, and provides actionable advice on s… | `skills/context-monitor` |
| [[grok-help]] | Grok documentation and configuration help. Use when users ask about setup, configuration, MCP server… | `skills/grok-help` |
| [[handoff]] | Compact the current conversation into a handoff document for another agent to pick up. | `skills/handoff` |
| [[response-effort-calibrator]] | Guides the AI on response effort, depth, and style (brief, concise, balanced, detailed, exhaustive) … | `skills/response-effort-calibrator` |
| [[strategic-compact]] | Suggests manual context compaction at logical intervals to preserve context through task phases rath… | `skills/strategic-compact` |

## Hub: code-review

| Page | Description | Sources |
|------|-------------|---------|
| [[code-review]] | Multi-axis review of changes since a fixed point: Spec (ticket/PRD fidelity), Standards (repo docs +… | `skills/code-review` |
| [[ponytail-review]] | Code review focused exclusively on over-engineering. Finds what to delete: reinvented standard libra… | `skills/ponytail-review` |
| [[security-and-hardening]] | Hardens code against vulnerabilities while building or remediating. Use when handling user input, au… | `skills/security-and-hardening` |
| [[software-architect]] | Act as a Grandmaster software architect and system designer. Analyze codebases/projects for current … | `skills/software-architect` |
| [[verify-work]] | Check your work with a verification subagent that reviews diffs, runs builds and tests, and evaluate… | `skills/verify-work` |

## Hub: diagnosing-bugs

| Page | Description | Sources |
|------|-------------|---------|
| [[diagnosing-bugs]] | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug t… | `skills/diagnosing-bugs` |
| [[tdd]] | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions … | `skills/tdd` |

## Hub: grilling

| Page | Description | Sources |
|------|-------------|---------|
| [[domain-modeling]] | Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology o… | `skills/domain-modeling` |
| [[grill-me]] | A relentless interview to sharpen a plan or design. | `skills/grill-me` |
| [[grill-with-docs]] | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as … | `skills/grill-with-docs` |
| [[grilling]] | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test … | `skills/grilling` |
| [[prototype]] | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whe… | `skills/prototype` |
| [[thinking-steel-manning]] | Use before rejecting a proposal or when you're inclined to just agree with the user. Build the stron… | `skills/thinking-steel-manning` |

## Hub: implement

| Page | Description | Sources |
|------|-------------|---------|
| [[code-comments]] | Write clear, professional API and surface documentation using the convention for the language in con… | `skills/code-comments` |
| [[execution-flow-comments]] | Write structured Execution Flow comments with numbered steps and ASCII branch trees (Input, Output, … | `skills/execution-flow-comments` |
| [[git-commit-helper]] | Helps generate high-quality git commit messages by analyzing staged changes, untracked files, or bot… | `skills/git-commit-helper` |
| [[implement]] | "Implement a piece of work based on a spec or set of tickets." | `skills/implement` |
| [[inline-comments]] | Add concise one-line comments immediately above non-obvious code blocks or slightly complex snippets… | `skills/inline-comments` |
| [[pr-summarizer]] | Summarize changes, write PR descriptions, or draft comments for pull requests. Trigger this skill wh… | `skills/pr-summarizer` |
| [[research]] | Investigate a question against high-trust primary sources and capture the findings as a Markdown fil… | `skills/research` |
| [[resolving-merge-conflicts]] | "Use when you need to resolve an in-progress git merge/rebase conflict." | `skills/resolving-merge-conflicts` |
| [[stepdown-rule]] | Enforce top-down file layout using the newspaper metaphor and stepdown rule (callers above callees, … | `skills/stepdown-rule` |

## Hub: improve-codebase-architecture

| Page | Description | Sources |
|------|-------------|---------|
| [[clean-craftsmanship]] | Q&A / principle reference from Clean Code and Clean Architecture (why, trade-offs, SOLID, Uncle Bob … | `skills/clean-craftsmanship` |
| [[codebase-design]] | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module'… | `skills/codebase-design` |
| [[coding-standards]] | Always-on lean coding standards for naming, modularity, error handling, and comments while generatin… | `skills/coding-standards` |
| [[improve-codebase-architecture]] | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill throug… | `skills/improve-codebase-architecture` |
| [[living-documentation-governor]] | Code-synced living documentation: trigger maps, placement into guides/ADR/ glossary/archive, drift c… | `skills/living-documentation-governor` |
| [[project-wiki-manager]] | Karpathy-style in-repo project wiki: docs/raw/ → docs/wiki/ concept pages, grounded Q&A, audit, comp… | `skills/project-wiki-manager` |

## Hub: learn

| Page | Description | Sources |
|------|-------------|---------|
| [[code-explainer]] | Explain source code (lines, blocks, functions, files, modules) at audience levels (Noob, Learner, Ju… | `skills/code-explainer` |
| [[learn]] | Domain hub for intellectual understanding — how/why something works, not shipping code or vault comp… | `skills/learn` |
| [[learning-explainer]] | Structured multi-level explanations (child through frontier) with knowledge probe, mental models, di… | `skills/learning-explainer` |
| [[resource-summarizer]] | Distills long resources (PDF, video/transcript, article, image) into learning-focused notes using 80… | `skills/resource-summarizer` |
| [[story-teacher]] | Use to turn any summary, lesson, educational text, article, book notes, video transcript, URL conten… | `skills/story-teacher` |
| [[teach]] | Multi-session teaching workspace in the current directory (MISSION.md, lessons, learning-records). U… | `skills/teach` |
| [[vault-explain]] | Explain a Rohitas's Notes Concept for learning — grounds in the vault note then redirects to learnin… | `skills/vault-explain` |

## Hub: office

| Page | Description | Sources |
|------|-------------|---------|
| [[defuddle]] | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to… | `skills/defuddle` |
| [[diagram-maker]] | Create SVG/HTML or Excalidraw diagrams for concepts, architecture, flows, and whiteboards. | `skills/diagram-maker` |
| [[docx]] | "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx f… | `skills/docx` |
| [[hatch-pet]] | Create, repair, validate, visually QA, and package Codex-compatible v2 animated pets from character … | `skills/hatch-pet` |
| [[imagine]] | How to use the image_gen and image_edit tool calls in Grok Build: when to build a visual with code i… | `skills/imagine` |
| [[json-canvas]] | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when wor… | `skills/json-canvas` |
| [[office]] | Domain hub for office/media tools — Word, slides, sheets, diagrams, images, canvas, web extract, pet… | `skills/office` |
| [[pptx]] | "Use this skill any time a .pptx file is involved in any way — as input, output, or both. This inclu… | `skills/pptx` |
| [[xlsx]] | "Use this skill any time a spreadsheet file is the primary input or output. This means any task wher… | `skills/xlsx` |

## Hub: ponytail

| Page | Description | Sources |
|------|-------------|---------|
| [[ponytail]] | Forces the laziest solution that actually works, simplest, shortest, most minimal. Channels a senior… | `skills/ponytail` |
| [[ponytail-audit]] | Whole-repo audit for over-engineering. Like ponytail-review, but scans the entire codebase instead o… | `skills/ponytail-audit` |
| [[ponytail-debt]] | Harvest every `ponytail:` comment in the codebase into a debt ledger, so the deliberate shortcuts an… | `skills/ponytail-debt` |
| [[ponytail-gain]] | Show ponytail's measured impact as a compact scoreboard: less code, less cost, more speed, from the … | `skills/ponytail-gain` |
| [[ponytail-help]] | Quick-reference card for all ponytail modes, skills, and commands. One-shot display, not a persisten… | `skills/ponytail-help` |

## Hub: review

| Page | Description | Sources |
|------|-------------|---------|
| [[codebase-review-strategy]] | Use when reviewing any codebase of unknown or varying size. Determines repo tier from measurable met… | `skills/codebase-review-strategy` |
| [[review]] | Domain hub for verification modes — multi-axis change review, security audit, architecture review, a… | `skills/review` |

## Hub: rohitas-vault-wiki

| Page | Description | Sources |
|------|-------------|---------|
| [[obsidian-bases]] | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when … | `skills/obsidian-bases` |
| [[obsidian-cli]] | Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, task… | `skills/obsidian-cli` |
| [[obsidian-markdown]] | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other O… | `skills/obsidian-markdown` |
| [[rohitas-vault-wiki]] | Steward Rohitas's Notes Obsidian vault — Atlas hubs, Concepts atoms, Inbox capture, Guides/Projects/… | `skills/rohitas-vault-wiki` |
| [[vault-inbox]] | Fast-capture notes into Rohitas's Notes Inbox while using agentic AI — no full ingest, no Concepts. … | `skills/vault-inbox` |
| [[vault-ingest]] | Ingest knowledge into Rohitas's Notes: process chat text, Inbox files, or URLs; create or update Con… | `skills/vault-ingest` |
| [[vault-lint]] | Health-check Rohitas's Notes vault: broken wikilinks, orphans, misplaced hubs, frontmatter, contradi… | `skills/vault-lint` |
| [[wiki-query]] | Answer questions against a personal LLM wiki / Obsidian vault using Karpathy-style query workflow (i… | `skills/wiki-query` |

## Hub: security-auditor

| Page | Description | Sources |
|------|-------------|---------|
| [[security-auditor]] | Multi-phase security and quality auditor for codebases and projects. Use for security audit, vulnera… | `skills/security-auditor` |

## Hub: setup-rohitas-skills

| Page | Description | Sources |
|------|-------------|---------|
| [[setup-rohitas-skills]] | Configure this repo for Rohitas engineering skills — issue tracker, triage labels, domain docs, and … | `skills/setup-rohitas-skills` |
| [[to-tickets]] | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring … | `skills/to-tickets` |

## Hub: skill-creator

| Page | Description | Sources |
|------|-------------|---------|
| [[create-skill]] | Thin entry for authoring skills. Loads skill-creator (body craft/eval), then skill-manager for catal… | `skills/create-skill` |
| [[skill-creator]] | Create, edit, and evaluate agent skills (body craft, evals, description optimization). Use when auth… | `skills/skill-creator` |
| [[writing-great-skills]] | Reference for writing and editing skills well — the vocabulary and principles that make a skill pred… | `skills/writing-great-skills` |

## Hub: skill-manager

| Page | Description | Sources |
|------|-------------|---------|
| [[discover-skills]] | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a … | `skills/discover-skills` |
| [[session-skill-reflect]] | Self-improving system for skills. Analyze session for corrections/approvals, extract learnings, prop… | `skills/session-skill-reflect` |
| [[skill-atomize]] | Make catalog skills atomic: one job each, Boundary tables, hard redirects, and ask-user forks for co… | `skills/skill-atomize` |
| [[skill-linter]] | Health-check agent skills for Matt-style lean SKILL.md, chaining (prev/next/hub), references, hub me… | `skills/skill-linter` |
| [[skill-manager]] | Catalog facilities manager: CRUD skills, place them under a domain hub workflow, create new hubs, in… | `skills/skill-manager` |

## Hub: triage

| Page | Description | Sources |
|------|-------------|---------|
| [[triage]] | Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if … | `skills/triage` |

## Hub: wayfinder

| Page | Description | Sources |
|------|-------------|---------|
| [[to-spec]] | Turn the current conversation into a spec and publish it to the project issue tracker — no interview… | `skills/to-spec` |
| [[wayfinder]] | Plan a huge chunk of work — more than one agent session can hold — as a shared map of decision ticke… | `skills/wayfinder` |

## Unassigned

| Page | Description | Sources |
|------|-------------|---------|
| [[pi-agent-rust]] | >- | `skills/pi-agent-rust` |

_Live skills: **80**._
