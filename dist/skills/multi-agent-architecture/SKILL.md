---
name: Multi-Agent Architecture Patterns
description: Architecture patterns for multi-agent systems — four-layer agent design, coordination patterns, lifecycle management, and production hardening. Use when designing systems where multiple AI agents coordinate, spawn sub-agents, or share tools and state.
tags: [agent-operations, agent-operations, multi-agent, architecture, coordination, lifecycle]
type: Playbook
---

# Multi-Agent Architecture Patterns

## Source

Distilled from the `building-multiagent-systems` Claude Code plugin by 2389 Research (MIT license, https://github.com/2389-research/building-multiagent-systems). Patterns adapted for AOMK agent operations.

## Four-Layer Agent Architecture

Every production-grade agent should separate concerns into four layers:

| Layer | Responsibility | Example |
|-------|---------------|---------|
| **1. Reasoning** | LLM model selection, prompt context | `'sonnet'` for complex reasoning, `'fast'` for routine tasks |
| **2. Orchestration** | Permission policy, lifecycle rules, timeout configuration | `permissions: ['file:read']`, `timeout: 120000` |
| **3. Tool Bus** | Schema-typed tools discoverable by sub-agents | `editTool`, `readTool`, `bashTool` with input/output schemas |
| **4. Deterministic Adapters** | Testable, non-LLM execution boundaries | API clients, file operations, shell commands |

**Key principle:** LLM calls live only in Layer 1. Tools in Layers 3-4 must be deterministic and testable.

## Seven Coordination Patterns

Use these patterns when designing multi-agent workflows:

1. **Fan-out/fan-in** — Spawn N specialist sub-agents in parallel, collect results. Best for independent review/analysis tasks.
2. **Sequential pipeline** — Agents pass work in sequence, each adding value. Best when order matters (draft → review → refine).
3. **Recursive delegation** — Agent spawns sub-agent which spawns its own sub-agents. Best for hierarchical decomposition.
4. **Work-stealing queue** — Idle agents pull from a shared task queue. Best for heterogeneous workloads with variable processing time.
5. **Map-reduce** → Distribute work map, then reduce/aggregate results. Best for large-scale analysis tasks.
6. **Peer collaboration** — Agents with equal authority share state and negotiate. Best for deliberation and consensus tasks.
7. **MAKER (Million-step Zero-error)** — Long-horizon agent with checkpointing and verification at each step. Best for complex multi-step operations.

## Lifecycle Management Patterns

- **Cascading stop** — When parent stops, all children stop recursively. Prevents orphaned agents.
- **Orphan detection** — Periodic heartbeat to detect and clean up agents whose parent died.
- **Permission inheritance** — Sub-agents inherit a subset of parent permissions, never superset. Default to read-only.
- **Timeout enforcement** — Every sub-agent spawn gets a timeout. No indefinite hangs.

## Production Hardening Checklist

- [ ] Four-layer architecture implemented (reasoning / orchestration / tool bus / adapters)
- [ ] Schema-first tools (typed contracts for tool discovery)
- [ ] Deterministic boundary (no LLM calls in tools)
- [ ] Cascading stop on parent termination
- [ ] Orphan detection via heartbeat
- [ ] Permission inheritance (read-only default for sub-agents)
- [ ] Timeout on every sub-agent spawn
- [ ] Concurrency bounds (max concurrent sub-agents)
- [ ] Cost tracking across agent hierarchy
- [ ] Partial-failure handling (don't cascade failures)
- [ ] State persistence for long-running workflows
- [ ] Coordinated tool access (no race conditions on shared resources)
- [ ] Right-sized model selection (fast model for routine, smart for complex)

## AOMK Integration

- Apply four-layer architecture when spawning sub-agents via `delegate_task`
- Use coordination patterns from this skill when designing `catalog/playbooks/` loops
- Reference production hardening checklist in `agent-operations/qa-gauntlet.md`
