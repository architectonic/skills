---
name: ai-seo
description: Optimize content for AI search and LLM citations across AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and similar systems. Covers AI visibility audit, three-pillar optimization strategy (structure/authority/presence), and monitoring.
tags: [productivity, seo, ai-search, llm-citations, geo, aeo, content-optimization]
domain: business
risk_level: low
requires_review: false
source: antigravity-awesome-skills / coreyhaines31 marketingskills
source_status: adapted-origin-unverified
review_notes: Low-risk marketing and content-structure reference; statistics and platform behavior should be refreshed before client-facing strategic use because AI search surfaces change quickly.
type: Reference
---

# AI SEO

Optimize content for AI search and LLM citations across AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and similar systems.

## When to Use

- Optimizing content to be cited by LLMs and AI search systems
- User asks about AI SEO, AEO, GEO, LLM visibility, or AI citations
- Traditional SEO alone is not the full question and AI-specific discoverability matters

## How AI Search Works

| Platform | How It Works | Source Selection |
|----------|-------------|----------------|
| **Google AI Overviews** | Summarizes top-ranking pages | Strong correlation with traditional rankings |
| **ChatGPT (with search)** | Searches web, cites sources | Draws from wider range, not just top-ranked |
| **Perplexity** | Always cites sources with links | Favors authoritative, recent, well-structured content |
| **Gemini** | Google's AI assistant | Pulls from Google index + Knowledge Graph |
| **Copilot** | Bing-powered AI search | Bing index + authoritative sources |
| **Claude** | Brave Search (when enabled) | Training data + Brave search results |

### Key Difference from Traditional SEO

Traditional SEO gets you ranked. AI SEO gets you **cited**.

In traditional search, you need to rank on page 1. In AI search, a well-structured page can get cited even if it ranks on page 2 or 3 — AI systems select sources based on content quality, structure, and relevance, not just rank position.

**Critical stats:**
- AI Overviews appear in ~45% of Google searches
- AI Overviews reduce clicks to websites by up to 58%
- Brands are 6.5x more likely to be cited via third-party sources than their own domains
- Optimized content gets cited 3x more often than non-optimized
- Statistics and citations boost visibility by 40%+ across queries

## AI Visibility Audit

### Step 1: Check AI Answers for Key Queries

Test 10-20 of your most important queries across platforms. Query types to test:
- "What is [your product category]?"
- "Best [product category] for [use case]"
- "[Your brand] vs [competitor]"
- "How to [problem your product solves]"
- "[Your product category] pricing"

### Step 2: Content Extractability Check

For each priority page, verify:
- Clear definition in first paragraph
- Self-contained answer blocks (work without surrounding context)
- Statistics with sources cited
- Comparison tables for "[X] vs [Y]" queries
- FAQ section with natural-language questions
- Schema markup (FAQ, HowTo, Article, Product)
- Expert attribution (author name, credentials)
- Recently updated (within 6 months)
- Heading structure matches query patterns
- AI bots allowed in robots.txt

### Step 3: AI Bot Access Check

Verify your robots.txt allows AI crawlers:
- **GPTBot** and **ChatGPT-User** — OpenAI (ChatGPT)
- **PerplexityBot** — Perplexity
- **ClaudeBot** and **anthropic-ai** — Anthropic (Claude)
- **Google-Extended** — Google Gemini and AI Overviews
- **Bingbot** — Microsoft Copilot (via Bing)

## Optimization Strategy: The Three Pillars

### Pillar 1: Structure — Make Content Extractable

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

**Content block patterns:**
- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X" queries
- **Comparison tables** for "X vs Y" queries
- **Pros/cons blocks** for evaluation queries
- **FAQ blocks** for common questions
- **Statistic blocks** with cited sources

**Structural rules:**
- Lead every section with a direct answer (don't bury it)
- Keep key answer passages to 40-60 words (optimal for snippet extraction)
- Use H2/H3 headings that match how people phrase queries
- Tables beat prose for comparison content
- Numbered lists beat paragraphs for process content

### Pillar 2: Authority — Make Content Citable

**The Princeton GEO research** (KDD 2024) ranked 9 optimization methods:

| Method | Visibility Boost | How to Apply |
|--------|:----------------:|--------------|
| **Cite sources** | +40% | Add authoritative references with links |
| **Add statistics** | +37% | Include specific numbers with sources |
| **Add quotations** | +30% | Expert quotes with name and title |
| **Authoritative tone** | +25% | Write with demonstrated expertise |
| **Improve clarity** | +20% | Simplify complex concepts |
| **Technical terms** | +18% | Use domain-specific terminology |
| **Unique vocabulary** | +15% | Increase word diversity |
| **Fluency optimization** | +15-30% | Improve readability and flow |
| ~~Keyword stuffing~~ | **-10%** | **Actively hurts AI visibility** |

**Best combination:** Fluency + Statistics = maximum boost. Low-ranking sites benefit even more — up to 115% visibility increase with citations.

### Pillar 3: Presence — Be Where AI Looks

**Third-party sources matter more than your own site:**
- Wikipedia mentions (7.8% of all ChatGPT citations)
- Reddit discussions (1.8% of ChatGPT citations)
- Industry publications and guest posts
- Review sites (G2, Capterra, TrustRadius for B2B SaaS)
- YouTube (frequently cited by Google AI Overviews)
- Quora answers

## Schema Markup for AI

| Content Type | Schema | Why It Helps |
|-------------|--------|-------------|
| Articles/Blog posts | `Article`, `BlogPosting` | Author, date, topic identification |
| How-to content | `HowTo` | Step extraction for process queries |
| FAQs | `FAQPage` | Direct Q&A extraction |
| Products | `Product` | Pricing, features, reviews |
| Reviews | `Review`, `AggregateRating` | Trust signals |
| Organization | `Organization` | Entity recognition |

Content with proper schema shows 30-40% higher AI visibility.

## Content Types That Get Cited Most

| Content Type | Citation Share | Why AI Cites It |
|-------------|:--------------:|----------------|
| **Comparison articles** | ~33% | Structured, balanced, high-intent |
| **Definitive guides** | ~15% | Comprehensive, authoritative |
| **Original research/data** | ~12% | Unique, citable statistics |
| **Best-of/listicles** | ~10% | Clear structure, entity-rich |
| **Product pages** | ~10% | Specific details AI can extract |
| **How-to guides** | ~8% | Step-by-step structure |

**Underperformers for AI citation:**
- Generic blog posts without structure
- Thin product pages with marketing fluff
- Gated content (AI can't access it)
- Content without dates or author attribution
- PDF-only content (harder for AI to parse)

## Common Mistakes

- **Ignoring AI search entirely** — ~45% of Google searches now show AI Overviews
- **Treating AI SEO as separate from SEO** — Good traditional SEO is the foundation
- **Writing for AI, not humans** — If content reads like it was written to game an algorithm, it won't get cited
- **No freshness signals** — Undated content loses to dated content
- **Gating all content** — AI can't access gated content
- **Ignoring third-party presence** — You may get more AI citations from a Wikipedia mention than from your own blog
- **No structured data** — Schema markup gives AI systems structured context
- **Keyword stuffing** — Actively reduces AI visibility by 10%
- **Blocking AI bots** — If blocked in robots.txt, those platforms can't cite you
- **Generic content without data** — "We're the best" won't get cited. Specific metrics will.

## Related Skills

- `competitive-intel` — Competitor analysis
- `content-strategy` — Content planning
- `copywriting` — Writing human-readable, AI-extractable content

## Source

- Distilled from antigravity-awesome-skills (https://github.com/coreyhaines31/marketingskills)
