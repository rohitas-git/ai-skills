# Tool schema patterns

Read this reference when choosing parameter shapes, separating tools, or specifying mutations.

## Boundaries

Create separate tools when operations have different:

- permissions or confirmation requirements;
- side effects or retry semantics;
- required parameter sets;
- latency or cost expectations;
- user intents that need distinct selection descriptions.

Keep one tool when a small enum selects behavior with identical safety and data requirements. Avoid exposing raw backend endpoints solely because they already exist.

## Parameter patterns

- Use `type: object` at the parameter root.
- Set `additionalProperties: false` when supported.
- Put every indispensable property in `required`; do not require fields with safe defaults.
- Use ISO 8601 strings with an explicit timezone for instants.
- Include units in names such as `timeout_seconds` or descriptions.
- Use opaque identifiers instead of free-form names for mutations after a lookup step.
- Set `minLength`, `maxLength`, `minimum`, `maximum`, `minItems`, and `maxItems` where the domain has real bounds.
- Use `enum` only for a closed set controlled by the implementation.
- Prefer shallow objects. Use `oneOf` only when the provider supports it reliably and branches are distinguishable.

`format`, `pattern`, delimiters and descriptions may be annotations or only partially
enforced by a provider. Enforce important bounds again in runtime code. A regex-shaped
URL/path constraint does not by itself establish an allowed destination or containment;
derive opaque targets from trusted state where practical and authorize the actual effect.
Do not expose idempotency or confirmation tokens merely because they are opaque: bind
them server-side to actor, normalized payload, expiry and single-use/replay policy.

## Mutation contract

Define these alongside the schema:

| Concern | Required decision |
| --- | --- |
| Authorization | Server-derived actor, tenant, and scope |
| Confirmation | Trigger, preview, expiry, and confirmation token |
| Idempotency | Key source, retention window, and duplicate result |
| Retry | Retryable error codes and backoff |
| Partial success | Per-item status and compensating action |
| Audit | Actor, operation, target, policy result, and timestamp |

Never make `confirmed: true` supplied by the model the sole proof of user confirmation.

## Example function definition

```json
{
  "name": "get_order_status",
  "description": "Get the current status of one order by opaque ID. Use after identifying the order; do not use to edit or cancel it.",
  "parameters": {
    "type": "object",
    "additionalProperties": false,
    "properties": {
      "order_id": {
        "type": "string",
        "description": "Opaque order identifier returned by order lookup.",
        "minLength": 1
      }
    },
    "required": ["order_id"]
  }
}
```

## Error envelope

Return stable codes and a safe message:

```json
{"ok":false,"error":{"code":"AUTHORIZATION_DENIED","message":"The caller cannot access this order.","retryable":false}}
```

Do not return stack traces, credentials, internal policy text, sensitive existence clues,
or unrelated records. Use the same outward result where distinguishing missing from
unauthorized would expose an object. Include structured field errors for safe input
fields and an operation identifier for ambiguous timeouts; query status before retrying
a mutation. Treat the result as untrusted before returning it to model context.

## Validator scope

See [validator contract](./validator-contract.md) for exact input, limits and exit codes.
The helper accepts a direct function definition or a `{"type":"function","function":{...}}`
wrapper. `structurally_valid` covers only its documented subset. Without `--strict`,
review warnings do not change exit status; with `--strict`, any warning returns exit 1.

Strict review findings include:

- tool names or string parameters that expose free-form command, shell, script, or code execution;
- caller-controlled privilege/elevation flags and credential- or secret-looking parameters;
- URL, URI, host, endpoint, file, directory, or path strings without an enum, restrictive pattern, or other closed constraint;
- missing or permissive `additionalProperties` on objects;
- missing `maxLength`/required `minLength` on ordinary free-form strings, missing item bounds on arrays, and missing numeric bounds on obviously limit-like fields.

These are conservative name-based heuristics, not a semantic parser. A warning can be
resolved by documented runtime controls rather than a schema-only contortion. A clean
result cannot detect semantic mismatches, hidden implementation behavior, authorization
flaws, sandbox escapes, SSRF/path traversal behind apparently bounded inputs, output
injection, or provider-specific incompatibility. Target runtime and implementation
tests remain authoritative; do not change backend behavior just to silence this aid.
