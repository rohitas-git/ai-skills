---
name: 1-marketing-ecommerce-blog-writing
description: >
  Draft or revise one e-commerce blog that answers a shopper question and connects useful education
  to relevant products. Use when: buyer's guides, product comparisons, product tutorials, or lifestyle
  articles need storytelling, SEO, natural product placement, and a funnel-matched CTA. Not for:
  healthcare blogs, technical-blog review, product-page copy, editorial calendars, or publishing.
  Hub: /0-marketing.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-marketing
    role: leaf
    when: ["draft or revise one e-commerce blog for shoppers"]
    not_when:
      - "healthcare or medical product blog → 1-marketing-healthcare-blog-writing"
      - "editorial roadmap → 1-marketing-content-strategy"
      - "product page or landing page → 1-marketing-copywriting"
      - "existing technical-blog review → 1-marketing-blog-editor"
    prev: [0-marketing]
    next: [0-marketing]
    cousins: [1-marketing-healthcare-blog-writing, 1-marketing-copywriting, 1-marketing-blog-editor, 1-marketing-content-strategy]
    triggers: ["e-commerce blog", "ecommerce blog writing", "buyer's guide", "shopping comparison", "product tutorial", "shoppable lifestyle article"]
    requires_setup: false
---

# E-commerce Blog Writing

Create one useful shopping article that earns the next action through clear advice, credible examples,
and relevant products. Return a draft and its source notes; publication is a separate operation.

## Boundary

| Need | Use |
|---|---|
| One shopper-facing guide, tutorial, lifestyle post, or comparison | **this skill** |
| Healthcare, supplement, or medical-device blog | `/1-marketing-healthcare-blog-writing` |
| Topic portfolio, calendar, or content pillars | `/1-marketing-content-strategy` |
| Landing page or product-page copy | `/1-marketing-copywriting` |
| Review an existing technical marketing blog | `/1-marketing-blog-editor` |
| Sitewide search audit or AI-search strategy | `/1-marketing-seo-audit` or `/1-marketing-ai-seo` |

## Process

1. Pin the reader, question, store, product/category, format, funnel stage, brand voice, source material,
   target query, intended next action, and requested output destination. Read existing brand/product context
   when available. Ask only for missing facts that materially change the article; otherwise state assumptions.
2. Read [the writing playbook](./references/writing-playbook.md). Choose one topic from real shopper questions,
   objections, support themes, or verified search evidence. Treat inferred demand as a hypothesis; never
   invent customer quotes, search volume, product tests, or firsthand experience.
3. Gather current product facts and useful source evidence. Verify specifications, prices, availability,
   instructions, and destination links when they appear in the article. Mark missing facts or omit them.
   Use anonymized support themes; remove personal information before research or quotation.
4. Choose the format that answers the question, sketch the reader's path, and draft a specific headline.
   Explain the benefit early. Build descriptive H2/H3 sections around decisions or tasks rather than keyword
   variations. Honor a requested length; otherwise write only as much as the question needs.
5. Write with concrete examples and the storefront's voice. Place products where their verified features
   solve the problem being discussed. Include fit limits, alternatives, and trade-offs when material.
6. Add one primary CTA matched to intent. Suggest images/video where they explain use, fit, or differences;
   provide placement and alt-text guidance using known facts. Request actual assets when needed.
7. Check that the headline promise is fulfilled, links and claims have support, comparisons use consistent
   criteria, product placement feels earned, and the CTA follows naturally. Identify anything still unverified.

## Deliverable

- Brief: audience, question, chosen format, search intent, funnel stage, primary query, and assumptions.
- Article: H1, opening, structured body, useful product links, and primary CTA; add FAQs only if useful.
- Search package: proposed slug, concise meta title and description, and relevant internal-link suggestions.
- Visual brief: placements, assets needed, and descriptive alt text; distinguish proposed from existing assets.
- Source notes: verified product facts, research links, comparison/test provenance, and unresolved checks.

Return only the requested stage for an outline-only or revision-only request. Do not force a full article bundle
when the user asked for a smaller artifact. Return to `/0-marketing` or the actual caller.
