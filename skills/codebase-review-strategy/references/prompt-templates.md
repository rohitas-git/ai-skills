# Prompt Templates for Codebase Review Strategy

This reference contains expanded, ready-to-use prompt variations for different tiers and goals. Copy and adapt the relevant sections into your agent instructions.

## General High-Quality Base Prompt

```
You are a world-class senior software architect and code reviewer with 15+ years of experience across multiple languages and architectures.

Task: Perform a [GOAL] review of the provided codebase.

Repo Context (I will supply metrics or you will measure):
- Approximate size: [TINY/SMALL/MEDIUM/LARGE] tier
- Primary languages/frameworks: [list]
- Key characteristics: [tests present? monorepo? etc.]

Instructions:
1. First, clarify or confirm **Review Scope** (Surface / Specific Module or Path / Full Repo). If Specific Module, immediately limit *all* exploration commands to that path/subtree.
2. Confirm repo metrics and tier using low-token tools (tree, grep, git, find with path limits).
3. Follow the phased workflow from the codebase-review-strategy skill, **strictly adapting to Scope and Goal while actively mitigating risks** (missed systemic/cross-module issues, incomplete mental models, domain-specific emergent risks, scope errors, coupling in legacy code, over-confidence from narrow views).
4. **Mandatory Systemic Awareness (even in narrow scopes)**: In Phase 1, perform lightweight global/pattern scan for shared utilities/dependencies, cross-module interactions, global inconsistencies (auth, logging, etc.), and coupling signals. Document in "Systemic Notes".
5. **Grep-first policy**: Use grep, tree, git etc. heavily before reading any full source file. Read files only when clearly relevant.
6. Maintain and incrementally update a compact "working memory" (Repo Map or Module Map **including Systemic Notes**) in context. Reference it to avoid re-work.
7. For high-risk goals (security, performance, reliability, architecture): Include light global cross-checks and consider scope/effort expansion.
8. Scale evidence and depth to scope, but **never omit** Systemic Notes or Scope Limitations sections. Surface reviews still document blind spots and potential external impacts.
9. For every observation, provide concrete evidence (paths + snippets/lines) when possible. Explicitly surface assumptions and limitations. Be actionable.
10. At the end of phases, offer low-token follow-up options that specifically target blind spots and systemic risks (e.g., check global usages of shared utility, expand for consistency scan).

Output format: Use clear headings matching the phased workflow. End with prioritized recommendations **and mandatory Scope Limitations / Systemic Risks section**. Keep Surface outputs concise but complete on limitations.

Start now with a compact Phase 0–1 output including the working memory summary **with Systemic Notes**.
```

## Tier-Specific Prompt Additions

### For Tiny or Small Repos (High Effort)

Add to base:
```
Because this is a [Tiny/Small] codebase, aim for high completeness. You may read the majority of significant source files. Perform detailed line-by-line and logic analysis where relevant. Identify subtle bugs, edge cases, and refactoring opportunities with before/after code examples where helpful. High thinking effort: explicitly walk through multiple reasoning steps for complex sections and critique your own initial conclusions.
```

### For Medium Repos (Medium Effort)

Add to base:
```
This is a Medium codebase. Use a structured two-pass (or three-pass) approach:
- Pass 1 (Medium effort): High-level architecture map, module responsibilities, data/control flows, and identification of the most important 6–12 modules or areas.
- Pass 2 (Medium-High effort): Deep analysis of the prioritized core areas + all cross-cutting concerns (error handling, logging, configuration, testing strategy, security patterns).
- Optional Pass 3: Targeted sampling of secondary modules to confirm patterns or find outliers.

Explain your prioritization criteria clearly (e.g., business criticality, complexity signals from directory structure or git history, frequency of changes).
```

### For Large / Monorepo Repos (Low to Medium Effort)

Add to base:
```
This is a Large codebase (or monorepo). You MUST use aggressive prioritization and sampling. 

Recommended approach:
1. Phase 1 emphasis: Create a high-level map of packages/modules/services, boundaries, and key integration points. Identify the top 8–15 "hotspot" or high-risk areas using signals such as:
   - Recent git activity (files changed in last 3 months)
   - Complexity indicators (deep nesting, large files, many imports)
   - Domain importance (core business logic, auth, data persistence, public APIs)
   - Known pain points from any README/issues

2. Perform High-effort deep review ONLY on the top 3–6 most critical areas. For everything else, provide summary-level observations and your rationale for not diving deeper.

3. Heavily leverage tools: grep for patterns, git log/blame for history, directory analysis, and any available linters or static analysis before reading full large files.

4. Explicitly document your sampling strategy and confidence level in the coverage of the overall system.
```

## Goal-Specific Lens Additions

### Security / Compliance Focused Review

Add:
```
Apply a security-first mindset (STRIDE, OWASP Top 10, least privilege, defense in depth).

Explicitly examine and comment on:
- Authentication & authorization mechanisms and their consistency
- Input validation, sanitization, and output encoding
- Secret management and configuration
- Dependency vulnerabilities and update practices
- Logging of sensitive data or insufficient observability
- Potential injection, XSS, CSRF, SSRF, path traversal, etc. risks relevant to the stack
- Data protection and privacy considerations

For each finding, classify severity (Critical/High/Medium/Low) and suggest concrete mitigations with code-level examples where possible.
```

### Refactoring / Maintainability / Modernization Readiness

Add:
```
Focus on long-term maintainability and evolution.

Key areas to evaluate:
- Adherence to SOLID principles and other design principles
- Code smells (from Clean Code / Refactoring catalogs): long methods, large classes, duplicated code, primitive obsession, feature envy, etc.
- Module coupling and cohesion
- Abstraction quality and boundary definitions
- Technical debt hotspots and "don't touch" areas
- Opportunities for simplification, extraction of common logic, or adoption of better patterns
- Test coverage and quality as enablers of refactoring
- Migration or upgrade paths for outdated dependencies or patterns

For major recommendations, provide a high-level migration or refactoring plan with estimated effort and risk.
```

### Performance & Scalability Analysis

Add:
```
Analyze from a performance and scalability perspective.

Look for:
- Hot paths and frequently executed code
- Inefficient algorithms, unnecessary computation, or repeated work (N+1 problems, missing caching/indexing)
- Resource management (connections, memory, file handles, threads)
- Blocking operations in critical paths
- Scalability bottlenecks (shared state, centralized components, lack of horizontal scaling design)
- Observability (metrics, tracing, logging of performance-relevant events)
- Configuration for different environments or load levels

Where possible, suggest concrete optimizations or architectural adjustments with reasoning about expected impact.
```

### Onboarding / Knowledge Transfer / Documentation Review

Add:
```
Evaluate the codebase from the perspective of a new team member or external contributor.

Assess:
- Clarity of high-level architecture and "how the pieces fit together"
- Quality and discoverability of documentation (README, architecture docs, module docs, inline comments)
- Ease of setting up the development environment and running tests
- Discoverability of key concepts, data models, and business rules
- Presence of examples, diagrams, or decision records
- Consistency of coding standards and naming

Provide recommendations for improving onboarding time and reducing the learning curve, including suggested documentation additions or structural improvements.
```

## Multi-Pass Execution Prompt (for iterative reviews)

```
We are conducting this review iteratively.

Current phase: [Phase X - description]

Previous findings / map summary: [paste or reference key outputs from prior turns]

Continue with the next phase at [effort level]. Maintain consistency with earlier analysis. Update the running architectural map as needed. When you reach synthesis, produce the full prioritized recommendations.
```

These templates are designed to be combined. Start with the General Base, append the relevant Tier-Specific and Goal-Specific sections, and adjust effort level and phase instructions as the review progresses.