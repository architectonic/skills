---
name: engineering-context-windows
description: Manage the agent context window as a scarce shared resource — decide what lives in always-loaded instructions, skills, memory, or the filesystem, and survive compaction without losing critical rules. Use when instructions bloat, agents forget mid-session rules, context overflows on long tasks, or when designing memory and retrieval for an agent system.
tags: [context-engineering, memory, compaction, agent-operations, okf]
type: Playbook
domain: agent-operations
risk_level: low
requires_review: false
---

# Engineering Context Windows

The context window is a public good: system prompt, conversation, tool schemas, skill metadata, and file contents all compete for it. Context engineering — deciding *what* is present *when* — has largely replaced prompt phrasing as the highest-leverage discipline.

## Placement ladder

Place each piece of information at the cheapest tier that still guarantees availability when needed:

```text
1. always-loaded (system prompt / AGENTS.md)   invariants, safety rules, routing pointers
2. skill metadata (name+description)           ~100 tokens per skill, triggers on-demand load
3. skill body / reference files                procedures, loaded when the task matches
4. filesystem (read on demand)                 corpora, schemas, data — zero cost until read
5. memory files (cross-session)                durable facts an agent re-reads next session
6. conversation                                ephemeral working state — assume it will be lost
```

Rule of thumb: **pointers up, payloads down.** Top tiers hold routing ("truth lives in X"); lower tiers hold the actual content.

## Compaction survival

Long sessions get summarized. Compaction preserves always-loaded files and recent turns; it thins the middle. Consequences:

- A rule stated once mid-conversation will eventually vanish — promote recurring corrections into AGENTS.md or a skill.
- Durable outcomes (decisions, findings, handoffs) must be written to files *before* they matter, not kept in chat.
- Ledgers and logs exist precisely so a fresh or compacted context can rebuild state by reading, not remembering.

## Memory discipline

- Memory records *traces*; knowledge bases record *claims*. Don't promote conversation context into durable memory without confirmation (chain of truth: memory = hints → index = known → source = true).
- One fact per memory entry, with a one-line description for recall relevance; link related entries.
- Memory is context, not evidence — re-verify anything memory asserts about files or systems before acting on it.

## Retrieval over stuffing

Prefer navigable structure to preloaded bulk: a SKILL.md that says "grep `reference/finance.md` for revenue metrics" beats inlining the schema. Give long reference files a table of contents so partial reads still reveal scope. Organize by domain so a task loads only its slice.

## Budget signals

Watch for: instructions file growing past a few hundred lines (split into skills); the same explanation pasted into multiple sessions (promote to a skill); agents re-deriving project state each session (create/refresh the ledger); tool schemas dwarfing conversation (defer/curate tools — see `engineering-agent-harnesses`).

## Related skills

- `engineering-agent-harnesses` — placement is one of the four harness surfaces.
- `authoring-agent-skills` — the on-demand tier's format and rules.
- `agent-memory-system` — file-based memory patterns.
