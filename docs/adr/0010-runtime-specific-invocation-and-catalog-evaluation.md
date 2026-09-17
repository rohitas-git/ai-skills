# ADR 0010: Runtime-specific invocation and catalog evaluation

## Status

Accepted

## Context

Claude and Codex expose different controls for whether a model may select a skill implicitly. Claude
reads `disable-model-invocation` from `SKILL.md`; Codex reads
`policy.allow_implicit_invocation` from `agents/openai.yaml`. Codex also has a separate
`skills.config[].enabled` installation filter. Treating these controls as one “model invocation”
switch hid divergent runtime behavior and made catalog-size evidence ambiguous.

The Butler and hub graph already own routing. This decision must not change their bodies, route
tables, membership, or progressive-disclosure flow.

## Decision

1. **Claude policy** — only `1-coding-standards` is implicitly invocable. Every other live skill
   sets `disable-model-invocation: true`.
2. **Codex policy** — the 21 top-level skills whose `metadata.catalog.role` is `hub`, plus
   `1-coding-standards`, are implicitly invocable. Every other live skill explicitly sets
   `agents/openai.yaml` → `policy.allow_implicit_invocation: false`. Existing interface,
   dependency, and metadata fields remain intact.
3. **Installation is separate** — `skills.config[].enabled` controls whether Codex presents an
   installed skill at all. Invocation policy does not remove a skill and explicit `$skill-name`
   invocation remains available for manual-only skills.
4. **Lint is runtime-specific** — JSON lint schema version 2 exposes
   `invocation_policies.claude` and `invocation_policies.codex`, each with implicit/manual names,
   convention violations, and an independent context-budget warning.
5. **Catalog-size evaluation is controlled** — the evaluator may compare `full-live` (all 283
   promoted live skills) with `hub-spine` (21 top-level hubs, five sub-hubs,
   `1-coding-standards`, and `2-verify-work`; 28 total) through per-process Codex overrides. It
   never edits the user's global Codex configuration.
6. **Profiles require accuracy evidence** — recommend selectable profiles only when `hub-spine`
   gains at least two routing successes over 18 trials, improves at least two of three
   repetitions, and introduces no reduced-only behavior failure. Warning, token, and latency
   reductions alone are operational evidence, not routing proof.

## Consequences

- Claude and Codex may intentionally expose different implicit catalogs while retaining the same
  Butler-and-hub architecture.
- Manual-only Codex manifests are numerous but mechanically uniform and lint-enforced.
- Evaluation records pin source, catalog, case, runtime, model, reasoning, service tier, skill-set,
  repetition, warning, latency, and available usage evidence.
- Installation profiles are not created by this ADR; the controlled comparison informs a later
  decision.

## Related

- ADR 0009 — catalog route surface for Butler
- Guideline — [`model-invocation-and-agent-judgment.md`](../../guidelines/model-invocation-and-agent-judgment.md)
- Evaluation — [`ai-native-evaluation.md`](../../guidelines/catalog/ai-native-evaluation.md)
