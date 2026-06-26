---
name: Signal Detector
description: Always-on ambient signal capture for ideas and entities. Fires on every inbound message to detect original thinking (user's ideas, observations, theses) and entity mentions (people, companies, concepts). Runs in parallel, never blocks the main response. Captures the user's exact phrasing — ideas are intellectual capital.
source: gbrain/skills/signal-detector/SKILL.md (MIT license, https://github.com/byungkyu/gbrain)
category: agent-operations
tags: [agent-operations, signal-detection, ambient-capture, ideas, entities, always-on, brain]
type: Playbook
---

# Signal Detector — Ambient Capture

## Purpose

Lightweight always-on skill that fires on every inbound message to capture TWO things with EQUAL priority:

1. **Original thinking** — the user's ideas, observations, theses, frameworks
2. **Entity mentions** — people, companies, media references

Original thinking is AT LEAST as valuable as entity extraction. Ideas are the intellectual capital. Entities are bookkeeping. Both compound over time.

## Contract

- Fires on every message (no exceptions unless purely operational)
- Runs in parallel (spawned, never blocks main response)
- Captures ideas with the user's EXACT phrasing (no paraphrasing)
- Detects entity mentions and creates/enriches knowledge pages
- Logs a one-line summary of what was captured
- Back-links all entity mentions
- Citations on every fact written

## Phases

### Phase 1: Idea/Observation Detection (PRIMARY)

When the user expresses a novel thought, observation, thesis, or framework:
- If it's the user's **original thinking** → capture to `originals/{slug}`
- If it's a **world concept** they're referencing → capture to `concepts/{slug}`
- If it's a **product or business idea** → capture to `ideas/{slug}`

**Capture exact phrasing.** The user's language IS the insight. Don't paraphrase.

**Cross-linking (MANDATORY):** Every original MUST link to related people, companies, meetings, and concepts.

### Phase 2: Entity Detection (SECONDARY)

1. Extract entity mentions (people, companies, media titles)
2. For each entity:
   - Check if a knowledge page already exists
   - If no page → check notability, create with enrichment if notable
   - If page exists but thin → trigger enrich
   - If page exists and rich → no action
3. For new facts with specific dates → add timeline entry

### Phase 3: Signal Logging

Always log a one-line summary:
- `Signals: 0 ideas, 0 entities (skipped: operational)`
- `Signals: 1 idea (captured → originals/x), 2 entities (enriched → people/y, companies/z)`

## Output

No visible output to the user. This skill runs silently in the background.
The output is knowledge pages created/updated and the signal log line.

## Anti-Patterns

- Blocking the main response to wait for signal detection
- Paraphrasing the user's original thinking instead of capturing exact phrasing
- Creating pages for non-notable entities (one-off mentions)
- Skipping back-links after creating/updating pages
- Running on purely operational messages ("ok", "thanks", "do it")
