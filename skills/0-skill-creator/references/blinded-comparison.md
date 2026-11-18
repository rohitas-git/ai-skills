# Blinded skill comparison

For a substantial behavior change, define an outcome-based rubric and freeze representative tasks before
running candidates. Give each candidate the same ordinary request in an isolated workspace, without the
rubric, variant identity, or knowledge of other candidates. Keep model/runtime settings matched when
comparing skill versions; use repeated trials for probabilistic behavior.

Use the existing [evaluation harness](../../../guidelines/catalog/ai-native-evaluation.md) for supported
fixture cases. Explicit execution runs the selected cases; structural checks and mocked output do not
replace observed workflow behavior. Retain unsuccessful attempts and infrastructure failures.

For a judge comparison, export only reviewed prompt/output/artifact text and run the
[packet preparer](../scripts/blind-packets.py), following [its input format and command](../../../guidelines/catalog/pstack-tooling.md#blinded-review-packets).
Give a fresh authorized judge only `judge.json`; keep `private-map.json` with the operator. Screen text for
identity leakage. Score both options on one rubric in one pass, then reconcile with real artifacts and
permitted transcripts before revealing identities. Self-report does not prove a skill was used or a test ran.

This is an optional measurement method, not authority to spawn agents, call providers, install software,
read unrelated transcripts, or publish results. A single workflow smoke run establishes no comparative gain.

Adapted from [pstack's eval playbook](https://github.com/cursor/plugins/blob/e1cc03121a0e71129a4fb730d7c5528a0a3e43c8/pstack/skills/poteto-mode/playbooks/eval.md), MIT, Lauren Tan.
