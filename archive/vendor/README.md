# Vendor

Third-party skill packs kept **out of default discovery**.

## Policy

- **Promote only via butler ingest** — never co-load a whole pack as peer skills, and never promote `using-agent-skills` (dual meta-router).
- Packs here are offline from symlink sync unless explicitly listed in `scripts/symlink-targets.json` `nestedSkillRoots` (default: empty).
- Prefer merging useful content into an existing catalog winner over promoting a near-duplicate.

## Packs

| Pack | Path | Status |
|------|------|--------|
| agent-skills (Addy Osmani et al.) | [agent-skills/](./agent-skills/) | Parked `6ca0cd7` (MIT). Selective promotes only via skill-manager ingest. TDD ideas merge into catalog `1-tdd`, not a second skill. |
| agent-skills selected refresh | [addyosmani-agent-skills-2026-11-15/](./addyosmani-agent-skills-2026-11-15/) | `39b723c` (MIT): five reference merges; all 25 source skills accounted for. [Review and dispositions](../../guidelines/catalog/ingest-addyosmani-2026-11-15.md). Helper archived as text only; original snapshot preserved. |
| ui-ux-pro-max-skill | [ui-ux-pro-max-skill/](./ui-ux-pro-max-skill/) | Parked. Selective promote into Domain 15 `/0-ui-ux` (see harvest table). CLI/`src`/`stack` stay archive-only. |
| superpowers (obra/Jesse Vincent) | [superpowers/](./superpowers/) | Parked v6.1.1. Selective promote + merges 2026-07-20. **Never** promote `using-superpowers` (dual meta-router). |
| bro-skill (luchasarie) | [bro-skill/](./bro-skill/) | Parked `01e51f8`. Promoted live `/1-bro` (0-butler session meta). Do not promote `install.sh`. |
| impeccable (pbakaus) | [impeccable/](./impeccable/) | Parked plugin-skill snapshot `fcc271c1` (Apache-2.0). Thin live `/1-impeccable` wrapper only; do not promote its broad UI router as a peer. |
| builderio-skills (BuilderIO) | [builderio-skills/](./builderio-skills/) | Parked `8cd5958` (MIT). Eight thin live skills; five overlaps merged into catalog winners. |
| awesome-ai-agent-skills (seb1n) | [awesome-ai-agent-skills/](./awesome-ai-agent-skills/) | Parked `75865a5` (MIT). Seven selective promotions, five merges, 91 broad-domain candidates remain archive-only. |
| DevOps-Security-Agent-Skills (BagelHole) | [devops-security-agent-skills/](./devops-security-agent-skills/) | Parked `0365f57` (MIT). Distilled into `/0-devops`; raw scripts and remote-installer examples remain archive-only. |
| awesome-copilot selections (GitHub) | [awesome-copilot/](./awesome-copilot/) | Parked `7568a48` (MIT). DevOps guidance merged; anti-ui-slop harvested without concealed-evidence behavior. |
| fernandobandeira/agents | [fernandobandeira-agents/](./fernandobandeira-agents/) | Parked `42be774` (no upstream license file). Six focused workflows promoted; five overlaps and one research subagent merged; OpenCode runtime personas remain archive-only. |
| ysskrishna/ai-agent-skills | [ysskrishna-ai-agent-skills/](./ysskrishna-ai-agent-skills/) | Parked `e213af5` (MIT). Two thinking leaves promoted, Six Thinking Hats merged into perspective analysis, and seven overlaps retained archive-only. |
| ayghri/i-have-adhd | [i-have-adhd/](./i-have-adhd/) | Parked `6f1f982` (MIT). One explicit, reversible action-first session-output mode promoted; plugins, hooks, installers, and medical framing remain archive-only. |
| Graphify-Labs/graphify | [graphify/](./graphify/) | Parked `23f2ffaa` (Apache-2.0 + MIT). Thin live `/1-graphify` wrapper only; installer, hooks, strict mode, backends, and persistent behavior remain archive-only. |
| Baneeishaque/ai-agent-rules | [ai-agent-rules/](./ai-agent-rules/) | Parked `e81343c` (MIT). Selective planning, helper-reuse, narrow-ignore, Git text-normalization, and rebase safeguards adapted; forced cleanup, host settings, and unapproved history/remote edits remain archive-only. |

## Harvest status (ingest into live winners)

**Forbidden peer:** `using-agent-skills` (dual meta-router) — never promote.

| Vendor skill / pack ref | Live winner | Where depth lives |
|-------------------------|-------------|-------------------|
| shipping-and-launch | `shipping-and-launch` | `references/full-guide.md` + versioning-changelog |
| observability-and-instrumentation | `observability-and-instrumentation` | `full-guide.md` + observability-checklist |
| performance-optimization | `performance-optimization` | `full-guide.md` + performance-checklist |
| api-and-interface-design | `api-and-interface-design` | `full-guide.md` |
| frontend-ui-engineering | `frontend-ui-engineering` | `full-guide.md` + accessibility-checklist |
| ci-cd-and-automation | `ci-cd-and-automation` | `full-guide.md` |
| browser-testing-with-devtools | `browser-testing-with-devtools` | `full-guide.md` |
| deprecation-and-migration | `deprecation-and-migration` | `full-guide.md` |
| doubt-driven-development | `doubt-driven-development` | `full-guide.md` |
| security-and-hardening | `security-and-hardening` | existing refs + security-checklist-vendor-pack |
| debugging-and-error-recovery | `diagnosing-bugs` | vendor-debugging-full + extras |
| code-review-and-quality | `code-review` | vendor-code-review-full + axes |
| code-simplification | `ponytail-review` | vendor-simplification-full |
| incremental-implementation | `implement` | vendor-incremental-full + slices |
| test-driven-development | `tdd` | vendor-tdd-full + testing-patterns-vendor |
| source-driven-development | `research` | source-driven-full |
| planning-and-task-breakdown | `to-tickets` (+ implement DoD) | vendor-planning-full + sizing-checkpoints |
| spec-driven-development | `to-spec` | vendor-spec-full |
| interview-me | `grilling` | interview-intent |
| idea-refine | `grilling` | vendor-idea-refine-full + frameworks/criteria/examples |
| context-engineering | `strategic-compact` (+ implement) | vendor-context-full + hierarchy |
| documentation-and-adrs | `living-documentation-governor` (+ domain-modeling) | vendor-docs-adrs-full + readme skeleton |
| git-workflow-and-versioning | `1-atomic-git-commits` (+ shipping) | vendor-git-workflow-full + workflow-discipline |
| constraint-driven-development | `1-constraint-driven-development` | thin live router + full body/reference |
| references/definition-of-done | `implement` | definition-of-done + vendor full |
| references/orchestration-patterns | `implement` | orchestration-patterns.md |
| references/*-checklist (obs/perf/a11y/sec/test) | matching winners above | copied |

### ui-ux-pro-max-skill pack (Domain 15)

| Vendor skill | Live winner | Hub |
|--------------|-------------|-----|
| ui-ux-pro-max | `1-ui-ux-pro-max` | `/0-ui-ux` pipeline |
| design | `1-design` | `/0-ui-ux` leaf |
| brand | `1-brand` | `/0-ui-ux` leaf |
| design-system | `1-design-system` | `/0-ui-ux` leaf |
| ui-styling | `1-ui-styling` | `/0-ui-ux` leaf |
| banner-design | `1-banner-design` | `/0-ui-ux` leaf |
| slides | `1-slides` | `/0-ui-ux` leaf (HTML decks; not `/1-pptx`) |
| *(dual)* | `1-frontend-ui-engineering` | Ship primary + soft dual UI/UX |

Do **not** peer-promote near-duplicates of grill / to-spec / to-tickets / tdd / code-review.

### BuilderIO skills

| Upstream skill | Disposition | Live winner / name |
|----------------|-------------|--------------------|
| agent-watchdog | **Merge** | `2-verify-work` |
| efficient-fable | **Merge** | `1-parallel-agents` |
| efficient-frontier | **Merge** | `1-parallel-agents` |
| read-the-damn-docs | **Merge** | `1-research` |
| stay-within-limits | **Merge** | `1-context-monitor` |
| plan-arbiter | **Promote** | `1-plan-arbiter` |
| plow-ahead | **Promote** | `1-plow-ahead` |
| quick-recap | **Promote** | `1-quick-recap` |
| rewind | **Promote** | `1-rewind` |
| visual-edit | **Promote** | `1-visual-edit` |
| visual-plan | **Promote** | `1-visual-plan` |
| visual-recap | **Promote** | `1-visual-recap` |
| webmcp | **Promote** | `1-webmcp` |

Upstream: https://github.com/BuilderIO/skills @ `8cd59582774e0badf23796a6fc86c26c7117988e` (MIT).

### awesome-ai-agent-skills

| Upstream skill | Disposition | Live winner / name |
|----------------|-------------|--------------------|
| agent-evaluation | **Promote** | `1-agent-evaluation` |
| tool-schema-design | **Promote** | `1-tool-schema-design` |
| human-in-the-loop | **Promote** | `1-human-in-the-loop` |
| mcp-server-building | **Promote** | `1-mcp-server-building` |
| prompt-injection-defense | **Promote** | `2-prompt-injection-defense` |
| skill-supply-chain-audit | **Promote** | `2-skill-supply-chain-audit` |
| pdf-processing | **Promote** | `1-pdf` |
| agent-observability | **Merge** | `1-observability-and-instrumentation` |
| multi-agent-orchestration | **Merge** | `1-parallel-agents` |
| agent-red-teaming | **Merge** | `1-thinking-red-team` |
| spreadsheet-analysis | **Merge** | `1-xlsx` |
| presentation-creation | **Merge** | `1-pptx` + `1-slides` |
| remaining 91 skills | **Park** | archive-only pending deliberate domain-hub expansion |

Upstream: https://github.com/seb1n/awesome-ai-agent-skills @ `75865a5d037a4cdaa7f409a4ec14ab9b0292920b` (MIT).

### DevOps-Security-Agent-Skills

The 163 upstream skills remain non-discoverable reference material. They are distilled into `/0-devops`, twelve focused operational children, and existing CI/CD, observability, shipping, agent, and security winners. Raw scripts and remote-installer examples are never promoted as trusted actions.

Upstream: https://github.com/BagelHole/DevOps-Security-Agent-Skills @ `0365f57a079b1332f95cf26e31dd2d5332a8399f` (MIT). See `devops-security-agent-skills/VENDOR-SOURCE.md`.

### GitHub awesome-copilot selections

| Upstream skill | Disposition | Live winner |
|----------------|-------------|-------------|
| gem-devops-guidelines | **Merge** | `/0-devops`, `1-ci-cd-and-automation`, `1-observability-and-instrumentation`, `1-shipping-and-launch` |
| anti-ui-slop | **Merge safely** | `1-frontend-ui-engineering` |

The anti-ui-slop instruction to conceal missing or rejected evidence is excluded. Upstream: https://github.com/github/awesome-copilot @ `7568a482ce2df38f8965ab5336a3220db796a4ba` (MIT). See `awesome-copilot/VENDOR-SOURCE.md`.

### superpowers pack (obra · v6.1.1)

| Upstream skill | Disposition | Live winner / name |
|----------------|-------------|-------------------|
| using-superpowers | **Refuse** (meta-router) | archive only |
| test-driven-development | **Merge** | `1-tdd` → `references/superpowers-tdd-full.md` |
| systematic-debugging | **Merge** | `0-diagnosing-bugs` → `references/superpowers-debugging-full.md` |
| requesting-code-review | **Merge** | `1-code-review` → `references/superpowers-request-review.md` |
| verification-before-completion | **Merge** | `2-verify-work` → `references/superpowers-evidence-gate.md` |
| writing-skills | **Merge** | `1-writing-great-skills` → `references/superpowers-writing-skills-full.md` |
| brainstorming | **Promote** | `1-brainstorm` (Design on-ramp) |
| writing-plans | **Promote** | `1-write-plan` |
| executing-plans | **Promote** | `1-execute-plan` |
| subagent-driven-development | **Promote** | `1-subagent-implement` |
| dispatching-parallel-agents | **Promote** | `1-parallel-agents` |
| using-git-worktrees | **Promote** | `1-git-worktrees` |
| finishing-a-development-branch | **Promote** | `1-finish-branch` |
| receiving-code-review | **Promote** | `1-receive-review` |

See also pack `VENDOR-SOURCE.md`.

## bro-skill (parked 2026-08-22)

- Upstream: https://github.com/luchasarie/bro-skill @ `01e51f8`
- License: MIT
- Snapshot: `archive/vendor/bro-skill/`
- Live: `/1-bro` session meta under `/0-butler`; examples in `skills/1-bro/references/`

## cc-thinking-skills (parked 2026-08-08)

- Upstream: https://github.com/tjboudreaux/cc-thinking-skills @ `7b8fece`
- License: MIT
- Snapshot: `archive/vendor/cc-thinking-skills/`
- Live: Domain 16 `/0-thinking` — 26 leaves as `1-thinking-*`; router folded into hub; `thinking-steel-manning` merged into existing `1-thinking-steel-manning` (primary Design, dual soft Thinking)

## fernandobandeira/agents (parked 2026-09-09)

- Upstream: https://github.com/fernandobandeira/agents @ `42be7749df8bf4043c1314b02199278cbcf44194`
- License: no license file found; snapshot retained for provenance only.
- Live: `/1-honest-advisor`, `/1-go-best-practices`, `/1-perspective-analysis`, `/1-strategic-analysis`, `/1-competitive-analysis`, `/1-user-research`.
- Merged: devil's advocate → `/1-critique`; ideation → `/1-brainstorm`; React practice → `/1-frontend-ui-engineering`; teacher → `/1-learning-explainer`; knowledge-harvester → `/1-research`. Root-cause content was already more rigorously covered by the existing five-whys, first-principles, and JTBD leaves.
- Archive-only: seven primary OpenCode personas and their host-specific Basic Memory, Beads, Tab, and crawl4ai instructions.

## ysskrishna/ai-agent-skills (parked 2026-09-10)

- Upstream: https://github.com/ysskrishna/ai-agent-skills @ `e213af5f6574ea982a64af85b5b1347a816c5bf8` (MIT).
- Live: `/1-thinking-lateral`, `/1-thinking-ethical` under `/0-thinking`.
- Merge: `six-thinking-hats` → `/1-perspective-analysis`.
- Archive-only: analytical, creative, critical, design, first-principles, strategic, and systems thinking; live catalog winners already cover those jobs.

## ECC selected ingestion (2026-11-15)

- [Selected MIT snapshot](./ecc-2026-11-15/) at `d2ef268`: 314 inventory entries, four new skills, two merges, one supporting source. [Assessment and validation](../../guidelines/catalog/ingest-ecc-2026-11-15.md). No hooks, adapters, installers, or executable source adopted.

## pstack selected ingestion (2026-11-15)

- [Selected MIT source](./pstack-2026-11-15/) at `bf0c7cd`, version `0.15.42`: four skills, two merges and three optional verification workflows. [Inventory, dispositions and review](../../guidelines/catalog/ingest-pstack-2026-11-15.md). No plugin, toolchain, renderer, bots or background automation installed.
