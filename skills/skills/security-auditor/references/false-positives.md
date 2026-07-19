# Common False-Positive Patterns to Reject

During Phase 3 (Validation) and Phase 6 (Independent Verification), actively use this list to reject or heavily demote weak candidates. The goal is high signal, not exhaustive reporting of every theoretical issue.

## Patterns That Are Usually False Positives or Low Value

### Checklist / Pattern Matching Without Reachability
- “Uses `eval` / `exec` / `system`” when the argument is a hard-coded constant or fully controlled by the developer.
- “SQL string concatenation” when the concatenated parts are all trusted constants or already parameterized.
- “Potential XSS” on server-side rendered pages that correctly escape by default (e.g., most modern frameworks) and the finding shows no bypass.
- “Missing CSRF token” on endpoints that are safe methods (GET) or already protected by other strong mechanisms (SameSite=Strict + additional checks) when the framework default is secure.
- “Insecure random” used for non-security purposes (UI animations, temporary IDs that are not secrets, etc.).

### Theoretical Issues Without Practical Impact
- Missing security headers on an internal-only service with no browser clients.
- “Information disclosure” of stack traces that only appear in development mode or are behind strong authentication and not reachable by attackers.
- Open redirect that can only redirect to a fixed allow-list of domains already controlled by the application.
- “Weak cryptography” used for non-security purposes (checksums, non-sensitive caching).

### Framework / Library Protections Already Present
- Claims of injection when the code uses a well-known safe API (parameterized queries, prepared statements, ORM methods that escape, React’s default escaping, etc.) and no escape hatch is used.
- Authorization bypass claims that ignore middleware or decorators clearly applied to the route.
- “Hard-coded secret” that is actually a public client ID, non-sensitive configuration, or a test fixture.

### Race Conditions That Are Benign or Extremely Unlikely
- Data races on variables that are only written during single-threaded initialization.
- TOCTOU on local files in a single-user CLI tool with no concurrent access.
- Races that can only produce a cosmetic or non-security inconsistency.

### Ambiguity Findings Without Consequence
- Naming inconsistencies that do not affect correctness or security.
- TODOs in non-critical paths that do not indicate unresolved security decisions.
- Documentation that is slightly outdated but the code itself is clear and correct.

### Overly Broad or Speculative Claims
- “This could be vulnerable to future library changes.”
- “If an attacker could somehow control X (but X is not controllable).”
- Findings that require multiple independent, high-privilege compromises already.

## Validation Questions to Ask Before Accepting a Finding
1. Is the dangerous sink actually reachable with attacker-controlled (or untrusted) data?
2. Are there mitigating controls (framework defaults, middleware, encoding, allow-lists, transactions) that the original hunter missed?
3. Does the claimed impact hold under realistic deployment and attacker capabilities?
4. Can I construct a concrete, end-to-end scenario, or is it only a code pattern?
5. Would a skilled human auditor report this, or would they filter it out as noise?

## When to Keep a Borderline Finding
- The impact is high (RCE, auth bypass, mass data leak) even if likelihood is lower.
- The code is in a security-critical path and the ambiguity meaningfully increases risk.
- There is clear evidence the developers intended a security control that is incomplete or incorrect.
- The finding is part of a larger chain that becomes dangerous when combined.

Reject early and often. A shorter list of high-confidence findings is far more valuable than a long list of theoretical issues.
