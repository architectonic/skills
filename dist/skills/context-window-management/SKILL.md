---
name: context-window-management
description: Strategies for managing LLM context windows including summarization, trimming, routing, and avoiding context rot. Tiered context strategy, serial position optimization, intelligent summarization, and token budget allocation.
tags: [agent-operations, context-engineering, llm, token-management, summarization, rag]
type: Playbook
---

# Context Window Management

Strategies for managing LLM context windows including summarization, trimming, routing, and avoiding context rot.

## When to Use

- Building any multi-turn conversation system
- Context exceeds optimal size for a model
- Need predictable context management across different model tiers
- Constructing prompts with significant context
- Avoiding context rot in long sessions

## Tiered Context Strategy

Different strategies based on context size:

| Model Tier | Max Tokens | Strategy | Model |
|------------|-----------|----------|-------|
| Small | 8,000 | full | claude-3-haiku |
| Medium | 32,000 | full | claude-3-5-sonnet |
| Large | 100,000 | summarize | claude-3-5-sonnet |
| Unlimited | ∞ | rag | claude-3-5-sonnet |

Select strategy based on token count of current messages.

## Serial Position Optimization

Place important content at start and end of prompts. LLMs weight beginning and end more heavily.

**Prompt structure:**
1. **START:** System instructions (always first)
2. **CRITICAL CONTEXT:** Right after system (high primacy)
3. **MIDDLE:** Conversation history (lower weight) — summarize if long, keep recent messages full
4. **END:** Current query (high recency)
5. **FINAL:** Reminder of key constraints

## Intelligent Summarization

Summarize by importance, not just recency. When summarizing:

1. Score each message by importance (0-1)
2. Boost messages with critical info (+0.5) and messages referenced later (+0.3)
3. Keep high-importance messages in full until 70% of target budget
4. Summarize remaining messages into a system message
5. Restore original order after selection

## Token Budget Allocation

Allocate token budget across context components:

| Component | Budget % | Purpose |
|-----------|----------|---------|
| System | 10% | System prompt |
| Critical Context | 15% | User prefs, key info |
| History | 40% | Conversation history |
| Query | 10% | Current query |
| Response | 25% | Reserved for response |

Reallocate unused budget to history (most valuable for conversation).

## Validation Checks

| Check | Severity | Fix |
|-------|----------|-----|
| Building context without token counting | WARNING | Count tokens before sending |
| Naive message truncation | WARNING | Summarize old messages instead of removing |
| Hardcoded token limit | INFO | Use model-specific limits from config |
| No context management strategy | WARNING | Implement budgets, summarization, or RAG |

## Patterns

### Pattern: Summarize Old Messages

When history exceeds threshold:
1. Keep last N messages in full
2. Summarize earlier messages into a single system message
3. Preserve user preferences, decisions, and key facts

### Pattern: RAG for Large Corpuses

When context exceeds model limits:
1. Store conversation history in vector DB
2. Retrieve relevant messages for current query
3. Combine retrieved context with recent messages

### Pattern: Context Compaction

When approaching context limit:
1. Identify low-importance messages
2. Summarize or remove them
3. Preserve system prompt and critical context
4. Always keep the last user turn

## Related Skills

- `context-engineering` — Broader context management patterns
- `rag-implementation` — RAG for large corpuses
- `conversation-memory` — Memory persistence
- `prompt-caching` — Caching optimization

## Source

- Distilled from antigravity-awesome-skills collection (vibeship-spawner-skills, Apache 2.0)
