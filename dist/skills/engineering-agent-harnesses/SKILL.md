---
name: engineering-agent-harnesses
description: Improve agent reliability by shaping the software around the model — repo instructions, tool budgets, permission tiers, schema-validated tool calls, and compaction-safe context placement. Use when an agent underperforms despite good prompts, when configuring a repo or workspace for agents, or when designing the runtime that hosts them.
tags: [harness-engineering, agent-operations, context, permissions, tooling, okf]
type: Playbook
domain: agent-operations
risk_level: low
requires_review: false
---

# Engineering Agent Harnesses

Harness engineering improves output quality by shaping the environment around a fixed model — instructions, tools, permissions, feedback loops — rather than only rewriting the prompt. Most production agent failures trace to harness defects (context drift, schema misalignment, state degradation), not model weakness.

## The harness is four surfaces

```text
INSTRUCTIONS  what is always loaded vs loaded on demand
TOOLS         what the agent can call, and how calls are validated
PERMISSIONS   what requires approval, per action class
FEEDBACK      how the agent learns whether its action worked
```

## Instructions: placement beats volume

- **Always-loaded files** (AGENTS.md / CLAUDE.md / system prompt): only rules that must survive context compaction — safety boundaries, source-of-truth pointers, non-negotiable conventions. Compaction can drop mid-conversation instructions; anything critical that lives only in chat history will eventually be lost.
- **On-demand (skills, reference files):** procedures, domain detail, examples — loaded when triggered (see `authoring-agent-skills`).
- Keep always-loaded files short and pointer-rich: they should route to truth (files, ledgers), not duplicate it. Stale embedded facts are worse than none.

## Tools: budget them

Agent performance degrades **non-linearly** as tool count grows — more tools means worse selection, not more capability. Curate the minimum set per task class; prefer deferred/searchable tool loading where the runtime supports it. Never let free-text reach an executor: the model emits a structured call, the harness validates schema and permissions, executes, and injects the result back.

## Permissions: tier by reversibility

```text
free          read, search, local reversible edits
confirm       pushes, publishes, external messages, config changes
gated         spending, credentials, deletion, production, outreach
forbidden     other actors' secrets, bypassing brokers
```

Broker credentials — the agent gets a scoped lease/proxy, never the raw secret; runs carry an owner/payer identity for audit.

## Feedback: close every action loop

An agent that cannot observe outcomes cannot correct. Give each action class its checker: builds → compile+test output; edits → read-back or lint; deploys → health endpoint; content → validator script or rubric. Wire the checker's output back into the same run (validator loop), and make failure messages verbose and specific — the error text is the agent's repair context.

## Environment hygiene

- Deterministic, scripted setup (a broken sandbox produces confident nonsense).
- State the platform truths the agent will otherwise guess wrong (shell dialect, path style, port map, which directories are runtime-managed and must not be hand-edited).
- Record per-run provenance: who ran, with what authority, touching what — the run ledger is the harness's memory and the audit trail.

## Diagnosing harness defects

When an agent misbehaves, check in order: (1) was the needed rule loaded at the moment of the mistake, or lost to compaction/on-demand placement? (2) did tool schema or naming mislead selection? (3) did stale state (cached notes, old ledger) contradict source truth? (4) was the feedback loop silent, letting a failure look like success? Fix the harness before blaming the model or adding prompt verbiage.

## Related skills

- `engineering-context-windows` — the context-placement discipline in depth.
- `engineering-loop-contracts` — the recurring-execution layer above the harness.
- `mcp-external-tool-security-review` — vetting third-party tools before they enter the harness.
