# Skill creator — full guide (ops)

> Progressive disclosure from `/0-skill-creator`. **Load when** running create → eval → iterate, not for craft theory.

**Craft theory:** `/1-writing-great-skills`  
**Eval method:** [agentskills-io-evaluating-skills.md](./agentskills-io-evaluating-skills.md)  
**Trigger method:** [agentskills-io-optimizing-descriptions.md](./agentskills-io-optimizing-descriptions.md)  
**Scripts:** [agentskills-io-using-scripts.md](./agentskills-io-using-scripts.md)  
**Format + house deltas:** [agentskills-io-specification.md](./agentskills-io-specification.md)

Jump to where the user is in the loop. User may skip formal evals (“just vibe”) — still ship lean body + route surface before place.

## Core loop

```text
intent → draft SKILL.md → eval (with/without baseline) → human review → revise → (optional description opt) → place
```

| Stage | Completion criterion |
|-------|----------------------|
| Intent | Job, when-to-trigger, I/O clear (or captured from this conversation) |
| Draft | Lean body + depth-prefix name plan + description contract |
| Eval | ≥2 cases run vs baseline; feedback collected |
| Revise | Generalized fix; no one-eval overfitting |
| Place | `/0-skill-manager` Gate PASS |

---

## 1. Capture intent

If the session already did the task (“turn this into a skill”), extract steps, corrections, I/O, project facts first.

Confirm:

1. What should the agent do?
2. When should it trigger? (**leading words** / phrases)
3. Expected output shape?
4. Eval worth it? Default **yes** for objective transforms; **no** for pure style/art — user decides.

Research edge cases, samples, deps (MCPs/subagents in parallel when useful).

**Done when:** user confirms scope before drafting (unless they said draft freely).

---

## 2. Draft the body

| Piece | Rule |
|-------|------|
| `name` / dir | This catalog: `{depth}-{kebab-slug}` — [specification house deltas](./agentskills-io-specification.md) |
| `description` | What + when; pushy coverage; house: Use when / Not for / Hub + `metadata.catalog` |
| Body | Imperative **steps** with **completion criteria**; disclose reference |
| Package | `scripts/` · `references/` · `assets/` as needed |

Anatomy:

```text
skill-name/
├── SKILL.md
├── scripts/      # optional
├── references/   # optional
└── assets/       # optional
```

**Writing style (short):** prefer *why* over ALL-CAPS MUST; generalize beyond the current example; prune **no-ops**. Full craft levers → `/1-writing-great-skills`.

**Safety:** no malware, exfil, or surprise intent vs description.

**Done when:** draft exists and is lean enough to eval (or user accepts draft-only path).

---

## 3. Eval (output quality)

Method detail → [evaluating-skills](./agentskills-io-evaluating-skills.md). **Do not stop mid-sequence** once started.

### 3a. Cases

Author 2–3 realistic prompts in `evals/evals.json` (`prompt`, `expected_output`, optional `files`). Assertions empty until after first outputs. Confirm set with user.

### 3b. Workspace

Sibling to skill:

```text
skill-workspace/iteration-N/eval-<name>/{with_skill,without_skill|old_skill}/{outputs,timing.json,grading.json}
skill-workspace/iteration-N/benchmark.json
```

### 3c. Spawn (same turn)

For each case, launch **with_skill** and **baseline** together (subagents or clean sessions).

```text
Execute this task:
- Skill path: <path> | (omit for baseline)
- Task: <prompt>
- Input files: …
- Save outputs to: …/with_skill/outputs/  (or without_skill / old_skill)
```

Improving existing: `cp -r` snapshot before edit → baseline = snapshot → `old_skill/`.

Write `eval_metadata.json` per case (descriptive name, empty assertions OK).

### 3d. While running — assertions

Draft objective assertions; update `evals.json` + metadata. Explain viewer tabs to user.

### 3e. On complete — timing

Save notification `total_tokens` / `duration_ms` to `timing.json` immediately (not persisted elsewhere).

### 3f. Grade → aggregate → viewer

1. Grade → `grading.json` fields: `text`, `passed`, `evidence` (use scripts for mechanical checks).  
2. `python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>`  
3. Analyst pass: always-pass both configs, always-fail, high variance, outliers — see `agents/analyzer.md` if present.  
4. Viewer:

```bash
nohup python <skill-creator-path>/eval-viewer/generate_review.py \
  <workspace>/iteration-N \
  --skill-name "my-skill" \
  --benchmark <workspace>/iteration-N/benchmark.json \
  > /dev/null 2>&1 &
```

Iteration 2+: `--previous-workspace …`. Headless: `--static <out.html>`. **Always generate viewer before self-revising.**

5. User submits → read `feedback.json`; empty feedback = fine. Kill viewer when done.

**Done when:** human feedback in hand (or user declined review).

---

## 4. Improve

Signals: failed assertions · human feedback · **transcripts** (not only finals).

| Rule | |
|------|--|
| Generalize | Skill serves many prompts, not these 3 |
| Lean | Cut waste seen in traces |
| Why | Purpose beats rigid MUST |
| Bundle | Same helper every run → `scripts/` ([using-scripts](./agentskills-io-using-scripts.md)) |

Then: apply → new `iteration-N+1/` with baselines → viewer with `--previous-workspace` → repeat until happy / empty feedback / flat gains.

Optional **blind A/B:** `agents/comparator.md` + `agents/analyzer.md` (needs subagents).

---

## 5. Description optimization (optional)

After body is good, offer trigger optimization. **Method** → [optimizing-descriptions](./agentskills-io-optimizing-descriptions.md).

House ops when tooling present:

1. ~20 should/should-not queries → user review (`assets/eval_review.html` if available).  
2. `python -m scripts.run_loop --eval-set … --skill-path … --model <session-model> --max-iterations 5 --verbose`  
3. Apply `best_description`; sync **route surface** for this catalog.

Skip on hosts without `claude -p` / loop tooling; still apply craft rules from the method file by hand.

---

## 6. Package / place

| Action | When |
|--------|------|
| `python -m scripts.package_skill <dir>` | Host has package tooling / user wants `.skill` |
| `/0-skill-manager` place or ingest | Living in this catalog (Gate PASS) |
| Entry alias | `/1-create-skill` |

Preserve original `name`/dir when updating installed skills; copy to writable path if install tree is read-only.

---

## Environment deltas

| Host | Adapt |
|------|--------|
| **No subagents** | Serial runs; skip baseline if meaningless; qualitative review in chat |
| **No browser** | `--static` viewer or paste outputs; feedback via download/path |
| **Cowork** | Prefer static viewer; generate viewer **before** self-grade; description loop OK via subprocess after body is done |

---

## Reference map

| Load when | Path |
|-----------|------|
| Grader / comparator / analyzer agents | `agents/*.md` (if present in creator package) |
| JSON schemas | `references/schemas.md` (if present) |
| Upstream format + house | [agentskills-io-specification.md](./agentskills-io-specification.md) |
| Eval method | [agentskills-io-evaluating-skills.md](./agentskills-io-evaluating-skills.md) |
| Scripts | [agentskills-io-using-scripts.md](./agentskills-io-using-scripts.md) |
| Triggers | [agentskills-io-optimizing-descriptions.md](./agentskills-io-optimizing-descriptions.md) |
| Predictability craft | `/1-writing-great-skills` |
| Catalog mutate | `/0-skill-manager` |
