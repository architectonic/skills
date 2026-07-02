---
type: Report
title: Skills Radar - 2026-07-02
description: Radar discovery notes for the skills aggregator daily operator loop.
tags: [skills, radar, discovery, sources, aggregator]
okf_version: "0.2"
status: active
---

# Skills Radar - 2026-07-02

## Selected Role

Radar.

## Selection Reason

The current São Paulo hour mapped to Radar by the default cadence. Today's queues were empty after two Reporter checkpoints, and the active blockers requested concrete public source candidates. Discovery was therefore the highest-value bounded action.

## Discovery Scope

Searched current public web and GitHub for:

- public agent skill repositories;
- agent skill benchmarks and evaluation repositories;
- agent skill orchestration / retrieval systems;
- runtime skill package standards;
- MCP procedure and tooling sources;
- current security research on unsafe or malicious agent skills.

## Candidate Sources Created

1. `sources/candidates/swe-skills-bench.md`
   - Source URL: https://github.com/GeniusHTX/SWE-Skills-Bench
   - Why it matters: benchmark evidence for whether skills improve software engineering outcomes.
   - Runtime target: software engineering agents / agent skill evaluation.
   - License clue: unknown; requires Source Reviewer inspection.
   - Risk: medium, because benchmark harnesses may include executable scripts and dependencies.

2. `sources/candidates/agentskillos.md`
   - Source URL: https://github.com/ynulihao/AgentSkillOS
   - Why it matters: ecosystem-scale skill organization, retrieval, orchestration, and benchmark structure.
   - Runtime target: skill orchestration and large skill corpus management.
   - License clue: unknown; requires Source Reviewer inspection.
   - Risk: medium, because orchestration and benchmark code may execute model calls, scripts, or dependencies.

3. `sources/candidates/agent-skills-open-standard.md`
   - Source URL: https://agentskills.io
   - Why it matters: emerging package format and cross-runtime compatibility surface for installable skills.
   - Runtime target: Claude / VS Code / GitHub / Cursor / Goose / Amp / OpenCode style skill consumers.
   - License clue: unknown; requires Source Reviewer inspection.
   - Risk: medium, because skill packages can include scripts, resources, and runtime-specific execution semantics.

4. `sources/candidates/model-context-protocol.md`
   - Source URL: https://modelcontextprotocol.io
   - Why it matters: many agent skills depend on external tools, servers, OAuth flows, filesystems, browser automation, or state-changing actions.
   - Runtime target: MCP clients, MCP servers, IDE agents, and tool-using runtimes.
   - License clue: unknown; requires Source Reviewer inspection.
   - Risk: high, because MCP sources can involve local command execution, credentials, filesystem access, network calls, and external mutations.

5. `sources/candidates/agent-skill-security-research.md`
   - Source URL: https://arxiv.org/abs/2603.16572
   - Why it matters: security review model for malicious or unsafe third-party skill candidates using repository context.
   - Runtime target: Claude Code, OpenClaw, local skill directories, and marketplace-distributed skills.
   - License clue: unknown; requires Source Reviewer inspection.
   - Risk: high, because it concerns malicious skill behavior and must remain defensive / summarized only.

## Queue Updates

Added five `review` queue items for Source Reviewer.

No normalization, catalog, packaging, or publication queue items were created because none of the sources have license, provenance, and security review yet.

## Safety Notes

No third-party content was copied. Candidate profiles record URLs, provenance clues, risk levels, and next actions only.

## Next Action

Source Reviewer should consume the highest-priority review items in this order:

1. MCP candidate, because it has the highest tool/action risk.
2. Agent skill security research, because it can improve review gates before growth.
3. Agent Skills open standard, because it may affect package compatibility.
4. SWE-Skills-Bench, because it can inform validation and pruning.
5. AgentSkillOS, because it can inform catalog organization and orchestration after basic review gates are stronger.
