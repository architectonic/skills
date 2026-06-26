---
name: session-usage-report
description: Generate an explorable HTML report of agent session usage (tokens, cache, subagents, skills, expensive prompts) from session transcripts. Use when the user wants to analyze agent usage patterns, review token consumption, identify expensive sessions, or generate a usage report. Adapted from anthropic-claude-plugins-official/session-report.
type: Playbook
---

# Session Usage Report

Produce a self-contained HTML report of agent usage and save it to the current working directory.

## Steps

1. **Identify session transcript location.** Check common paths:
   - Hermes: `~/.hermes/sessions/` or `~/.hermes/projects/`
   - Claude Code: `~/.claude/projects/`
   - Generic: Ask the user where session transcripts are stored.

2. **Analyze sessions.** If a bundled analyzer script is available, run it:
   ```sh
   node <skill-dir>/analyze-sessions.mjs --json --since 7d > /tmp/session-report.json
   ```
   For all-time, omit `--since`.

   If no analyzer is available, manually scan transcript files and extract:
   - Session ID, date, project
   - Input/output token counts
   - Cache hit rates
   - Subagent invocations
   - Skills used
   - Top prompts by token cost

3. **Read and summarize the data.** Look for:
   - Total token consumption
   - Per-project breakdown
   - Per-skill breakdown
   - Cache efficiency
   - Most expensive sessions/prompts
   - Anomalies (disproportionate consumption, low cache hits)

4. **Generate the report.** Create a self-contained HTML file with:
   - Summary hero (total tokens, sessions, date range)
   - Per-project breakdown table
   - Per-skill breakdown table
   - Top expensive sessions
   - Top expensive prompts
   - 3-5 key findings (anomalies, optimization opportunities)
   - 1-4 actionable optimization suggestions

5. **Save and report.** Write to `./session-report-YYYYMMDD-HHMM.html` in the current working directory. Report the file path to the user.

## Report Format

The HTML report should be:
- Self-contained (all CSS/JS inlined)
- Responsive (works on mobile and desktop)
- Sortable tables where applicable
- Include both data tables and visual bar charts
- Color-code findings: red for waste/anomalies, green for healthy, blue for neutral

## Key Metrics to Surface

- **Token efficiency**: cache hit rate, tokens per session
- **Cost concentration**: % of total from top sessions/skills
- **Subagent overhead**: tokens spent on subagent orchestration
- **Prompt bloat**: single prompts consuming disproportionate tokens
- **Skill utilization**: which skills are used most/least

## Source

Adapted from: `anthropic-claude-plugins-official/plugins/session-report/skills/session-report/SKILL.md`
Original license: MIT
