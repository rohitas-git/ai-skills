# MCP server design

Optional shape only. Use fields that support the fixed decision; do not fill sections by invention.

## Decision summary

- User job:
- In scope:
- Out of scope:
- Supported clients:
- Transport:
- Protocol revision(s):
- Runtime and SDK:
- Owner:

## Trust and data flow

Describe host, client, server, downstream systems, identities, credentials, trust boundaries, and sensitive data.

## Tool catalog and manifest

When using the bundled structural validator, set top-level
`"manifestProfile": "ai-skills-mcp-tool-manifest-v1"`. This selects the validator's opinionated
design vocabulary; it is not an MCP protocol field and must not be sent to clients as one.

| Tool | Purpose | Effects | Data classes | Authorization mode / enforcement | Idempotency | Input / output / error schemas |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Represent effects and data classes as arrays, even when each contains one value. Give every tool an authorization object; use `mode: public` explicitly rather than omitting authorization. Store machine-checkable `inputSchema`, `outputSchema`, and `errorSchemas` in the JSON manifest. A passing structural lint is not protocol conformance or a safety certification.

## Authorization model

- Authentication:
- Tenant/object/action checks:
- Scopes:
- Downstream token exchange:
- Approval requirements:
- Credential storage and rotation:

## Reliability and limits

- Timeouts:
- Retry policy:
- Concurrency and rate limits:
- Pagination and payload limits:
- Cancellation:

## Verification plan

| Requirement | Test | Expected result | Evidence |
|---|---|---|---|
|  |  |  |  |

For an advertised `2026-07-28` path, include server discovery, per-request metadata, matching
Streamable HTTP header/body routing, required result/cache fields, and MRTR only where applicable.
Test initialize/session behavior only for explicitly supported earlier revisions, separately.

## Operations

- Logs and audit events:
- Metrics and alerts:
- Deployment strategy:
- Rollback:
- Credential revocation:

## Assumptions and residual risk

- Assumptions:
- Unverified items:
- Residual risks and owners:
