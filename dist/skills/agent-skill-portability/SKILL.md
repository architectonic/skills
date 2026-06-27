---
name: agent-skill-portability
description: Research on agent skill portability, security implications, and cross-agent
  compatibility challenges.
tags:
- agent-operations
- research
- skill-portability
- security
- cross-agent
- compatibility
- agent-ecosystem
- okf
type: Playbook
title: Agent Skill Portability and Security Studies
domain: agent-operations
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# Agent Skill Portability and Security Studies (2026)

## Overview

Research examining how agent skills transfer across different agent runtimes (Claude Code, OpenClaw, Cursor, Codex) and the security implications of portable skill packages.

## Key Topics

### Skill Format Portability
- Skills written for one agent runtime may behave differently in another
- Format differences: SKILL.md (OpenClaw), .claude-plugin (Claude Code), .cursorrules (Cursor), AGENTS.md (Codex)
- Common denominator: markdown instruction files with structured frontmatter

### Security Implications of Portability
- Skills designed for sandboxed execution may have different security boundaries in other runtimes
- Tool availability varies across agents — a skill relying on `exec` may fail or be restricted
- Credential injection: different agents handle env vars and secrets differently

### Distribution Channel Risks
- Marketplace scanners disagree significantly on maliciousness classification
- Repository hijacking: abandoned repos with active skill references
- Need for immutable snapshots and provenance metadata

### Cross-Agent Compatibility Findings
- Skills authored for Claude Code show degraded performance in OpenClaw without adaptation
- Tool name mapping (exec → bash, browser → web_fetch) needed for portability
- Conditional activation (gating) helps prevent skill failures in incompatible environments

## Recommendations for Portable Skills

1. Use standard SKILL.md format with minimal runtime-specific assumptions
2. Include gating (requires.bins, requires.env) for tool dependencies
3. Document which agent runtimes the skill supports
4. Avoid hardcoding runtime-specific paths or tool names
5. Test across at least 2 target runtimes before publishing

## Related Work
- Trace2Skill: trajectory-to-skill pipeline (cross-model portability)
- SkillOps: self-maintaining skill libraries (contract-based dependencies)
- Repository-Aware Security Analysis: supply chain risks
