# Resource Summarizer return contract

Use `/1-resource-summarizer` as a separate read-only leaf only when faithful ingest needs
source-level compression or explicit coverage mapping. Length alone is not a gate.

Pass the exact source snapshot/version, acquired and missing content, ingest question,
desired form/locators, privacy limits, caller `/1-vault-ingest`, and no vault-write authority.

Require source identity, observed coverage, source-attributed claims/evidence/disagreement/
limitations, separately labeled transformations/inference, locators, and extraction gaps.

On return, pin the same source snapshot before reconciliation. The summary is evidence—not
canonical truth, a write plan, or permission to discard existing notes. If the material is
already bounded and directly usable, proceed without this leaf and record that decision.
