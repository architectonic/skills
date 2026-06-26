---
name: Repo Contract
description: Define project identity, agent permissions, source-of-truth locations, and done criteria for a repository. Use when onboarding an agent into a new project or establishing project boundaries.
tags: [agent-operations, agent-operations, onboarding, contract, boundaries, permissions]
type: Playbook
---

# Repo Contract

## Purpose

A repo contract tells an agent what it may change, what it must not touch, where truth lives, and when work is done. Fill this in with real project values when onboarding.

## Project Identity

```
Project name:
Project type:
Primary users:
Primary runtime:
Primary language/framework:
Deployment target:
```

## Source of Truth

```
Product requirements:
Architecture decisions:
Issue tracker:
Design system:
API contract:
Database schema:
Deployment config:
```

## Agent Permissions

### The agent may change:
- documentation files
- tests related to the requested task
- implementation files directly required by the task
- examples and templates when explicitly requested

### The agent must ask before changing:
- authentication or authorization
- billing or payments
- database migrations
- production deployment config
- secrets or environment variable names
- public API contracts
- destructive scripts
- legal, compliance, or licensing text

## Definition of Done

A task is complete when:
1. the named problem is addressed
2. relevant tests or checks were run, or the reason they could not run is stated
3. changed files are listed
4. risks and unknowns are stated
5. no private data or secrets were added

## Non-Goals

Record what the project is not trying to do. This prevents scope drift.

```
Non-goal 1:
Non-goal 2:
Non-goal 3:
```

## Template Usage

Copy this file into a real project and replace all placeholders. Remove sections that do not apply. Keep examples generic.
