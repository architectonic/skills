---
type: Skill
title: Architecture Review
description: Use when checking a codebase for boundary drift or duplicated responsibility.
tags: [architectonic, core-skill]
source_status: native
source_name: Architectonic reviewed core
source_license: Apache-2.0
risk_level: low
requires_review: false
status: reviewed
---

# Architecture Review

## Trigger

Use when checking a codebase for boundary drift or duplicated responsibility.

## Inputs

The relevant sources, task boundary, authority context, and intended durable output.

## Procedure

1. Identify declared architectural boundaries.
2. Trace source-of-truth ownership and dependency direction.
3. Find duplicated invariants, circular authority, speculative abstractions, and unverified integration points.
4. Propose the smallest boundary repair and a verification plan.

## Verification

- Each finding names evidence, consequence, owner, and verification.

## Failure Modes

- Replacing working code with a larger architecture that has no demonstrated need.
