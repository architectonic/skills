---
name: Markdown Mermaid Writing
description: Comprehensive markdown and Mermaid diagram writing standard. Use when creating any document, report, analysis, or visualization. Establishes text-based diagrams as the default documentation format with full style guides (markdown + mermaid), 24 diagram type references, and 9 document templates.
source: K-Dense-AI/scientific-agent-skills (MIT)
original-author: Clayton Young / Superior Byte Works, LLC (@borealBytes)
distilled: 2026-06-23
type: Reference
---

# Markdown & Mermaid Writing

## When to Use

- Creating **any document** — reports, analyses, manuscripts, READMEs, decision records
- Writing **any documentation** — how-tos, project docs
- Producing **any diagram** — workflows, architectures, timelines, relationships
- Generating **any output that will be version-controlled**
- Someone asks you to "add a diagram" or "visualize the relationship"

**Golden rule:** Mermaid in Markdown first, always. Images are Phase 2/3 optional conversions.

## Source Format Philosophy

| What matters | Mermaid in Markdown | Python / AI Image |
|---|---|---|
| Git diff readable | ✅ | ❌ binary blob |
| Editable without regenerating | ✅ | ❌ |
| Token efficient vs. prose | ✅ smaller | ❌ larger |
| Renders without build step | ✅ | ❌ needs hosting |
| Parseable by AI without vision | ✅ | ❌ |
| Works in GitHub/GitLab/Notion | ✅ | ⚠️ if hosted |
| Accessible (screen readers) | ✅ accTitle/accDescr | ⚠️ needs alt text |
| Convertible to image later | ✅ anytime | — already image |

## Three-Phase Workflow

**Phase 1 (MANDATORY):** Create Mermaid in Markdown — this is the source of truth.
**Phase 2 (optional):** Python-generated data charts when Mermaid can't express it (scatter plots with real data).
**Phase 3 (optional):** AI-generated visuals for polish.

The Mermaid source always stays committed even if you proceed to Phase 2/3.

## 24 Mermaid Diagram Types

Match the relationship to the type — don't default to flowcharts for everything:

| Use case | Diagram type |
|---|---|
| Workflow / decision logic | Flowchart |
| Service interactions / API calls | Sequence |
| Data model / schema | ER diagram |
| State machine / lifecycle | State |
| Project timeline / roadmap | Gantt |
| Proportions / composition | Pie |
| System architecture (zoom levels) | C4 |
| Concept hierarchy / brainstorm | Mindmap |
| Chronological events | Timeline |
| Class hierarchy / type relationships | Class |
| User journey | User Journey |
| Two-axis comparison / prioritization | Quadrant |
| Requirements traceability | Requirement |
| Flow magnitude / resource distribution | Sankey |
| Numeric trends / bar + line charts | XY Chart |
| Component layout / spatial arrangement | Block |
| Work item status / task columns | Kanban |
| Cloud infrastructure / service topology | Architecture |
| Multi-dimensional comparison | Radar |
| Hierarchical proportions / budget | Treemap |
| Binary protocol / data format | Packet |
| Git branching / merge strategy | Git Graph |
| Code-style sequence | ZenUML |
| Multi-diagram composition | Complex Examples |

## Core Workflow

1. **Identify document type** — use a template (see below)
2. **Read the style guide** before writing any `.md` file
3. **Pick the diagram type** and read its guide
4. **Write the document** — start from template, apply style guide, place diagrams inline
5. **Commit as text** — the `.md` file with embedded Mermaid is what gets committed

## Document Templates

| Document type | Template |
|---|---|
| Pull request record | `templates/pull_request.md` |
| Issue / bug / feature request | `templates/issue.md` |
| Sprint / project board | `templates/kanban.md` |
| Architecture decision (ADR) | `templates/decision_record.md` |
| Presentation / briefing | `templates/presentation.md` |
| Research paper / analysis | `templates/research_paper.md` |
| Project documentation | `templates/project_documentation.md` |
| How-to / tutorial | `templates/how_to_guide.md` |
| Status report | `templates/status_report.md` |

## Markdown Style Rules

- **One H1 per document** — the title
- **Emoji on H2 headings only** — one emoji per H2, none in H3/H4
- **Cite everything** — every external claim gets `[^N]` with full URL
- **Bold sparingly** — max 2-3 bold terms per paragraph
- **Horizontal rule after every `</details>`** — mandatory
- **Tables over prose** for comparisons, structured data
- **Diagrams over walls of text** — if it describes flow/structure/relationships, add Mermaid

## Mermaid Rules

Every diagram must start with:
```
accTitle: Short Name 3-8 Words
accDescr: One or two sentences explaining what this diagram shows.
```

- **No `%%{init}` directives** — breaks GitHub dark mode
- **No inline `style`** — use `classDef` only
- **One emoji per node max** — at the start of the label
- **`snake_case` node IDs** — match the label
- **radar-beta** not `radar` (bare keyword doesn't exist)

## Integration with Other Skills

- **scientific-schematics**: Use Mermaid as the brief for AI-powered PNG generation
- **scientific-writing**: All diagrams in manuscripts should use this skill's standards
- **literature-review**: Create concept maps (Mindmap), publication timelines (Timeline), methodology comparisons (Quadrant)
- **Any skill**: Before finalizing any document, apply this skill's checklist

## Attribution

Ported from SuperiorByteWorks-LLC/agent-project (Apache-2.0), authored by Clayton Young (@borealBytes), integrated into K-Dense-AI/scientific-agent-skills (MIT).
