# AI interaction states

Load for an AI-powered interaction within the parent's existing product and accessibility contract.
This is interaction implementation guidance, not permission to invent product policy or a new visual system.

- Distinguish suggestion, editable draft, pending operation, proposed action and confirmed completion.
  Streamed text is not a saved result or proof that an external action succeeded.
- Define applicable no-answer, conflicting/stale evidence, refusal, incomplete response, unavailable
  provider and policy-denied states. A generic retry button must not duplicate a consequential action.
- Give users the appropriate ability to edit, reject, cancel, inspect sources, use a fallback or escalate.
  Explain cancellation limits when work may already have taken effect; do not promise universal undo.
- Preserve keyboard/focus and screen-reader semantics while results stream. Avoid announcements on every
  token; keep status and final-result changes understandable without relying on color or animation.
- Show sources when they help assess the answer, while distinguishing citations from proof of correctness.
  Do not display a model's self-reported confidence as a calibrated guarantee or an authorization signal.
- Make feedback specific enough to diagnose the issue. Explain its use and preserve privacy/consent rules;
  interacting with a suggestion is not necessarily agreement with it.
- Exercise representative short/long, partial, error, denied and corrected states with synthetic fixtures.
  Label mocked rendering separately from model quality and end-to-end action verification.

[Research basis](../../../guidelines/catalog/research-ai-app-engineering-2026-11-17.md): S1, S8, S11.
