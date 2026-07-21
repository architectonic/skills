---
type: Skill
title: Document-Guided Organization Bootstrap
description: Use when establishing or repairing a human–AI organization by interrogating documents first and asking the human only where material gaps remain.
tags: [architectonic, core-skill, onboarding, grill-users-with-docs]
source_status: native
source_name: Architectonic reviewed core
source_license: Apache-2.0
risk_level: low
requires_review: false
status: reviewed
---

# Document-Guided Organization Bootstrap

## Trigger

Use when a human–AI organization, project, actor model, agent definition, or knowledge system is new, incomplete, stale, or internally inconsistent.

## Inputs

The organization map, local organization-owned documents, relevant source artifacts, current task, known authority boundaries, and the human responsible for unresolved decisions.

## Procedure

1. Run the organization map and inspect the smallest relevant local documents and upstream contracts.
2. Inspect recoverable source artifacts before asking the human for information.
3. Classify each material item as sourced fact, explicit human decision, inference, assumption, contradiction, or unknown.
4. Select the highest-value unresolved question: one whose answer changes a document, decision, risk, authority boundary, or justified action.
5. Ask the human with the relevant document gap and consequence visible. Use one question or one coherent batch; do not administer a generic questionnaire.
6. Record the explicit answer in its primary organization-owned file with date, scope, authority, and source status. Do not write local facts into upstream package files.
7. Preserve unresolved items in the open-question ledger instead of filling them by inference.
8. Verify the updated organization map, then stop when enough is known for the current work.

## Verification

- Every question names the document, decision, risk, or action it will change.
- No question asks for information already recoverable from inspected sources.
- Every durable answer is labeled as source-backed fact, explicit human decision, assumption, or unknown.
- Authority, approval, escalation, and stopping rights are explicit where material.
- Local organization files change; upstream contracts remain unmodified.
- The interview stops at a task-relevant sufficiency threshold.

## Failure Modes

- Asking a broad questionnaire before reading available documents.
- Treating an explicit human preference or decision as empirical evidence about the world.
- Converting temporary communication style or private biography into durable identity.
- Hiding unknowns behind polished prose.
- Continuing interrogation after the current work is sufficiently grounded.
- Editing installed package contracts to store organization-specific facts.
