---
name: Doc Co-Authoring Workflow
description: Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers.
source: anthropics-skills (Apache-2.0 license, https://github.com/anthropics/skills)
category: productivity
tags: [productivity, documentation, co-authoring, workflow, technical-writing, specs]
type: Playbook
---

# Doc Co-Authoring Workflow

## Overview

This skill provides a structured workflow for guiding users through collaborative document creation. Act as an active guide, walking users through three stages: Context Gathering, Refinement & Structure, and Reader Testing.

## When to Use

- User mentions writing documentation: "write a doc", "draft a proposal", "create a spec", "write up"
- User mentions specific doc types: "PRD", "design doc", "decision doc", "RFC"
- User seems to be starting a substantial writing task

## The Three Stages

### Stage 1: Context Gathering

User provides all relevant context while you ask clarifying questions:

1. **What is the document about?** — Get the topic, purpose, and scope
2. **Who is the audience?** — Engineers, stakeholders, customers, future agents?
3. **What decisions need to be made?** — What's already decided vs. still open?
4. **What are the constraints?** — Timeline, format requirements, existing templates?
5. **What existing context exists?** — Related docs, code, previous discussions?

Ask one question at a time. Don't overwhelm the user with a long list.

### Stage 2: Refinement & Structure

1. **Draft the structure** — Propose an outline with section headings
2. **Fill in content** — Write each section based on gathered context
3. **Iterate** — Present drafts to the user for feedback, refine based on input
4. **Add detail** — Expand sections that need more depth
5. **Check completeness** — Ensure all questions from Stage 1 are answered

### Stage 3: Reader Testing

1. **Read from the reader's perspective** — Would they understand it without the conversation context?
2. **Check for assumptions** — Are there implicit assumptions that need to be made explicit?
3. **Verify actionability** — Can the reader act on this document?
4. **Test the structure** — Does the flow make sense? Can you skim it and get the gist?
5. **Final polish** — Fix grammar, formatting, and clarity issues

## Document Types

### Technical Spec / PRD
- Problem statement
- Proposed solution
- User stories / requirements
- Technical approach
- Out of scope
- Success criteria

### Decision Doc / ADR
- Context
- Decision
- Alternatives considered
- Consequences

### Design Doc
- Overview
- Architecture
- Data model
- API design
- UI/UX considerations
- Migration plan

## Tips

- Start with the structure before writing content
- Use the user's vocabulary and domain terms
- Include concrete examples where possible
- Make the document useful for future readers who weren't in the conversation
- Link to related documents and resources
