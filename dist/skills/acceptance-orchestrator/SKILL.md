---
name: acceptance-orchestrator
description: Orchestrate coding work as a state machine from issue intake through implementation, review, deployment, and acceptance verification. Core rule: optimize for DoD proven, not code changed.
type: Playbook
---

# Acceptance Orchestrator

Orchestrate coding work as a state machine that ends only when acceptance criteria are verified with evidence or the task is explicitly escalated.

**Core rule: do not optimize for "code changed"; optimize for "DoD proven".**

## Use this skill when

- The task has an issue or clear acceptance criteria and should run end-to-end with minimal human re-intervention
- You need structured handoff across implementation, review, deployment, and final verification
- You want explicit stop conditions and escalation instead of silent partial completion

## Do not use this skill when

- The task is a simple one-step change without acceptance criteria
- You don't have an issue or clear DoD to work from

## Required Sub-Skills

- `create-issue-gate` — validate issue is ready before starting
- `closed-loop-delivery` — implement and locally verify
- `verification-before-completion` — no success claims without evidence

Optional supporting skills: `deploy-dev`, `pr-watch`, `pr-review-autopilot`, `git-ship`

## Inputs

Required:
- Issue ID or issue body
- Issue status
- Acceptance criteria (DoD)
- Target environment (`dev` default)

Fixed defaults:
- Max iteration rounds: `2`
- PR review polling: `3m → 6m → 10m`

## State Machine

```
intake → issue-gated → executing → review-loop → deploy-verify → accepted
                                    ↓
                                escalated
```

## Workflow

### 1. Intake
- Read issue and extract task goal + DoD.

### 2. Issue Gate
- Use `create-issue-gate` logic.
- If issue is not `ready` or execution gate is not `allowed`, stop immediately.
- **Do not implement anything while issue remains `draft`.**

### 3. Execute
- Hand off to `closed-loop-delivery` for implementation and local verification.

### 4. Review Loop
- If PR feedback is relevant, batch polling windows:
  - Wait `3m` → then `6m` → then `10m`
- After the `10m` round, stop waiting and process all visible comments together.

### 5. Deploy and Runtime Verification
- If DoD depends on runtime behavior, deploy only to `dev` by default.
- Verify with real logs/API behavior, not assumptions.

### 6. Completion Gate
- Before any claim of completion, require `verification-before-completion`.
- **No success claim without fresh evidence.**

## Stop Conditions

**Move to `accepted`** only when every acceptance criterion has matching evidence.

**Move to `escalated`** when any of these happen:
- DoD still fails after `2` full rounds
- Missing secrets/permissions/external dependency blocks progress
- Task needs production action or destructive operation approval
- Review instructions conflict and cannot both be satisfied

## Human Gates

Always stop for human confirmation on:
- Prod/stage deploys beyond agreed scope
- Destructive git/data operations
- Billing or security posture changes
- Missing user-provided acceptance criteria

## Output Contract

When reporting status, always include:

| Field | Description |
|-------|-------------|
| **Status** | intake / executing / accepted / escalated |
| **Acceptance Criteria** | pass/fail checklist |
| **Evidence** | commands, logs, API results, or runtime proof |
| **Open Risks** | anything still uncertain |
| **Need Human Input** | smallest next decision, if blocked |

**Do not report "done" unless status is `accepted`.**

## Source

Distilled from `antigravity-awesome-skills/skills/acceptance-orchestrator/SKILL.md` (community contribution, 2026-03-12).
