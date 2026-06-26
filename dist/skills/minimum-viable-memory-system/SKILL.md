---
name: Minimum Viable Memory System
description: The 10-file governed memory kit every project needs for safe, continuous agent work. Use when setting up a new project memory layer, onboarding agents to an existing project, or diagnosing missing project memory infrastructure.
tags: [canonical, memory, kit, agent-operations, onboarding, governance]
type: Playbook
---

# Minimum Viable Memory System

## Purpose

A useful agent memory system needs only 10 durable Markdown files. This kit gives any project a governed memory layer that preserves continuity, decision integrity, safety boundaries, and epistemic hygiene across sessions, agents, and humans.

## The 10-File Kit

```text
AGENTS.md              ← Agent-facing rules and operating constraints
START_HERE.md          ← Read order and first-5-minutes checklist
repo_contract.md       ← What this repo is and is not
authority.md           ← Who decides what, and how conflicts resolve
memory_model.md        ← Memory classes, lifecycle states, scopes
decision_log.md        ← Durable decisions with rationale
handoff_log.md         ← Session-to-session continuity records
qa_gauntlet.md         ← Pre-completion checklist
security_review.md     ← Public boundary, risk classification, prohibited actions
tool_use_guardrails.md ← Before/after rules for tool mutation
```

## File Specifications

### 1. AGENTS.md — Operating Rules
- Source hierarchy (what to trust, in order)
- Public boundary (what never enters the repo)
- Aggregation rules (how to ingest external material)
- Completion standard (when work is done)
- OKF frontmatter requirements
- Graphify usage rules (if applicable)

### 2. START_HERE.md — Read Order + First 5 Minutes
- Two read orders: normal kit use and OKF aggregation work
- First 5 minutes checklist (identify request, read contract, check decisions, identify affected files, state known/inferred/unknown, make smallest plan)
- When to ask before acting vs. when to proceed
- Output standard (what changed, where verified, what remains unknown)

### 3. repo_contract.md — Project Identity
- What this repository is
- What it is not
- Primary audience
- Scope boundaries

### 4. authority.md — Decision Authority
- Who has authority over what
- How to resolve conflicts between sources
- Role definitions (human, agent, orchestrator, worker)
- Escalation path

### 5. memory_model.md — Memory Classes and Lifecycle
- Memory types: Fact, Assumption, Decision, Rule, Question, Risk
- Lifecycle states: Observation → Assumption → Verified Fact → Decision → Rule → Superseded → Deprecated → Deleted
- Scope separation: public patterns / private preferences / project rules / task-local / source-derived / agent inferences
- Promotion and demotion criteria

### 6. decision_log.md — Decision Records
- Entry template: Date, Decision, Rationale, Alternatives Considered, Author, Status
- Link to related handoffs and QA gauntlet entries
- Supersede mechanism (don't delete, mark superseded)

### 7. handoff_log.md — Continuity Records
- Entry template: Date, From, To, Context, Open Questions, Next Steps, Risks
- What the next agent needs to know without re-reading everything
- Keep entries concise; link to decision log for rationale

### 8. qa_gauntlet.md — Pre-Completion Checklist
- Standard checklist items (files readable, no private identifiers, instructions actionable, sources provenance'd, security marked)
- Project-specific additions
- Sign-off convention

### 9. security_review.md — Safety Boundaries
- Public boundary definition
- Risk classification scheme (low / medium / high)
- Prohibited actions
- Block conditions for external sources
- External system mutation safety rules

### 10. tool_use_guardrails.md — Tool Mutation Discipline
- Before tool mutation: verify intent, check scope, confirm idempotency
- After tool mutation: read back state, verify result, log what changed
- Tool-specific rules (terminal, browser, file write, network, MCP)

## Deployment Procedure

1. **Create** the 10 files in the project root using the structure above.
2. **Populate** AGENTS.md with project-specific operating rules (source hierarchy, public boundary, aggregation rules, completion standard).
3. **Populate** START_HERE.md with the read order and first-5-minutes checklist.
4. **Write** a one-paragraph repo_contract.md stating what the project is.
5. **Write** a one-page authority.md with role definitions.
6. **Adapt** memory_model.md to your project's ontology needs.
7. **Create empty** decision_log.md and handoff_log.md with entry templates.
8. **Adapt** qa_gauntlet.md from the completion standard in AGENTS.md.
9. **Adapt** security_review.md from the public boundary section of AGENTS.md.
10. **Adapt** tool_use_guardrails.md from the operating rules.

## Verification

- [ ] All 10 files exist and are valid Markdown
- [ ] AGENTS.md has source hierarchy, public boundary, completion standard
- [ ] START_HERE.md has read order for both kit use and aggregation work
- [ ] repo_contract.md is one clear paragraph
- [ ] authority.md defines at least 2 roles and conflict resolution
- [ ] memory_model.md defines at least 4 memory types and lifecycle states
- [ ] decision_log.md and handoff_log.md have entry templates
- [ ] qa_gauntlet.md checklist matches the completion standard
- [ ] security_review.md defines risk levels and prohibited actions
- [ ] tool_use_guardrails.md covers before/after mutation for at least 3 tool types
- [ ] No private identifiers, credentials, or secrets in any file

## Failure Modes

- **Over-engineering**: Adding too much process too early. Keep it boring. Plain Markdown first.
- **Scope creep**: Adding project-specific details to generic kit files. Keep generic files generic; use separate files for project specifics.
- **Stale files**: Files created once and never updated. Review at least when the project scope changes.
- **Mixing private context**: Accidentally including private notes or credentials. Run a privacy review before publishing.

## Scope Note

This kit is runtime-neutral and agent-framework-agnostic. It works for Hermes, Cursor, Codex, Claude Code, or any agent that can read Markdown. Add runtime-specific adapter notes in a separate file if needed.

## Source Provenance

- `memory_ops_doctrine.md` lines 100-115 — the original 10-file list and rationale
- `curator/root-meta/AGENTS.md` — source hierarchy, aggregation rules, completion standard
- `curator/root-meta/START_HERE.md` — read order, first 5 minutes, output standard
