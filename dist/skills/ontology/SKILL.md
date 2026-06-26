---
name: Ontology
description: Core entity model for classifying agent knowledge. Use when deciding whether information is a fact, assumption, decision, rule, question, or risk — and when determining what should become durable memory.
tags: [agent-operations, agent-operations, ontology, classification, knowledge-model, decision-framework]
type: Playbook
---

# Ontology

## Purpose

Define the core entities and relationships that agents use to classify, store, and retrieve knowledge. Without ontology, memory becomes a pile of notes — untyped, unscoped, and unranked.

## Core Entities

```
Human, Agent, Repository, Task, Plan, Action, Artifact,
Source, Claim, Fact, Assumption, Decision, Rule,
Question, Risk, Verification, Memory, Handoff, Boundary, Authority
```

## Claim Classes

Every claim about a project, task, system, or environment must be classified:

| Class | Meaning | Storage Rule |
|-------|---------|--------------|
| Fact | Backed by a recoverable source | Link to source; can become memory |
| Assumption | Provisional, not verified | Label clearly; do not treat as fact |
| Decision | Chosen direction with reason | Record when future agents need it |
| Rule | Durable instruction for future work | Keep rare; justify by repeated evidence |
| Question | Known unknown | Keep visible until answered or irrelevant |
| Risk | Potential failure or harm | Name before action; classify severity |

## Authority Ranking

When sources conflict, rank them:

```
1. Current user instruction
2. Current repository source files
3. Tests, typechecks, build output, CI, runtime evidence
4. Repo-local AGENTS.md
5. Repo contract
6. Accepted decision records
7. Current handoff
8. Memory facts with recoverable sources
9. Assumptions explicitly labeled
10. Agent inference
11. Model prior knowledge
```

Do not average conflicting sources into a compromise claim. Rank them explicitly.

## Memory Write Filter

Before writing durable memory, ask:

```
What entity is this about?
What claim is being made?
What source supports it?
What authority does the source have?
What lifecycle state should this claim occupy?
Who will need this later?
```

If those questions cannot be answered, the note belongs in scratch context, not durable memory.

## Relationship Model

```
Human assigns Task
Agent performs Action
Action modifies or produces Artifact
Artifact may contain Source
Source supports Claim
Claim is classified as Fact, Assumption, Decision, Rule, Question, or Risk
Verification strengthens or rejects Claim
Memory preserves selected durable Claims
Handoff transfers Task state
Boundary constrains Action
Authority ranks Sources and Claims
```

## Trigger

Use this skill when:
- An agent wants to write new durable memory
- Classifying information found during work
- Deciding between storing and discarding a note
- Resolving a conflict between two sources
- Determining whether a claim needs verification before action

## Procedure

1. Identify the entity the information is about (Human, Task, Artifact, etc.).
2. Classify the claim: Fact, Assumption, Decision, Rule, Question, or Risk.
3. Identify the source and its authority rank.
4. Determine the lifecycle state (Observation → Assumption → Verified Fact → Decision → Rule).
5. Decide: durable memory or scratch context?
6. If durable, write with source link and claim class label.
7. If not durable, keep in session context only.

## Verification

- Every durable memory entry has a claim class and source link.
- No assumption is stored as a fact.
- Questions remain visible until resolved.
- Authority conflicts are ranked explicitly, not blended.

## Failure Modes

- Storing assumptions as facts → false confidence
- Mixing memory scopes (public vs private) → privacy risk
- Writing without source link → unverifiable claims
- Promoting every observation → memory landfill
- Not classifying claims → inability to reason about reliability

## Security Notes

- Low risk: ontology is a classification framework, not a procedure.
- The main risk is misclassification — treating an assumption as a fact.
- Apply the memory write filter before every durable write.

## Sources

- curator/root-meta/ontology.md — full entity model and operating implications
- curator/legacy/root-meta/authority.md — authority hierarchy
- curator/legacy/cognition/decision_principles.md — decision procedure
