# Phase 2 — Hunting / Attack and Review Classes

Use the architecture map from Phase 1 to focus effort. Run specialized passes (or parallel sub-agents) for the classes below. Not every class applies to every project — select those relevant to the stack and architecture.

For each candidate finding record:
- Precise location (file + line or function)
- Category (security / logic / ambiguity / bug)
- Concrete scenario or reproduction steps
- Impact (what an attacker or user can achieve, or what fails)
- Estimated severity (Critical / High / Medium / Low) and confidence
- Evidence (code snippets, data-flow reasoning)

## Security Classes

### Injection
SQL, NoSQL, command, template, LDAP, XPath, OS command, header, log injection. Check all sinks that incorporate untrusted data.

### Broken Access Control / Authorization
Missing or incorrect checks, IDOR, privilege escalation, forced browsing, mass assignment, insecure direct object references, missing function-level access control, CORS misconfigurations that enable unauthorized actions.

### Authentication & Session Management
Weak password storage, missing MFA where expected, session fixation, insecure session tokens, improper logout, credential stuffing vectors, broken password reset, JWT issues (alg none, weak secrets, missing validation).

### Cryptographic Failures
Weak algorithms, hardcoded keys, improper IV/nonce handling, missing encryption for sensitive data at rest or in transit, insecure random number generation, certificate validation bypasses.

### Security Misconfiguration
Default credentials, unnecessary features enabled, verbose errors, missing security headers, overly permissive file permissions, debug endpoints left active, insecure cloud or container defaults.

### Software Supply Chain
Vulnerable or abandoned dependencies, typosquatting risks, compromised packages, insecure build scripts that pull untrusted code, missing integrity checks (checksums, signatures).

### Sensitive Data Exposure
Secrets in source, logs, or error messages; PII leakage; excessive data in API responses; insecure temporary files; client-side storage of sensitive data.

### Business Logic & Feature Abuse
Workflow bypasses, race conditions in multi-step processes, price/quantity manipulation, coupon abuse, infinite loops via user input, privilege confusion across roles.

### Client-Side (when applicable)
XSS (reflected, stored, DOM), CSRF, clickjacking, prototype pollution, open redirects, insecure postMessage, CSP bypasses.

### AI / LLM / Agent-Specific (when the project contains these)
Prompt injection, indirect prompt injection, tool/function calling abuse, excessive agency, sensitive data in prompts or embeddings, jailbreak surfaces, insecure plugin or skill loading.

### Chained and Wildcard
Look for multi-step attack chains. Also perform open-ended exploration of unusual or creative attack paths suggested by the architecture.

## Logical, Functional, and Quality Classes

### Functional / Logical Errors
Incorrect algorithms, inverted or incomplete conditions, off-by-one errors, wrong state transitions, missing cases in switches or pattern matches, incorrect assumptions about input ranges or invariants.

### Concurrency and Race Conditions
Shared mutable state without proper synchronization, TOCTOU bugs, deadlocks, livelocks, incorrect use of locks/atomics/channels, data races, order-of-operations issues under concurrency.

### Edge Cases and Boundary Conditions
Empty inputs, maximum/minimum values, null/None/undefined handling, very large or very small numbers, Unicode edge cases, resource exhaustion (memory, file descriptors, connections), timeouts.

### Error Handling and Exceptional Conditions
Swallowed exceptions, overly broad catch blocks, information leakage in errors, missing cleanup on error paths, fail-open security decisions, unhandled error codes from libraries.

### Ambiguity Detection
- Code or documentation that can reasonably be interpreted in multiple conflicting ways.
- Inconsistent naming or overloaded terms across modules.
- Contracts between components that are incomplete or contradictory.
- TODOs, FIXMEs, or comments that indicate unresolved design decisions in security- or correctness-critical paths.
- Mismatches between documented behavior and actual implementation.
Surface these as findings when they can lead to defects, security issues, or maintenance hazards.

## Hunting Strategy Tips

- Start with high-risk areas identified in recon (auth, input handling, crypto, privileged operations, concurrency hotspots).
- Trace data from untrusted sources to sensitive sinks.
- Consider both attacker-controlled input and privileged insider or compromised-component scenarios.
- For libraries, focus on misuse resistance and safe defaults.
- Prefer depth on critical paths over shallow coverage of everything.
- Record negative findings only when they are surprising or high-value (e.g. "auth checks are consistently present and correctly placed").
