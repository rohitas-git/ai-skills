# Secrets and rate limiting

Follow the parent's scope and authority. These controls need the application's
identity, deployment and legitimate-use contracts, not universal numeric defaults.

## Secrets

Use the existing secret-management mechanism. Keep actual secrets out of source,
fixtures, screenshots and logs. Commit placeholder templates only; ignore the
specific sensitive/local files the project uses without blanket-hiding unknown
tool-state directories or legitimate certificates/public keys.

Inspect scoped staged/unstaged/new files privately and use an existing trusted
redacting scanner when available and permitted. Do not print matching lines from
a raw diff or entire environment into tool output. Report locations and secret
categories, never values. A keyword grep is neither a reliable secret detector nor
proof that history is clear.

Suspected exposure requires redacted evidence and a containment recommendation.
Removing a string is not revocation. Do not test the credential, rotate/revoke it,
rewrite history or force-push automatically. Those actions can disrupt consumers
and need explicit authority, coordinated scope and verification; route authorized
credential work to /1-identity-and-secrets-management and incident coordination to
/1-incident-response. Git history operations require their own approval.

## Rate limiting

Determine which operation and scarce resource need protection. Choose keys from
trusted identity/network context; distinguish per-account, per-tenant, per-origin
and global limits as appropriate. Do not trust a spoofable forwarded IP, log raw
sensitive identifiers, or lock out shared-NAT users with an arbitrary threshold.

For multiple workers/instances or ephemeral runtimes, validate that counters and
limits hold across the actual topology; process-local counters are not a global
budget. Reuse an existing shared enforcement layer where appropriate. A new store
or external vendor is an integration decision, not an automatic fix.

Specify reset/expiry, proxy handling, retry response and failure policy. Test
legitimate bursts, repeated denied requests, concurrent instances and store failure
with synthetic local inputs. Do not run live abuse/load tests or modify production
limits to establish evidence. Report limitations when topology cannot be reproduced.
