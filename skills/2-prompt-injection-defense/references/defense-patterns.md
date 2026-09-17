# Prompt-injection defense patterns

Prompt injection exploits the absence of a dependable instruction/data boundary inside current model processing. Use layered controls to limit authority and consequences; do not represent any single pattern as prevention.

## Attack-path inventory

### Direct

An attacker supplies instructions through the normal user channel. Consider multi-turn setup, claimed authority, role-play, encoding, language switching, and request fragmentation.

### Indirect

Instructions arrive inside content the system was asked to process: web pages, email, chat history, documents, code comments, issues, database rows, API fields, tool results, or retrieved passages.

### Stored and delayed

Attacker-controlled content persists in memory, summaries, vector indexes, profiles, logs later re-ingested, or shared workspaces and activates in a later task.

### Cross-agent

One agent passes tainted instructions or an overbroad delegation to another. Summaries can erase provenance while retaining the attacker's instruction.

### Multimodal

Instructions may be hidden in images, OCR layers, PDFs, audio, metadata, CSS, off-screen text, or alternate representations. A text-only filter does not cover these paths.

## Control placement

### Before model context

- Authenticate source and preserve provenance.
- Limit supported formats, size, retrieval count, and active content.
- Parse risky formats in an isolated process.
- Retrieve only data authorized for the current actor and task.
- Mark mixed/untrusted content structurally rather than relying only on delimiters.
- Detect known patterns for telemetry or step-up controls, not as blanket permission.

### At the model boundary

- Keep trusted task policy in a separate control plane.
- Minimize sensitive data and available tools.
- Use structured fields for goal, evidence, and candidate action.
- State that untrusted content cannot grant authority, while recognizing this is defense in depth.
- Require uncertainty and provenance in outputs used for decisions.

### At the tool boundary

- Authenticate the actor and authorize tenant, object, action, and fields outside the model.
- Validate narrow schemas, bounds, destinations, and state preconditions.
- Separate read, preview, and commit tools.
- Use least-privilege, short-lived identities per tool or capability.
- Apply destination and network egress allowlists.
- Bind high-risk approval to the exact action and normalized parameters.
- Rate-limit, sandbox, and make writes idempotent where possible.

### At the output sink

- Treat model output as untrusted input.
- Use context-appropriate escaping for rendered content; parameterized SQL and argv/typed APIs for execution. Generic string escaping is not a substitute for authorization or safe APIs.
- Validate URL schemes/destinations and rendered links; constrain redirects and the actual connection, not merely a preflight DNS result.
- Apply data-loss prevention and canary detection before external release.
- Do not render active links, scripts, or attachments without safe handling.

### In memory and orchestration

- Store provenance, trust class, owner, creation time, and expiry with memories.
- Do not promote retrieved content to durable instruction without an authorized process.
- Recalculate permissions for every agent hop.
- Limit delegation depth, tool budgets, time, and data scope.
- Recommend isolation/quarantine of tainted entries to the authorized owner; do not mutate shared memory or destroy evidence during an assessment.

## Boundary-manifest example

```json
{
  "system": "support-triage-agent",
  "protected_assets": [
    {
      "id": "customer-records",
      "classification": "personal",
      "owner": "support-data-owner"
    }
  ],
  "data_sources": [
    {
      "id": "customer-email",
      "trust": "untrusted",
      "modalities": ["text", "html", "attachment"],
      "control_ids": ["source-isolation", "provenance"]
    }
  ],
  "sinks": [
    {
      "id": "ticket-draft",
      "type": "database",
      "trust": "trusted",
      "owner": "support-platform",
      "control_ids": ["tenant-authorization", "output-validation"]
    }
  ],
  "memory_stores": [
    {
      "id": "case-memory",
      "trust": "mixed",
      "read_principals": ["support-agent"],
      "write_principals": ["memory-service"],
      "control_ids": ["provenance", "memory-promotion"]
    }
  ],
  "agent_hops": [
    {
      "id": "triage-to-drafter",
      "from_agent": "triage-agent",
      "to_agent": "draft-agent",
      "control_ids": ["hop-authentication", "tenant-authorization", "provenance"]
    }
  ],
  "destinations": [
    {
      "id": "ticket-store",
      "kind": "internal-api",
      "owner": "support-platform",
      "control_ids": ["destination-allowlist"]
    }
  ],
  "credential_boundaries": [
    {
      "id": "ticket-api-token",
      "credential_class": "service-token",
      "holder": "tool-gateway",
      "audience": "ticket-api",
      "storage": "managed-secret-store",
      "downstream_passthrough": false,
      "control_ids": ["credential-isolation"]
    }
  ],
  "tools": [
    {
      "id": "ticket-draft-update",
      "effects": ["write"],
      "risk": "medium",
      "destination_ids": ["ticket-store"],
      "sink_ids": ["ticket-draft"],
      "control_ids": ["tenant-authorization", "output-validation"],
      "confirmation": {
        "mode": "risk-based",
        "enforcement_point": "tool-gateway",
        "owner": "support-platform"
      }
    }
  ],
  "controls": [
    {
      "id": "source-isolation",
      "kind": "instruction-data-separation",
      "status": "implemented",
      "enforcement_point": "ingestion-parser",
      "owner": "support-platform",
      "evidence_ids": ["code:parser-boundaries"],
      "test_ids": [],
      "time_limited": false,
      "expires_at": null
    },
    {
      "id": "provenance",
      "kind": "source-provenance",
      "status": "planned",
      "enforcement_point": "ingestion-and-memory-metadata",
      "owner": "support-platform",
      "evidence_ids": [],
      "test_ids": [],
      "time_limited": false,
      "expires_at": null
    },
    {
      "id": "memory-promotion",
      "kind": "authorized-memory-write",
      "status": "missing",
      "enforcement_point": "memory-service",
      "owner": "support-platform",
      "evidence_ids": [],
      "test_ids": [],
      "time_limited": false,
      "expires_at": null
    },
    {
      "id": "hop-authentication",
      "kind": "agent-handoff-authentication",
      "status": "verified",
      "enforcement_point": "orchestrator",
      "owner": "agent-platform",
      "evidence_ids": ["config:handoff-signatures"],
      "test_ids": ["test:forged-handoff-denied"],
      "time_limited": false,
      "expires_at": null
    },
    {
      "id": "tenant-authorization",
      "kind": "object-authorization",
      "status": "verified",
      "enforcement_point": "tool-gateway",
      "owner": "support-platform",
      "evidence_ids": ["code:tenant-policy"],
      "test_ids": ["test:cross-tenant-denied"],
      "time_limited": false,
      "expires_at": null
    },
    {
      "id": "output-validation",
      "kind": "typed-output-validation",
      "status": "implemented",
      "enforcement_point": "ticket-adapter",
      "owner": "support-platform",
      "evidence_ids": ["schema:ticket-update-v2"],
      "test_ids": [],
      "time_limited": false,
      "expires_at": null
    },
    {
      "id": "destination-allowlist",
      "kind": "destination-policy",
      "status": "verified",
      "enforcement_point": "network-policy",
      "owner": "security-platform",
      "evidence_ids": ["config:ticket-api-egress"],
      "test_ids": ["test:unapproved-destination-denied"],
      "time_limited": false,
      "expires_at": null
    },
    {
      "id": "credential-isolation",
      "kind": "audience-bound-credential",
      "status": "verified",
      "enforcement_point": "tool-gateway",
      "owner": "security-platform",
      "evidence_ids": ["config:ticket-token-audience"],
      "test_ids": ["test:token-passthrough-denied"],
      "time_limited": false,
      "expires_at": null
    }
  ]
}
```

The example is synthetic, not evidence about any real deployment. The manifest records architectural intent, implementation claims, and visible gaps. `implemented` means implementation evidence exists for the stated candidate/environment; it does not imply deployed state. `verified` additionally requires named tests whose actual results support that claim. Inspect those sources separately: the checker only validates their IDs' structure, not their existence or truth. Keep `missing` and `planned` entries instead of converting unknowns into unsupported assertions. Lint success is not proof the controls work or that every real path was inventoried. Empty arrays mean confirmed not applicable, not unknown; disclose unknown surfaces in the report.

## Evaluation design

Create an invariant-first case table:

| Case | Source | Protected invariant | Expected safe behavior | Utility expectation | Evidence |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Use inert canaries and synthetic identities. Include normal content that discusses attacks so detectors are tested for false positives. Repeat stochastic cases enough to report a rate and configuration, not a single anecdote.

Pin model/version, prompt/configuration, tool policy, candidate and dataset. Check enforcement at the effect boundary, not only what the model says: a refused answer can accompany a tool action, and an attempted unauthorized action may be safely denied. Track attempts separately from completed violations. Do not turn a passing sample into a universal guarantee. Minimize logs; synthetic canaries belong only in approved test systems, never live external destinations. If real data or an unexpected effect appears, stop the test and report to the owner; containment changes require authority.

## Primary references

- [OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [OWASP Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
- [OWASP LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
