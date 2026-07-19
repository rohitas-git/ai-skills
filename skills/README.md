# Skills catalog

Rohitas skills — Matt buckets + **hub-of-hubs** routing.

## Quickstart

1. **`/setup-rohitas-skills`** once per consumer repo.
2. **`/butler`** when lost (routes to domain hubs; does not mutate the catalog).
3. **`/skill-manager`** to add, place, rehouse, deprecate, or lint skills.

## Promotion rule

Root lists only **engineering**, **productivity**, **misc**. Not promoted: personal, in-progress, deprecated (git-only), vendor.

## Install

`skills/<bucket>/<name>/SKILL.md` · `scripts/sync-skills-symlinks.sh` flattens discoverable buckets (not deprecated/vendor).

## Buckets

| Bucket | Hub notes |
|--------|-----------|
| [engineering/](./engineering/) | setup, grilling/implement/review, on-ramps |
| [productivity/](./productivity/) | **butler**, **skill-manager**, author, ponytail, learn |
| [misc/](./misc/) | **misc** hub + office leaves |
| [personal/](./personal/) | rohitas-vault-wiki + vault-* |
| [deprecated/](./deprecated/) | tombstones |
| [vendor/](./vendor/) | offline packs |

## Promoted skills

### Engineering

- [check-work](./engineering/check-work/) — Check your work with a verification subagent that reviews diffs, runs builds
- [clean-craftmanship](./engineering/clean-craftmanship/) — Use for questions about clean code, clean architecture, SOLID principles, writing maintainable software, code structure and design, Uncle…
- [code-comments](./engineering/code-comments/) — Write clear, professional API and surface documentation using the convention
- [code-explainer](./engineering/code-explainer/) — Explain code (lines, blocks, functions, files, modules) at different audience levels (Noob, Learner, Junior, Senior) and depths (Brief, S…
- [code-review](./engineering/code-review/) — Multi-axis review of changes since a fixed point: Spec (ticket/PRD fidelity),
- [codebase-design](./engineering/codebase-design/) — Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportuni…
- [codebase-review-strategy](./engineering/codebase-review-strategy/) — Use when reviewing any codebase of unknown or varying size. Determines repo tier from measurable metrics, selects optimal thinking effort…
- [coding-standards](./engineering/coding-standards/) — Enforce lean coding standards for naming, modularity, error handling, and
- [diagnosing-bugs](./engineering/diagnosing-bugs/) — Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/thr…
- [domain-modeling](./engineering/domain-modeling/) — Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology or a ubiquitous language, record an ar…
- [execution-flow-comments](./engineering/execution-flow-comments/) — Write structured Execution Flow comments with numbered steps and ASCII branch
- [git-commit-helper](./engineering/git-commit-helper/) — Helps generate high-quality git commit messages by analyzing staged changes, untracked files, or both. Supports brief and detailed modes.…
- [grill-with-docs](./engineering/grill-with-docs/) — A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
- [implement](./engineering/implement/) — Implement a piece of work based on a spec or set of tickets.
- [improve-codebase-architecture](./engineering/improve-codebase-architecture/) — Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- [inline-comments](./engineering/inline-comments/) — Add concise one-line comments immediately above non-obvious code blocks or
- [living-documentation-governor](./engineering/living-documentation-governor/) — Use for maintaining living project documentation, enforcing code-to-docs synchronization via trigger maps, deciding knowledge placement i…
- [pi-agent-rust](./engineering/pi-agent-rust/) — Speeds up pi_agent_rust development and verification workflows. Use when editing providers,
- [pr-summarizer](./engineering/pr-summarizer/) — Summarize changes, write PR descriptions, or draft comments for pull requests. Trigger this skill whenever the user asks to "write a PR d…
- [project-wiki-manager](./engineering/project-wiki-manager/) — Use to maintain a living structured interlinked Markdown wiki knowledge base from raw sources — ingest documents, synthesize concepts wit…
- [prototype](./engineering/prototype/) — Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels rig…
- [research](./engineering/research/) — Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user want…
- [resolving-merge-conflicts](./engineering/resolving-merge-conflicts/) — Use when you need to resolve an in-progress git merge/rebase conflict.
- [setup-rohitas-skills](./engineering/setup-rohitas-skills/) — Configure this repo for Rohitas engineering skills — issue tracker, triage labels, domain docs, and optional vault root SSOT. Run once be…
- [software-architect](./engineering/software-architect/) — Act as a Grandmaster software architect and system designer. Analyze codebases/projects for current architectural strategy, evaluate agai…
- [stepdown-rule](./engineering/stepdown-rule/) — Enforce top-down file layout using the newspaper metaphor and stepdown rule
- [tdd](./engineering/tdd/) — Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integr…
- [to-spec](./engineering/to-spec/) — Turn the current conversation into a spec and publish it to the project issue tracker — no interview, just synthesis of what you've alrea…
- [to-tickets](./engineering/to-tickets/) — Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the …
- [triage](./engineering/triage/) — Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs.
- [wayfinder](./engineering/wayfinder/) — Plan a huge chunk of work — more than one agent session can hold — as a shared map of decision tickets on your issue tracker, and resolve…

### Productivity

- [butler](./productivity/butler/) — Hub of hubs for this skills catalog — real-life butler. Use when lost ("which skill?"),
- [skill-manager](./productivity/skill-manager/) — Catalog facilities manager: CRUD skills, place them under a domain hub workflow,
- [context-monitor](./productivity/context-monitor/) — Monitors conversation context usage, warns at ~50% of the limit, and provides actionable advice on saving tokens and optimizing conversat…
- [create-skill](./productivity/create-skill/) — Thin entry for authoring skills. Loads skill-creator (body craft/eval), then
- [find-skills](./productivity/find-skills/) — Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that …
- [grill-me](./productivity/grill-me/) — A relentless interview to sharpen a plan or design.
- [grilling](./productivity/grilling/) — Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' t…
- [handoff](./productivity/handoff/) — Compact the current conversation into a handoff document for another agent to pick up.
- [help](./productivity/help/) — Grok documentation and configuration help. Use when users ask about
- [learn](./productivity/learn/) — Use this skill when the user wants intellectual understanding — learning how or why something works, not getting a task done or solicitin…
- [learning-explainer](./productivity/learning-explainer/) — Unified skill for summarizing resources and explaining them across audience
- [ponytail](./productivity/ponytail/) — Forces the laziest solution that actually works, simplest, shortest, most
- [ponytail-audit](./productivity/ponytail-audit/) — Whole-repo audit for over-engineering. Like ponytail-review, but scans the
- [ponytail-debt](./productivity/ponytail-debt/) — Harvest every `ponytail:` comment in the codebase into a debt ledger, so the
- [ponytail-gain](./productivity/ponytail-gain/) — Show ponytail's measured impact as a compact scoreboard: less code, less
- [ponytail-help](./productivity/ponytail-help/) — Quick-reference card for all ponytail modes, skills, and commands.
- [ponytail-review](./productivity/ponytail-review/) — Code review focused exclusively on over-engineering. Finds what to delete:
- [reflect](./productivity/reflect/) — Self-improving system for skills. Analyze session for corrections/approvals, extract learnings, propose/update skill files, and push chan…
- [resource-summarizer](./productivity/resource-summarizer/) — Summarizes key information from resources like videos PDFs text or images using 80-20 rule Feynman technique Cornell method and other lea…
- [response-effort-calibrator](./productivity/response-effort-calibrator/) — Guides the AI on response effort, depth, and style (brief, concise, balanced, detailed, exhaustive) based on prompt cues. Use for request…
- [skill-creator](./productivity/skill-creator/) — Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch,…
- [story-teacher](./productivity/story-teacher/) — Use to turn any summary, lesson, educational text, article, book notes, video transcript, URL content, or raw document into an original, …
- [strategic-compact](./productivity/strategic-compact/) — Suggests manual context compaction at logical intervals to preserve context through task phases rather than arbitrary auto-compaction.
- [teach](./productivity/teach/) — Teach the user a new skill or concept, within this workspace.
- [thinking-steel-manning](./productivity/thinking-steel-manning/) — Use before rejecting a proposal or when you're inclined to just agree with the user. Build the strongest version of the opposing case fir…
- [writing-great-skills](./productivity/writing-great-skills/) — Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable.

### Misc

- [misc](./misc/misc/) — Hub for office/media and cross-cutting tool skills (docx, pptx, xlsx, diagrams, images,
- [defuddle](./misc/defuddle/) — Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. Use instead of WebFetch…
- [diagram-maker](./misc/diagram-maker/) — Create SVG/HTML or Excalidraw diagrams for concepts, architecture, flows, and whiteboards.
- [docx](./misc/docx/) — Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention o…
- [hatch-pet](./misc/hatch-pet/) — Create, repair, validate, visually QA, and package Codex-compatible v2 animated pets from character art, generated images, company or pro…
- [imagine](./misc/imagine/) — How to use the image_gen and image_edit tool calls in Grok Build: when to
- [json-canvas](./misc/json-canvas/) — Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with .canvas files, creating vis…
- [pptx](./misc/pptx/) — Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks…
- [xlsx](./misc/xlsx/) — Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit,…

## Success metrics

| Check | Target |
|-------|--------|
| Hub of hubs | butler (route only) |
| Catalog mutate | skill-manager |
| Misc hub | misc → leaves |
| Lint | ./scripts/lint-skills → 0 critical |

Flows: `productivity/butler/references/flows.md` · Chart: `.scratch/skills-catalog-reorg/flows-chart.html`
