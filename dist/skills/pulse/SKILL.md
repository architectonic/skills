---
name: pulse
description: Multi-source recency research — takes the pulse of any topic across Reddit, Hacker News, and the open web within a configurable recent window (default 30 days). Forcing intake clarifies topic specificity, angle (trend/sentiment/problems/opportunities/comparison), time window, and platform scope. Returns a synthesized briefing with citations, engagement metrics, and cross-platform pattern analysis. Use when the user requests multi-source recency intelligence (e.g., 'pulse on [topic]', 'what's happening with [topic]', 'what are people saying about [topic]').
type: Metric
---

# Pulse — Multi-Source Recency Research

A recency-oriented research skill that synthesizes what people are saying about a topic across Reddit, Hacker News, and the open web — within a configurable time window. Output is a single coherent briefing with citations, engagement signals, and cross-platform pattern analysis.

## Invocation Triggers

- "pulse on [topic]"
- "what's happening with [topic]"
- "what are people saying about [topic]"
- "current conversation about [topic]"
- "take the pulse of [topic]"
- "trending: [topic]"

Also covers: competitor research, trend discovery, tool comparisons, audience sentiment analysis.

## Agent Integrity Rules

- **Execution discipline.** Phases 1–3 run in parallel (Reddit + HN + Web are independent). Within each phase, sequential calls only. 1 q/sec rate limit per platform.
- **Source discipline.** Cite only sources returned by this session's tool calls. Training knowledge labeled `[Background — not from search]` and excluded.
- **Three-count tracking.** Queries sent / sources received / sources cited.
- **Retry policy.** On failure → wait 3s → retry once → log. After 3 consecutive failures: stop, alert user.

## Phase 0: Grill-Me Intake (2–4 forcing questions, one at a time)

### Q1 (root) — Topic Specificity

> **What's the topic? State it in 1–2 sentences — be specific. "AI" or "tech" will get you a vague survey; "self-hosted LLM deployment for small teams" will get you a useful answer.**

**Refuse mush.** If the user says "AI", push back once: "What about AI — adoption, safety, capability, regulation, or comparison?"

### Q2 (depends on Q1) — Angle

> **What angle matters most? Pick one:**
> 1. **Trend** — what's accelerating or decelerating
> 2. **Sentiment** — what people feel about it
> 3. **Problems** — pain points and complaints
> 4. **Opportunities** — gaps and unmet needs
> 5. **Comparison** — how it stacks up against alternatives

### Q3 (always) — Time Window

> **Time window: 7 / 14 / 30 / 60 / 90 days? Default is 30.**

### Q4 (depends on Q1) — Platform Scope

> **Any platform to skip? Default: Reddit + Hacker News + open web.**

**Stop condition:** After Q4 (or earlier with dependency skips), commit and start Phase 1.

## Phase 1: Reddit (parallel with HN + Web)

**API:** `reddit.com/search.json` (unauthenticated, public JSON).

**Queries (sequential within Reddit, 1 q/sec):**
1. `sort=top&t=<window>&q=<topic>` — top posts in window
2. `sort=new&t=<window>&q=<topic>` — new posts in window
3. For top 3–5 posts by score: fetch comments JSON for top 10–20 comments

Throttle to 1 q/sec. If 429, wait 3s, retry once.

## Phase 2: Hacker News (parallel with Reddit + Web)

**API:** Algolia HN search (`hn.algolia.com/api/v1/`).

**Queries (sequential within HN, 1 q/sec):**
1. `search?query=<topic>&numericFilters=created_at_i><timestamp>&tags=story`
2. `search?query=<topic>&numericFilters=created_at_i><timestamp>&tags=comment`

**HN bias note:** HN skews technical / builder. Surface this in synthesis.

## Phase 3: Web Search (parallel with Reddit + HN)

**Query strategy (sequential within Web, 1 q/sec):**
1. **Trusted publishers** — `"<topic>" site:nytimes.com OR site:wsj.com OR site:wired.com OR site:theverge.com OR site:techcrunch.com after:<date>`
2. **Recent reviews** — `"<topic>"`
3. **Honest-opinion sources** — `"<topic>" problems OR complaints OR "worth it" after:<date>`

Fetch the top 3–5 URLs per query. Every claim must trace to a fetched URL.

## Synthesis (Cross-Platform Patterns)

After Phases 1–3 complete, produce the synthesis:

1. **Consensus signals** — points where 3+ platforms agree (highest confidence)
2. **Controversy signals** — points where platforms disagree
3. **Pain points** — recurring complaints (esp. Reddit + Web)
4. **Excitement signals** — recurring enthusiasm (esp. HN)
5. **Emerging trends** — first-time mentions in newest posts but absent from older ones
6. **Gaps** — what's notably absent that you'd expect to find

For each pattern, **cite the source URLs** that support it.

## Output Format

```markdown
# [TOPIC] — Pulse (Last [N] Days)
*Generated: [DATE] | Angle: [Q2 choice]*

## TL;DR
[2-3 sentences max]

## Reddit
### Top Posts
- **[Title]** (r/sub) — [score, comments] — [summary] — [URL]
### What Reddit Is Saying
[Narrative paragraph]

## Hacker News
### Notable Stories
- **[Title]** — [points, comments] — [summary] — [URL]
### What HN Is Saying
[Narrative paragraph; note HN's technical/builder bias]

## Web
### Key Sources
- **[Title]** ([Publication]) — [takeaway] — [URL]
### What the Web Is Saying
[Narrative paragraph]

## Cross-Platform Patterns
[Highest-confidence signals across sources]

## Key Takeaways
- [3-5 bullets]

---
*Audit:* Queries sent: N (Reddit: a, HN: b, Web: c).
Sources received: M. Sources cited: K.
```

## Anti-Patterns To Reject

- Starting any search before the user commits to topic specificity
- Batching intake questions
- Citing training knowledge in the cited count
- Fabricating sources to fill out a section

---

**Version:** 1.0.0 (distilled 2026-07-23)
**Source:** claude-skills/research/pulse — MIT License
