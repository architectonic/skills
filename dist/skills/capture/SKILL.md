---
name: Capture
description: Save any thought or content into persistent knowledge storage via one command. The single human-facing ingestion entrypoint that handles both local and remote installs. Use when the user says "capture this", "save this thought", "remember this", or "save to brain".
source: gbrain/skills/capture/SKILL.md (MIT license, https://github.com/byungkyu/gbrain)
category: agent-operations
tags: [agent-operations, capture, ingestion, brain, knowledge, save, remember]
type: Playbook
---

# Capture — Single Ingestion Entrypoint

## Purpose

When the user wants to save a thought, an article snippet, a transcript fragment, or any text into persistent knowledge storage, use the capture pattern. This is the front door — it handles local and remote storage the same way.

## Contract

- **Input:** the content to save (inline, file, or stdin)
- **Output:** a page in knowledge storage AND a markdown file on disk
- **Idempotency:** same content → same slug (content-hash dedup)
- **Trust:** all captures via this skill are local-CLI trust

## When to Invoke

- "Capture this thought" / "save this" / "remember this"
- The user pastes content and asks to keep it
- After a meeting summary, research note, or any synthesis worth keeping

## How to Use

```bash
# Inline capture
capture "the thought I want remember"

# From file
capture --file ./notes/today.md

# From pipe
echo "from a pipe" | capture --stdin

# Custom slug
capture "..." --slug daily/2026-05-21

# With type
capture "..." --type idea --source voice-whisper

# Script-friendly (prints just the slug)
capture "..." --quiet

# Structured output for agents
capture "..." --json
```

## Defaults

- **Slug:** `inbox/YYYY-MM-DD-<hash8>` (stable for same content; dedup catches re-captures)
- **Type:** `note` (override with `--type idea` etc.)
- **Title:** first non-empty line of the body, capped at 80 chars

## Output

Default prints a receipt:
```
captured:
  slug:          inbox/2026-05-21-abcdef12
  status:        created_or_updated
  content_hash:  f3a7b9c0d1e2f3a4…
  file:          /path/to/brain/inbox/2026-05-21-abcdef12.md
  captured_at:   2026-05-21T04:15:00.000Z
```

## Anti-Patterns

- **Don't use bulk import for single thoughts.** Capture is for single thoughts/notes.
- **Don't pre-format content with frontmatter** unless needed. Capture wraps plain prose in sensible frontmatter.
- **Don't pass secrets as inline content** (lands in shell history). Use `--file` or `--stdin`.

## When NOT to Use

- Bulk ingestion of many files → use bulk import/sync instead
- Article/link with author + publication metadata → use idea-ingest
- Meeting transcripts → use meeting-ingestion

This skill is for the simple "I have a thought, save it" case.
