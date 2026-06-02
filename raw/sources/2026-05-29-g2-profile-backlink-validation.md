---
source_url: https://g2.com/
canonical_url: https://www.g2.com/
ingested: 2026-05-29
ingested_by: agent-alpha
source_type: article
category: uncategorized
credibility_tier: primary
evidence_grade: medium
context: "Historical Tolaria backfill from ledger: validate whether G2 allows a company/profile listing with website link and whether it is relevant to DR/backlink building. first_seen=2026-05-14T16:21:53.653437; session_file=/home/admin/.hermes/profiles/agent-alpha/sessions/session_20260514_162153_6f9108.json"
---

# G2 profile backlink validation

## Original request

Inspect https://www.g2.com/ as a candidate backlink/source mentioned in the image. Determine whether the claim "create company profile + link site" is real, whether it is relevant to DR/backlink building.

## Fetch notes

- Primary URL: https://www.g2.com/
- Canonical URL used: https://www.g2.com/
- Direct HTTP fetch of the homepage returned a DataDome/anti-bot page: status 403, title `g2.com`, message `Please enable JS and disable any ad blocker`.
- Browser navigation reached the same DataDome device-check page.
- Because the homepage was bot-blocked, Alpha inspected G2-owned public documentation and the Sell.G2 profile landing page.

## Related links inspected

- https://sell.g2.com/create-a-profile — G2-owned landing page for creating/claiming a G2 product profile.
- https://documentation.g2.com/help/docs/finding-or-listing-a-product-on-g2 — G2 help article describing product submission and profile claiming.
- https://documentation.g2.com/docs/product-information — G2 documentation for managing profile information; mentions product and company website URLs on G2 and UTM parameters.
- https://documentation.g2.com/docs/get-started-with-g2 — G2 onboarding documentation for product profile setup, reviews, buyer intent, and leads.

## Captured evidence

### G2 create-profile page

From `https://sell.g2.com/create-a-profile`:

> Your G2 Profile It all starts with a profile. A search. Some words in a web browser. A few clicks. And millions of people landing on G2 to find software or services just like yours. 86% of software buyers, across segments, use peer review sites when buying software.

> Create your product profile so you can gather reviews, build your brand, use customer content for campaigns, and leverage buyer intent data to drive quality pipeline.

> My product or service isn’t on G2. Follow these steps to get going: 1. We have one of those request forms everyone loves—but this one’s actually worth it. After submitting yours, your product or service will be conditionally approved. ... Our G2 research team verifies your product or service—in about 3-5 business days—before placing it in the right category. ... 2. Once you’ve submitted the request form, your profile is live on our site and ready to be claimed. 3. Head on over to your profile, and claim your G2 listing so that you can make any necessary updates. After submitting your claim request, our team will review your submission for final approval within 1-3 business days.

### G2 finding/listing documentation

From `https://documentation.g2.com/help/docs/finding-or-listing-a-product-on-g2`:

> G2 does not accept business-to-consumer (B2C) products or products that are currently in the alpha or beta stage of development.

> To add a product: Fill out the Product Submission Form. G2’s research team will verify eligibility and categorization. Once approved, claim your profile to manage your listing.

> Once your G2 Profile is approved, you must claim your listing to customize it and add your branding. To claim a G2 profile: Navigate to the G2 profile. Hover over Unclaimed, then select Claim this profile. After you submit a claim request, G2 will review it and provide final approval within 1–3 business days.

### G2 product-information documentation

From `https://documentation.g2.com/docs/product-information`:

> The Product Information tab enables you to showcase your brand and manage information about your product.

> Managing your product information in my.G2 You can customize your product’s profile assets by going to my.G2, then navigate to Product Profile > Product Information.

> UTM Params Use the UTM Params section to set UTM parameters for your product and company website URLs on G2, enabling you to easily track direct referral traffic from G2 in your third-party analytics software.

This confirms G2 profiles can include URLs to the product/company website, at least as outbound referral links with G2-added/tracked UTM parameters.

### G2 get-started documentation

From `https://documentation.g2.com/docs/get-started-with-g2`:

> Set up your G2 product profile Build your product profile to showcase your product to G2 buyers. The more complete and informative each section of your profile is, the more context buyers have about your product and how it can solve their specific software needs.

> A complete product profile includes information about your product’s values and ethics, packages and pricing, and multimedia content such as screenshots and videos that show your product in action.

## Assessment

- Claim status: partly real.
- G2 does allow product/service profile submission, approval, claiming, and profile management.
- G2 documentation confirms product/company website URLs exist on G2 profiles and can carry UTM tracking for direct referral traffic.
- This is not an arbitrary "create a company profile for any website" directory. G2 limits listings to eligible products/services, excludes B2C and alpha/beta products, and requires G2 research review/approval.
- DR/backlink relevance: limited and conditional. A legitimate G2 listing can be useful for brand/entity trust, referral traffic, review/social proof, and possibly a citation/backlink from a high-authority review platform. It should not be treated as a simple guaranteed DR hack, because eligibility/review gates apply and the SEO value of outbound links was not verified from live profile HTML due G2 anti-bot blocking.

## Classification

- Actionability: archive_only / no_action.
- Useful if the operator has a real B2B software/service that belongs on G2.
- Not useful as a generic backlink-building tactic without a legitimate eligible product/service and customer-review strategy.

## Open questions

- Live profile HTML was not fetched because `www.g2.com` was blocked by DataDome; therefore exact `rel` attributes (`nofollow`, `sponsored`, redirect behavior) were not verified.
- If a future SEO audit needs exact link equity evidence, inspect a real G2 product profile through a browser session or third-party crawler that can render the profile and check the outbound website link attributes.
