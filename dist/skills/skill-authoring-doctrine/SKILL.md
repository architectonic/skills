---
name: skill-authoring-doctrine
description: Doctrine for writing and editing high-quality agent skills. Use when authoring new skills, reviewing existing skills, or diagnosing skill failure modes. Covers predictability as the root virtue, context load vs cognitive load tradeoffs, information hierarchy, failure modes (premature completion, duplication, sediment, sprawl, no-op), leading words, and pruning discipline.
tags: [skill-management, skill-management, skill-authoring, doctrine, predictability]
type: Reference
---

# skill-authoring-doctrine

Doctrine for writing high-quality agent skills. Extracted from mattpocock/skills `writing-great-skills` (MIT license, https://github.com/mattpocock/skills).

## Root Virtue: Predictability

A skill exists to wrangle determinism out of a stochastic system. **Predictability** — the agent taking the same _process_ every run, not producing the same output — is the root virtue. Every lever below serves it.

## Invocation Model

Two choices, trading different costs:

- **Model-invoked** skill: keeps a `description`, so the agent can fire it autonomously. Contributes to **context load** (description sits in the window every turn). Pick only when the agent must reach the skill on its own.
- **User-invoked** skill: `disable-model-invocation: true`, strips the description. Zero context load, but spends **cognitive load** (the human must remember it exists). Fires only when the user types its name.

When user-invoked skills multiply past what a human can remember, the cure is a **router skill** — one user-invoked skill that names the others and when to reach for each.

## Information Hierarchy

Content ranked by how immediately the agent needs it:

1. **In-skill step** — ordered action in SKILL.md (primary tier). Each step ends on a **completion criterion**.
2. **In-skill reference** — definition/rule/fact in SKILL.md, consulted on demand.
3. **External reference** — pushed into a separate file behind a **context pointer**, loaded only when the pointer fires.

Push too little down → top bloats. Push too much → hide material the agent needs.

**Progressive disclosure**: move reference down the ladder so the top stays legible. Inline what every branch needs; push behind a pointer what only some branches reach.

## Writing the Description (Model-Invoked Skills)

The description does two jobs: state what the skill is, and list the **branches** that should trigger it.

- Front-load the skill's leading word.
- One trigger per branch. Synonyms that rename a single branch = duplication.
- Cut identity that's already in the body.

## Completion Criteria

A completion criterion should be:
- **Checkable**: can the agent tell done from not-done?
- **Exhaustive**: "every modified model accounted for" not "produce a change list"

A vague criterion invites **premature completion**. A demanding criterion drives thorough **legwork**.

## Leading Words

A **leading word** is a compact concept already living in the model's pretraining (e.g. _lesson_, _fog of war_, _tracer bullets_). It anchors behavior in the fewest tokens by recruiting priors the model already holds.

Serves predictability twice:
- In the body → anchors **execution** (same behavior every time the word appears)
- In the description → anchors **invocation** (agent fires it when it sees the word in context)

## When to Split Skills

- **By invocation**: split off a model-invoked skill when you have a distinct leading word that should trigger it on its own, or another skill must reach it.
- **By sequence**: split a run of steps when the steps ahead tempt the agent to rush the current step (premature completion).

## Pruning Discipline

- Keep each meaning in a **single source of truth**.
- Check every line for **relevance**: does it still bear on what the skill does?
- Hunt **no-ops**: does the line change behavior vs. the model's default?
- When a sentence fails the no-op test, delete the whole sentence — don't trim words.

## Failure Modes

| Mode | Cause | Cure |
|------|-------|------|
| **Premature completion** | Agent ends step before it's done; attention slips to being done | Sharpen completion criterion first (cheap, local); hide post-completion steps only if criterion is irreducibly fuzzy |
| **Duplication** | Same meaning in more than one place | Consolidate to single source of truth |
| **Sediment** | Stale layers accumulate because adding feels safe and removing feels risky | Regular pruning discipline |
| **Sprawl** | Skill too long, even when all lines are live and unique | Push reference behind context pointers; split by branch or sequence |
| **No-op** | Line tells the model what it already does by default | Delete it; replace weak leading words with stronger ones |
