---
name: Canonicalization
description: Convert useful information into durable project knowledge. Use when deciding whether to promote an observation to canonical memory, what form it should take, and how to store it.
tags: [agent-operations, agent-operations, memory, canonicalization, knowledge-management]
type: Playbook
---

# Canonicalization

## Principle

Not every observation deserves permanent storage. Canonicalization is the process of converting useful information into durable project knowledge.

## Trigger

Use when:
- An agent wants to store a lesson, fact, or rule
- Deciding whether a note belongs in durable memory
- Converting raw observations into structured memory
- Reviewing existing memory for continued relevance

## Promote

Promote to canonical memory:
- verified facts;
- durable rules;
- stable constraints;
- architectural decisions;
- recurring failure corrections;
- validated terminology.

## Do Not Promote

Do not promote:
- moods;
- temporary plans;
- speculation;
- one-off conversations;
- unsupported assumptions;
- stale implementation details.

## Procedure

1. **Classify the information.** Is it a fact, decision, rule, assumption, or question?
2. **Verify the source.** A fact without a recoverable source is an assumption.
3. **Remove temporary context.** Strip session-specific details that will not help a future reader.
4. **Store the smallest durable version.** If a sentence captures the lesson, do not write a paragraph.
5. **Link to the source when possible.** Future agents should be able to re-verify.

## The Six-Month Test

If the information would still be useful six months from now, it is a candidate for canonical memory. If not, keep it in scratch context or discard it.

## Verification

- Every canonical entry has a source link or explicit provenance.
- No temporary context remains in stored memory.
- The entry is the smallest durable version (not bloated with irrelevant detail).

## Failure Modes

- Promoting everything → memory landfill, future agents cannot distinguish signal from noise.
- Promoting unverified claims → false confidence in stale or incorrect information.
- Storing too much context → maintenance burden, stale details mislead future work.
- Never promoting → repeated mistakes, lost lessons.

## Security Notes

- Low risk: canonicalization is a knowledge management discipline.
- Medium risk: promoting unverified claims can cause future agents to act on false premises.
