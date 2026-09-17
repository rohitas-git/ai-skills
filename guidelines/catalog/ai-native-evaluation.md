# AI-native catalog evaluation

## Decision

Do **not** create selectable Codex installation profiles from the current evidence. In the accepted
matched campaign, `full-live` and `hub-spine` both passed 18/18 routing trials and 12/12 behavior
trials. Hub-spine produced no routing gain and improved zero of three repetitions, so it did not
meet the frozen accuracy gate even though it used fewer input tokens.

Structural lint remains necessary but is not behavioral proof. Runtime invocation and installation
filtering are separate policies; see [ADR 0010](../../docs/adr/0010-runtime-specific-invocation-and-catalog-evaluation.md).

## Controlled candidates

- Frozen cases: [`evals/ai-native-cases.json`](./evals/ai-native-cases.json), six routing and four
  disposable-fixture behavior cases.
- `full-live`: all 283 promoted live skills; inbox candidates excluded.
- `hub-spine`: 21 top-level hubs, five sub-hubs, `1-coding-standards`, and the frozen behavior
  target `2-verify-work`; 28 skills total.
- Bundled/system and plugin availability was held identical between candidates by using the same
  disposable Codex home construction for every trial.
- Codex CLI 0.154.0, `gpt-5.6-sol`, high reasoning, default service tier; three repetitions in
  fixed case order per candidate.
- Every provider session used a disposable `CODEX_HOME` with copied credentials, linked installed
  skills, and a temp-only trust entry. The user's global Codex configuration was not used or
  changed by the accepted campaign.

Codex 0.154.0 prompt inspection showed that manual-only skills are not ordinarily listed for
implicit selection; explicit `$2-verify-work` behavior still passed. Enabled-skill counts therefore
describe the controlled installation scope, not a claim that all enabled descriptions were injected
into every initial prompt.

## Commands

```bash
rtk ./scripts/evaluate-skills validate guidelines/catalog/evals/ai-native-cases.json
rtk ./scripts/evaluate-skills run --runtime codex --cases guidelines/catalog/evals/ai-native-cases.json --all --variant full-live --skill-set full-live --repetitions 3 --model gpt-5.6-sol --reasoning-effort high --service-tier default --output .scratch/ai-native-eval/full-live.jsonl --timeout 240 --execute
rtk ./scripts/evaluate-skills run --runtime codex --cases guidelines/catalog/evals/ai-native-cases.json --all --variant hub-spine --skill-set hub-spine --repetitions 3 --model gpt-5.6-sol --reasoning-effort high --service-tier default --output .scratch/ai-native-eval/hub-spine.jsonl --timeout 240 --execute
rtk ./scripts/evaluate-skills compare .scratch/ai-native-eval/full-live.jsonl .scratch/ai-native-eval/hub-spine.jsonl
```

`run` requires explicit `--execute`, refuses output outside `.scratch/`, starts a fresh session and
fixture per case, disables agent network access, and records commands without exposing prompts in
the command ledger. The harness raises only the Codex child process's open-file soft limit so the
complete catalog loads without descriptor errors.

## Accepted evidence — 2026-09-17

| Candidate | Enabled | Routing | Behavior | Selection errors | Context warnings | Infrastructure failures | Input tokens | Mean latency |
|-----------|--------:|--------:|---------:|-----------------:|-----------------:|------------------------:|-------------:|-------------:|
| `full-live` | 283 | 18/18 | 12/12 | 0 | 0 | 0 | 3,154,956 | 35,820 ms |
| `hub-spine` | 28 | 18/18 | 12/12 | 0 | 0 | 0 | 2,943,639 | 37,955 ms |

Hub-spine used 211,317 fewer input tokens (6.7%) but was 64,028 ms slower in aggregate (6.0%).
These are secondary operational observations: there was no accuracy improvement, and lower token
use alone is not proof that profiles improve routing.

Decision-rule result:

- Additional routing successes: **0**; required at least 2.
- Repetitions with routing improvement: **0/3**; required at least 2/3.
- Reduced-only behavior failures: **0**; maximum allowed 0.
- Recommendation: **do not recommend selectable profiles from this evidence**.

## Reproducibility identity

| Field | Value |
|-------|-------|
| Git revision | `917e139d1dba39ef438a54d7667d003966d7e030` |
| Dirty-state fingerprint | `669bc1dc66ccbd112167d92bbb1b631b3c3874458e805e6e5db40a14233cc403` |
| Catalog version | `1.4.0` |
| Catalog content hash | `7c09f0b71f986d76294d20f21a543f01b272c05579ba180dfd40be8210d4538e` |
| Evaluation-case hash | `fd5c6cae74398de676155270daf7b038eeacbd331cfa05d2e82086b919915900` |
| Full-live set hash | `ecf631aa6e1f516411b949f1d75ac720b2193f3625762d7c0c05ab1e276b63fe` |
| Hub-spine set hash | `2e5127329ded28685dee8e39c748c8b66b1e184cbe7c2dbc32ccf96610ed7c6b` |

Raw prompts, outputs, timings, usage, assertions, and retained attempts remain private scratch
evidence under `.scratch/ai-native-eval/` and are not catalog artifacts. One hub-spine attempt
encountered a provider-capacity exit and was retained in full, then the entire 30-call candidate was
repeated with identical parameters. Application-level misses in retained attempts were not
selectively rerun or removed.

## Acceptance gate

1. Both route projections cover the live skill set; generated projection changes remain outside
   this invocation-policy change.
2. Catalog lint has zero critical invocation-policy findings and Gate PASS.
3. Deterministic routing and evaluator tests pass.
4. Accepted candidate sets contain exactly 18 routing and 12 behavior trials, with matched source,
   catalog, case, model, reasoning, and service-tier identity.
5. Runtime warnings and unavailable telemetry are reported and never promoted into a stronger
   claim.
