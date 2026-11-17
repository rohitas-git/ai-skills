# Wiki Index

**Summary**: Live skills by domain hub. Physical path is always `skills/<name>/`.

**Last updated**: 2026-09-11 (Learn Tutor atomization and wiring audit)

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
| [[1-bro]] | Re-explain the previous assistant message in plain language (`/bro`). | `skills/1-bro` |
| [[1-caveman]] | Compress a response into terse, technically precise prose on explicit request. | `skills/1-caveman` |
| [[1-action-first-output]] | Maintain an explicit action-first session-output mode with visible progress and small next steps. | `skills/1-action-first-output` |
| [[1-context-monitor]] | Assess continuity risk from available evidence; recommend continue, compact, or hand off without invented telemetry. | `skills/1-context-monitor` |
| [[1-grok-help]] | Answer one local Grok CLI/TUI question from focused docs or secret-minimized configuration evidence. | `skills/1-grok-help` |
| [[1-handoff]] | Write one redacted, non-overwriting, verified continuation artifact at a safe task boundary. | `skills/1-handoff` |
| [[1-plow-ahead]] | Continue through routine ambiguity when the user explicitly requests autonomy. | `skills/1-plow-ahead` |
| [[1-quick-recap]] | End work with a concise green, yellow, or red completion-state signal. | `skills/1-quick-recap` |
| [[1-response-effort-calibrator]] | Apply an explicit one-request response-depth overlay without changing task scope, evidence, or authority. | `skills/1-response-effort-calibrator` |
| [[1-rewind]] | Retrieve one bounded recent moment from local Clips Rewind without acting on recovered content. | `skills/1-rewind` |
| [[1-strategic-compact]] | Produce a host-neutral same-session continuation capsule at a safe task boundary. | `skills/1-strategic-compact` |
| [[1-webmcp]] | Perform one scoped open/read/write request through a specified page's own tools with verified readback. | `skills/1-webmcp` |
| [[1-pi-agent-rust]] | Supply current-checkout pi_agent_rust surfaces and command candidates to the owning engineering workflow. | `skills/1-pi-agent-rust` |

## Hub: 1-code-review

| Page | Description | Sources |
|------|-------------|---------|
| [[1-code-review]] | Multi-axis 0-review of changes since a fixed point: Spec (ticket/PRD fidelity), Standards (repo docs +… | `skills/1-code-review` |
| [[2-ponytail-review]] | Read-only review of one pinned diff solely for evidence-backed removable complexity. | `skills/2-ponytail-review` |
| [[2-thermo-nuclear-code-quality-review]] | Extremely strict maintainability-only review: abstraction quality, giant files, spaghetti-condition growth, code-judo. | `skills/2-thermo-nuclear-code-quality-review` |
| [[2-security-and-hardening]] | Hardens code against vulnerabilities while building or remediating. Use when handling user input, au… | `skills/2-security-and-hardening` |
| [[2-dependency-security]] | Review application dependency vulnerabilities, staleness, and newly introduced packages without turning existing debt into unrelated PR blockers. | `skills/2-dependency-security` |
| [[2-software-architect]] | Bounded, evidence-backed system decision analysis with viable alternatives, conditions, and migration/verification implications. | `skills/2-software-architect` |
| [[2-verify-work]] | Check your work with a verification subagent that reviews diffs, runs builds and tests, and evaluate… | `skills/2-verify-work` |

## Hub: 0-diagnosing-bugs

| Page | Description | Sources |
|------|-------------|---------|
| [[0-diagnosing-bugs]] | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug t… | `skills/0-diagnosing-bugs` |
| [[1-parallel-agents]] | One focused agent per independent problem domain (dual Ship; multi-failure). | `skills/1-parallel-agents` |
| [[1-tdd]] | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions … | `skills/1-tdd` |
| [[1-browser-testing-with-devtools]] | Runtime browser verification via Chrome DevTools MCP (DOM, console, network, performance,… | `skills/1-browser-testing-with-devtools` |
| [[1-playwright-browser-testing]] | Write and run focused Playwright checks for permitted web applications. | `skills/1-playwright-browser-testing` |
| [[1-performance-optimization]] | Measure-first performance work across FE/BE/DB. Use when Core Web Vitals, load times, N+1… | `skills/1-performance-optimization` |

## Hub: 0-grilling

| Page | Description | Sources |
|------|-------------|---------|
| [[1-domain-modeling]] | Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology o… | `skills/1-domain-modeling` |
| [[1-grill-me]] | A relentless interview to sharpen a plan or design. | `skills/1-grill-me` |
| [[1-grill-with-docs]] | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as … | `skills/1-grill-with-docs` |
| [[0-grilling]] | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test … | `skills/0-grilling` |
| [[1-anti-sycophancy]] | Eliminate sycophantic agreement: independent claim assessment, evidence-first conclusions, praise/empathy suppression. | `skills/1-anti-sycophancy` |
| [[1-brainstorm]] | Hard-gate design before implementation: approaches, design doc, approval. Superpowers harvest. | `skills/1-brainstorm` |
| [[1-critique]] | Rigorous intellectual scrutiny on explicit request: challenge assumptions, demand evidence, logical gaps, framing. | `skills/1-critique` |
| [[1-honest-advisor]] | Pressure-test an interpersonal conflict or decision with facts, assumptions, opposing view, and one concrete move. | `skills/1-honest-advisor` |
| [[1-prototype]] | Build a throwaway 1-prototype to answer a design question. Use when the user wants to sanity-check whe… | `skills/1-prototype` |
| [[1-visual-plan]] | Publish a plan as an interactive visual review artifact. | `skills/1-visual-plan` |
| [[1-thinking-steel-manning]] | Use before rejecting a proposal or when you're inclined to just agree with the user. Build the stron… | `skills/1-thinking-steel-manning` |

## Hub: 0-implement

| Page | Description | Sources |
|------|-------------|---------|
| [[1-code-comments]] | Assess or edit language-native documentation for one public/exported code surface. | `skills/1-code-comments` |
| [[1-execution-flow-comments]] | Assess or edit one explicitly requested numbered execution-flow block for one function. | `skills/1-execution-flow-comments` |
| [[1-execute-plan]] | Execute a written implementation plan in a separate session with review checkpoints. | `skills/1-execute-plan` |
| [[1-finish-branch]] | After tests pass: merge, open PR, or cleanup the branch. | `skills/1-finish-branch` |
| [[1-atomic-git-commits]] | Partition changes into small, independently understandable and revertible verified commits. | `skills/1-atomic-git-commits` |
| [[1-git-worktrees]] | Isolated workspace via platform tools or git worktree. | `skills/1-git-worktrees` |
| [[0-implement]] | "Implement a piece of work based on a spec or set of tickets." | `skills/0-implement` |
| [[1-inline-comments]] | Assess or edit one concise why/constraint comment for one internal code block. | `skills/1-inline-comments` |
| [[1-karpathy-guidelines]] | Behavioral guidelines that cut common LLM coding mistakes: surface assumptions, simplicity first, surgical diffs, goal-driven verification. | `skills/1-karpathy-guidelines` |
| [[1-parallel-agents]] | One focused agent per independent problem domain (parallel investigations). | `skills/1-parallel-agents` |
| [[1-pr-summarizer]] | Summarize changes, write PR descriptions, or draft comments for pull requests. Trigger this skill wh… | `skills/1-pr-summarizer` |
| [[1-research]] | Answer one bounded question from current authoritative sources; persist only when requested. | `skills/1-research` |
| [[1-resolving-merge-conflicts]] | "Use when you need to resolve an in-progress git merge/rebase conflict." | `skills/1-resolving-merge-conflicts` |
| [[1-stepdown-rule]] | Assess or apply one behavior-independent top-down declaration reorder in one source file. | `skills/1-stepdown-rule` |
| [[1-subagent-implement]] | Same-session plan execution: fresh implementer subagent per task + reviews. | `skills/1-subagent-implement` |
| [[1-write-plan]] | Bite-sized implementation plan from an approved design/spec before coding. | `skills/1-write-plan` |
| [[1-to-spec]] | Synthesize one settled source into one right-sized draft, local, or tracker specification artifact. | `skills/1-to-spec` |
| [[1-to-tickets]] | Derive or materialize one dependency-aware ticket set from one approved specification. | `skills/1-to-tickets` |
| [[1-ci-cd-and-automation]] | Build/test/deploy pipelines and quality gates. Use when setting up or changing CI, releas… | `skills/1-ci-cd-and-automation` |
| [[1-observability-and-instrumentation]] | Logging, metrics, tracing, and alerting so production behavior is diagnosable. Use when a… | `skills/1-observability-and-instrumentation` |
| [[1-shipping-and-launch]] | Pre-launch checklist, staged rollout, monitoring, and rollback planning. Use when prepari… | `skills/1-shipping-and-launch` |
| [[1-constraint-driven-development]] | Establish a measurable quality contract and detect attempts to weaken it. | `skills/1-constraint-driven-development` |

## Hub: 0-improve-codebase-architecture

| Page | Description | Sources |
|------|-------------|---------|
| [[1-clean-craftsmanship]] | Context-sensitive maintainability and Clean Code/Architecture principles, trade-offs, and low-risk next steps. | `skills/1-clean-craftsmanship` |
| [[1-codebase-design]] | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module'… | `skills/1-codebase-design` |
| [[1-coding-standards]] | Always-on lean standards for naming, modularity, and comments. | `skills/1-coding-standards` |
| [[1-error-handling]] | Atomic failure contracts, TS/JS errors, safe recovery, cleanup, and verification. | `skills/1-error-handling` |
| [[1-go-best-practices]] | Idiomatic Go design, error, concurrency, API, and testing practice for Go changes and reviews. | `skills/1-go-best-practices` |
| [[1-graphify]] | Build or query an explicitly requested local Graphify codebase graph; never installs or enables persistent behavior. | `skills/1-graphify` |
| [[0-improve-codebase-architecture]] | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill throug… | `skills/0-improve-codebase-architecture` |
| [[1-living-documentation-governor]] | Pinned code↔canonical-doc contract: drift assessment, scoped updates, and honest trigger enforcement. | `skills/1-living-documentation-governor` |
| [[1-project-wiki-manager]] | Grounded in-repository concept wiki from declared project sources; scoped ingest and read-only query/audit. | `skills/1-project-wiki-manager` |
| [[1-api-and-interface-design]] | Stable APIs and module boundaries (REST/GraphQL/types). Use when designing public interfa… | `skills/1-api-and-interface-design` |
| [[1-deprecation-and-migration]] | Sunset APIs/features and migrate callers safely. Use when removing systems, expand/contra… | `skills/1-deprecation-and-migration` |
| [[1-pending-migration-hygiene]] | Rewrite pending migrations only with complete observed provenance or exact human attestation; otherwise retain or append forward. | `skills/1-pending-migration-hygiene` |
| [[1-supabase-schema-migration]] | Author and locally verify one application-owned schema concept on an exact disposable stack. | `skills/1-supabase-schema-migration` |
| [[1-supabase]] | Implement or diagnose one bounded Supabase product-integration concern. | `skills/1-supabase` |
| [[1-supabase-postgres-best-practices]] | Analyze or improve one measured Postgres query, schema, RLS, lock, or connection concern. | `skills/1-supabase-postgres-best-practices` |

## Hub: 0-learn

| Page | Description | Sources |
|------|-------------|---------|
| [[1-code-explainer]] | Explain one exact supplied or current-worktree code candidate without reviewing, testing, or editing it. | `skills/1-code-explainer` |
| [[1-explain-with-example]] | Explain one exact selected object with evidence-preserving lenses, one grounded example, and a non-executing dry run. | `skills/1-explain-with-example` |
| [[0-learn]] | Domain hub for intellectual understanding — how/why something works, not shipping code or vault comp… | `skills/0-learn` |
| [[1-learning-explainer]] | Route one concept request to exactly one diagnostic, first explanation, model, or deep-dive leaf. | `skills/1-learning-explainer` |
| [[1-learning-diagnostic]] | Return a minimal evidence-labeled learner profile without teaching or persistence. | `skills/1-learning-diagnostic` |
| [[1-level-explainer]] | Give one truth-preserving first explanation at one evidenced audience level. | `skills/1-level-explainer` |
| [[1-mental-model-builder]] | Build one mapped, predictive model and state where it breaks. | `skills/1-mental-model-builder` |
| [[1-progressive-deep-dive]] | Add one requested layer to one identified part of an existing explanation. | `skills/1-progressive-deep-dive` |
| [[1-tutor]] | Guide one learner through one bounded problem with progressive hints and transfer evidence. | `skills/1-tutor` |
| [[1-resource-summarizer]] | Summarize one supplied source or bounded selection while preserving provenance, claim status, and coverage limits. | `skills/1-resource-summarizer` |
| [[1-story-teacher]] | Transform one supplied idea into one original narrative without losing source caveats or inventing evidence. | `skills/1-story-teacher` |
| [[1-teach]] | Route one durable multi-session learning-workspace operation to a focused leaf. | `skills/1-teach` |
| [[1-teaching-workspace]] | Establish one explicit learning workspace and its confirmed mission. | `skills/1-teaching-workspace` |
| [[1-lesson-authoring]] | Author one new, mission-linked, non-overwriting lesson in an explicit workspace. | `skills/1-lesson-authoring` |
| [[1-learning-progress-record]] | Append one evidence-labeled learning event that changes the next teaching decision. | `skills/1-learning-progress-record` |
| [[1-learning-glossary]] | Govern one evidence-grounded canonical term without rewriting glossary history. | `skills/1-learning-glossary` |
| [[1-vault-explain]] | Bind one exact private-vault Concept evidence packet to one Learn explanation and return read-only. | `skills/1-vault-explain` |

## Hub: 0-office

| Page | Description | Sources |
|------|-------------|---------|
| [[1-defuddle]] | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to… | `skills/1-defuddle` |
| [[1-diagram-maker]] | Create SVG/HTML or Excalidraw diagrams for concepts, architecture, flows, and whiteboards. | `skills/1-diagram-maker` |
| [[1-docx]] | "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx f… | `skills/1-docx` |
| [[1-hatch-pet]] | Route one Codex v2 animated-pet request to one build, repair, validate, or install operation. | `skills/1-hatch-pet` |
| [[2-hatch-pet-build]] | Build one new validated Codex v2 pet candidate without installing or publishing it. | `skills/2-hatch-pet-build` |
| [[2-hatch-pet-repair]] | Repair one verified defect class in a copied Codex v2 pet candidate. | `skills/2-hatch-pet-repair` |
| [[2-hatch-pet-validate]] | Read-only validate one immutable Codex v2 pet atlas or package. | `skills/2-hatch-pet-validate` |
| [[2-hatch-pet-install]] | Install one hash-pinned validated Codex v2 pet candidate into one exact local destination. | `skills/2-hatch-pet-install` |
| [[1-imagine]] | Generate or edit one raster image through the current host capability with explicit reference and effect boundaries. | `skills/1-imagine` |
| [[1-internal-comms]] | Draft concise internal communications: status or leadership updates, project updates, incident reports, FAQs, and company newsletters. | `skills/1-internal-comms` |
| [[1-json-canvas]] | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when wor… | `skills/1-json-canvas` |
| [[0-office]] | Route one immutable office/media artifact request to one smallest leaf without performing the artifact work. | `skills/0-office` |
| [[1-pptx]] | "Use this skill any time a .pptx file is involved in any way — as input, output, or both. This inclu… | `skills/1-pptx` |
| [[1-pdf]] | Safely inspect, create, edit, and verify PDF files. | `skills/1-pdf` |
| [[1-xlsx]] | "Use this skill any time a spreadsheet file is the primary input or output. This means any task wher… | `skills/1-xlsx` |

## Hub: 0-ui-ux

| Page | Description | Sources |
|------|-------------|---------|
| [[0-ui-ux]] | Route one UI/UX request to one smallest specialist without performing design, implementation, browser, or file work. | `skills/0-ui-ux` |
| [[1-ui-ux-pro-max]] | Produce one evidence-labeled, read-only UI/UX direction packet from the bundled local corpus. | `skills/1-ui-ux-pro-max` |
| [[1-impeccable]] | Run one explicit command from the current installed Impeccable UI workflow on one pinned surface. | `skills/1-impeccable` |
| [[1-visual-edit]] | Run one explicit open, inspect, preview, or apply operation through installed Agent-Native Design. | `skills/1-visual-edit` |
| [[1-brand]] | Route one brand request to guideline authoring, read-only review, or context extraction. | `skills/1-brand` |
| [[2-brand-guidelines]] | Draft or apply one evidence-backed brand-guideline contract. | `skills/2-brand-guidelines` |
| [[2-brand-review]] | Read-only review one candidate against one approved brand contract. | `skills/2-brand-review` |
| [[2-brand-context-extract]] | Extract one minimal brand context packet for one named consumer. | `skills/2-brand-context-extract` |
| [[1-design-system]] | Draft or apply one versioned token and component-contract set without implementing UI. | `skills/1-design-system` |
| [[1-ui-styling]] | One behavior-preserving presentation-only UI change | `skills/1-ui-styling` |
| [[1-design]] | Create or revise one logo, icon, social image, or identity mockup. | `skills/1-design` |
| [[1-banner-design]] | Create or revise one banner, ad, hero image, or print promotion. | `skills/1-banner-design` |
| [[1-slides]] | Create or revise one self-contained HTML presentation (not Office PPTX). | `skills/1-slides` |
| [[1-frontend-ui-engineering]] | Production a11y UI engineering (Ship primary; soft dual here) | `skills/1-frontend-ui-engineering` |
| [[1-user-research]] | Route one study-plan or completed-evidence synthesis operation. | `skills/1-user-research` |
| [[2-user-research-plan]] | Author one decision-linked research protocol without executing it. | `skills/2-user-research-plan` |
| [[2-user-research-synthesis]] | Synthesize one fixed participant-evidence set with provenance and privacy limits. | `skills/2-user-research-synthesis` |
| [[1-customer-experience-audit]] | Audit one external-customer journey and rank evidence-marked, high-leverage improvements. | `skills/1-customer-experience-audit` |

## Hub: 0-thinking

| Page | Description | Sources |
|------|-------------|---------|
| [[1-perspective-analysis]] | Separate stakeholder, persona, or thinking-mode viewpoints before synthesizing a decision. | `skills/1-perspective-analysis` |
| [[1-thinking-ethical]] | Map stakeholders, values, harms, power, safeguards, and residual risk. | `skills/1-thinking-ethical` |
| [[1-thinking-lateral]] | Escape a stuck framing through a safe provocation and testable candidates. | `skills/1-thinking-lateral` |
| [[1-strategic-analysis]] | Assess strategic position, market forces, scenarios, and option trade-offs. | `skills/1-strategic-analysis` |
| [[1-competitive-analysis]] | Compare named competitors with an evidence-marked matrix and positioning recommendation. | `skills/1-competitive-analysis` |

## Hub: 0-ponytail

| Page | Description | Sources |
|------|-------------|---------|
| [[0-ponytail]] | Explicit coding-only overlay and router for the smallest correct, repository-aligned solution. | `skills/0-ponytail` |
| [[1-ponytail-audit]] | Read-only audit of evidence-backed removable complexity in one bounded repository snapshot. | `skills/1-ponytail-audit` |
| [[1-ponytail-debt]] | Return a bounded read-only ledger of exact `0-ponytail:` markers. | `skills/1-ponytail-debt` |
| [[1-ponytail-gain]] | Display one pinned upstream agentic benchmark with methodology and limitations. | `skills/1-ponytail-gain` |
| [[1-ponytail-help]] | Catalog-accurate one-shot reference for Ponytail levels and child skills. | `skills/1-ponytail-help` |

## Hub: 0-review

| Page | Description | Sources |
|------|-------------|---------|
| [[1-codebase-review-strategy]] | Produce one risk-based coverage and evidence plan for an unfamiliar codebase. | `skills/1-codebase-review-strategy` |
| [[1-agent-pr-review]] | Risk-focused review pass for AI-authored pull requests: CI protection, duplicate utilities, critical paths, and agent workflows. | `skills/1-agent-pr-review` |
| [[1-clean-tautological-tests]] | Audit and rewrite tautological, echo, mock-only and zero-signal unit tests into behavioral tests behind a mutation check. | `skills/1-clean-tautological-tests` |
| [[1-complete-pr-review]] | Comprehensive, evidence-backed, risk-weighted review of one fixed PR; read-only and scope-bounded. | `skills/1-complete-pr-review` |
| [[1-receive-review]] | Process incoming code review feedback with technical rigor (verify, evaluate, implement one-by-one). | `skills/1-receive-review` |
| [[0-review]] | Domain hub for verification modes — multi-axis change 0-review, security audit, architecture 0-review, a… | `skills/0-review` |
| [[1-doubt-driven-development]] | Run one read-only adversarial pass over a consequential claim or decision. | `skills/1-doubt-driven-development` |
| [[1-visual-recap]] | Draft, create, or update one private visual orientation artifact for one exact change candidate. | `skills/1-visual-recap` |

## Hub: 0-rohitas-vault-wiki

| Page | Description | Sources |
|------|-------------|---------|
| [[1-obsidian-bases]] | Create or edit one exact `.base` candidate or named view with version-aware static and optional runtime evidence. | `skills/1-obsidian-bases` |
| [[1-obsidian-cli]] | Execute one exact supported Obsidian CLI operation against one pinned vault/target with explicit effects. | `skills/1-obsidian-cli` |
| [[1-obsidian-markdown]] | Make one bounded Obsidian-specific syntax change in one exact Markdown file without app or vault-wide effects. | `skills/1-obsidian-markdown` |
| [[0-rohitas-vault-wiki]] | Route one operation for Rohitas's configured personal vault while preserving schema, privacy, authority, and caller return. | `skills/0-rohitas-vault-wiki` |
| [[1-vault-inbox]] | Capture one supplied item as one new, privacy-bounded, non-overwriting Inbox note and return evidence. | `skills/1-vault-inbox` |
| [[1-vault-ingest]] | Reconcile one fixed source snapshot into one explicit, verified permanent-note change set. | `skills/1-vault-ingest` |
| [[1-vault-lint]] | Produce one snapshot-bound, read-only Vault health report with explicit coverage and evidence. | `skills/1-vault-lint` |
| [[1-vault-repair]] | Revalidate and repair one accepted Vault Lint finding without broad cleanup or a new audit. | `skills/1-vault-repair` |
| [[1-wiki-query]] | Answer one bounded question from a pinned personal-vault snapshot with exact note evidence and no writes. | `skills/1-wiki-query` |

## Hub: 1-security-auditor

| Page | Description | Sources |
|------|-------------|---------|
| [[1-security-auditor]] | Multi-phase security and quality auditor for codebases and projects. Use for security audit, vulnera… | `skills/1-security-auditor` |
| [[2-prompt-injection-defense]] | Design and verify prompt-injection defenses at agent trust boundaries. | `skills/2-prompt-injection-defense` |
| [[2-skill-supply-chain-audit]] | Audit third-party agent skills and packages for provenance and risky behavior. | `skills/2-skill-supply-chain-audit` |

## Hub: 0-setup-rohitas-skills

| Page | Description | Sources |
|------|-------------|---------|
| [[0-setup-rohitas-skills]] | Configure this repo for Rohitas engineering skills — issue tracker, 0-triage labels, domain docs, and … | `skills/0-setup-rohitas-skills` |
| [[1-setup-issue-tracker]] | Configure the repository issue-tracker SSOT. | `skills/1-setup-issue-tracker` |
| [[1-setup-domain-docs]] | Configure CONTEXT.md and ADR document layout. | `skills/1-setup-domain-docs` |
| [[1-setup-vault-root]] | Record the personal vault root for repository-local skills. | `skills/1-setup-vault-root` |
| [[1-setup-triage-labels]] | Configure the opt-in 0-triage label mapping. | `skills/1-setup-triage-labels` |

## Hub: 0-skill-creator

| Page | Description | Sources |
|------|-------------|---------|
| [[1-create-skill]] | Thin entry that returns one new body candidate through 0-skill-creator; it does not auto-place or install. | `skills/1-create-skill` |
| [[0-skill-creator]] | Author or evaluate one pinned skill body in draft, update, trigger-eval, or output-eval mode. | `skills/0-skill-creator` |
| [[1-writing-great-skills]] | Apply concise invocation, disclosure, completion, and pruning craft to one body candidate. | `skills/1-writing-great-skills` |
| [[1-source-backed-skill]] | Author one private reference-skill candidate from an authorized fixed corpus. | `skills/1-source-backed-skill` |

## Hub: 0-skill-manager

| Page | Description | Sources |
|------|-------------|---------|
| [[1-discover-skills]] | Discover and vet external skill candidates without installing or executing them. | `skills/1-discover-skills` |
| [[1-session-skill-reflect]] | Read-only reflection that proposes one evidence-backed skill improvement from a bounded completed run. | `skills/1-session-skill-reflect` |
| [[1-skill-atomize]] | Assess or repair one pinned cluster of overlapping live skills without broadening their jobs. | `skills/1-skill-atomize` |
| [[1-skill-linter]] | Report structural and routing health for one pinned skill, hub, diff, or catalog snapshot. | `skills/1-skill-linter` |
| [[0-skill-manager]] | Apply one bounded catalog change-set with revision-safe writes and separately gated external effects. | `skills/0-skill-manager` |

## Hub: 0-triage

| Page | Description | Sources |
|------|-------------|---------|
| [[0-triage]] | Route one raw human issue or external-PR triage request to exactly one atomic operation. | `skills/0-triage` |
| [[1-triage-inbox]] | Return one read-only, cutoff-bounded snapshot of raw tracker items needing attention. | `skills/1-triage-inbox` |
| [[1-triage-assess]] | Produce one read-only triage assessment and transition draft for one issue or external PR. | `skills/1-triage-assess` |
| [[1-triage-apply]] | Apply and verify one explicitly approved transition packet to one exact tracker candidate. | `skills/1-triage-apply` |

## Hub: 0-wayfinder

| Page | Description | Sources |
|------|-------------|---------|
| [[0-wayfinder]] | Route one multi-session uncertainty-map request without reading or mutating the candidate itself. | `skills/0-wayfinder` |
| [[1-wayfinder-chart]] | Produce one new draft, local, or tracker uncertainty-map set from an accepted destination. | `skills/1-wayfinder-chart` |
| [[1-wayfinder-advance]] | Advance one existing map through exactly one frontier decision-ticket cycle. | `skills/1-wayfinder-advance` |

## Unassigned

| Page | Description | Sources |
|------|-------------|---------|
| [[1-pi-agent-rust]] | >- | `skills/1-pi-agent-rust` |

## Hub: 0-git

| Page | Description | Sources |
|------|-------------|---------|
| [[0-git]] | Route safe Git workflows: worktrees, atomic commits, conflicts, and branch completion. | `skills/0-git` |
| [[1-git-worktrees]] | Create or reuse an isolated workspace and choose safe local-service isolation. | `skills/1-git-worktrees` |
| [[1-atomic-git-commits]] | Partition changes into small, independently understandable and revertible verified commits. | `skills/1-atomic-git-commits` |
| [[1-git-text-normalization]] | Diagnose or apply one authorized exact-path encoding, EOL, or Git-attribute correction. | `skills/1-git-text-normalization` |
| [[1-git-changelog]] | Draft an editable changelog or release summary from local Git history. | `skills/1-git-changelog` |
| [[1-resolving-merge-conflicts]] | Resolve an active Git merge or rebase conflict. | `skills/1-resolving-merge-conflicts` |
| [[1-github-cli]] | Run one explicitly authorized GitHub CLI operation with read-only default. | `skills/1-github-cli` |
| [[1-github-pr-comment-intake]] | Fetch and classify GitHub PR discussion into a repair queue without changing it. | `skills/1-github-pr-comment-intake` |
| [[1-pr-comment-drafter]] | Draft one evidence-backed outbound PR response or status comment without posting it. | `skills/1-pr-comment-drafter` |
| [[1-stacked-pr-review-and-repair]] | Review, repair, rebase, and verify every PR in a dependent stack. | `skills/1-stacked-pr-review-and-repair` |
| [[1-stacked-pr-repair]] | Repair known findings and blockers across a PR stack without performing a fresh review. | `skills/1-stacked-pr-repair` |
| [[1-finish-branch]] | Choose and execute the outcome for a verified branch. | `skills/1-finish-branch` |
| [[1-pr-summarizer]] | Draft a reviewer-ready main PR description from verified intent, changes, and validation. | `skills/1-pr-summarizer` |
| [[1-pr-repair]] | Repair known findings and blockers on one PR without performing a fresh review. | `skills/1-pr-repair` |
| [[1-pr-review-and-repair]] | Review, repair, rebase, push, and verify one PR until clean and green. | `skills/1-pr-review-and-repair` |

_Live skills: **174**._

## Domain 18 — Agent Engineering

| Page | Description | Sources |
|------|-------------|---------|
| [[0-agent-engineering]] | Route one AI-agent-system concern to one specialist while preserving candidate, trust, worktree, and authority boundaries. | `skills/0-agent-engineering` |
| [[1-agent-evaluation]] | Design evaluation sets, graders, baselines, and release gates. | `skills/1-agent-evaluation` |
| [[1-tool-schema-design]] | Design constrained, model-facing tool schemas. | `skills/1-tool-schema-design` |
| [[1-human-in-the-loop]] | Design approval gates, escalation paths, and human oversight. | `skills/1-human-in-the-loop` |
| [[1-mcp-server-building]] | Design, implement, and validate MCP servers. | `skills/1-mcp-server-building` |
| [[1-agent-workflow-observer]] | Identify safe automation and skill-improvement opportunities from a bounded agent run. | `skills/1-agent-workflow-observer` |
| [[1-parallel-agents]] | Coordinate independent concurrent workstreams (Diagnose primary). | `skills/1-parallel-agents` |
| [[1-observability-and-instrumentation]] | Add traces, costs, SLOs, and agent telemetry (Ship primary). | `skills/1-observability-and-instrumentation` |
| [[2-prompt-injection-defense]] | Prompt-injection boundaries (Security primary). | `skills/2-prompt-injection-defense` |
| [[2-skill-supply-chain-audit]] | Third-party skill/package provenance (Security primary). | `skills/2-skill-supply-chain-audit` |

## Domain 19 — DevOps

| Page | Description | Sources |
|------|-------------|---------|
| [[0-devops]] | Route infrastructure, platform, delivery, reliability, incident, and compliance operations. | `skills/0-devops` |
| [[1-infrastructure-as-code]] | Design and verify declarative infrastructure definitions and plans. | `skills/1-infrastructure-as-code` |
| [[1-cloud-platform-operations]] | Operate AWS, Azure, GCP, and Cloudflare managed resources. | `skills/1-cloud-platform-operations` |
| [[1-container-platform-operations]] | Operate container images, registries, Kubernetes, Helm, and GitOps. | `skills/1-container-platform-operations` |
| [[1-database-and-storage-operations]] | Operate databases, storage, backups, and restore paths. | `skills/1-database-and-storage-operations` |
| [[1-postgres-read-only]] | Inspect PostgreSQL schema or data using bounded, non-mutating queries. | `skills/1-postgres-read-only` |
| [[1-network-and-edge-operations]] | Operate DNS, traffic routing, edge, firewall, VPN, and TLS controls. | `skills/1-network-and-edge-operations` |
| [[1-server-and-fleet-operations]] | Operate hosts, system services, SSH, patches, and device fleets. | `skills/1-server-and-fleet-operations` |
| [[1-platform-engineering]] | Build internal platforms, golden paths, and reproducible environments. | `skills/1-platform-engineering` |
| [[1-ai-platform-operations]] | Operate model serving, RAG, GPU, caching, and LLMOps infrastructure. | `skills/1-ai-platform-operations` |
| [[1-identity-and-secrets-management]] | Operate IAM, SSO, access review, KMS, Vault, and secret lifecycle. | `skills/1-identity-and-secrets-management` |
| [[1-incident-response]] | Coordinate active incident containment, recovery, and evidence. | `skills/1-incident-response` |
| [[1-resilience-and-disaster-recovery]] | Design and test backup, failover, disaster recovery, and continuity. | `skills/1-resilience-and-disaster-recovery` |
| [[1-compliance-engineering]] | Translate compliance requirements into technical controls and evidence. | `skills/1-compliance-engineering` |

## Domain 20 — Marketing

| Page | Description | Sources |
|------|-------------|---------|
| [[0-marketing]] | Route one marketing request to the narrowest focused specialist. | `skills/0-marketing` |
| [[1-marketing-ab-testing]] | Plan and assess one marketing A/B experiment. | `skills/1-marketing-ab-testing` |
| [[1-marketing-ad-creative]] | Draft and iterate paid-ad creative. | `skills/1-marketing-ad-creative` |
| [[1-marketing-ads]] | Plan or audit one paid-advertising campaign. | `skills/1-marketing-ads` |
| [[1-marketing-ai-seo]] | Improve one site's visibility in AI-generated search answers. | `skills/1-marketing-ai-seo` |
| [[1-marketing-analytics]] | Design or audit marketing tracking and measurement. | `skills/1-marketing-analytics` |
| [[1-marketing-aso]] | Audit or improve one app-store listing. | `skills/1-marketing-aso` |
| [[1-marketing-attribution]] | Analyze which marketing activity drives conversion or revenue. | `skills/1-marketing-attribution` |
| [[1-marketing-churn-prevention]] | Design one customer-retention or cancellation intervention. | `skills/1-marketing-churn-prevention` |
| [[1-marketing-co-marketing]] | Plan one co-marketing or partner campaign. | `skills/1-marketing-co-marketing` |
| [[1-marketing-cold-email]] | Draft one B2B cold-email sequence. | `skills/1-marketing-cold-email` |
| [[1-marketing-community-marketing]] | Plan one community-led marketing program. | `skills/1-marketing-community-marketing` |
| [[1-marketing-competitor-profiling]] | Build an evidence-backed marketing profile of named competitors. | `skills/1-marketing-competitor-profiling` |
| [[1-marketing-competitors]] | Create one competitor-comparison or alternative-page plan. | `skills/1-marketing-competitors` |
| [[1-marketing-content-strategy]] | Plan one marketing content portfolio or roadmap. | `skills/1-marketing-content-strategy` |
| [[1-marketing-copy-editing]] | Edit one existing piece of marketing copy. | `skills/1-marketing-copy-editing` |
| [[1-marketing-copywriting]] | Write one bounded marketing page or message. | `skills/1-marketing-copywriting` |
| [[1-marketing-cro]] | Audit or improve conversion on one marketing page or form. | `skills/1-marketing-cro` |
| [[1-marketing-customer-research]] | Conduct or synthesize customer research for a marketing decision. | `skills/1-marketing-customer-research` |
| [[1-marketing-directory-submissions]] | Prepare a bounded product-directory submission plan. | `skills/1-marketing-directory-submissions` |
| [[1-marketing-emails]] | Create or improve one lifecycle-email sequence. | `skills/1-marketing-emails` |
| [[1-marketing-events]] | Plan one marketing event, webinar, sponsorship, or speaking motion. | `skills/1-marketing-events` |
| [[1-marketing-free-tools]] | Design one free tool as a marketing asset. | `skills/1-marketing-free-tools` |
| [[1-marketing-image]] | Specify or optimize one marketing-image asset. | `skills/1-marketing-image` |
| [[1-marketing-influencer-marketing]] | Plan one influencer, creator, or ambassador program. | `skills/1-marketing-influencer-marketing` |
| [[1-marketing-launch]] | Plan one product-marketing launch or announcement. | `skills/1-marketing-launch` |
| [[1-marketing-lead-magnets]] | Plan or improve one lead magnet. | `skills/1-marketing-lead-magnets` |
| [[1-marketing-marketing-council]] | Compare several named marketing perspectives on one question. | `skills/1-marketing-marketing-council` |
| [[1-marketing-marketing-ideas]] | Generate and prioritize marketing tactics for a software product. | `skills/1-marketing-marketing-ideas` |
| [[1-marketing-marketing-loops]] | Design one bounded recurring marketing workflow. | `skills/1-marketing-marketing-loops` |
| [[1-marketing-marketing-plan]] | Build one evidence-bounded marketing plan. | `skills/1-marketing-marketing-plan` |
| [[1-marketing-marketing-psychology]] | Apply behavioral principles to one marketing decision. | `skills/1-marketing-marketing-psychology` |
| [[1-marketing-offers]] | Design or improve one commercial offer. | `skills/1-marketing-offers` |
| [[1-marketing-onboarding]] | Optimize one post-signup activation or onboarding flow. | `skills/1-marketing-onboarding` |
| [[1-marketing-paywalls]] | Optimize one in-product paywall or upgrade prompt. | `skills/1-marketing-paywalls` |
| [[1-marketing-popups]] | Optimize one marketing popup, modal, overlay, or banner. | `skills/1-marketing-popups` |
| [[1-marketing-pricing]] | Research or design one pricing and packaging decision. | `skills/1-marketing-pricing` |
| [[1-marketing-product-marketing]] | Create or update one product-marketing context document. | `skills/1-marketing-product-marketing` |
| [[1-marketing-programmatic-seo]] | Plan one template-and-data programmatic SEO system. | `skills/1-marketing-programmatic-seo` |
| [[1-marketing-prospecting]] | Build an evidence-backed prospecting plan or shortlist. | `skills/1-marketing-prospecting` |
| [[1-marketing-public-relations]] | Plan one earned-media or public-relations motion. | `skills/1-marketing-public-relations` |
| [[1-marketing-referrals]] | Design one referral or affiliate program. | `skills/1-marketing-referrals` |
| [[1-marketing-revops]] | Design one revenue-operations lifecycle, routing, or reporting change. | `skills/1-marketing-revops` |
| [[1-marketing-sales-enablement]] | Create one bounded sales-enablement asset. | `skills/1-marketing-sales-enablement` |
| [[1-marketing-schema]] | Design or audit website structured-data markup. | `skills/1-marketing-schema` |
| [[1-marketing-seo-audit]] | Audit one site's technical and on-page SEO. | `skills/1-marketing-seo-audit` |
| [[1-marketing-signup]] | Optimize one signup, registration, or trial-start flow. | `skills/1-marketing-signup` |
| [[1-marketing-site-architecture]] | Plan one marketing-site hierarchy, navigation, and URL structure. | `skills/1-marketing-site-architecture` |
| [[1-marketing-sms]] | Plan or draft one compliant SMS or MMS marketing sequence. | `skills/1-marketing-sms` |
| [[1-marketing-social]] | Plan or draft one social-media content program. | `skills/1-marketing-social` |
| [[1-marketing-video]] | Plan one marketing-video concept, script, or production specification. | `skills/1-marketing-video` |

## Domain 16 — Thinking

| [[0-thinking]] | Domain hub: structured mental models (diagnose/decide/create/risk) | `skills/0-thinking` |
| [[1-plan-arbiter]] | Compare competing plans and choose one executable direction. | `skills/1-plan-arbiter` |
| [[1-thinking-bounded-rationality]] | Use when search or investigation could run forever. Set an explicit good-enough … | `skills/1-thinking-bounded-rationality` |
| [[1-thinking-circle-of-competence]] | Use when a specific claim may lack grounding. Check evidence boundary, size wron… | `skills/1-thinking-circle-of-competence` |
| [[1-thinking-cynefin]] | When the right response mode is unclear, classify the cause-effect domain first;… | `skills/1-thinking-cynefin` |
| [[1-thinking-effectuation]] | Under genuine uncertainty with no reliable forecast, inventory means, cap downsi… | `skills/1-thinking-effectuation` |
| [[1-thinking-first-principles]] | When a constraint is treated as fixed, separate physics from convention, keep on… | `skills/1-thinking-first-principles` |
| [[1-thinking-lateral]] | Escape a stuck framing with a safe provocation, concept fan, and actionable candidates. | `skills/1-thinking-lateral` |
| [[1-thinking-five-whys-plus]] | When a fault is localized and the proximate cause is known but the systemic root… | `skills/1-thinking-five-whys-plus` |
| [[1-thinking-jobs-to-be-done]] | Deciding what to build or why adoption fails. Recover the progress users hire a … | `skills/1-thinking-jobs-to-be-done` |
| [[1-thinking-kepner-tregoe]] | Use when a selective defect needs IS/IS-NOT difference analysis or a consequenti… | `skills/1-thinking-kepner-tregoe` |
| [[1-thinking-lindy-effect]] | Use when longevity of a non-perishable option matters. Treat survival duration a… | `skills/1-thinking-lindy-effect` |
| [[1-thinking-ethical]] | Examine an action through stakeholders, values, harms, power, safeguards, and residual risk. | `skills/1-thinking-ethical` |
| [[1-thinking-map-territory]] | When a claim, doc, test, metric, or assumption conflicts with observed behavior,… | `skills/1-thinking-map-territory` |
| [[1-thinking-margin-of-safety]] | When provisioning, setting a limit, or committing an estimate under uncertainty,… | `skills/1-thinking-margin-of-safety` |
| [[1-thinking-model-combination]] | When one mental model leaves a material blind spot on a multi-domain or high-sta… | `skills/1-thinking-model-combination` |
| [[1-thinking-ooda]] | Use under time pressure when the situation is still changing and you must act be… | `skills/1-thinking-ooda` |
| [[1-thinking-opportunity-cost]] | Before committing scarce time, people, or money, name the best forgone use of th… | `skills/1-thinking-opportunity-cost` |
| [[1-thinking-pre-mortem]] | Before committing to a plan or launch, assume it already failed and reason backw… | `skills/1-thinking-pre-mortem` |
| [[1-thinking-probabilistic]] | Use when forecasting, estimating, or sizing risk — anchor on base rates, give ra… | `skills/1-thinking-probabilistic` |
| [[1-thinking-red-team]] | For authorized security review of code, auth, or APIs you control, model the att… | `skills/1-thinking-red-team` |
| [[1-thinking-reversibility]] | Before heavy deliberation, classify the decision as cheap or costly to undo; dec… | `skills/1-thinking-reversibility` |
| [[1-thinking-scientific-method]] | When a symptom has several plausible causes, rank falsifiable hypotheses and run… | `skills/1-thinking-scientific-method` |
| [[1-thinking-second-order]] | When a change has effects past the immediate fix—incentives, scale, feedback—tra… | `skills/1-thinking-second-order` |
| [[1-thinking-socratic]] | When a request is vague, assumption-laden, or "obvious," ask the few load-bearin… | `skills/1-thinking-socratic` |
| [[1-thinking-steel-manning]] | Use before rejecting a proposal or when you're inclined to just agree with the u… | `skills/1-thinking-steel-manning` |
| [[1-thinking-systems]] | When behavior is emergent across components—fixes elsewhere break, loops/delays … | `skills/1-thinking-systems` |
| [[1-thinking-theory-of-constraints]] | When throughput or latency is pipeline-limited, identify the single binding cons… | `skills/1-thinking-theory-of-constraints` |
| [[1-thinking-thought-experiment]] | When a real test is too rare, large, or irreversible, run a controlled counterfa… | `skills/1-thinking-thought-experiment` |
| [[1-thinking-triz]] | When two design requirements seem mutually exclusive, name the contradiction, se… | `skills/1-thinking-triz` |
| [[1-thinking-via-negativa]] | Use when the reflex is to add a feature, layer, or process. Prefer removing harm… | `skills/1-thinking-via-negativa` |

## Available skill additions

| [[1-to-questionnaire]] | Discovery questionnaire for an external knowledge holder. | `skills/1-to-questionnaire` |
| [[1-runtime-feature-map]] | Map user paths, preconditions and verification evidence. | `skills/1-runtime-feature-map` |
| [[1-i18n-sync]] | Synchronize selected JSON locale keys with context and validation. | `skills/1-i18n-sync` |
| [[1-migrate-to-shoehorn]] | Migrate scoped TypeScript test fixtures to Shoehorn. | `skills/1-migrate-to-shoehorn` |
| [[1-statechart-modeling]] | Model states, actions, guards and invariants clearly. | `skills/1-statechart-modeling` |
| [[1-change-impact]] | Trace affected consumers, compatibility, and verification obligations. | `skills/1-change-impact` |
| [[1-visual-explainer]] | Create one figure-led HTML explanation of a concept, system, or supplied comparison. | `skills/1-visual-explainer` |
| [[1-design-rationale]] | Explain recorded design decisions and their trade-offs. | `skills/1-design-rationale` |
| [[1-scaffold-exercises]] | Scaffold course exercise directories from an agreed plan. | `skills/1-scaffold-exercises` |
| [[1-design-review]] | Fresh-context EGM review of a pre-code software design/spec/plan; preserves the full workflow and development concepts. | `skills/1-design-review` |
| [[1-pr-walkthrough]] | Walk through a project PR with real UI components, non-UI before/after examples and useful engineering diagrams; local-only page. | `skills/1-pr-walkthrough` |
| [[1-pre-merge]] | Run frozen-candidate project readiness gates and return a final QA handoff without merging. | `skills/1-pre-merge` |
| [[1-dev-test]] | Run the project's risk-matched development testing loop before final pre-merge QA. | `skills/1-dev-test` |
| [[1-formal-verification]] | Evaluate a fixed formal check with explicit scope. | `skills/1-formal-verification` |
| [[1-pr-splitter]] | Split a source PR into smaller review units with extraction, verification, release-note, and drift tracking. | `skills/1-pr-splitter` |
| [[1-prompt-optimizer]] | Rewrite one prompt without executing it or inventing requirements. | `skills/1-prompt-optimizer` |
| [[1-llm-cost-design]] | Design one LLM spending policy with quality and budget controls. | `skills/1-llm-cost-design` |
| [[1-ai-suitability]] | Assess AI fit, non-AI alternatives and the level of automation. | `skills/1-ai-suitability` |
| [[1-context-retrieval-design]] | Design relevant, permission-aware context, retrieval and memory. | `skills/1-context-retrieval-design` |
| [[1-asd-ste100]] | Rewrite agent-facing English without changing conditions, uncertainty, or requirement strength. | `skills/1-asd-ste100` |
| [[1-manual-procedure-wizard]] | Author a human-run manual procedure wizard without executing it. | `skills/1-manual-procedure-wizard` |
| [[1-marketing-blog-editor]] | Review one technical marketing blog post before publication. | `skills/1-marketing-blog-editor` |
| [[1-marketing-ecommerce-blog-writing]] | Draft or revise one e-commerce guide, tutorial, lifestyle article, or product comparison. | `skills/1-marketing-ecommerce-blog-writing` |
| [[1-marketing-healthcare-blog-writing]] | Draft or revise one evidence-backed healthcare e-commerce blog and its medical/compliance review packet. | `skills/1-marketing-healthcare-blog-writing` |
