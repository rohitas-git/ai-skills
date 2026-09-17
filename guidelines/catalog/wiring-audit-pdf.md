# PDF wiring audit

Reviewed:

- `skills/1-pdf/SKILL.md`, OpenAI entry, processing-record template, and all three references
- complete `scripts/inspect_pdf.py`
- Office parent and adjacent DOCX, PPTX, and spreadsheet routes

## Result

PDF now performs exactly one requested PDF operation on one immutable, hash-identified source set and
returns one verified output set. It pins caller, source order and page labels, operation, acceptance criteria,
destination, fidelity/accessibility/archive/print priorities, confidentiality, trust/encryption/signature state,
credential channel, overwrite/cleanup/publication rules, and read/write authority. Repository-bound work also
carries the exact repository/worktree/branch/`HEAD`, dirty ownership, allowed paths, and working-tree versus
committed state; worktree isolation is not misrepresented as viewer, parser, font, credential, cloud, account,
or destination isolation.

PDF content and active features are sensitive untrusted data. Raw byte inspection precedes deep parsing of
untrusted inputs; deep parse/render requires a verified disposable no-secret/no-network sandbox, and the
inspector's confirmation flag is correctly described as an operator assertion rather than proof. Sources are
preserved, final writes are revision/collision/containment checked, and implicit tool installation is prohibited.
Extraction, OCR, correction, true redaction, encryption, signing, conversion, and publication stay distinct.
Signing and overwrite require target-specific authority; redaction requires full rewrite/object-history removal
and independent checks. Verification is operation-proportional and does not present OCR, visual review, or a
successful parse as legal/factual accuracy.

Partial results are reported without blind retry, cleanup, recall, replacement, or distribution. The imported
broad vendor workflow is provenance only, the OpenAI entry uses the live `$1-pdf` ID, and the actual caller gets
source/output hashes, mapping, versions, verification scope, effects, residual risks, and untested features.

## Verification

- Focused PDF routing and inspector tests: 7 passed.
- Full routing suite: 541 passed.
- Generated route index: 223 live skills.
- Catalog lint: 0 critical, 0 warnings, 50 informational findings, 0 hub-member orphans.
- `git diff --check`: passed.

The raw-inspector test used a disposable synthetic byte fixture and proved source preservation plus output-alias
refusal. No user PDF was opened or changed; no parser/viewer was launched; and no worktree, package, publication,
host sync, Git history, or remote system was changed.
