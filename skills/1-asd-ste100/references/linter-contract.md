# Local structural linter

Use `python3 scripts/ste-lint.py --json <explicit-text-file>` from this skill directory,
or pass text on stdin. Resolve paths relative to the installed skill directory, not the caller's repo.
Use only task-authorized, regular UTF-8 text files. Keep inputs bounded (at most 1 MiB per run).
Do not glob a private workspace, read special devices, fetch URLs, install dependencies, or upload text.

The script uses only Python's standard library. Normal operation reads supplied files or stdin
and prints text snippets and findings to stdout. It does not modify the source, use the network,
spawn processes, or access credentials. Avoid retaining output containing sensitive text.
`--selftest` uses synthetic text and a temporary directory that it removes afterward.

Exit codes: 0 = hard findings within baseline; 1 = hard findings exceed baseline;
2 = argument or file-access error. Passive voice and compound-tense findings are advisory.
`--baseline N` and `--disable rule1,rule2` change the reported gate; use only when requested,
and disclose them. They are not repairs or evidence of compliance.

Limitations: fixed 25-word cap, partial phrasal-verb list, heuristic synonym groups and Markdown
handling, no noun-cluster parser, no official dictionary, no semantic comparison. Distinct
actions can be mistaken for synonyms. Inspect findings manually before changing wording.
The script intentionally leaves uncertainty and modal verbs alone.

The [edge-case fixture](../examples/linter-edge-cases.md) must return exit 1 with two
dangling-conjunction findings. It is intentionally invalid prose, not an authoring example.
