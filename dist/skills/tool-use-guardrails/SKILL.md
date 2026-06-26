---
name: Tool Use Guardrails
description: Discipline for using tools that mutate external state. Use before any tool call that modifies files, systems, or data outside the agent's immediate context.
tags: [agent-operations, agent-operations, safety, tool-use, verification]
type: Playbook
---

# Tool Use Guardrails

## General Rule

Do not mutate external systems until the target and intended change are clear.

External systems include: GitHub repositories, databases, cloud services, calendars, email, deployment platforms, payment systems, production applications.

## Before Tool Use

1. Identify the target.
2. Identify the operation.
3. Identify expected output.
4. Identify whether the operation is read-only or mutating.
5. Ask before risky mutations.

## After Mutation

1. Read back the changed state.
2. Compare it to the intended state.
3. Report evidence.
4. State remaining risks.

## Never Do This

- Do not trust UI-selected repo/account context without verification.
- Do not force-push unless explicitly authorized.
- Do not delete data without explicit confirmation.
- Do not expose secrets in logs or examples.
- Do not perform broad cleanup when the task requires a narrow fix.

## Tool Report Template

```
Tool used:
Target:
Operation:
Result:
Read-back verification:
Risk:
```

## Sources

- curator/legacy/root-meta/tool_use_guardrails.md — original guardrails
- skills/agent-operations/external-system-mutation.md — external system specific procedure
