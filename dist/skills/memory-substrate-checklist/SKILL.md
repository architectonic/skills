---
name: Memory Substrate Checklist
description: Evaluation checklist for assessing persistent memory systems for coding agents. Use when evaluating, setting up, or auditing a memory substrate (like agentmemory) that stores observations, decisions, and session context across agent runs.
tags: [agent-operations, agent-operations, memory, substrate, evaluation, checklist, persistent-memory]
source_license: Apache-2.0
distilled_at: 2026-06-22
type: Playbook
---

# Memory Substrate Checklist

## Purpose

Evaluate whether a persistent memory system for coding agents is safe, effective, and appropriate for the project. This checklist covers storage, retrieval, lifecycle, security, and operational concerns.

## Checklist

### Source Identity
- [ ] License and redistribution terms verified
- [ ] Provenance documented (who maintains it, how active is development)
- [ ] Version pinned or update policy understood

### Storage Model
- [ ] Storage root identified (where memories live on disk)
- [ ] Separation between memory data and workspace source code confirmed
- [ ] Git-versioning or backup strategy for memory data exists
- [ ] Storage growth is bounded (compression, consolidation, or retention policy)

### Retrieval Policy
- [ ] Search mode documented (BM25, vector, graph, hybrid)
- [ ] Relevance scoring is explainable (not a black box)
- [ ] Recall can be scoped by project, session, or time window
- [ ] Empty results are handled honestly (no fabrication)

### Write Policy
- [ ] What triggers a write (manual, hook, automatic) is explicit
- [ ] Write gates exist for self-improvement lessons (not every observation becomes permanent)
- [ ] Concept tagging is specific, not generic (`jwt-refresh-rotation` not `auth`)
- [ ] Provenance fields (who, when, why) are captured with each write

### Confidence and Lifecycle
- [ ] Importance/priority scores are assigned to memories
- [ ] Lifecycle states exist: candidate → verified → degraded → deprecated → archived
- [ ] Compression/summarization is opt-in (not silent)
- [ ] Forgetting/purge is possible (by memory ID, by session, by age)

### Runtime Adapters
- [ ] Supported agent runtimes are documented
- [ ] Adapter installation is reviewed (does it modify agent config files?)
- [ ] MCP tool surface is documented (what tools does the memory server expose?)
- [ ] Hook surface is documented (what lifecycle events trigger capture?)

### Tool / MCP Surfaces
- [ ] Full tool inventory reviewed (capture, retrieve, govern, audit tools)
- [ ] Tool visibility can be restricted (core set vs. full set)
- [ ] Governance tools exist: delete, audit, verify, heal, diagnose

### Audit and Rollback
- [ ] Audit log exists for write gate decisions and failed distillations
- [ ] Rollback path is documented (how to purge all memories from a session)
- [ ] Recall evaluation is possible (test retrieval accuracy on known inputs)

### Security and Privacy
- [ ] Authentication on REST API is available (bearer token)
- [ ] No secrets or credentials stored in memory content
- [ ] Session data is isolated per project/directory boundary
- [ ] Network access requirements documented (local-only vs. cloud LLM)

## Red Flags

- No storage growth bounds (memory grows forever)
- Silent compression or summarization (agent can't tell what was altered)
- No way to delete specific memories
- Hooks capture everything without opt-out
- MCP tools expose mutation surfaces without review
- No separation between memory data and workspace code
- Benchmark claims without reproduction path

## Recommended Pattern

```
source identity
→ license and provenance
→ storage location
→ retrieval policy
→ write policy
→ confidence and lifecycle fields
→ runtime adapters
→ tool/MCP surfaces
→ hook surfaces
→ rollback and purge path
→ independent recall evaluation
```
