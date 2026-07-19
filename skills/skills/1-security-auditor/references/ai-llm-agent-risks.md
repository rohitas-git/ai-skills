# AI / LLM / Agent-Specific Risks (Expanded)

Load this reference when the project contains LLM calls, prompt construction, agent loops, tool/function calling, RAG pipelines, skills, plugins, or multi-agent systems. These risks are often novel and high-impact.

## Prompt Injection (Direct & Indirect)
- User-controlled input concatenated into system or developer prompts without clear separation or sanitization.
- Indirect prompt injection via retrieved documents, emails, web pages, or tool outputs that the model is instructed to follow.
- Jailbreak or instruction override techniques that survive current defenses.
- Multi-turn conversation history that allows gradual escalation.

## Tool / Function Calling & Agency Abuse
- Tools that can execute code, run shell commands, write files, or make network requests with insufficient authorization or confirmation.
- Overly powerful tools granted to the model by default.
- Missing human-in-the-loop for high-impact actions (delete, transfer money, send emails, change permissions).
- Tool argument injection (model-generated arguments that escape intended constraints).
- Recursive or unbounded tool use leading to cost or resource exhaustion.
- Confused deputy problems when the agent acts on behalf of a user with higher privileges.

## RAG & Knowledge Base Risks
- Retrieval of sensitive documents that should not be accessible to the current user/context.
- Poisoned or adversarial documents that alter model behavior.
- Insufficient access control on the vector store or document corpus.
- Leakage of other users’ data through similarity search.

## Secrets & Sensitive Data in Context
- API keys, credentials, PII, or internal documents included in prompts or conversation history.
- Logging of full prompts/responses that contain secrets.
- Model providers or intermediate services receiving sensitive data without proper controls.
- Embeddings that inadvertently encode sensitive information.

## Output Handling & Downstream Risks
- LLM output treated as trusted (executed as code, rendered as HTML without sanitization, used in SQL, etc.).
- Hallucinated but plausible-looking sensitive data or instructions.
- Insecure deserialization or evaluation of model-generated structures.

## Multi-Agent & Orchestration Risks
- Agent-to-agent communication without authentication or authorization.
- Privilege escalation across agents with different trust levels.
- Shared memory or state that one compromised agent can poison.
- Lack of isolation between different users’ agent sessions.

## Skills, Plugins & Dynamic Code Loading
- Skills or plugins loaded from untrusted sources without integrity checks or sandboxing.
- Skills that contain prompt-injection payloads, malicious code, or excessive permissions.
- Dynamic tool registration based on untrusted input.
- Insufficient 0-review or allow-listing of available skills/tools.

## Supply Chain & Model Risks
- Use of untrusted or unpinned model versions / fine-tunes.
- Malicious or backdoored models.
- Dependency on external model APIs without fallback or rate limiting.
- Training data or fine-tuning data that introduces biases or backdoors.

## Denial of Service & Cost Abuse
- Unbounded generation, recursive agent loops, or expensive tool calls triggered by user input.
- Prompt that forces very long context or high token usage.
- Lack of timeouts, max-iterations, or budget controls on agent runs.

## Detection & Finding Guidance
- Trace every place user or external data enters a prompt or tool argument.
- Look for string concatenation or template rendering into prompts.
- Examine system prompts and safety instructions for robustness.
- Check authorization decisions that rely solely on the model’s judgment.
- Prefer findings with a concrete attack scenario (e.g., “User sends X → model calls tool Y with Z → impact”).
- Note residual risk even when mitigations (such as output filters) are present.

Map findings to categories such as “prompt-injection”, “tool-abuse”, “excessive-agency”, “data-leakage”, or “insecure-output-handling”.
