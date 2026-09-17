# Office extraction and internal-communication wiring audit

Reviewed:

- `skills/1-defuddle/SKILL.md` and its source-provenance reference
- `skills/1-internal-comms/SKILL.md` and its vendor-provenance reference
- `0-office`, adjacent Research, Vault, Brand, PR-writing, document, presentation, browser, and Incident routes
- official `kepano/defuddle` CLI documentation retrieved 2026-09-12

## Result

Defuddle now owns one immutable supplied URL or local HTML snapshot and returns one clean Markdown result.
It pins caller, source/as-of, output mode and destination, requested fields, rights/privacy, network/read/write
authority, and exact repository/worktree identity only when local files are involved. HTML and extracted content
are sensitive untrusted data; links and page instructions cannot authorize more reads or execution. The leaf
does not install software, auto-download through `npx`, bypass access controls, run a browser, crawl, research,
summarize, ingest, or publish. Its old nonexistent `1-defuddle` package/executable recipe was corrected to the
official `defuddle` CLI interface, with runtime help/version observation required. Output verification separates
successful extraction from factual correctness and full-page coverage.

Internal Communications now owns one evidence-cutoff-bound draft for one internal audience, purpose, channel,
and delivery context. It pins classification, terminology/template, owner, facts and source revisions, result
destination, and write/publication authority; treats all source material as sensitive untrusted data; labels
facts, estimates, assumptions, risks, and requests; and returns gaps rather than inventing impact, status,
metrics, dates, commitments, approvals, recipients, or update times. “Internal” never means unrestricted.
Incident operation, external brand copy, PR prose, DOCX/PPTX conversion, shared-document editing, sending,
scheduling, and publication remain separately selected and authorized work.

Both leaves return their result, provenance, coverage, verification, effects, and limits to `0-office` or the
actual caller. They create no worktree and distinguish repository isolation from shared network, account,
browser, messaging, document, recipient, and URL state.

## Verification

- Focused Office text-leaf routing tests: 7 passed.
- Full routing suite: 534 passed.
- Generated route index: 223 live skills.
- Catalog lint: 0 critical, 0 warnings, 50 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

No web page was extracted, communication drafted or sent, file created outside the catalog, package installed,
worktree created, host sync run, Git history changed, or external system mutated.
