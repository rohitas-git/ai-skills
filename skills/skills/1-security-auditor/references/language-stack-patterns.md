# Language- and Stack-Specific Attack Patterns

Load this reference during Phase 2 (Hunting) when the project uses one or more of the languages or stacks below. Focus on the relevant sections. These patterns complement the general classes in `attack-classes.md`.

## Python
- Command injection via `os.system`, `subprocess` with `shell=True`, or `eval`/`exec` on untrusted input.
- Pickle / YAML / Marshal deserialization of untrusted data.
- Path traversal in `open()`, `os.path.join` without proper sanitization, or `shutil` operations.
- SQL injection when using raw strings instead of parameterized queries (even with ORMs if `.extra()` or raw SQL is used).
- Insecure temporary files (`tempfile` misuse, predictable names).
- SSRF via `requests`/`urllib` with user-controlled URLs and no allow-list or metadata protection.
- Hard-coded secrets, debug flags left enabled (`DEBUG=True` in Django/Flask production configs).
- Race conditions in file operations or shared state without locks.
- Jinja2 / Mako template injection when user input reaches templates unsafely.

## JavaScript / TypeScript (Node.js & Browser)
- Prototype pollution (`__proto__`, `constructor.prototype`) via deep merges or object assignment.
- ReDoS (Regular Expression Denial of Service) on user-controlled patterns.
- Command injection via `child_process.exec` / `execSync` with unsanitized input.
- Path traversal in `fs` operations or `path.join` without normalization + root checks.
- SSRF / open redirects.
- XSS (reflected, stored, DOM-based) — especially in React/Vue/Angular when dangerouslySetInnerHTML or similar is used.
- Insecure JWT handling (alg=none, weak secrets, missing `exp`/`iss` validation).
- Dependency confusion or typosquatting in package.json.
- Client-side secrets in frontend bundles.
- Missing CSRF protection on state-changing endpoints.

## Go
- Command injection via `os/exec` with user input in arguments when shell is involved, or unsafe `Cmd`.
- Path traversal (`filepath.Join` + user input without `filepath.Clean` + root confinement).
- Race conditions on shared maps/slices without mutexes or channels (detect with `-race`).
- SQL injection when using string concatenation instead of placeholders.
- Insecure TLS (`InsecureSkipVerify: true`).
- Unsafe reflection or `unsafe` package misuse.
- Hard-coded credentials or API keys.
- Goroutine leaks or unbounded concurrency leading to DoS.

## Java / Kotlin
- Deserialization gadgets (especially older libraries, Jackson, XStream, etc.).
- SQL / LDAP / XPath / OGNL / SpEL injection.
- XXE in XML parsers (DocumentBuilder, SAX, etc.) when external entities are enabled.
- Path traversal in file operations.
- Insecure random (`java.util.Random` for security decisions).
- Hard-coded keys or weak crypto (ECB mode, MD5/SHA1 for passwords).
- Mass assignment / binding vulnerabilities.
- SSRF via URL connections or HTTP clients without restrictions.

## Rust
- Unsafe blocks that violate memory safety or create data races.
- Integer overflows in release builds (when checks are disabled).
- Path traversal or TOCTOU in file system operations.
- Command injection via `std::process::Command` with unsanitized arguments.
- Deserialization of untrusted data with `serde` without validation.
- Misuse of `unsafe` FFI boundaries.
- Missing bounds checks that can lead to panics used for DoS.

## General Web / API Stacks (regardless of language)
- Broken object-level authorization (IDOR).
- Missing rate limiting on authentication or expensive endpoints.
- Overly permissive CORS.
- Missing or weak Content-Security-Policy, X-Frame-Options, etc.
- GraphQL: introspection enabled in production, missing query depth/complexity limits, authorization bypasses.
- gRPC / WebSocket authorization gaps.
- File upload: unrestricted types, path control, malware scanning absence, oversized files.

## Other / Emerging
- For mobile (if present): insecure data storage, weak certificate pinning, exported components.
- For infrastructure-as-code (Terraform, CloudFormation, etc.): overly permissive IAM, public resources, missing encryption.
- For serverless: excessive permissions on functions, event injection, cold-start side channels.

When a language-specific pattern is found, map it to the corresponding general class (Injection, Broken Access Control, etc.) and note the language context in the finding.
