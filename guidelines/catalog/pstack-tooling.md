# Adopted pstack tooling

Source: [pstack 0.15.43, commit e1cc031](https://github.com/cursor/plugins/tree/e1cc03121a0e71129a4fb730d7c5528a0a3e43c8/pstack), MIT, Lauren Tan.
The [file manifest](./pstack-tooling-manifest.json) records upstream and adopted hashes.
The [adoption report](./adopt-pstack-tooling-2026-11-18.md) records changes, review coverage, and verification.
These tools belong to existing skills. They do not activate another mode, install a plugin, or grant external-write authority.

## Statecharts

The CLI and upstream test corpus live in [1-statechart-modeling/scripts](../../skills/1-statechart-modeling/scripts/).
Model authoring remains with `/1-statechart-modeling`; executing a reviewed fixed check belongs to `/1-formal-verification`.

```bash
rtk skills/1-statechart-modeling/scripts/statechart Model.tla --config Model.cfg --out Model-proof --timeout 120
```

Set `TLA2TOOLS` to an existing reviewed `tla2tools.jar`; optionally set `JAVA` to the Java binary.
The command never installs Java, TLC, or a renderer. Use Node 22.18–22.x or 23.6+, Bun 1.1.5+, or Deno 2+.
The deadline stops the owned worker group, returns an error, and leaves no published proof directory.
Output requires a new or empty directory. Exit 0 means the original TLC check succeeded; 1 means a rule broke;
2 means an error or deadline, with signals reported separately. Inspect the per-property report and bounds.
A successful bounded model check is evidence about that model, not automatic proof about implementation code.

`--view FILE` loads executable JavaScript. Use only a reviewed trusted module in an authorized run.
Treat TLA+ modules and any Java overrides as executable/trusted inputs too; this CLI is not a sandbox.
Use a restricted disposable environment for unfamiliar input. Keep source-to-model correspondence and
property qualification with the evidence. Rendering preserves the upstream per-rule and mixed-state reporting.

Runtime dependencies are built in. Tests additionally use locked `fast-check`:

```bash
rtk bun install --cwd skills/1-statechart-modeling/scripts --frozen-lockfile --ignore-scripts
rtk bun test --cwd skills/1-statechart-modeling/scripts
```

Node's native test runner covers additional V8/import-hook checks unavailable in Bun. Java/TLC differential
checks require a separately provided toolchain. Renderer checks are opt-in with `STATECHART_RENDER_TESTS=1`
and reviewed locally installed Pele/Mermaid/jsdom packages; the tests never install them or write global caches.

## PR status

The watcher lives in [1-pr-repair/scripts/watch-pr](../../skills/1-pr-repair/scripts/watch-pr/).
It reads GitHub through the existing authenticated `gh` CLI. It never merges, comments, pushes, retries CI, or fetches Git refs.

```bash
rtk bun install --cwd skills/1-pr-repair/scripts --frozen-lockfile --ignore-scripts
rtk skills/1-pr-repair/scripts/watch-pr/watch-pr --owner OWNER --repo REPO --pr 123 --status-only
rtk skills/1-pr-repair/scripts/watch-pr/watch-pr --owner OWNER --repo REPO --pr 123 --stack --timeout 300
```

Dependencies must be installed explicitly; invoking the watcher never bootstraps them.
JSON is the default, with `--pretty` for human output. Prefer a single snapshot during interactive work.
`--status-only` exits 0 when the query completes, even if the payload reports blockers; inspect the verdict.
Polling can be bounded with `--timeout`; this is a polling deadline, not a guarantee that a stalled `gh` subprocess is interrupted.
Every check, including one named `Code Review Gate`, retains normal pending/failed semantics.
Upstream Bugbot annotations are retained as provider-specific observations. A READY verdict is not merge approval
and does not replace required-check policy, tested-SHA evidence, or human review.

## Local worktree audit

```bash
rtk python3 skills/1-git-worktrees/scripts/worktree-audit.py --base origin/main /path/to/repo
```

This standard-library adaptation reads local Git metadata only. It performs no fetch, PR lookup, transcript
scan, size scan, or cleanup. The base is explicit and its SHA is captured once. All untracked files count as
work to preserve. Primary, locked, dirty, prunable, and unknown worktrees are held; clean ones are marked
`review`, never automatically safe to delete. Local ancestry does not establish squash-merge status.
Exit 1 means a worktree could not be inspected; exit 2 means invalid input or a missing base.

## Decision logs

```bash
rtk python3 skills/0-implement/scripts/log-decision.py .scratch/decisions.tsv design 'Use the existing parser' 'Matches accepted input' 'parser.py:20' accepted
```

The TSV adapter appends a timestamp plus phase, decision, why, evidence, and result. It locks concurrent
appends, validates an existing header, refuses symlink/nonregular files, creates new logs with mode 0600,
and escapes spreadsheet formulas even after leading whitespace. It preserves existing rows.
Use local evidence pointers; do not put credentials or private payloads in a log. Existing file permissions
are preserved, so choose a private parent and file. This POSIX helper supports macOS/Linux.

## Blinded review packets

The standard-library [packet preparer](../../skills/0-skill-creator/scripts/blind-packets.py) adopts pstack's
blinding method rather than its model-specific agent orchestration. Each candidate file contains
`{"cases":[{"case_id":"one","prompt":"the same organic request","output":"reviewed response","artifacts":{"result.txt":"reviewed text"}}]}`.
A rubric file is a JSON array of three to six concrete criteria. Inputs are local reviewed exports;
do not include raw transcripts, credentials, or unrelated files.

```bash
rtk python3 skills/0-skill-creator/scripts/blind-packets.py --candidate baseline=first.json --candidate revision=second.json --rubric rubric.json --out .scratch/new-packet
```

The helper rejects unmatched cases/prompts, randomizes option labels, strips candidate metadata and case IDs,
and creates private `judge.json` and `private-map.json` files without overwriting an existing directory.
Give the judge only `judge.json`; keep the map separate. This is metadata blinding: inspect the exported
prompt/output/artifact text for identifying clues. It does not anonymize arbitrary prose or launch a judge.
Grade all options together, inspect the actual artifacts and permitted transcripts, then reveal identities.
Do not infer execution from a candidate's claim. Repetitions and a matched baseline are required before
making comparative claims; packet generation alone provides no quality evidence.

## Common checks

```bash
rtk python3 scripts/generate-workflow-guide --check
rtk python3 scripts/test-pstack-tooling.py
rtk python3 scripts/evaluate-skills validate guidelines/catalog/evals/ai-native-cases.json
```

The [daily workflow guide](./daily-workflows.md) is generated from one recipe source and existing route
metadata. Tool-specific source/adaptation hashes can be checked with `rtk python3 scripts/check-pstack-tooling`.
