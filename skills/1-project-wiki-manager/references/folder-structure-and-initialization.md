# Folder Structure and Session Initialization

## Purpose and Rationale
A consistent, predictable folder layout enables reliable automation, easy navigation, and long-term maintainability of the knowledge base. By isolating raw immutable sources from the editable wiki, the system prevents accidental corruption while allowing the wiki to evolve as a synthesized, interlinked view. This separation also makes it trivial to re-ingest updated sources or audit lineage.

The design deliberately avoids any assumptions about or interaction with source code, binaries, or implementation folders. The wiki serves any knowledge domain — product planning, 1-research notes, operational procedures, meeting outcomes, or technical concepts — as long as raw materials can be placed in `docs/raw/`.

## Standard Folder Layout
```
{project-root}/
├── docs/
│   ├── raw/                  # Immutable raw sources (PDF, MD, TXT, images, etc.)
│   │   └── (user places new files here)
│   └── wiki/                 # Editable knowledge base (Markdown only)
│       ├── index.md          # Categorized table of contents
│       ├── log.md            # Append-only operation history with sentinel
│       └── *.md              # All other pages (concept summaries, source digests, etc.)
```

- `{project-root}` is the directory that directly contains the `docs/` folder.
- `docs/raw/` holds originals exactly as provided. The agent **never** writes here.
- `docs/wiki/` contains only `.md` files. No subdirectories except by explicit future proposal and user approval.
- All paths are relative to the confirmed project root.

## Session Initialization Workflow (Mandatory Every Session)
At the very beginning of any interaction involving this skill:

1. **Resolve the project root**
   - Search upward from the current working directory for a folder containing `docs/`.
   - If multiple candidates exist, list them and ask the user to confirm the correct `{project-root}`.
   - If no `docs/` exists yet, propose creating `docs/raw/` and `docs/wiki/` under the current or a user-specified directory. Wait for explicit confirmation before creating anything.

2. **Verify wiki and raw directories**
   - Confirm `docs/raw/` and `docs/wiki/` exist.
   - If either is missing, offer to initialize them with the minimal skeleton:
     - `docs/raw/` (empty or with a README explaining its purpose)
     - `docs/wiki/index.md` (starter categorized table)
     - `docs/wiki/log.md` (with initial entry and `<!-- END OF LOG -->` sentinel)
   - Never proceed to modifications until the user approves the layout.

3. **State the resolved environment clearly**
   - Example output: "Resolved project root: /home/user/my-project. Wiki located at docs/wiki/. Raw sources at docs/raw/. Ready for operations."
   - Ask: "Is this the correct project? Shall I proceed with the current wiki state or initialize a fresh structure?"

4. **Load current wiki state (lightweight)**
   - Read `docs/wiki/index.md` to understand existing categories and pages.
   - Check for presence of `log.md` and its sentinel.
   - Do **not** read every page unless the task requires it (progressive disclosure).

## Nuances and Edge Cases
- **Multiple docs/ folders:** Always surface the choice to the user. Never guess.
- **Wiki already contains content:** Respect it. Never overwrite index.md or log.md without logging the action and user awareness.
- **User wants a different structure:** Record the request, propose a migration plan in the log, but do not execute until confirmed. The default layout is strongly recommended for interoperability with future tools.
- **Non-English raw sources:** Process them into English wiki content while preserving key original terms or quotes for traceability (see citation rules).
- **Large or binary raw files:** Use available tools (read_file for text/images, or appropriate document tools) to extract text. For very large files, focus first on table of contents, executive summary, and key sections; discuss findings with user before full synthesis.
- **Implications of poor initialization:** Skipping confirmation leads to writing in the wrong location, broken links later, or duplicate wikis. Always confirm.

## Why This Matters
A clean initialization prevents "wiki sprawl," ensures every new page is discoverable via index.md, and creates an auditable history from day one. It also signals to the user that the agent treats their knowledge assets with care and discipline.