---
name: 0-marketing
description: 'Route one marketing request to the narrowest strategy, research, conversion, content, SEO, distribution, measurement, lifecycle, or sales specialist. Use when: marketing work spans several channels or no direct marketing child is obvious. Not for: a clearly matched child or non-marketing work. Hub: /0-marketing.

  '
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-marketing
    role: hub
    when: [marketing work spans multiple specialties, the correct marketing specialist is unclear]
    not_when: [one marketing child directly matches → use it, non-marketing request → 0-butler]
    prev: [0-butler]
    next: [0-butler, 1-marketing-ab-testing, 1-marketing-ad-creative, 1-marketing-ads, 1-marketing-ai-seo, 1-marketing-analytics, 1-marketing-aso, 1-marketing-attribution, 1-marketing-blog-editor, 1-marketing-churn-prevention, 1-marketing-co-marketing, 1-marketing-cold-email, 1-marketing-community-marketing, 1-marketing-competitor-profiling, 1-marketing-competitors, 1-marketing-content-strategy, 1-marketing-copy-editing, 1-marketing-copywriting, 1-marketing-cro, 1-marketing-customer-research, 1-marketing-directory-submissions, 1-marketing-emails, 1-marketing-events, 1-marketing-free-tools, 1-marketing-image, 1-marketing-influencer-marketing, 1-marketing-launch, 1-marketing-lead-magnets, 1-marketing-marketing-council, 1-marketing-marketing-ideas, 1-marketing-marketing-loops, 1-marketing-marketing-plan, 1-marketing-marketing-psychology, 1-marketing-offers, 1-marketing-onboarding, 1-marketing-paywalls, 1-marketing-popups, 1-marketing-pricing, 1-marketing-product-marketing, 1-marketing-programmatic-seo, 1-marketing-prospecting, 1-marketing-public-relations, 1-marketing-referrals, 1-marketing-revops, 1-marketing-sales-enablement, 1-marketing-schema, 1-marketing-seo-audit, 1-marketing-signup, 1-marketing-site-architecture, 1-marketing-sms, 1-marketing-social, 1-marketing-video]
    cousins: [1-brand, 1-user-research, 1-strategic-analysis, 1-competitive-analysis]
    triggers: [marketing, growth marketing, go to market, marketing strategy, which marketing skill]
    requires_setup: false
  vendor:
    source: coreyhaines31/marketingskills
    commit: 5b2c0007766c6a1cf1d53fd8fc73e979e0821022
    license: MIT
---


# Marketing

Route one marketing job to one specialist. The hub does not publish, send, submit, spend, change live accounts, use credentials, or run campaigns.

## Category map

| Need | Use |
|---|---|
| Foundation and strategy | `/1-marketing-product-marketing`, `/1-marketing-marketing-plan`, `/1-marketing-marketing-ideas`, `/1-marketing-marketing-council`, `/1-marketing-marketing-psychology`, `/1-marketing-offers`, `/1-marketing-pricing` |
| Research and positioning | `/1-marketing-customer-research`, `/1-marketing-competitor-profiling`, `/1-marketing-competitors` |
| Conversion and lifecycle | `/1-marketing-cro`, `/1-marketing-signup`, `/1-marketing-onboarding`, `/1-marketing-popups`, `/1-marketing-paywalls`, `/1-marketing-churn-prevention`, `/1-marketing-ab-testing` |
| Content and messaging | `/1-marketing-content-strategy`, `/1-marketing-copywriting`, `/1-marketing-copy-editing`, `/1-marketing-emails`, `/1-marketing-cold-email`, `/1-marketing-sms`, `/1-marketing-social`, `/1-marketing-video`, `/1-marketing-image`, `/1-marketing-lead-magnets` |
| Search and discovery | `/1-marketing-seo-audit`, `/1-marketing-ai-seo`, `/1-marketing-programmatic-seo`, `/1-marketing-site-architecture`, `/1-marketing-schema`, `/1-marketing-aso`, `/1-marketing-directory-submissions` |
| Paid and measurement | `/1-marketing-ads`, `/1-marketing-ad-creative`, `/1-marketing-analytics`, `/1-marketing-attribution` |
| Growth, partnerships, and sales | `/1-marketing-co-marketing`, `/1-marketing-community-marketing`, `/1-marketing-events`, `/1-marketing-free-tools`, `/1-marketing-influencer-marketing`, `/1-marketing-launch`, `/1-marketing-marketing-loops`, `/1-marketing-prospecting`, `/1-marketing-public-relations`, `/1-marketing-referrals`, `/1-marketing-revops`, `/1-marketing-sales-enablement` |

## Boundary

| Need | Route |
|---|---|
| Marketing orientation | **this hub** |
| Product/UX research | `/1-user-research` |
| General strategy or competitive analysis | `/1-strategic-analysis` or `/1-competitive-analysis` |
| Brand system | `/1-brand` |
| Software delivery or release | `/0-implement` or `/1-shipping-and-launch` |
| Non-marketing work | `/0-butler` |

## Process

1. Pin the marketing outcome, audience, product, supplied evidence, jurisdiction, live-account state, and authority.
2. Use the category map and route index to select one direct child. Ask F-M1 only when two categories would materially change the deliverable.
3. Validate the chosen live `SKILL.md`; prefer the narrowest child over running this hub first.
4. Return the route and first action. Do not execute the child or infer authority for external effects.

## Fork F-M1

**Which marketing outcome is primary?** Recommend the narrowest evidence-backed category; options are strategy/research, conversion/lifecycle, content/messaging, search/discovery, paid/measurement, growth/partnerships/sales, or **Agent judgment**.

## Source and constraints

The children adapt the pinned MIT-licensed MarketingSkills snapshot documented in [the ingest record](../../guidelines/catalog/marketingskills-ingest.md). Upstream tool adapters, installers, plugin metadata, and live-effect permissions were not promoted.

Return: `/0-butler`.

## Available specialist additions

- `/1-marketing-blog-editor` — use for its scoped contract; return to this hub.
