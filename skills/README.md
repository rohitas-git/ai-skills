# Live skills

Flat skill bodies: `skills/<name>/SKILL.md`.

- Index: [../wikis/index.md](../wikis/index.md)
- Hubs: [../hubs/](../hubs/)
- Rules: [../CLAUDE.md](../CLAUDE.md)

Do not re-nest by domain here. Domain grouping is logical (hubs + wiki).

## Vendor harvest (promoted)

- [agent-evaluation](./1-agent-evaluation/) — evaluation sets, graders, baselines, and release gates
- [api-and-interface-design](./1-api-and-interface-design/) — vendor harvest (lean); see skill description
- [error-handling](./1-error-handling/) — atomic failure contracts, TS/JS patterns, safe recovery, and verification
- [browser-testing-with-devtools](./1-browser-testing-with-devtools/) — vendor harvest (lean); see skill description
- [ci-cd-and-automation](./1-ci-cd-and-automation/) — vendor harvest (lean); see skill description
- [constraint-driven-development](./1-constraint-driven-development/) — measurable project quality contracts
- [deprecation-and-migration](./1-deprecation-and-migration/) — vendor harvest (lean); see skill description
- [doubt-driven-development](./1-doubt-driven-development/) — one read-only adversarial claim/decision pass
- [frontend-ui-engineering](./1-frontend-ui-engineering/) — vendor harvest (lean); see skill description
- [human-in-the-loop](./1-human-in-the-loop/) — approval gates and human oversight
- [mcp-server-building](./1-mcp-server-building/) — MCP server contracts and implementation
- [observability-and-instrumentation](./1-observability-and-instrumentation/) — vendor harvest (lean); see skill description
- [performance-optimization](./1-performance-optimization/) — vendor harvest (lean); see skill description
- [pdf](./1-pdf/) — safe PDF inspection, editing, creation, and verification
- [prompt-injection-defense](./2-prompt-injection-defense/) — agent trust-boundary defenses
- [skill-supply-chain-audit](./2-skill-supply-chain-audit/) — third-party skill/package provenance audits
- [shipping-and-launch](./1-shipping-and-launch/) — vendor harvest (lean); see skill description
- [tool-schema-design](./1-tool-schema-design/) — model-facing tool schemas

## Process hygiene

- [1-karpathy-guidelines](./1-karpathy-guidelines/) — LLM coding process: think, simple, surgical, goal-driven (Ship soft)
- [1-anti-sycophancy](./1-anti-sycophancy/) — independent claim assessment; praise-kill; evidence-first (Design soft)
- [1-critique](./1-critique/) — explicit rigorous critique / devil's advocate of ideas (Design soft)
- [1-action-first-output](./1-action-first-output/) — explicit, reversible session mode for action-first output and visible progress (Butler soft)

## Architecture tooling

- [1-graphify](./1-graphify/) — explicitly requested local codebase-graph build/query; no installation, hooks, or remote backend by default

## Source-backed reference skills

- [1-source-backed-skill](./1-source-backed-skill/) — private, progressive-disclosure reference skills from authorized source material

## Dependency security

- [2-dependency-security](./2-dependency-security/) — dependency vulnerability ratchets, staleness reports, and new-package reviews (Security)

## Domain 17 — Git (`/0-git`)

- [0-git](./0-git/) — Git workflow router
- [1-git-worktrees](./1-git-worktrees/) — isolated workspaces and concurrent local-service setup
- [1-atomic-git-commits](./1-atomic-git-commits/) — small, independently understandable and revertible commit groups
- [1-git-text-normalization](./1-git-text-normalization/) — diagnose or apply one authorized exact-path text correction
- [1-resolving-merge-conflicts](./1-resolving-merge-conflicts/) — merge/rebase conflict recovery
- [1-stacked-pr-review-and-repair](./1-stacked-pr-review-and-repair/) — converge an entire PR stack base-to-tip
- [1-stacked-pr-repair](./1-stacked-pr-repair/) — repair known findings and blockers across a PR stack without review
- [1-finish-branch](./1-finish-branch/) — merge, PR, retain, or cleanup choices
- [1-pr-summarizer](./1-pr-summarizer/) — soft Ship-primary PR prose
- [1-pr-repair](./1-pr-repair/) — repair known findings and blockers on one PR without review
- [1-pr-review-and-repair](./1-pr-review-and-repair/) — converge one PR through review, repair, rebase, and CI

## Domain 18 — Agent Engineering (`/0-agent-engineering`)

- [0-agent-engineering](./0-agent-engineering/) — agent-system router
- [1-agent-evaluation](./1-agent-evaluation/) — evaluations and release gates
- [1-tool-schema-design](./1-tool-schema-design/) — model-facing tool contracts
- [1-human-in-the-loop](./1-human-in-the-loop/) — approval and escalation design
- [1-mcp-server-building](./1-mcp-server-building/) — MCP server design and validation
- [2-prompt-injection-defense](./2-prompt-injection-defense/) — prompt-injection boundaries (security primary)
- [2-skill-supply-chain-audit](./2-skill-supply-chain-audit/) — package provenance and behavior (security primary)

## Domain 19 — DevOps (`/0-devops`)

- [0-devops](./0-devops/) — infrastructure and production-operations router
- [1-infrastructure-as-code](./1-infrastructure-as-code/) — Terraform, OpenTofu, CloudFormation, and Bicep
- [1-cloud-platform-operations](./1-cloud-platform-operations/) — AWS, Azure, GCP, and Cloudflare operations
- [1-container-platform-operations](./1-container-platform-operations/) — containers, registries, Kubernetes, Helm, and GitOps
- [1-database-and-storage-operations](./1-database-and-storage-operations/) — data services, durable storage, backups, and restores
- [1-network-and-edge-operations](./1-network-and-edge-operations/) — DNS, traffic, edge, firewall, VPN, and TLS
- [1-server-and-fleet-operations](./1-server-and-fleet-operations/) — hosts, services, SSH, and managed devices
- [1-platform-engineering](./1-platform-engineering/) — internal platforms, golden paths, and reproducible environments
- [1-ai-platform-operations](./1-ai-platform-operations/) — model serving, RAG, GPU, caching, and LLMOps
- [1-identity-and-secrets-management](./1-identity-and-secrets-management/) — IAM, SSO, access, KMS, Vault, and encrypted secrets
- [1-incident-response](./1-incident-response/) — active production incident coordination
- [1-resilience-and-disaster-recovery](./1-resilience-and-disaster-recovery/) — backups, failover, continuity, RTO, and RPO
- [1-compliance-engineering](./1-compliance-engineering/) — compliance controls, evidence, and verification
- Shared: [1-ci-cd-and-automation](./1-ci-cd-and-automation/), [1-observability-and-instrumentation](./1-observability-and-instrumentation/), [1-shipping-and-launch](./1-shipping-and-launch/)

## Domain 20 — Marketing (`/0-marketing`)

- [0-marketing](./0-marketing/) — marketing-domain router
- Foundation: [1-marketing-product-marketing](./1-marketing-product-marketing/), [1-marketing-marketing-plan](./1-marketing-marketing-plan/), [1-marketing-marketing-ideas](./1-marketing-marketing-ideas/), [1-marketing-marketing-council](./1-marketing-marketing-council/), [1-marketing-marketing-psychology](./1-marketing-marketing-psychology/), [1-marketing-offers](./1-marketing-offers/), [1-marketing-pricing](./1-marketing-pricing/)
- Research: [1-marketing-customer-research](./1-marketing-customer-research/), [1-marketing-competitor-profiling](./1-marketing-competitor-profiling/), [1-marketing-competitors](./1-marketing-competitors/)
- Conversion and lifecycle: [1-marketing-cro](./1-marketing-cro/), [1-marketing-signup](./1-marketing-signup/), [1-marketing-onboarding](./1-marketing-onboarding/), [1-marketing-popups](./1-marketing-popups/), [1-marketing-paywalls](./1-marketing-paywalls/), [1-marketing-churn-prevention](./1-marketing-churn-prevention/), [1-marketing-ab-testing](./1-marketing-ab-testing/)
- Content and messaging: [1-marketing-content-strategy](./1-marketing-content-strategy/), [1-marketing-copywriting](./1-marketing-copywriting/), [1-marketing-copy-editing](./1-marketing-copy-editing/), [1-marketing-emails](./1-marketing-emails/), [1-marketing-cold-email](./1-marketing-cold-email/), [1-marketing-sms](./1-marketing-sms/), [1-marketing-social](./1-marketing-social/), [1-marketing-video](./1-marketing-video/), [1-marketing-image](./1-marketing-image/), [1-marketing-lead-magnets](./1-marketing-lead-magnets/)
- Search: [1-marketing-seo-audit](./1-marketing-seo-audit/), [1-marketing-ai-seo](./1-marketing-ai-seo/), [1-marketing-programmatic-seo](./1-marketing-programmatic-seo/), [1-marketing-site-architecture](./1-marketing-site-architecture/), [1-marketing-schema](./1-marketing-schema/), [1-marketing-aso](./1-marketing-aso/), [1-marketing-directory-submissions](./1-marketing-directory-submissions/)
- Paid and measurement: [1-marketing-ads](./1-marketing-ads/), [1-marketing-ad-creative](./1-marketing-ad-creative/), [1-marketing-analytics](./1-marketing-analytics/), [1-marketing-attribution](./1-marketing-attribution/)
- Growth, partnerships, and sales: [1-marketing-co-marketing](./1-marketing-co-marketing/), [1-marketing-community-marketing](./1-marketing-community-marketing/), [1-marketing-events](./1-marketing-events/), [1-marketing-free-tools](./1-marketing-free-tools/), [1-marketing-influencer-marketing](./1-marketing-influencer-marketing/), [1-marketing-launch](./1-marketing-launch/), [1-marketing-marketing-loops](./1-marketing-marketing-loops/), [1-marketing-prospecting](./1-marketing-prospecting/), [1-marketing-public-relations](./1-marketing-public-relations/), [1-marketing-referrals](./1-marketing-referrals/), [1-marketing-revops](./1-marketing-revops/), [1-marketing-sales-enablement](./1-marketing-sales-enablement/)

## Superpowers harvest (promoted 2026-07-20)

- [1-brainstorm](./1-brainstorm/) — design gate before code (Design)
- [1-write-plan](./1-write-plan/) — implementation plan from design
- [1-execute-plan](./1-execute-plan/) — run plan in a separate session
- [1-subagent-implement](./1-subagent-implement/) — same-session subagent plan exec
- [1-parallel-agents](./1-parallel-agents/) — independent multi-domain agents
- [1-git-worktrees](./1-git-worktrees/) — isolated workspaces
- [1-finish-branch](./1-finish-branch/) — merge/PR/cleanup after green
- [1-receive-review](./1-receive-review/) — process incoming review feedback

## Domain 16 — Thinking (`/0-thinking`)

Structured mental models. The core is from `tjboudreaux/cc-thinking-skills` (MIT); selective leaves retain their own source attribution. Hub routes; leaves are soft frames.

| Skill | Role |
|-------|------|
| **0-thinking** | ★ Hub — model router / F-T1 · F-T2 |
| **1-thinking-scientific-method** | Hypothesis differential |
| **1-thinking-five-whys-plus** | Systemic root after localization |
| **1-thinking-kepner-tregoe** | IS/IS-NOT + must/want |
| **1-thinking-systems** | Flows, feedback, delays |
| **1-thinking-map-territory** | Docs vs live behavior |
| **1-thinking-cynefin** | Cause-effect domain |
| **1-thinking-socratic** | Hidden requirements via questions |
| **1-thinking-reversibility** | Cheap vs costly-to-undo decisions |
| **1-thinking-opportunity-cost** | Best forgone use of resources |
| **1-thinking-probabilistic** | Base rates, ranges, belief updates |
| **1-thinking-second-order** | Delayed effects, incentives |
| **1-thinking-steel-manning** | Strongest opposing case (dual · primary Design) |
| **1-thinking-bounded-rationality** | Good-enough stop |
| **1-thinking-circle-of-competence** | Evidence boundary |
| **1-thinking-lindy-effect** | Durability with domain-change check |
| **1-thinking-first-principles** | Physics vs convention |
| **1-thinking-lateral** | Escape stuck framings with safe provocations |
| **1-thinking-triz** | Design contradictions |
| **1-thinking-via-negativa** | Remove before add |
| **1-thinking-thought-experiment** | Controlled counterfactuals |
| **1-thinking-jobs-to-be-done** | Progress users hire product for |
| **1-thinking-effectuation** | Means under uncertainty |
| **1-thinking-pre-mortem** | Failure paths before commit |
| **1-thinking-red-team** | Authorized exploit-path review |
| **1-thinking-margin-of-safety** | Buffers under uncertainty |
| **1-thinking-theory-of-constraints** | Binding throughput constraint |
| **1-thinking-ooda** | Time-pressured act loop |
| **1-thinking-model-combination** | Sequence distinct models |
| **1-perspective-analysis** | Separate stakeholder or persona viewpoints |
| **1-thinking-ethical** | Values, harms, power, and safeguards |
| **1-strategic-analysis** | Strategic position, market forces, and plausible futures |
| **1-competitive-analysis** | Evidence-marked named-competitor comparison |

## Fernandobandeira agents harvest (promoted 2026-09-09)

- [1-honest-advisor](./1-honest-advisor/) — interpersonal conflict and personal-decision accuracy check (Design)
- [1-go-best-practices](./1-go-best-practices/) — Go-specific implementation and review practice (Architecture)
- [1-perspective-analysis](./1-perspective-analysis/) — stakeholder/persona analysis (Thinking)
- [1-strategic-analysis](./1-strategic-analysis/) — strategic choices and scenarios (Thinking)
- [1-competitive-analysis](./1-competitive-analysis/) — competitor matrix and positioning (Thinking)
- [1-user-research](./1-user-research/) — research planning and synthesis (UI/UX)
- [1-customer-experience-audit](./1-customer-experience-audit/) — one evidence-marked external-customer audit (UI/UX)

## Available skill additions

- [1-design-review](./1-design-review/) — Elephant-Goldfish pre-code design/spec/plan review; [workflow, connections and concepts](./1-design-review/references/workflow-and-connections.md)
- [1-pr-splitter](./1-pr-splitter/) — split a source PR into coherent smaller PRs and track review drift
- [1-ai-suitability](./1-ai-suitability/) — Assess AI fit, non-AI alternatives and the level of automation.
- [1-context-retrieval-design](./1-context-retrieval-design/) — Design relevant, permission-aware context, retrieval and memory.
- Content and messaging: [1-marketing-content-strategy](./1-marketing-content-strategy/), [1-marketing-copywriting](./1-marketing-copywriting/), [1-marketing-copy-editing](./1-marketing-copy-editing/), [1-marketing-blog-editor](./1-marketing-blog-editor/), [1-marketing-emails](./1-marketing-emails/), [1-marketing-cold-email](./1-marketing-cold-email/), [1-marketing-sms](./1-marketing-sms/), [1-marketing-social](./1-marketing-social/), [1-marketing-video](./1-marketing-video/), [1-marketing-image](./1-marketing-image/), [1-marketing-lead-magnets](./1-marketing-lead-magnets/)
- [1-manual-procedure-wizard](./1-manual-procedure-wizard/) — Author a human-run manual procedure wizard without executing it
- [1-migrate-to-shoehorn](./1-migrate-to-shoehorn/) — Migrate scoped TypeScript test fixtures to Shoehorn
- [1-i18n-sync](./1-i18n-sync/) — Synchronize selected JSON locale keys with context and validation.
- [1-prompt-optimizer](./1-prompt-optimizer/) — Rewrite one prompt without executing it or inventing requirements.
- [1-llm-cost-design](./1-llm-cost-design/) — Design one LLM spending policy with quality and budget controls.
- [1-change-impact](./1-change-impact/) — Trace affected consumers, compatibility, and verification obligations.
- [1-design-rationale](./1-design-rationale/) — Explain recorded design decisions and their trade-offs.
