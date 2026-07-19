# codebase-review-strategy — full guide

> Progressive disclosure body moved from SKILL.md for Matt-lean main file.

# Codebase Review Strategy

## Overview

This skill provides a systematic, size-aware framework for planning and executing high-quality AI agent reviews of codebases ranging from tiny scripts to large monorepos. It matches analysis depth to repo scale, review goals, model constraints and cost, preventing both superficial results on complex systems and wasted effort on simple ones.

## When to Activate

Load this skill automatically or explicitly for any task involving "review the codebase", "analyze the full repo", "code quality assessment", "refactoring recommendations", "security review of the project", or similar. It is especially valuable before starting deep work on unfamiliar or large repositories.

## Interactive Clarification Mode (Mandatory First Step — Do Not Skip)

When this skill is loaded for a **new review session**, **do not immediately begin measuring the repository, running commands, or reading any code files**.

Instead, enter **Interactive Clarification Mode** (see full details in `references/interactive-clarification.md`). This is the most important step for delivering a high-quality, efficient, and personalized review.

**Core Rule**: Ask the user a short series of multiple-choice questions to determine Goal, Scope, Depth, Priorities, Constraints, and Output Style. Present questions one at a time or in small batches. After answers, summarize the **Confirmed Review Parameters** clearly and obtain explicit confirmation before proceeding to Phase 0.

The agent must never assume details or start exploration until the user confirms the parameters. All subsequent workflow decisions (effort level, early-exit rules, Systemic Awareness intensity, token-saving techniques, and risk mitigations) are driven by these confirmed parameters.

## Core Principles

- Size is a proxy for cognitive load and interdependency density — not just raw volume.
- Effort must be calibrated: exhaustive review is rarely optimal.
- **Always start with Interactive Clarification Mode** (multiple-choice questions) before any measurement or code reading. Never assume or expect the user to provide detailed Goal/Scope/Depth upfront.
- Use phased, tool-augmented analysis rather than single monolithic prompts.
- Prioritize evidence (specific files, lines, patterns) and actionable, prioritized recommendations.
- Account for practical limits: context window, token budget, available tools (grep, read_file, git, static analyzers), and time.

## 1. Measure Repository Size & Characteristics

**Only perform this step after completing Interactive Clarification Mode and receiving user confirmation on the parameters.**

First action in any review: Gather objective metrics using available tools.

**Recommended Commands (run via bash or equivalent):**

- Basic file count: `find . -type f \( -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.java" -o -name "*.go" -o -name "*.rs" -o -name "*.cpp" -o -name "*.c" -o -name "*.rb" -o -name "*.php" \) | wc -l`
- Approximate source LOC (rough, language-agnostic): `find . -type f \( ... same extensions ... \) -exec wc -l {} + | tail -1`
- Better: Install/use `cloc` if possible (`cloc --quiet .` or per language). Fallback to per-extension wc.
- Tracked files: `git ls-files | wc -l`
- Directory structure insight: `tree -L 3 --dirsfirst -I 'node_modules|__pycache__|venv|target|dist|build' | head -100`
- Key indicators:
  - Tests: `find . -path '*/test*' -o -path '*/tests*' -o -name '*_test.*' | wc -l`
  - Package managers: Check for package.json, requirements.txt, Cargo.toml, go.mod, pom.xml, etc.
  - Monorepo signals: presence of lerna.json, nx.json, pnpm-workspace.yaml, or many top-level packages/.

**Record:**
- Approx source LOC
- Source file count
- Main languages & frameworks
- Presence/quality of tests, documentation, CI config
- Architectural style hints (monolith, services, layered, etc.)
- Recent activity (git log --oneline -20)

## 2. Classify Repository Tier

Use the metrics above to assign a tier. Adjust upward if high coupling, legacy code, many languages, or critical domain.

| Tier       | Source LOC     | Source Files | Typical Structure                  | LLM Review Feasibility          | Default Effort |
|------------|----------------|--------------|------------------------------------|---------------------------------|----------------|
| **Tiny**   | < 1,500       | < 25        | Single file or flat 1-2 modules   | Excellent — full context easy  | Medium        |
| **Small**  | 1,500 – 8,000 | 25 – 80     | Few modules, low nesting          | Very good — most files readable| Medium-High   |
| **Medium** | 8,000 – 40,000| 80 – 400    | Multiple modules, clear boundaries| Good with structure & sampling | Medium        |
| **Large**  | > 40,000      | > 400       | Deep nesting, many packages/services | Requires heavy prioritization & sampling | Low-Medium (phased) |

**Special Cases:**
- Monorepo or workspace: Treat as "Large" or review by logical package/sub-repo after high-level map.
- Heavily generated / vendor code: Exclude or down-weight in sizing.
- Legacy / high technical debt: Bump tier up one level (increases effective complexity).

## 3. Clarify Review Goal, Scope & Constraints

From the user request or by asking, determine:

**Primary Goal(s)** (examples):
- Quick health/overview (surface)
- Detailed maintainability & code quality
- Security, compliance or vulnerability focus
- Performance, scalability or resource analysis
- Refactoring / modernization readiness
- Onboarding / knowledge extraction
- Comprehensive (all of the above — rare for large repos)

**Review Scope** (critical for token optimization — always clarify or infer):
- **Surface / High-Level Only**: Architecture overview, top-level structure, directory map, obvious strengths/red flags, and high-level patterns via grep. Minimal or no deep file reads. Ideal for quick triage, initial assessment, or when token budget is tight.
- **Specific Module(s) / Path / Subtree**: Restrict analysis almost exclusively to the named directory or files (e.g., `src/auth/`, `packages/core/payment/`, `lib/utils.py`). Perform deep analysis *only* inside the scope. Reference global architecture lightly for context. This dramatically reduces tokens and keeps focus sharp.
- **Full Repo**: Standard complete phased review (default when user says "review the complete codebase").

**Constraints**:
- Available context window / token budget (surface or specific-module scopes are strongly preferred when tokens are limited)
- Time sensitivity
- Whether full tool access (filesystem, git, execution) is available
- Output format expectations (report, actionable tasks, PR suggestions)

## 4. Select Thinking Effort Level

Thinking effort is multi-dimensional:

- **Depth**: Surface observations vs. root-cause + implications + alternatives.
- **Breadth/Scope**: Exhaustive vs. risk-prioritized sampling.
- **Iteration & Critique**: Single pass vs. self-review + refinement loops.
- **Cross-referencing**: Isolated files vs. tracing data/control flows across modules.
- **Synthesis**: List of issues vs. prioritized roadmap with effort/impact estimates.

**Mapping (Tier × Goal × Scope → Effort):**

- **Any tier + Surface scope** (regardless of goal): **Low effort**. Phase 0 + Phase 1 only + light synthesis. Heavy use of tree/grep summaries. Stop early.
- **Tiny/Small + Specific Module or Full + any goal**: Medium to High. Feasible to go deeper within the (small) scope.
- **Medium + Specific Module**: Medium effort focused inside the module. Light global context only if needed for integration points.
- **Medium + Full + Quick health**: Low-Medium. High-level map + top issues via sampling/grep.
- **Medium + Full + Detailed/Security/Refactor**: Medium-High. Structured passes + deep dives on core paths *within prioritized modules*.
- **Large + Specific Module**: Medium effort (deep inside module) + minimal global map. One of the most token-efficient deep reviews possible.
- **Large + Full + Quick/Surface**: Low. High-level map + hotspot identification via git/grep. No deep dives.
- **Large + Full + Detailed/Security**: Medium. Heavy sampling + targeted high-effort deep dives on only 3–6 critical areas. Strongly prefer "specific module" follow-ups for deeper work.
- **Any + Comprehensive**: Start at appropriate level for scope, escalate only on explicit request. Plan multi-turn with cached summaries.

**High Effort Characteristics (use when justified):**
- Multiple explicit reasoning passes (map → analyze → critique → synthesize).
- What-if simulations ("If we change X, what breaks?").
- Explicit consideration of edge cases, failure modes, future evolution.
- Detailed evidence quotes + line references.
- Prioritized recommendations with rationale, alternatives, and rough effort estimates.

## 5. Execute the Phased Review Workflow (Scope-Adaptive for Token Efficiency)

**Always start with Phase 0 + Phase 1** (high-level only). Then adapt or early-exit based on **Scope**:

**Phase 0: Preparation (mandatory, low token)**
- Run sizing commands and classify tier.
- Explore top-level directory structure (`tree -L 2` or limited) and key files (README, package manifests, main entrypoints).
- Identify high-level domains/modules and data flows.
- **For Specific Module scope**: Immediately `cd` into or limit all commands to the target path (e.g., `find src/auth/ ...`, `grep -r ... src/auth/`).

**Phase 1: Architecture & High-Level Map + Systemic Awareness (all tiers & scopes — keep very compact)**
- Tech stack, frameworks, build/test/CI setup (from manifests + top files).
- Overall (or module-internal) structure and responsibilities.
- Main entry points and high-level flows.
- Obvious strengths and red flags via grep (TODO, FIXME, unsafe patterns, large files).
- **Systemic Awareness (mandatory even for Surface/Specific scopes — key risk mitigator)**: 
  - Identify and note shared utilities, common dependencies, or modules imported/called by the in-scope code.
  - Quick grep for global patterns (e.g., auth, logging, error handling, config) and any inconsistencies visible at high level.
  - For Specific-Module scope: Identify key integration points and potential ripple effects outside the module.
  - Flag any high-coupling signals (many cross-imports, large shared files, recent changes to shared code via git).
- **Token optimization**: Produce a short "Repo/Map Summary" (or "Module Summary") including a "Systemic Notes" subsection — 150-400 tokens max. Cache this summary (with systemic notes) in context/memory for the rest of the session. Reference it instead of re-exploring. Update the systemic notes as deeper analysis reveals more.

**Early Exit Rules (major token saver):**
- **Surface / High-Level Only scope** → Stop after Phase 1 + light Phase 4. Do **not** enter Phase 2 or 3 unless user explicitly requests deeper analysis on a finding.
- **Specific Module scope** → Focus Phase 2/3 *exclusively* inside the module subtree. Use path-limited tools. Only pull in 1-2 global files if integration points are critical (and justify why).
- **Full Repo + Surface goal** → Same as Surface scope.

**Phase 2: Targeted Deep Analysis (only if scope allows and goal justifies — skip for Surface)**
- **Specific Module**: Deep dive inside the module (read key files after grep filtering). Trace internal flows.
- **Full Repo (non-surface)**: Prioritize 3–8 highest-value modules/areas only. Use git history, complexity signals, and grep to select. Sample secondary areas lightly.
- Techniques (always grep-first): Pattern matching before any full read. Hierarchical summarization of large files ("Summarize this 800-line file in 5 bullets focusing on X").
- **Memory caching**: Update the cached "Repo/Map Summary" incrementally with new findings instead of repeating context.

**Phase 3: Cross-Cutting & Specialized Lenses (goal-dependent, scope-limited)**
- Apply lenses *only within current scope*.
- For Surface: Skip or do very lightly via global grep (e.g., "grep for secret patterns across repo").
- For Specific Module: Deep on relevant lenses inside module; note cross-module implications at high level only.
- Maintainability, Security, Performance, etc. — same categories but bounded.

**Phase 4: Synthesis & Recommendations (always produce, but scale detail)**
- Consolidate findings (Critical/High/Medium/Low).
- Prioritize by impact × effort.
- Concrete examples with evidence (for Surface: mostly directory/grep evidence + 1-2 snippets; for deep: more quotes).
- Note positives.
- High-level next steps + explicit offers for deeper follow-up on specific areas.
- Self-critique (lighter for Surface).

**Phase 5: Output & Iteration**
- Structured report (see Section 8, but trim for Surface).
- Strongly encourage iteration: "For deeper analysis on any finding or module, reply with 'Deep dive on X using high effort' — this will use additional targeted tokens efficiently."
- Maintain and reference the cached summary across turns to avoid re-work.

## 6. Prompt Templates & Agent Instructions

Use these as base. Adapt language to the specific model/agent.

**Base Prompt Structure (Interactive Clarification First):**

"You are an expert senior software engineer performing a codebase review.

**Critical first step — Interactive Clarification Mode (do this before any code exploration or measurement):**
Follow the exact Interactive Clarification Mode described in the codebase-review-strategy skill. Ask the standard multiple-choice questions (Q1–Q5) one by one or in small batches. Wait for user answers. Then summarize the confirmed parameters in a clear table and ask for final confirmation before proceeding.

Only after user confirmation on Goal, Scope, Depth, Priorities, and Constraints:
- Proceed to measurement and the phased workflow.
- Use the clarified parameters to select the exact effort level, early-exit rules, Systemic Awareness intensity, and risk mitigations.
- Strictly respect the chosen Scope (never explore outside it unless the user later expands it).
- Apply all token-saving, memory-caching, and risk-mitigation rules from the skill.

You are now in clarification mode. Start by greeting the user and asking Q1."

**Tier-Specific Variations (scope-aware + risk-mitigating):**

- **Small/Tiny + Surface or Specific Module**: High completeness *within scope* while still performing the mandatory lightweight Systemic Awareness scan. Keep summaries compact but include Systemic Notes.
- **Medium + Specific Module**: Focused two-pass inside the module only, plus light global context specifically for integration points, shared utilities, and cross-module patterns. Document any coupling signals.
- **Large + Surface or Specific Module**: Extremely efficient. Global high-level map (with strong Systemic Awareness) + deep work bounded to scope. Aggressive grep + summarization. Explicitly call out blind spots and over-confidence risks in output.
- **Large + Full + non-Surface**: Strong prioritization + sampling. Perform high-effort deep review on only a handful of areas. Prefer converting deeper or systemic-risk work to "Specific Module" or targeted follow-ups. Always include full Scope Limitations section.

**Goal-Specific Lenses** (add to prompt):
- Security: "Apply STRIDE or OWASP mindset. Explicitly look for [list common issues relevant to stack]."
- Refactoring: "Focus on SOLID violations, code smells (from Martin Fowler / Clean Code), technical debt hotspots, and opportunities for simplification or better abstraction."

## 7. Best Practices, Nuances & Edge Cases

**Tool Maximization:**
- Use grep extensively for patterns before full file reads.
- Leverage git blame, git log, git diff for change context and ownership.
- If static analysis tools (eslint, pylint, sonar, semgrep) are present or installable, run them and incorporate results.
- For very large repos, consider generating a high-level summary first, then drill-down sessions.

**Token & Memory Optimization Rules (core to this skill — apply aggressively):**
- **Grep-first, read-second policy**: Use `grep`, `find`, `tree`, and `git` extensively *before* ever calling read_file on a source file. Only read a file if grep output indicates it is highly relevant to the current scope/goal.
- **Scope bounding**: For Specific Module reviews, prefix all exploration commands with the target path. Never explore outside the declared scope unless explicitly justified.
- **Hierarchical & incremental summarization**: After any exploration, immediately produce a compact summary (bullets or short paragraphs). Cache this "working memory map" in the conversation context and update it in-place across turns instead of re-generating.
- **Early stopping for Surface/Specific scopes**: Do not perform deep cross-referencing, what-if simulations, or multi-file tracing unless the goal explicitly requires it or a critical finding demands it.
- **Evidence scaling**: Surface reviews → directory structure + grep hits + at most 2-3 short snippets. Deep reviews → more detailed quotes + line refs.
- **Limit file reads**: In any single pass, read at most N key files fully (N=3-8 depending on tier/scope). Summarize the rest.
- **Memory caching strategy**: Maintain a persistent compact "Repo Summary" or "Module Summary" object in context (e.g., key modules, responsibilities, known hotspots, integration points). Reference and update it rather than re-reading source.
- For very large contexts: Ask the model to output a "compressed context update" at the end of each phase that can be carried forward.

**Common Pitfalls to Instruct Against:**
- Over-generalizing from a few files.
- Missing distributed concerns (e.g., assuming local state in a microservice).
- Ignoring tests or treating them as secondary.
- Suggesting changes without considering breaking impact or migration cost.
- Hallucinating file contents or structure.

**Edge Cases:**
- Mostly generated code or low human-written LOC: Focus on generator config, custom logic, and maintenance of generated parts.
- No tests / poor test coverage: Increase emphasis on testability recommendations and manual reasoning about correctness.
- Legacy or "works but don't touch" code: Balance improvement suggestions with risk assessment.
- Mixed languages or polyglot services: Analyze per-language strengths and integration points.
- Rapidly evolving repo: Weight recent changes more heavily.
- Very small but critical (e.g., security library): Treat as higher tier.

**Iteration & Validation:**
- After initial report, invite user to request deeper analysis on specific areas.
- In multi-turn: Maintain a running map of the codebase and update it.
- Self-check: "Does every claim have traceable evidence? Have I considered the opposite perspective?"

**Trade-offs of Surface / Specific-Module / Abbreviated Reviews (for awareness):**
**Benefits (why we optimize this way):**
- Dramatic token and cost savings (often 5–20× reduction on large repos).
- Faster turnaround and ability to do more iterations or follow-ups within the same context window.
- Sharper focus and less noise — especially valuable when user has a clear narrow goal.
- Better "memory" efficiency: cached summaries stay relevant and compact.
- Enables practical reviews of huge codebases that would otherwise be impossible in one go.

**Risks & Trade-offs:**
- Potential to miss cross-module or systemic issues (e.g., a problem in the target module caused by changes elsewhere, or a global pattern that only becomes visible at full-repo scale).
- Less holistic understanding; recommendations may be locally optimal but globally suboptimal.
- For security, performance, or architecture reviews, surface/targeted modes can under-detect distributed risks or inconsistencies.
- If the declared scope or goal is imprecise (user error or ambiguity), important areas can be overlooked.
- In highly coupled/legacy codebases, even "specific module" reviews may still need some global context, reducing the token savings.
- Over-reliance on abbreviated modes without follow-up can lead to incomplete mental models for the reviewer or user.

**Mitigation (built into the skill — actively counters each risk):**
- **Missed systemic issues & incomplete mental model**: Every review (including Surface and Specific-Module) **always** performs a compact global Phase 0+1 high-level map first. In Phase 1, explicitly scan for and document: shared utilities/dependencies used by the scope, cross-module imports/calls, global patterns (e.g., inconsistent auth/logging/error handling), and potential ripple effects. The cached "working memory map" includes a "Systemic Notes" section.
- **Domain-specific risk amplification** (security, performance, reliability, architecture): If the goal includes any of these (or "comprehensive"), the skill automatically triggers a **lightweight global cross-check** even in scoped reviews: grep for related patterns outside the declared scope, note inconsistencies, and flag emergent risks. For these goals, default effort is raised and scope expansion is recommended.
- **User/scope error amplification & imprecise coupling**: Phase 0/1 includes quick heuristics for coupling (number of cross-imports, size of shared modules, recent changes to shared code). If high coupling or legacy signals are detected, the agent must explicitly warn the user, document the limitation, and offer to expand scope or perform a broader scan.
- **Coupled/legacy code penalty**: Detection of high interdependency (via grep for imports, shared files, or git history) triggers automatic recommendation to treat the review as higher effective tier or to include a "global context light scan". Token savings are still achieved by keeping the deep analysis scoped, but the initial map is richer.
- **Over-confidence risk**: The output **always** includes a dedicated "Scope Limitations, Blind Spots & Systemic Risks" section (see Section 8). The agent must list what was *not* reviewed in depth and potential areas where problems could hide. Follow-up suggestions are phrased to directly address these blind spots (e.g., "Check usages of shared utility X across the repo").
- **General safeguards**: Strong "grep-first + document assumptions" policy. Explicit self-critique in Phase 4: "What systemic issues or global patterns might I have missed due to scope?"
- Low-friction iteration is emphasized throughout: every output ends with targeted, low-token follow-up options that specifically target the above risks.

## 8. Output Structure Recommendation (Risk-Aware)

Organize final deliverable as:

1. Executive Summary (tier, overall health, top 3 findings, **high-level scope & key systemic notes**)
2. Repository Metrics & Classification
3. Architecture Overview (with diagram description if possible) **+ Systemic Notes** (shared utilities, cross-module interactions, global patterns observed, coupling signals)
4. Detailed Findings (by category or module, with evidence) — bounded to declared scope but with notes on potential external implications
5. Prioritized Recommendations (table: Finding | Severity | Effort | Suggested Action | Rationale) — include any scope-related caveats
6. Positive Observations & Strengths
7. **Scope Limitations, Blind Spots & Systemic Risks** (mandatory section): 
   - What was reviewed at what depth
   - Explicit list of potential blind spots (e.g., unexamined cross-module effects, global inconsistencies not fully checked, areas outside scope that could affect findings)
   - Coupling/legacy observations and whether they reduced token savings or required extra global context
   - Over-confidence warnings if applicable
8. Next Steps / Follow-up Opportunities (strongly encourage targeted deep dives that address the blind spots listed above, e.g., "Check global impact of shared utility X" or "Expand to full-repo scan for security patterns")
9. Appendix: Sampling strategy, tools used, assumptions, and exact scope declaration

This framework ensures reviews are consistent, appropriately scoped, **and explicitly honest about limitations and risks**. Load this skill early in any codebase review task and follow its phased approach.

## Resources

- `references/prompt-templates.md` — Expanded ready-to-copy prompt variations for different tiers and review goals.
- `references/measurement-commands.md` — Portable and enhanced bash commands for gathering accurate repo metrics (file counts, LOC, tests, activity, monorepo signals).

## Don't use when

- Diff/PR review since a fixed point → multi-axis `/code-review`
- Full security audit with findings schema → `/security-auditor`
- Single-module design vocabulary → `/codebase-design`

## Related

- **Parent domain:** `/review` (**on-ramp** — plan tier/effort, then load a sub-hub)
- **After plan:** `/code-review` · `/security-auditor` · `/software-architect` as goal dictates
- **Domain router:** `/review`
