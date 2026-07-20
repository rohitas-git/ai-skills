# OWASP Top 10:2025 and Secure Coding Reference

Use this as a structured checklist during the Hunting phase. Map findings to these categories where applicable, but never force a finding solely to match a category. Prefer concrete impact over category compliance.

## OWASP Top 10:2025 (condensed)

1. **A01 Broken Access Control**  
   Missing, incorrect, or bypassable authorization. IDOR, privilege escalation, CORS issues enabling unauthorized actions, forced browsing, mass assignment.

2. **A02 Security Misconfiguration**  
   Insecure defaults, unnecessary features, verbose errors, missing headers, misconfigured permissions, debug modes in production, cloud/container misconfigs.

3. **A03 Software Supply Chain Failures**  
   Vulnerable dependencies, compromised packages, insecure build pipelines, missing integrity verification, malicious or abandoned components.

4. **A04 Cryptographic Failures**  
   Weak or outdated crypto, improper key management, missing encryption, insecure randomness, certificate validation failures.

5. **A05 Injection**  
   SQL, NoSQL, OS command, template, LDAP, etc. Untrusted data reaching interpreters without proper sanitization or parameterization.

6. **A06 Insecure Design**  
   Missing or weak threat modeling, business logic flaws, lack of security controls by design, insecure architecture patterns.

7. **A07 Identification and Authentication Failures**  
   Broken authentication, weak session management, credential stuffing vectors, missing MFA where warranted, improper password storage or recovery.

8. **A08 Software and Data Integrity Failures**  
   Insecure CI/CD, unsigned or unverified updates, deserialization of untrusted data, integrity failures in critical data.

9. **A09 Security Logging and Monitoring Failures**  
   Insufficient logging of security events, logs that contain secrets, inability to detect or respond to incidents, missing alerting.

10. **A10 Mishandling of Exceptional Conditions**  
   Improper error handling that leads to security or availability issues, fail-open behavior, resource leaks on error paths, unhandled edge conditions.

## Core Secure Coding Practices (actionable checklist)

### Input Validation
- Validate on a trusted system (server-side).
- Prefer allow-lists over block-lists.
- Check length, type, range, format, and encoding.
- Canonicalize before validation where needed.
- Treat all external data (users, files, APIs, environment) as untrusted.

### Output Encoding
- Context-aware encoding (HTML, JavaScript, URL, CSS, SQL, etc.).
- Encode as late as possible, on a trusted system.

### Authentication & Password Management
- Store passwords with strong, adaptive hashing (bcrypt, scrypt, Argon2).
- Enforce reasonable password policy without creating usability traps.
- Protect credentials in transit and at rest.
- Implement secure password reset and account recovery.
- Consider MFA for sensitive operations.

### Session Management
- Generate strong, unpredictable session identifiers.
- Invalidate sessions on logout and after privilege changes.
- Protect session tokens (HttpOnly, Secure, SameSite where applicable).
- Set reasonable idle and absolute timeouts.

### Access Control
- Enforce least privilege.
- Check authorization on every request for every sensitive action.
- Deny by default.
- Avoid client-side-only enforcement.

### Cryptographic Practices
- Use well-vetted libraries and algorithms.
- Never invent crypto.
- Manage keys securely; never hard-code secrets.
- Use authenticated encryption where appropriate.

### Error Handling & Logging
- Fail securely.
- Do not leak sensitive details in error messages to users.
- Log security-relevant events without logging secrets.
- Ensure logs are protected and monitored.

### Data Protection
- Minimize sensitive data collection and retention.
- Encrypt sensitive data at rest and in transit.
- Protect backups and temporary files.
- Implement proper disposal.

### Communication Security
- Use TLS correctly (modern versions, proper certificate validation).
- Avoid mixed content.
- Set appropriate security headers.

### System Configuration
- Keep components patched.
- Remove or disable unnecessary features and accounts.
- Apply principle of least privilege to processes and accounts.
- Harden configurations.

### Database Security
- Use parameterized queries / prepared statements.
- Apply least privilege to database accounts.
- Protect connection strings and credentials.

When a finding maps cleanly to one of the above, note the mapping in the finding record. This aids prioritization and remediation planning.
