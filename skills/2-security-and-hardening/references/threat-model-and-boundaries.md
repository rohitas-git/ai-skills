# Threat model and authority

Follow the parent's task, scope, workspace and caller-return contract. Hardening
does not grant new operational authority or reopen unrelated architecture choices.

## Understand the changed boundary

Identify who wrote the input, its trust level, consequential sinks, assets and
existing controls. Include local files, another process's output, job payloads,
webhooks, third-party data and model output; “came from the OS” is not provenance.

Use STRIDE where useful: spoofing, tampering, repudiation, disclosure, denial of
service and privilege escalation. Map plausible abuse cases to the actual feature,
then identify the smallest control and test that would reject each case. Include
legitimate behavior the control must preserve. A fixed five-minute ritual is not
evidence of adequate threat modeling.

## Three tiers

**Within authorized implementation:** validate input at trust boundaries, authorize
protected effects, parameterize queries, encode output for its sink, minimize data,
preserve safe failures and add meaningful tests. Reuse the project's mechanisms.

**Ask when not already authorized:** new auth/data-sharing flows, changed roles or
access policy, a new vendor/dependency, new persistent infrastructure, consequential
CORS/retention/rate-limit policy changes or broader PR scope. Do not ask again for
a narrowly specified fix the user already approved.

**Never infer permission:** live credential testing/rotation, production operations,
history rewriting, remote migrations, executing untrusted install scripts, weakening
gates or deleting user data. Respect stricter repository constraints.

## Match controls to context

Browser headers and cookie policy need browser/session context; a native client,
public static asset, OAuth callback and private cookie-authenticated API have
different requirements. Do not force a blanket cookie/CORS/header recipe onto each.
Use modern password-hashing guidance when this code actually owns passwords; do
not replace a managed identity provider or migrate existing hashes incidentally.

A security audit or review caller stays read-only. If implementation is required,
return the scoped finding and proposed verification to that caller for authority.
