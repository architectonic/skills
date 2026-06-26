---
name: Managed Agent Launch
description: Launch a Claude Managed Agent (CMA) from idea to scheduled deployment — interview, scope, build kit, launch, eval, iterate. Use when the user wants to create a hosted agent on Anthropic's managed infrastructure.
tags: [autonomous-ai-agents, cma, claude, managed-agents, deployment, workflow, launch]
runtime_targets: [claude-code]
type: Playbook
---

# Managed Agent Launch

## Purpose

Launch a Claude Managed Agent (CMA) from idea to scheduled deployment. This skill covers the full lifecycle: interview → scope → build kit → launch → eval → iterate → scheduled deployment.

CMA is a hosted agent harness — Anthropic runs the agent loop, tool execution, and sandboxed Linux container server-side. Ideal for long-running, asynchronous, stateful work.

## Trigger

User wants to create a hosted agent on Anthropic's managed infrastructure, or mentions "managed agent", "CMA", "hosted agent", or "scheduled agent".

## Prerequisites

- Claude Code with `/launch-your-agent` skill installed, OR
- API access with `anthropic-beta: managed-agents-2026-04-01` header
- `ant` CLI installed (`brew install anthropics/tap/ant`) for CLI-based flows

## The 4 Phases

### Phase 1: Interview

Understand what the founder wants. Start warm — 2-3 archetype examples, then an open question. Let them explain before suggesting anything.

Key primitives to identify:
- **Model**: Opus-class by default, Sonnet when speed/cost matters more
- **Outcome**: What success looks like (`user.define_outcome`, max_iterations 3)
- **Connectors**: Email, Slack, etc. (mock in v0, wire for real in v1)
- **Memory**: Whether the agent needs persistent memory stores
- **Schedule**: Whether it runs on a clock (cron + timezone) or one-off

### Phase 2: Scope & Build Kit

Produce a CMA-shaped brief:
- Primitives table (what each primitive is, what we set, live ID)
- v1/v2 section for deferred capabilities
- Eval table

Build the agent folder with:
- Agent config (model, system prompt, tools, MCP servers, skills)
- Environment setup
- Draft `.env` file (chmod 600, gitignored) for any API keys

### Phase 3: Launch & Eval

Create the agent via API:
```
POST /v1/agents
{
  "name": "my-agent",
  "model": "claude-opus-4-8",
  "system": "...",
  "tools": [...],
  "skills": [...]
}
```

Create environment → create session → send user event.

Eval with founder's real past cases as golden set. Case 1 = build input, rest held back. Rubric = per-run grader.

### Phase 4: Iterate & Schedule

- Write NEXT-DIRECTIONS.md for anything deferred from v0
- Re-run evals before promoting to deployment
- For recurring use cases: create scheduled deployment via `POST /v1/deployments` with cron + timezone
- Invoke `/wrap-up` for the celebratory close

## CMA Primitives

| Primitive | What it is | ID prefix |
|-----------|-----------|-----------|
| **Agent** | Reusable, versioned config (model + prompt + tools + MCP + skills) | `agent_…` |
| **Environment** | Where sessions run (cloud sandbox or self-hosted) | (env id) |
| **Session** | One running agent instance; holds conversation history + sandbox state | `sesn_…` |
| **Events** | Bi-directional messages (user.*/system.* in, agent.*/session.*/span.* out) | (event ids) |

## Key Rules

- **Drafts-first**: Default to drafts + `always_ask` gate for write actions
- **Mock connectors in v0**: Slack/email need real setup — mock the outbox in v0, wire in v1
- **No spend-limit step**: The iteration bound (`max_iterations: 3`) is the quiet cost default
- **Keys never in chat**: Pre-create `.env` file, founder pastes key via absolute path
- **Scheduled deployments only for recurring use cases**: Don't schedule one-off agents
- **Use relative dates in initial_events**: They're replayed verbatim

## Verification

- [ ] Agent created and responds to test input
- [ ] Environment provisioned
- [ ] Session created and completes with `session.status_idle`
- [ ] Evals pass with golden set
- [ ] NEXT-DIRECTIONS.md written for deferred capabilities
- [ ] Schedule configured (if recurring) with cron + timezone
- [ ] Overview page generated and reviewed with founder

## Failure Modes

- **Agent doesn't respond**: Check `anthropic-beta` header, verify model name format
- **Session hangs**: Check max_iterations, verify tool permissions
- **Connector fails**: Fall back to mock outbox, defer to v1
- **Eval fails**: Add more golden cases, sharpen rubric

## Security Notes

- CMA is NOT eligible for Zero Data Retention or HIPAA BAA (stateful by design)
- Delete sessions/files when no longer needed
- Never put API keys in chat — use `.env` file with chmod 600
- High-risk skill: involves API calls, account actions, deployment mutation
