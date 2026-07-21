---
type: Skill
title: Public Skill Adoption
description: Use before installing, copying, vendoring, or authorizing a publicly available agent skill.
tags: [architectonic, core-skill, skills, supply-chain]
source_status: native
source_name: Architectonic reviewed core
source_license: Apache-2.0
risk_level: medium
requires_review: true
status: reviewed
---

# Public Skill Adoption

## Trigger

Use when a public skill, prompt package, procedure, MCP integration, or agent workflow is being considered for local use.

## Inputs

The exact source repository and revision, license, skill files, referenced scripts and tools, network and credential behavior, mutation scope, runtime targets, test evidence, and local authority policy.

## Procedure

1. Resolve the exact source, path, revision, author, and license; do not adopt from an unattributed copy.
2. Read the complete skill and every referenced script, command, dependency, template, and hidden instruction surface.
3. Classify network, shell, filesystem, credential, account, payment, production, destructive, and external communication effects.
4. Identify prompt injection, tool poisoning, data exfiltration, authority escalation, and unsafe default behavior.
5. Compare the procedure with local doctrine, privacy, permissions, and review gates.
6. Define representative inputs, expected outputs, verification, and failure cases.
7. Copy or vendor only the minimal reviewed material with preserved provenance and update policy.
8. Keep the skill disabled until an authorized local agent explicitly selects it within scope.
9. Re-review when the upstream revision, dependencies, tools, or local authority model changes.

## Verification

- Provenance and license are recoverable.
- Hidden scripts and tool calls have been inspected.
- Risk and authority boundaries are explicit.
- Representative tests and failure cases exist.
- Installation and authorization are separate decisions.
- Popularity is not used as capability or safety evidence.

## Failure Modes

- Trusting a skill because it is popular or published by a known organization.
- Reviewing only the top-level description.
- Granting credentials or production access during evaluation.
- Losing upstream provenance after copying.
- Allowing automatic updates to overwrite locally reviewed behavior.
