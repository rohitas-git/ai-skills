# Phase 1 — Reconnaissance

Perform a thorough mapping of the project before any hunting. The goal is a shared, accurate mental model that guides later phases and reduces false positives.

## Steps

1. **Identify project type and stack**
   - Languages, frameworks, major libraries.
   - Application style: web app, API/service, library/SDK, CLI, mobile, desktop, smart contracts, ML/AI system, infrastructure, etc.
   - Build system, package manager, test framework, CI/CD presence.

2. **Map architecture and components**
   - Main modules, services, or packages and their responsibilities.
   - Data stores (databases, caches, file systems, queues).
   - External integrations and third-party services.
   - Privilege levels and trust boundaries (user vs admin, internal vs external, sandbox boundaries).

3. **Identify entry points and attack surfaces**
   - HTTP/API endpoints, CLI commands, message consumers, file parsers, RPC methods, webhooks, etc.
   - Authentication and authorization entry points.
   - Configuration surfaces (env vars, config files, feature flags, admin UIs).
   - User-controlled input paths (query params, body, headers, files, environment).

4. **Data flows and sensitive data**
   - Where sensitive data (credentials, PII, tokens, secrets, financial data) is created, stored, transmitted, logged, or deleted.
   - Encryption, hashing, and key management practices visible in code or config.

5. **Dependencies and supply chain**
   - Direct and notable transitive dependencies.
   - Lockfiles present? Outdated or known-risky packages?
   - Build and deployment scripts that pull external code or artifacts.

6. **Documentation and ambiguity signals**
   - README, architecture docs, ADRs, OpenAPI/Swagger, comments, TODOs, FIXMEs.
   - Note inconsistencies between documentation and code, underspecified contracts, or conflicting statements.
   - Missing or incomplete security-related documentation (threat models, auth flows, etc.).

7. **Configuration and deployment**
   - Hard-coded secrets or insecure defaults.
   - Debug modes, verbose error pages, or overly permissive CORS/CSP that may reach production.
   - Infrastructure-as-code or policy files if present.

## Output

Produce a concise but complete `architecture.md` containing:
- Project type and tech stack summary
- High-level component diagram description (text or Mermaid if helpful)
- Trust boundaries and privilege model
- Key entry points and data flows
- Sensitive data inventory
- Notable dependencies and supply-chain observations
- List of ambiguities or incomplete specifications discovered
- Suggested high-priority hunting areas based on the map

Keep the document factual and grounded. Do not speculate about vulnerabilities yet — that belongs in the hunting phase.
