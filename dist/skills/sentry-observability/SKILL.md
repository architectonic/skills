---
name: Sentry Observability (Read-only)
description: Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI. Perform read-only queries using the `sentry` command.
source: openai-skills (MIT license, https://github.com/openai/skills)
category: software-development
tags: [devops, sentry, observability, production, errors, monitoring, read-only]
type: Playbook
---

# Sentry Observability (Read-only)

## Overview

Inspect Sentry issues and events using the Sentry CLI for read-only queries. This skill helps you understand production errors without modifying any Sentry configuration.

## When to Use

- The user asks to inspect Sentry issues or events
- The user wants a summary of recent production errors
- The user wants to pull basic Sentry health data
- You need to understand what's happening in production

## Prerequisites

- Sentry CLI installed: `curl https://cli.sentry.dev/install -fsS | bash`
- Authentication: `sentry auth login` or `SENTRY_AUTH_TOKEN` env var
- The CLI auto-detects org/project from DSNs in `.env` files, source code, config defaults, and directory names

## Core Tasks

### List Issues (ordered by most recent)

```bash
sentry issue list \
  --org <org> --project <project> \
  --env production \
  --limit 20 \
  --json
```

### Get Issue Details

```bash
sentry issue show <issue-id> \
  --org <org> --project <project> \
  --json
```

### List Events for an Issue

```bash
sentry event list <issue-id> \
  --org <org> --project <project> \
  --limit 10 \
  --json
```

### Get Event Details

```bash
sentry event show <event-id> \
  --org <org> --project <project> \
  --json
```

### Health Summary

```bash
# Recent issues count
sentry issue list --limit 1 --json | jq 'length'

# Issues by status
sentry issue list --limit 100 --json | jq 'group_by(.status) | map({status: .[0].status, count: length})'
```

## Defaults

- Time range: `24h`
- Environment: `production`
- Limit: `20`
- Always use `--json` when processing output programmatically
- Use `--json --fields` to select specific fields and reduce output size

## Tips

- Use `sentry schema <resource>` to discover API endpoints quickly
- Never ask the user to paste the full token in chat — ask them to set it locally
- If auto-detection fails, specify `<org>/<project>` explicitly
