---
name: managed-agent-launch-cma
title: Managed Agent Launch
description: Help a **technical founder** build whatever they want on Claude Managed
  Agents (CMA) — an internal worker, a piece of their product, a customer-facing agent.
  Interview them about what they want, scope a v0, launch it in their own account,
  grade it against their own definition of done, iterate, and (if it should run on
  a clock) put it on a scheduled deployment.
type: Playbook
domain: agent-operations
tags:
- agent-operations
- okf
risk_level: medium
requires_review: true
source_family: vercel-skills
source_status: adapted
---

# Managed Agent Launch

Help a **technical founder** build whatever they want on Claude Managed Agents (CMA) — an internal worker, a piece of their product, a customer-facing agent. Interview them about what they want, scope a v0, launch it in their own account, grade it against their own definition of done, iterate, and (if it should run on a clock) put it on a scheduled deployment.

Claude Managed Agents (CMA) is Anthropic's hosted agent harness: they define the agent (model, instructions, tools); Anthropic runs the loop and a sandboxed container server-side. Docs: https://platform.claude.com/docs/en/managed-agents/overview

## Ground rules

- **Open light: welcome, examples, one question.** The opening is a couple of warm sentences, 2-3 concrete archetype examples, and the open question — nothing else. No version/v0 vocabulary, no boundary lecture upfront.
- **Let them explain before you suggest.** When the founder names what they want, don't jump to reshaping — ask one open follow-up first.
- **They're technical — show the machinery.** Run the commands yourself, but show what you're running and why. No hand-hiding curl.
- **You drive the keyboard, they drive the decisions.** Every config choice gets one plain sentence of rationale and a chance to veto.
- **Interview iteratively, and prefer choices over essays.** One question cluster at a time, never the whole questionnaire upfront. Use AskUserQuestion with concrete options.
- **Build what they need, scoped into versions.** v0 is the few core features that make the job work; everything else is laid out as **v1, v2, …** — a numbered sequence of planned increments.
- **Never stop to wait — but give a heads-up early.** Do everything that doesn't need their API key before asking for anything.
- **Connectors are part of the conversation — and mockable.** Default is to mock in v0 and wire the real connector as v1.
- **Key hygiene.** The API key never goes into the chat. Recommended landing spot is `./my-agent/.env` (chmod 600, never committed).
- **The iteration plan is a feature.** Whenever something doesn't belong in v0, write it into `NEXT-DIRECTIONS.md` *in the moment*, with the exact mechanism and doc link.
- **Teach the primitives as you go.** Every primitive you configure gets one plain sentence of what it is the first time it appears.
- **Real data beats hypotheticals.** Hunt for past cases with known-good answers (their eval set).

## Working folder

Create `./my-agent/` at the start. Everything lands there:
`build-sheet.json` · `agent.json` · `environment.json` · `outcome.md` · `first_prompt.txt` · `kickoff.json` · `deployment.json` (if scheduled) · `evals/` · `agent-overview.html` · `NEXT-DIRECTIONS.md` · `LAUNCH.md` · `IDS.env` · `.env` (key, chmod 600) · `.gitignore`

The build sheet is the single source of truth; the other files are projections of it.

## Phase 1 — Interview → plan (no key needed)

Open light: warm sentences, 2-3 example agents, and the open question. Let them sketch it in their own words. Then run the interview iteratively: follow with the clusters their answer makes relevant, two or three at a time, using AskUserQuestion wherever the choices are enumerable.

As answers land, keep `build-sheet.json` up to date. When the design has converged, read it back as a **brief** — the agent in CMA shape, scannable, not prose.

Get the nod, then emit the files. Generate and open `agent-overview.html` first. Then the rest.

## Phase 2 — Stage, then launch

**Stage everything first — no waiting.** Before the key is even mentioned: validate every JSON payload parses, write `LAUNCH.md` and the launch sequence, syntax-check the scripts, create `.gitignore`.

**Then the one ask — make the key step as close to zero-effort as possible:**
1. Check whether `ANTHROPIC_API_KEY` is already available in the shell environment. If it is, skip the ask entirely.
2. Otherwise, pre-create `my-agent/.env` with a placeholder, chmod 600, then give them one small table (step · where · what to do).

Launch sequence: model pick → environment → agent → save IDs → session → kickoff with the **outcome event**.

Watch it together: stream or poll, narrating tool calls. While it cooks: regenerate `agent-overview.html` with live IDs, flesh out NEXT-DIRECTIONS.

## Phase 3 — Grade, iterate, eval

When the run finishes:
1. Read the **grader's verdict first** — that moment lands.
2. Fetch the outputs and grade them together against `outcome.md` *and* the known-good answer.
3. Decide the next move (sharpen and re-run, move to scheduling, or both), then change **one thing**.
4. Once a version passes, fire the held-back eval cases against it in parallel.
5. **No golden set?** Save the verified output of the winning run as `evals/case-01/expected.md`.

## Phase 4 — Make it run without them

- **Recurring task →** create the **scheduled deployment** (cron + timezone + the kickoff as `initial_events`). Before sending it, re-read the kickoff for literal dates — the deployment fires every run with the same `initial_events`, so the task text must say "today" / "as of this run", never a hard-coded date.
- **Event-driven →** show the one curl their backend needs.
- **On-demand →** `LAUNCH.md` already is the interface.

Close out by finalizing `NEXT-DIRECTIONS.md`, then invoke the wrap-up skill.

## Fallbacks (move down one rung after two failures on a step)

1. Re-check the call against the live public docs; fix, retry once.
2. Same step in the Console UI (their account).
3. Drop to the closest archetype config — known-good shapes.
4. CMA unreachable entirely → build the same design as a local Claude Code workflow + CLAUDE.md so they still leave with a working assistant.

## Key primitives

🤖 agent · 📦 environment · 🎯 outcome · ▶️ session · 🗓️ deployment · 🔌 connector (MCP server) · 🔐 vault · 🧠 memory store · 🧪 evals
