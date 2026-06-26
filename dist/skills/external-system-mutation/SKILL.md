---
name: external system mutation
description: External System Mutation Skill. Use when the agent needs to external system mutation.
tags: [agent-operations, agent-operations]
type: Playbook
---

## Trigger

Use before changing any external system: GitHub, databases, calendars, email, cloud services, deployments, payment systems, or production applications.

## Inputs

- Target system.
- Intended mutation.
- Current state, if readable.
- Rollback path or damage boundary.

## Procedure

1. Verify the exact target.
2. Read current state.
3. Identify the intended mutation.
4. Identify whether the change is reversible.
5. Perform the smallest necessary change.
6. Read back the resulting state.
7. Verify the mutation landed on the intended target.
8. Report evidence.

## Verification

The operation is not complete until the changed state has been read back from the target system.

## Failure Modes

- Writing to the wrong repo/account/project.
- Trusting UI-selected context.
- Assuming success from an API response alone.
- Making a broad mutation for a narrow request.
- Failing to record what changed.
