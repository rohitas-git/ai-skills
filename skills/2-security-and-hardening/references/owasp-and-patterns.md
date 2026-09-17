# Focused prevention patterns

Apply the parent's scope/authority contract. These are design constraints and small
illustrations, not complete endpoints or an instruction to install example libraries.
Use the project's actual APIs and verify against its pinned versions.

## Input, authorization and state

Normalize when the contract requires it, then validate type, length, range and
allowed fields. Validate the normalized value: trimming after a nonempty check
can leave whitespace-only content. Bound request/decoded sizes before expensive
parsing; choose safe error fields rather than echoing raw validation payloads.

For a protected mutation, obtain identity from verified authentication, apply the
actual tenant/role/ownership policy at the effect, and permit only intended fields.
A prior lookup followed by an unrestricted update can race or allow mass assignment.
For example, an owner-scoped title update might use a parameterized predicate:

```sql
UPDATE tasks
SET title = $1
WHERE id = $2 AND owner_id = $3
RETURNING id, title;
```

Here $1 must already be validated, $3 must come from authenticated state, and the
real application may additionally need tenant/state/version predicates and RLS.
Handle zero rows using the agreed not-found/forbidden policy without leaking
existence. Never pass the entire request body into an update merely because an
earlier ownership check passed. Test unauthorized fields and concurrent state changes.
See [authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).

## Output and sensitive fields

Prefer parameterized database access and sink-appropriate encoding. ORM use alone
does not secure raw query escape hatches. Render ordinary text as text; when rich
HTML is genuinely required, use the existing maintained sanitizer with an appropriate
policy and test the actual sink.

Choose public fields explicitly; excluding a few currently known secret fields
can expose a new private column later:

```typescript
// Illustration: select only fields this public contract permits.
return { id: user.id, displayName: user.displayName };
```

Do not put raw records, SQL, stack traces, validation inputs or tokens in client
errors. Keep necessary internal diagnostics access-controlled and redacted.

## Sessions, browser policy and transport

Use existing authentication/session facilities. Select cookie flags, expiry and
CSRF protection for the actual flow; SameSite is defense-in-depth, not universal
proof against CSRF. Test callbacks, embedded flows and legitimate cross-site cases.
See [CSRF guidance](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html).

CORS controls browser response access, not caller authorization. Explicitly public
credential-free resources may allow any origin; sensitive credentialed endpoints
need an appropriate origin policy. Do not reflect arbitrary origins or fall back
to a localhost allowlist in production configuration. See [CORS semantics](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS).

Configure CSP, framing, HSTS and Permissions-Policy for the app's deployment and
features. Do not disable camera/microphone, framing or required integrations
universally. HSTS subdomain/preload commitments and restrictive CSP need rollout
and compatibility evidence, not copy-pasted global defaults.
[Header guidance](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html).

## Server-side URL fetching

Establish allowed schemes, destination domains/ports, credentials, redirect policy,
timeouts and response-size limits. Evaluate every resolved address and every
permitted redirect hop, including IPv4/IPv6 special ranges and cloud metadata.

The enforcement must constrain the actual connection. Resolving DNS to validate
a URL and then passing the hostname to an ordinary fetch leaves a second-resolution
race; it is not a complete SSRF defense. Use a verified existing egress enforcement
mechanism or a reviewed client that binds destination validation to the connection
while preserving TLS hostname verification. Do not install an unfamiliar “safe fetch”
package without inspecting its guarantees and authorization.

Test rejected destinations and redirects using inert local fixtures, not production
metadata endpoints. See [SSRF guidance](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html).

## Uploads

Client MIME type, extension and magic bytes alone do not prove a file safe. Enforce
streaming size limits, intended file/content types, safe parsing/processing and
resource limits. Use server-controlled names and storage outside executable/public
paths unless serving behavior is deliberately constrained. Authorize upload/read/
delete separately; prevent overwrites and traversal, and reject hostile archives
or decompression growth. Scanning/processing tools need privacy and execution
authority; do not send private files to a remote service implicitly.
[Upload guidance](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html).
