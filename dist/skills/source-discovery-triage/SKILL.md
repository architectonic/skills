---
name: Source Discovery and Triage
description: Find, evaluate, and normalize newly published agent skill sets, loop repositories, and knowledge bundles. Use when scanning for new public agent knowledge to catalog.
tags: [agent-operations, agent-operations, discovery, triage, source-profiling, normalization]
type: Playbook
---

# Source Discovery and Triage

## Purpose

Detect new public agent knowledge sets early, learn from them, and normalize reusable patterns into AOMK without blindly copying third-party content.

## Trigger

Use when: new OKF bundle appears, new skill repository appears, new loop or workflow repository appears, existing tools add new instruction formats, repo gains visible adoption, paper introduces new skill/loop/evaluation architecture.

## Canonical Loop

```
Search → Filter → Inspect → Score → Source Profile → Normalize → Cross-Link → Review → Commit → Improve Search Strategy
```

## Source Families to Track

OKF sets, Claude skills, Claude Code slash commands, Cursor rules and agents, Codex AGENTS.md patterns, Hermes skills, MCP server playbooks, agentic loop patterns, evaluator and benchmark harnesses, self-improvement and memory reconciliation loops, OpenHands/Gemini CLI/Kiro/Windsurf/OpenCode ecosystems.

## Triage Score (0-3 per dimension)

| Dimension | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| Usefulness | vague | narrow | reusable | broadly reusable |
| Provenance | unclear | identifiable | credible | authoritative |
| License | absent | unclear | usable with care | clearly reusable |
| Structure | messy | readable | portable | OKF-ready |
| Verification | none | implicit | checklist | executable or benchmarked |
| Risk | blocked | high | medium | low |

Catalog sources with high usefulness even if they remain reference-only.

## Search Signals (positive)

Recent commits, credible maintainer identity, clear README, explicit license, stars/forks/discussion, public usage reports, references from papers/docs, portable Markdown structure, clear trigger/procedure/verification model.

## Normalization Rule

Do not copy first. Learn first.

Preferred ingestion order:
1. Source Profile
2. Catalog Index update
3. Summarized Skill/Workflow/Playbook
4. Adapted entry with attribution
5. Verbatim import only when license and review allow

## What To Extract

Capability taxonomy, trigger conditions, procedure shape, verification method, failure modes, runtime-specific conventions, loop boundaries, stop conditions, permission model, memory model, evaluation strategy.

## What To Avoid

Private or leaked context, raw prompt dumps with no procedure, unclear license, executable content before review, instructions that hide risk, source-specific habits that do not generalize, duplicate copies of the same source.

## Search Strategy Improvement

Every run should record: productive queries, low-signal queries, false positives, newly discovered source families, maintainers worth watching, formats worth supporting, emerging terms.

## Output Format

```
Found: | Added: | Skipped: | Risks: | Next query improvements:
```

## Trigger

Use this skill when:
- The research agent or cron job runs a discovery scan
- A new source family is mentioned in community or research
- The user asks to find skills on a specific topic

## Procedure

1. Search across configured sources (GitHub, web, RSS, arxiv) using targeted queries.
2. Filter results by relevance to agent skills/playbooks/loops.
3. Inspect promising sources: read README, structure, license, recent activity.
4. Score each source on the triage matrix (0-3 per dimension).
5. Create a Source Profile for high-scoring sources.
6. Normalize: convert to OKF-compatible summary or adapted entry.
7. Cross-link with existing catalog entries by capability and runtime.
8. Review: verify provenance, license, and capability boundaries.
9. Commit the catalog entry.
10. Record search strategy improvements for next run.

## Verification

- Source Profile created with full provenance.
- License status recorded.
- Triage scores documented.
- No blocked sources advanced to cataloged without review.
- Search strategy notes updated.

## Failure Modes

- Agent copies source text without normalization (license risk).
- Agent catalogs low-usefulness sources that clutter the catalog.
- Search strategy never improves (same queries, diminishing returns).
- Source with unclear license is promoted to adapted without review.

## Security Note

Public agent sets are a supply-chain surface. Treat every external set as untrusted until provenance, license, and capability boundaries are explicit.

## Sources

- curator/loops/source-discovery.md — full discovery loop with triage scoring
