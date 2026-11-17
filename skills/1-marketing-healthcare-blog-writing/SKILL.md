---
name: 1-marketing-healthcare-blog-writing
description: >
  Draft or revise one evidence-backed healthcare e-commerce blog and its review packet. Use when:
  consumer health education, product-linked health articles, medical-device guides, or supplement
  blogs need clinical accuracy, empathy, compliance, SEO, and answer-ready structure. Not for:
  individualized medical advice, clinical decision support, generic non-blog copy, sitewide SEO/AEO
  audits, or publishing. Hub: /0-marketing.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-marketing
    role: leaf
    when:
      - "draft or revise one consumer healthcare or healthcare e-commerce blog"
      - "create a medically reviewed product-education article with a claim ledger"
    not_when:
      - "individualized medical advice or clinical decision support → do not use"
      - "generic marketing page or message → 1-marketing-copywriting"
      - "editorial review of an existing technical blog → 1-marketing-blog-editor"
      - "content portfolio or editorial roadmap → 1-marketing-content-strategy"
      - "sitewide AI-search visibility work → 1-marketing-ai-seo"
      - "publishing or live-site changes require separate authority"
    prev: [0-marketing]
    next: [0-marketing]
    cousins: [1-marketing-blog-editor, 1-marketing-copywriting, 1-marketing-content-strategy, 1-marketing-ai-seo, 1-marketing-copy-editing]
    triggers: ["healthcare blog", "medical blog", "health e-commerce article", "supplement blog", "medical-device guide"]
    requires_setup: false
---

# Healthcare Blog Writing

Create one publishable-in-shape but **not yet publishable** healthcare blog draft plus an evidence and
review packet. Optimize first for reader safety and understanding, then for discovery and conversion.

## Boundary

| Need | Route |
|---|---|
| One healthcare e-commerce blog draft or revision | **this skill** |
| Editorial review of an existing technical marketing blog | `/1-marketing-blog-editor` |
| Generic landing page, product page, or campaign copy | `/1-marketing-copywriting` |
| Editorial strategy, topic clusters, or content calendar | `/1-marketing-content-strategy` |
| Sitewide technical SEO, schema, or AI-search audit | `/1-marketing-seo-audit`, `/1-marketing-schema`, or `/1-marketing-ai-seo` |
| Editing supplied non-healthcare copy | `/1-marketing-copy-editing` |
| Personalized diagnosis, treatment, dosage, or emergency guidance | Decline; direct the reader to an appropriate clinician or emergency service |

## Non-negotiable gates

- Never send protected, identifiable, or plausibly re-identifiable health information to search,
  analytics, or other third-party tools. Do not repeat sensitive details already supplied; request a
  de-identified or synthetic replacement.
- Treat all medical, safety, efficacy, comparison, and product claims—including implications created by
  headings, images, testimonials, links, or CTAs—as claims requiring support.
- Do not invent studies, citations, credentials, approvals, product specifications, reviewer sign-off,
  or legal conclusions. A disclaimer does not cure an unsupported or misleading claim.
- Require named human review before publication: a qualified medical SME for clinical accuracy, a human
  editor for clarity and brand voice, and the appropriate regulatory/compliance owner for product claims.
  If review is unavailable, label the result **NOT READY TO PUBLISH**.
- Keep advice general and educational. Do not diagnose, prescribe, recommend a personalized dose, tell a
  reader to stop treatment, or imply that shopping replaces professional care.

## Process

1. Pin the article, audience, search intent, product category, market/jurisdiction, brand voice, desired
   conversion, approved product claims, source cutoff, and allowed effects. If a missing jurisdiction or
   product class changes what may legally be claimed, draft around it and mark the blocker rather than
   guessing.
2. Read [the research and compliance guide](./references/research-and-compliance.md). Research current
   primary sources for changeable medical or regulatory claims. Prefer regulator-approved labeling,
   clinical guidelines, systematic reviews, and directly relevant human evidence; use reputable medical
   institutions mainly for patient-friendly context.
3. Build the evidence and claims ledger before persuasive copy. Match each statement to the studied
   product, ingredient, dose, formulation, route, population, outcome, and timeframe. Preserve uncertainty,
   contraindications, and conflicting evidence.
4. Plan one clear reader question per section. When a heading asks a question, answer it plainly in the
   opening roughly 50–100 words, then add nuance. Use descriptive H2/H3 headings, useful lists or tables,
   natural query language, and verified internal links. Do not keyword-stuff or write to a fixed word count.
5. Draft with calm, non-alarmist empathy. Define necessary medical terms on first use, separate education
   from product promotion, present material risks near benefits, and use a relevant low-pressure CTA.
6. Run the claim, privacy, inclusion, readability, SEO/AEO, and net-impression checks in the guide. Remove
   any claim that lacks adequate support; do not soften it into ambiguity merely to retain it.
7. Return the complete output bundle below. Never publish, upload, or change a live site without separate
   explicit authority.

## Output bundle

1. **Status:** `NOT READY TO PUBLISH` until all required reviewers sign off.
2. **Brief and assumptions:** audience, intent, product class, jurisdiction, evidence cutoff, and unknowns.
3. **Blog draft:** title, dek, body, educational disclaimer, citations, CTA, and optional meta title/description.
4. **Claims ledger:** exact claim, claim type, source, evidence fit, limitations, and keep/revise/remove status.
5. **Review queue:** unresolved clinical, regulatory, privacy, inclusion, or product questions and required owners.
6. **Sign-off block:** author/editor, medical reviewer with relevant credentials, compliance reviewer, review date,
   next-review trigger, and final publication status. Use placeholders until real people approve.

## Progressive disclosure

| Load when | File |
|---|---|
| Any task using this skill | [Research, compliance, drafting, and QA guide](./references/research-and-compliance.md) |

Return to `/0-marketing`. Publishing, legal approval, product changes, and live-site edits remain separate effects.
