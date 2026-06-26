---
name: site-architecture
description: Plan or restructure website hierarchy, navigation, URL patterns, breadcrumbs, and internal linking. Use when mapping pages, sections, and site structure for new sites or restructuring existing ones. Not for XML sitemap auditing or schema markup.
type: Playbook
---

# Site Architecture

Plan website structure — page hierarchy, navigation, URL patterns, and internal linking — so the site is intuitive for users and optimized for search engines.

## When to Use

- Planning or restructuring page hierarchy, navigation, and URL structure
- Mapping site sections, breadcrumbs, and internal linking
- Designing information architecture for a new site
- Restructuring an existing site with SEO or usability problems

## When NOT to Use

- XML sitemap generation or schema markup implementation
- Individual page conversion optimization (use CRO skills)
- Content strategy or topic cluster planning

## Context Gathering

Before planning, gather:

1. **Business Context**: What does the company do? Who are the primary audiences? Top 3 site goals?
2. **Current State**: New or restructuring? What's broken? Existing URLs to preserve?
3. **Site Type**: SaaS marketing, content/blog, e-commerce, documentation, hybrid, small business?
4. **Content Inventory**: How many pages? Most important pages? Planned expansions?

## Site Types and Starting Points

| Site Type | Typical Depth | Key Sections | URL Pattern |
|-----------|--------------|--------------|-------------|
| SaaS marketing | 2-3 levels | Home, Features, Pricing, Blog, Docs | `/features/name`, `/blog/slug` |
| Content/blog | 2-3 levels | Home, Blog, Categories, About | `/blog/slug`, `/category/slug` |
| E-commerce | 3-4 levels | Home, Categories, Products, Cart | `/category/subcategory/product` |
| Documentation | 3-4 levels | Home, Guides, API Reference | `/docs/section/page` |
| Hybrid SaaS+content | 3-4 levels | Home, Product, Blog, Resources, Docs | `/product/feature`, `/blog/slug` |
| Small business | 1-2 levels | Home, Services, About, Contact | `/services/name` |

## Page Hierarchy Design

### The 3-Click Rule

Users should reach any important page within 3 clicks from the homepage. If critical pages are buried 4+ levels deep, restructure.

### Flat vs Deep

| Approach | Best For | Tradeoff |
|----------|----------|----------|
| Flat (2 levels) | Small sites, portfolios | Simple but doesn't scale |
| Moderate (3 levels) | Most SaaS, content sites | Good balance |
| Deep (4+ levels) | E-commerce, large docs | Scales but risks burying content |

**Rule of thumb**: Go as flat as possible while keeping navigation clean. If a nav dropdown has 20+ items, add a level of hierarchy.

### ASCII Tree Format

```
Homepage (/)
├── Features (/features)
│   ├── Analytics (/features/analytics)
│   └── Automation (/features/automation)
├── Pricing (/pricing)
├── Blog (/blog)
│   └── [Category: SEO] (/blog/category/seo)
├── Docs (/docs)
│   ├── Getting Started (/docs/getting-started)
│   └── API Reference (/docs/api)
└── About (/about)
```

## Navigation Design

### Header Navigation Rules

- **4-7 items max** in the primary nav (more causes decision paralysis)
- **CTA button** goes rightmost ("Start Free Trial", "Get Started")
- **Logo** links to homepage (left side)
- **Order by priority**: most important/visited pages first
- If you have a mega menu, limit to 3-4 columns

### Footer Organization

Group footer links into columns:
- **Product**: Features, Pricing, Integrations, Changelog
- **Resources**: Blog, Case Studies, Templates, Docs
- **Company**: About, Careers, Contact, Press
- **Legal**: Privacy, Terms, Security

### Breadcrumb Format

```
Home > Features > Analytics
Home > Blog > SEO Category > Post Title
```

Breadcrumbs should mirror the URL hierarchy. Every segment should be a clickable link except the current page.

## URL Structure

### Design Principles

1. **Readable by humans** — `/features/analytics` not `/f/a123`
2. **Hyphens, not underscores** — `/blog/seo-guide` not `/blog/seo_guide`
3. **Reflect the hierarchy** — URL path should match site structure
4. **Consistent trailing slash policy** — pick one and enforce it
5. **Lowercase always** — `/About` should redirect to `/about`
6. **Short but descriptive** — prefer `/blog/landing-page-conversions` over `/blog/how-to-improve-landing-page-conversion-rates`

### URL Patterns by Page Type

| Page Type | Pattern | Example |
|-----------|---------|---------|
| Homepage | `/` | `example.com` |
| Feature page | `/features/{name}` | `/features/analytics` |
| Blog post | `/blog/{slug}` | `/blog/seo-guide` |
| Blog category | `/blog/category/{slug}` | `/blog/category/seo` |
| Documentation | `/docs/{section}/{page}` | `/docs/api/authentication` |
| Comparison | `/vs/{competitor}` | `/vs/competitor-name` |
| Integration | `/integrations/{name}` | `/integrations/slack` |

### Common URL Mistakes

- **Dates in blog URLs** — `/blog/2024/01/15/post-title` adds no value. Use `/blog/post-title`.
- **Over-nesting** — `/products/category/subcategory/item/detail` is too deep.
- **Changing URLs without redirects** — Every old URL needs a 301 redirect.
- **IDs in URLs** — `/product/12345` is not human-readable. Use slugs.
- **Query parameters for content** — `/blog?id=123` should be `/blog/post-title`.

## Internal Linking Strategy

### Rules

1. **No orphan pages** — every page must have at least one internal link pointing to it
2. **Descriptive anchor text** — "our analytics features" not "click here"
3. **5-10 internal links per 1000 words** of content (approximate guideline)
4. **Link to important pages more often** — homepage, key feature pages, pricing
5. **Use breadcrumbs** — free internal links on every page
6. **Related content sections** — "Related Posts" at page bottom

### Hub-and-Spoke Model

For content-heavy sites, organize around hub pages:

```
Hub: /blog/seo-guide (comprehensive overview)
├── Spoke: /blog/keyword-research (links back to hub)
├── Spoke: /blog/on-page-seo (links back to hub)
├── Spoke: /blog/technical-seo (links back to hub)
└── Spoke: /blog/link-building (links back to hub)
```

Each spoke links back to the hub. The hub links to all spokes.

## Output Format

When creating a site architecture plan, provide:

1. **Page Hierarchy** (ASCII Tree) — Full site structure with URLs at each node
2. **Visual Sitemap** (Mermaid) — `graph TD` diagram with navigation zones
3. **URL Map Table** — Page, URL, Parent, Nav Location, Priority
4. **Navigation Spec** — Header nav items, footer sections, sidebar, breadcrumbs
5. **Internal Linking Plan** — Hub pages and spokes, cross-section links, orphan audit

## Verification

- [ ] Every page reachable within 3 clicks from homepage
- [ ] No orphan pages (all have at least one inbound internal link)
- [ ] URL patterns are consistent across the site
- [ ] Breadcrumbs mirror URL hierarchy
- [ ] All old URLs have 301 redirects (if restructuring)
- [ ] Navigation has 4-7 items max in primary nav
