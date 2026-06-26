---
type: Skill
title: Intent to Contract
description: Use when a human describes work informally, imprecisely, unusually, or with terms that may map to a more precise delivery artifact.
tags: [skill, intent, contract, clarification, scope, okf]
timestamp: 2026-06-26T00:00:00-03:00
okf_version: "0.1"
source_status: distilled
source_name: private dogfood skill pattern
risk_level: low
requires_review: false
---

# Intent to Contract

## Trigger

Use when a human describes work informally, imprecisely, unusually, or with domain terms that may map to a more precise delivery artifact.

## Purpose

Translate human intent into the correct working terminology without discarding the human's framing.

## Inputs

- Human wording.
- Current context.
- Relevant source artifacts, if any.
- Expected deliverable, if stated.

## Procedure

1. Capture the human's wording without replacing it too early.
2. Identify likely standard terms or delivery artifacts.
3. State the mapping explicitly.
4. Preserve any novel framing that may be useful.
5. Define the deliverable.
6. Define validity conditions.
7. Ask for confirmation before execution when the mapping changes scope.

## Examples

- `Milestone` may mean goal, phase, contract, or delivery checkpoint.
- `Plan` may mean implementation plan, patch contract, slice, handoff, or task breakdown.
- `Fix` may mean root-cause patch, workaround removal, refactor, or regression test.

## Verification

The human should be able to say: yes, that is what I meant, and now I understand the correct working term.

## Failure Modes

- Replacing the human's idea with standard jargon.
- Dismissing unusual framing that may be valuable.
- Over-explaining terminology instead of clarifying the deliverable.
- Executing before the contract is clear.
