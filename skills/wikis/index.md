# Wiki Index

**Summary**: Live skills by domain hub. Physical path is always `skills/<name>/`.

**Last updated**: 2026-07-19

**Sources**: `skills/<name>`; hubs in `hubs/`; flows SSOT `skills/0-butler/references/flows.md`.

---

## Project Overview

| Page | Description | Sources |
|------|-------------|---------|
| [[layout]] | Six-folder catalog layout | guidelines/layout.md |
| [[flows]] | Domain hubs + forks | skills/0-butler/references/flows.md |
| [[hubs]] | Hub packages | hubs/ |

## Hub: 0-butler

| Page | Description | Sources |
|------|-------------|---------|
| [[0-butler]] | Hub of hubs for this skills catalog — real-life butler. Use when lost ("which skill?"), need orienta… | `skills/0-butler` |
| [[1-context-monitor]] | Monitors conversation context usage, warns at ~50% of the limit, and provides actionable advice on s… | `skills/1-context-monitor` |
| [[1-grok-help]] | Grok documentation and configuration help. Use when users ask about setup, configuration, MCP server… | `skills/1-grok-help` |
| [[1-handoff]] | Compact the current conversation into a handoff document for another agent to pick up. | `skills/1-handoff` |
| [[1-response-effort-calibrator]] | Guides the AI on response effort, depth, and style (brief, concise, balanced, detailed, exhaustive) … | `skills/1-response-effort-calibrator` |
| [[1-strategic-compact]] | Suggests manual context compaction at logical intervals to preserve context through task phases rath… | `skills/1-strategic-compact` |

## Hub: 1-code-review

| Page | Description | Sources |
|------|-------------|---------|
| [[1-code-review]] | Multi-axis 0-review of changes since a fixed point: Spec (ticket/PRD fidelity), Standards (repo docs +… | `skills/1-code-review` |
| [[1-ponytail-review]] | Code 0-review focused exclusively on over-engineering. Finds what to delete: reinvented standard libra… | `skills/1-ponytail-review` |
| [[1-security-and-hardening]] | Hardens code against vulnerabilities while building or remediating. Use when handling user input, au… | `skills/1-security-and-hardening` |
| [[1-software-architect]] | Act as a Grandmaster software architect and system designer. Analyze codebases/projects for current … | `skills/1-software-architect` |
| [[1-verify-work]] | Check your work with a verification subagent that reviews diffs, runs builds and tests, and evaluate… | `skills/1-verify-work` |

## Hub: 0-diagnosing-bugs

| Page | Description | Sources |
|------|-------------|---------|
| [[0-diagnosing-bugs]] | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug t… | `skills/0-diagnosing-bugs` |
| [[1-tdd]] | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions … | `skills/1-tdd` |

## Hub: 0-grilling

| Page | Description | Sources |
|------|-------------|---------|
| [[1-domain-modeling]] | Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology o… | `skills/1-domain-modeling` |
| [[1-grill-me]] | A relentless interview to sharpen a plan or design. | `skills/1-grill-me` |
| [[1-grill-with-docs]] | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as … | `skills/1-grill-with-docs` |
| [[0-grilling]] | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test … | `skills/0-grilling` |
| [[1-prototype]] | Build a throwaway 1-prototype to answer a design question. Use when the user wants to sanity-check whe… | `skills/1-prototype` |
| [[1-thinking-steel-manning]] | Use before rejecting a proposal or when you're inclined to just agree with the user. Build the stron… | `skills/1-thinking-steel-manning` |

## Hub: 0-implement

| Page | Description | Sources |
|------|-------------|---------|
| [[1-code-comments]] | Write clear, professional API and surface documentation using the convention for the language in con… | `skills/1-code-comments` |
| [[1-execution-flow-comments]] | Write structured Execution Flow comments with numbered steps and ASCII branch trees (Input, Output, … | `skills/1-execution-flow-comments` |
| [[1-git-commit-helper]] | Helps generate high-quality git commit messages by analyzing staged changes, untracked files, or bot… | `skills/1-git-commit-helper` |
| [[0-implement]] | "Implement a piece of work based on a spec or set of tickets." | `skills/0-implement` |
| [[1-inline-comments]] | Add concise one-line comments immediately above non-obvious code blocks or slightly complex snippets… | `skills/1-inline-comments` |
| [[1-pr-summarizer]] | Summarize changes, write PR descriptions, or draft comments for pull requests. Trigger this skill wh… | `skills/1-pr-summarizer` |
| [[1-research]] | Investigate a question against high-trust primary sources and capture the findings as a Markdown fil… | `skills/1-research` |
| [[1-resolving-merge-conflicts]] | "Use when you need to resolve an in-progress git merge/rebase conflict." | `skills/1-resolving-merge-conflicts` |
| [[1-stepdown-rule]] | Enforce top-down file layout using the newspaper metaphor and stepdown rule (callers above callees, … | `skills/1-stepdown-rule` |

## Hub: 0-improve-codebase-architecture

| Page | Description | Sources |
|------|-------------|---------|
| [[1-clean-craftsmanship]] | Q&A / principle reference from Clean Code and Clean Architecture (why, trade-offs, SOLID, Uncle Bob … | `skills/1-clean-craftsmanship` |
| [[1-codebase-design]] | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module'… | `skills/1-codebase-design` |
| [[1-coding-standards]] | Always-on lean coding standards for naming, modularity, error handling, and comments while generatin… | `skills/1-coding-standards` |
| [[0-improve-codebase-architecture]] | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill throug… | `skills/0-improve-codebase-architecture` |
| [[1-living-documentation-governor]] | Code-synced living documentation: trigger maps, placement into guides/ADR/ glossary/archive, drift c… | `skills/1-living-documentation-governor` |
| [[1-project-wiki-manager]] | Karpathy-style in-repo project wiki: docs/raw/ → docs/wiki/ concept pages, grounded Q&A, audit, comp… | `skills/1-project-wiki-manager` |

## Hub: 0-learn

| Page | Description | Sources |
|------|-------------|---------|
| [[1-code-explainer]] | Explain source code (lines, blocks, functions, files, modules) at audience levels (Noob, Learner, Ju… | `skills/1-code-explainer` |
| [[0-learn]] | Domain hub for intellectual understanding — how/why something works, not shipping code or vault comp… | `skills/0-learn` |
| [[1-learning-explainer]] | Structured multi-level explanations (child through frontier) with knowledge probe, mental models, di… | `skills/1-learning-explainer` |
| [[1-resource-summarizer]] | Distills long resources (PDF, video/transcript, article, image) into learning-focused notes using 80… | `skills/1-resource-summarizer` |
| [[1-story-teacher]] | Use to turn any summary, lesson, educational text, article, book notes, video transcript, URL conten… | `skills/1-story-teacher` |
| [[1-teach]] | Multi-session teaching workspace in the current directory (MISSION.md, lessons, learning-records). U… | `skills/1-teach` |
| [[1-vault-explain]] | Explain a Rohitas's Notes Concept for learning — grounds in the vault note then redirects to learnin… | `skills/1-vault-explain` |

## Hub: 0-office

| Page | Description | Sources |
|------|-------------|---------|
| [[1-defuddle]] | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to… | `skills/1-defuddle` |
| [[1-diagram-maker]] | Create SVG/HTML or Excalidraw diagrams for concepts, architecture, flows, and whiteboards. | `skills/1-diagram-maker` |
| [[1-docx]] | "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx f… | `skills/1-docx` |
| [[1-hatch-pet]] | Create, repair, validate, visually QA, and package Codex-compatible v2 animated pets from character … | `skills/1-hatch-pet` |
| [[1-imagine]] | How to use the image_gen and image_edit tool calls in Grok Build: when to build a visual with code i… | `skills/1-imagine` |
| [[1-json-canvas]] | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when wor… | `skills/1-json-canvas` |
| [[0-office]] | Domain hub for office/media tools — Word, slides, sheets, diagrams, images, canvas, web extract, pet… | `skills/0-office` |
| [[1-pptx]] | "Use this skill any time a .pptx file is involved in any way — as input, output, or both. This inclu… | `skills/1-pptx` |
| [[1-xlsx]] | "Use this skill any time a spreadsheet file is the primary input or output. This means any task wher… | `skills/1-xlsx` |

## Hub: 0-ponytail

| Page | Description | Sources |
|------|-------------|---------|
| [[0-ponytail]] | Forces the laziest solution that actually works, simplest, shortest, most minimal. Channels a senior… | `skills/0-ponytail` |
| [[1-ponytail-audit]] | Whole-repo audit for over-engineering. Like 1-ponytail-review, but scans the entire codebase instead o… | `skills/1-ponytail-audit` |
| [[1-ponytail-debt]] | Harvest every `0-ponytail:` comment in the codebase into a debt ledger, so the deliberate shortcuts an… | `skills/1-ponytail-debt` |
| [[1-ponytail-gain]] | Show ponytail's measured impact as a compact scoreboard: less code, less cost, more speed, from the … | `skills/1-ponytail-gain` |
| [[1-ponytail-help]] | Quick-reference card for all 0-ponytail modes, skills, and commands. One-shot display, not a persisten… | `skills/1-ponytail-help` |

## Hub: 0-review

| Page | Description | Sources |
|------|-------------|---------|
| [[1-codebase-review-strategy]] | Use when reviewing any codebase of unknown or varying size. Determines repo tier from measurable met… | `skills/1-codebase-review-strategy` |
| [[0-review]] | Domain hub for verification modes — multi-axis change 0-review, security audit, architecture 0-review, a… | `skills/0-review` |

## Hub: 0-rohitas-vault-wiki

| Page | Description | Sources |
|------|-------------|---------|
| [[1-obsidian-bases]] | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when … | `skills/1-obsidian-bases` |
| [[1-obsidian-cli]] | Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, task… | `skills/1-obsidian-cli` |
| [[1-obsidian-markdown]] | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other O… | `skills/1-obsidian-markdown` |
| [[0-rohitas-vault-wiki]] | Steward Rohitas's Notes Obsidian vault — Atlas hubs, Concepts atoms, Inbox capture, Guides/Projects/… | `skills/0-rohitas-vault-wiki` |
| [[1-vault-inbox]] | Fast-capture notes into Rohitas's Notes Inbox while using agentic AI — no full ingest, no Concepts. … | `skills/1-vault-inbox` |
| [[1-vault-ingest]] | Ingest knowledge into Rohitas's Notes: process chat text, Inbox files, or URLs; create or update Con… | `skills/1-vault-ingest` |
| [[1-vault-lint]] | Health-check Rohitas's Notes vault: broken wikilinks, orphans, misplaced hubs, frontmatter, contradi… | `skills/1-vault-lint` |
| [[1-wiki-query]] | Answer questions against a personal LLM wiki / Obsidian vault using Karpathy-style query workflow (i… | `skills/1-wiki-query` |

## Hub: 1-security-auditor

| Page | Description | Sources |
|------|-------------|---------|
| [[1-security-auditor]] | Multi-phase security and quality auditor for codebases and projects. Use for security audit, vulnera… | `skills/1-security-auditor` |

## Hub: 0-setup-rohitas-skills

| Page | Description | Sources |
|------|-------------|---------|
| [[0-setup-rohitas-skills]] | Configure this repo for Rohitas engineering skills — issue tracker, 0-triage labels, domain docs, and … | `skills/0-setup-rohitas-skills` |
| [[1-to-tickets]] | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring … | `skills/1-to-tickets` |

## Hub: 0-skill-creator

| Page | Description | Sources |
|------|-------------|---------|
| [[1-create-skill]] | Thin entry for authoring skills. Loads 0-skill-creator (body craft/eval), then 0-skill-manager for catal… | `skills/1-create-skill` |
| [[0-skill-creator]] | Create, edit, and evaluate agent skills (body craft, evals, description optimization). Use when auth… | `skills/0-skill-creator` |
| [[1-writing-great-skills]] | Reference for writing and editing skills well — the vocabulary and principles that make a skill pred… | `skills/1-writing-great-skills` |

## Hub: 0-skill-manager

| Page | Description | Sources |
|------|-------------|---------|
| [[1-discover-skills]] | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a … | `skills/1-discover-skills` |
| [[1-session-skill-reflect]] | Self-improving system for skills. Analyze session for corrections/approvals, extract learnings, prop… | `skills/1-session-skill-reflect` |
| [[1-skill-atomize]] | Make catalog skills atomic: one job each, Boundary tables, hard redirects, and ask-user forks for co… | `skills/1-skill-atomize` |
| [[1-skill-linter]] | Health-check agent skills for Matt-style lean SKILL.md, chaining (prev/next/hub), references, hub me… | `skills/1-skill-linter` |
| [[0-skill-manager]] | Catalog facilities manager: CRUD skills, place them under a domain hub workflow, create new hubs, in… | `skills/0-skill-manager` |

## Hub: 0-triage

| Page | Description | Sources |
|------|-------------|---------|
| [[0-triage]] | Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if … | `skills/0-triage` |

## Hub: 0-wayfinder

| Page | Description | Sources |
|------|-------------|---------|
| [[1-to-spec]] | Turn the current conversation into a spec and publish it to the project issue tracker — no interview… | `skills/1-to-spec` |
| [[0-wayfinder]] | Plan a huge chunk of work — more than one agent session can hold — as a shared map of decision ticke… | `skills/0-wayfinder` |

## Unassigned

| Page | Description | Sources |
|------|-------------|---------|
| [[1-pi-agent-rust]] | >- | `skills/1-pi-agent-rust` |

_Live skills: **80**._
