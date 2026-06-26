---
name: firecrawl-web-scraper
description: Web scraping and crawling with Firecrawl v2 API — converts websites into LLM-ready markdown or structured data. Use when scraping websites, crawling entire sites, extracting web content, converting HTML to markdown, building web scrapers, handling dynamic JavaScript content, bypassing anti-bot protection, or extracting structured data from web pages.
tags: [research, web-scraping, firecrawl, data-extraction, crawling]
source: AgentSkillOS — data/skill_seeds/firecrawl-scraper/SKILL.md (MIT license)
type: Playbook
---

# Firecrawl Web Scraper

Web Data API for AI that turns entire websites into LLM-ready markdown or structured data.

## What It Handles

- **JavaScript rendering** — Executes client-side JavaScript for dynamic content
- **Anti-bot bypass** — Gets past CAPTCHA and bot detection
- **Format conversion** — Outputs as markdown, JSON, or structured data
- **Screenshot capture** — Visual representations of pages
- **Browser automation** — Full headless browser capabilities

## Authentication

Requires API key (starts with `fc-`). Sign up at https://www.firecrawl.dev.

**NEVER hardcode API keys in code.** Store in environment variables:
```
FIRECRAWL_API_KEY=fc-your-api-key-here
```

## API Endpoints

### `/v2/scrape` — Single Page Scraping

Scrapes a single webpage and returns clean, structured content.

**Key options:**
- `formats`: `["markdown", "html", "screenshot"]`
- `onlyMainContent`: true/false (removes nav, footer, ads)
- `waitFor`: milliseconds to wait before scraping
- `actions`: browser automation actions (click, scroll, etc.)

**Use cases:** Extract article content, get product details, scrape specific pages.

### `/v2/crawl` — Full Site Crawling

Crawls all accessible pages from a starting URL.

**Key options:**
- `limit`: max pages to crawl
- `maxDepth`: how many links deep to follow
- `allowedDomains`: restrict to specific domains
- `excludePaths`: skip certain URL patterns

**Use cases:** Index documentation sites, archive website content, build knowledge bases.

### `/v2/map` — URL Discovery

Maps all URLs on a website without scraping content.

**Use cases:** Find sitemap, discover all pages, plan crawling strategy, audit site structure.

### `/v2/extract` — Structured Data Extraction

Uses AI to extract specific data fields from pages using a schema.

**Key options:**
- `schema`: Zod or JSON schema defining desired structure
- `systemPrompt`: guide AI extraction behavior

**Use cases:** Extract product prices, parse contact information, build structured datasets.

## Python SDK

```bash
pip install firecrawl-py
```

**Single page:**
```python
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])
result = app.scrape_url(url, params={"formats": ["markdown"], "onlyMainContent": True})
markdown = result.get("markdown")
```

**Crawl:**
```python
result = app.crawl_url(url, params={"limit": 100, "scrapeOptions": {"formats": ["markdown"]}})
```

**Extract structured data:**
```python
result = app.extract(urls=[url], params={"schema": schema, "systemPrompt": "Extract product info"})
```

## TypeScript/Node.js SDK

```bash
npm install @mendable/firecrawl-js
```

**Single page:**
```typescript
import FirecrawlApp from '@mendable/firecrawl-js';
const app = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const result = await app.scrapeUrl(url, { formats: ['markdown'], onlyMainContent: true });
```

**Extract with Zod:**
```typescript
const schema = z.object({ title: z.string(), price: z.number() });
const result = await app.extract({ urls: [url], schema, systemPrompt: 'Extract product details' });
```

## Common Use Cases

### Documentation → RAG
Crawl entire docs site with `onlyMainContent: true`, save each page as markdown for ingestion into a knowledge base.

### Product Data Extraction
Define a schema with product fields, use `/v2/extract` to get structured data from product pages.

### News Article Scraping
Use `onlyMainContent: true` and `removeBase64Images: true` to get clean article content without ads/navigation.

## Best Practices

1. **Use `onlyMainContent: true`** to reduce credits and get cleaner data
2. **Set reasonable limits** on crawls to avoid excessive costs
3. **Handle retries** with exponential backoff for transient errors
4. **Cache results** locally to avoid re-scraping same content
5. **Use `map` first** to plan crawling strategy
6. **Batch extract calls** when processing multiple URLs
7. **Monitor credit usage** in dashboard

## Rate Limits

- Free tier: 500 credits/month
- Paid tiers: Higher limits based on plan
- Credits consumed vary by endpoint and options

## Cloudflare Workers Note

The Firecrawl SDK cannot run in Cloudflare Workers (uses Node.js `http` module). Use the direct REST API with `fetch` instead, or use the [workers-firecrawl](https://github.com/G4brym/workers-firecrawl) package.
