---
name: claude-api-reference
description: Full reference for the Claude API / Anthropic SDK — model IDs, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration.
type: API Endpoint
---

# Claude API Reference

Comprehensive reference for building LLM-powered applications with Claude.

## Current Models (cached 2026-06-04)

| Model | Model ID | Context | Input $/1M | Output $/1M |
|-------|----------|---------|------------|-------------|
| Claude Fable 5 | `claude-fable-5` | 1M | $10.00 | $50.00 |
| Claude Opus 4.8 | `claude-opus-4-8` | 1M | $5.00 | $25.00 |
| Claude Opus 4.7 | `claude-opus-4-7` | 1M | $5.00 | $25.00 |
| Claude Opus 4.6 | `claude-opus-4-6` | 1M | $5.00 | $25.00 |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | 1M | $3.00 | $15.00 |
| Claude Haiku 4.5 | `claude-haiku-4-5` | 200K | $1.00 | $5.00 |

**Default to `claude-opus-4-8`** unless user explicitly names a different model.

## Thinking & Effort

- **Fable 5 / Opus 4.8 / 4.7:** Adaptive thinking only. `thinking: {type: "adaptive"}`. `budget_tokens` is removed.
- **Effort parameter:** `output_config: {effort: "low"|"medium"|"high"|"max"}`. Default is `high`.
- **Opus 4.7+:** `"xhigh"` available between `high` and `max`.

## Compaction

For long-running conversations exceeding context window. Server-side compaction automatically summarizes earlier context. Requires beta header `compact-2026-01-12`.

## Prompt Caching

Prefix match caching. Any byte change invalidates everything after it. Render order: `tools` → `system` → `messages`. Keep stable content first, volatile content after last `cache_control` breakpoint.

## Managed Agents (Beta)

Server-managed stateful agents with Anthropic-hosted tool execution. Available on first-party API and Claude Platform on AWS. Not available on Bedrock/Vertex/Foundry.

Flow: Agent (create once) → Session (every run). Store agent ID, reference by ID.

## Common Pitfalls

- Don't truncate inputs
- Fable 5/Opus 4.8/4.7: adaptive thinking only, no `budget_tokens`
- Prefill removed on 4.6+ family
- Fable 5: `refusal` stop reason, ~30% more tokens
- `max_tokens` defaults: ~16000 non-streaming, ~64000 streaming
- Tool call JSON parsing differences on 4.6+
- Use SDK types, not custom interfaces
