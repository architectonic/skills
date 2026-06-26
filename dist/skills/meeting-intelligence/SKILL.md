---
name: meeting-intelligence
description: Prepare meeting materials by gathering context from knowledge bases, drafting agendas/pre-reads, and tailoring content to attendees. Use when the user wants to prep for meetings with structured agendas, context gathering, and attendee-specific materials. Works with or without Notion.
tags: [meetings, agenda, preparation, productivity]
source: openai/skills notion-meeting-intelligence (generalized beyond Notion)
type: Playbook
---

# Meeting Intelligence

Prep meetings by gathering context, tailoring agendas/pre-reads, and enriching with research.

## When to use
- User wants to prepare for an upcoming meeting
- Need to gather context from existing docs/knowledge bases
- Drafting agendas, pre-reads, or meeting materials
- Tailoring content to specific attendees

## Workflow

### 1. Gather inputs
- Confirm: meeting goal, desired outcomes/decisions, attendees, duration, date/time
- Ask for prior materials (notes, specs, OKRs, decisions)
- Identify blockers/risks and open questions up front

### 2. Gather context
- Search existing knowledge bases for relevant docs, past notes, specs, action items
- Fetch key pages/sections
- Pull attendee context (roles, prior contributions, current work)

### 3. Choose format
| Meeting type | Template |
|---|---|
| Status/update | Status template |
| Decision/approval | Decision template |
| Planning (sprint/project) | Planning template |
| Retro/feedback | Retrospective template |
| 1:1 | One-on-one template |
| Ideation | Brainstorming template |

### 4. Build the agenda/pre-read
Structure:
- **Context**: Background, links to relevant docs
- **Goals**: What we need to accomplish/decide
- **Agenda**: Items with owners and timeboxes
- **Decisions needed**: Explicit decision points
- **Risks/blockers**: Known issues to address
- **Prep asks**: What attendees should review before

### 5. Enrich with research
- Add concise research where helpful: market/industry facts, benchmarks, risks, best practices
- Keep claims cited with source links; separate fact from opinion

### 6. Finalize and share
- Add next steps and owners for follow-ups
- Create tasks for action items if needed
- Update the page/doc when details change; keep a brief changelog

## Tips
- Assign owners for each agenda item; call out timeboxes
- Include links to pulled context docs
- Keep pre-reads concise — respect attendees' time
- Flag decisions that need to be made during the meeting
