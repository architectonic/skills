---
type: Skill
name: mission-grounded-learning-workspace
title: Mission-Grounded Learning Workspace
description: Use when turning a learner's goal into a durable, workspace-scoped learning loop with explicit artifacts, source checks, lesson records, and safe file-write boundaries.
tags: [skill, teaching, learning-workspace, pedagogy, knowledge-work, agent-operations]
domain: agent-operations
timestamp: 2026-07-06T18:11:00-03:00
okf_version: "0.2"
source_status: normalized
source_name: mattpocock/skills teach source-profile synthesis
source_url: https://github.com/mattpocock/skills/tree/main/skills/productivity/teach
source_profile: sources/reviewed/mattpocock-teach.md
license: MIT reference source; this normalized skill is original Architectonic procedure text
risk_level: medium
requires_review: true
---

# Mission-Grounded Learning Workspace

## Trigger

Use this when a user asks to learn a topic, practice a skill, build a study plan, create lessons, or turn a project workspace into a durable learning environment.

Do not use this for a one-off factual answer, a generic course outline, motivational advice, or a topic where the learner has not given enough purpose to choose useful artifacts.

## Inputs

- Learner's concrete mission: what they want to be able to do, decide, build, explain, or practice.
- Current level and known constraints: time, tools, domain background, language, accessibility, and preferred medium.
- Workspace boundary: repository, folder, document, notebook, or other explicitly approved place where learning artifacts may be written.
- Source requirements for the topic: current documentation, primary sources, textbooks, papers, official references, or trusted domain sources.
- Safety and privacy boundaries: files that must not be read or changed, sensitive user notes, credential locations, and any topics that need professional review.
- Desired output shape: lesson, drill, reference sheet, worked example, quiz, implementation exercise, diagram, or progress ledger.

## Procedure

1. Restate the learner mission as an operational target: "After this loop, the learner should be able to...".
2. Define the workspace boundary before creating or editing any file. If no safe boundary exists, keep all learning output in the chat or a single user-approved document.
3. Create or update a compact learning ledger with the mission, current assumptions, source list, completed lessons, open questions, and next practice step.
4. Separate artifact types instead of mixing everything into one document:
   - mission record for goals and constraints;
   - source notes for cited references and uncertainty;
   - short lessons for one concrete concept or task;
   - reference sheets for durable lookup;
   - practice records for attempts, errors, feedback, and next drills;
   - optional reusable components for diagrams, examples, or exercises.
5. Before teaching factual or current material, check appropriate sources. Use model memory only for stable background knowledge or explicitly mark it as unverified.
6. Build the smallest useful lesson: one concept, one example, one practice task, and one verification step.
7. Tie every lesson back to the mission. Remove interesting but irrelevant material unless it is required to unblock the next practice step.
8. Prefer retrieval and practice over passive exposition. Ask the learner to recall, apply, compare, debug, derive, or produce something when that fits the topic.
9. Record non-obvious mistakes and corrections in the learning ledger so future lessons adapt to evidence, not vibes.
10. Keep reference artifacts concise. Move long explanations, source excerpts, and exploratory notes out of the primary reference sheet.
11. For reusable lesson components, distinguish static artifacts from executable or interactive assets. Do not add scripts, widgets, browser assets, or generated code unless the user explicitly requested them and the runtime boundary is safe.
12. End each loop with a next action: review, practice, build, test, ask for feedback, or consult an external community/human expert.

## Verification

A valid learning-workspace pass has all of the following:

- The learner mission is explicit and narrow enough to guide lesson selection.
- File writes, if any, stayed inside an approved workspace boundary.
- Factual claims that could be current, technical, legal, medical, financial, or otherwise sensitive cite appropriate sources or are marked as unverified.
- The created lesson has a concrete practice or verification step.
- The learning ledger records at least one of: completed lesson, source checked, misconception corrected, open question, or next practice task.
- Reference artifacts are concise enough to be reused later.
- The output distinguishes agent-teachable knowledge from wisdom, mentorship, certification, community feedback, or real-world practice that requires humans or external institutions.

## Failure Modes

- Starting with a syllabus before understanding the learner's mission.
- Writing files into a repository or workspace without explicit scope.
- Turning the lesson into a broad survey with no practice task.
- Treating model memory as sufficient for current or specialized topics.
- Copying external lesson formats, templates, examples, or assets instead of creating original artifacts.
- Creating interactive assets that execute scripts or fetch network resources without a safety review.
- Overclaiming learning outcomes because a lesson was generated.
- Recommending communities, courses, credentials, or mentors from memory without verifying they are current and safe.
- Letting the learning ledger become a dump of notes rather than a compact state record.

## Boundaries

- Do not read or summarize private learner notes unless the user explicitly provides or authorizes them.
- Do not create credentialed, professional, medical, legal, financial, aviation, security, or hazardous-skill instruction without appropriate safety constraints and source verification.
- Do not guarantee mastery, certification, employability, or outcome improvement.
- Do not copy third-party prose, templates, assets, examples, component files, or skill bodies into this repository.
- Do not silently trigger this skill; the user must be asking for learning, teaching, practice, or workspace-backed study.

## Provenance Note

This skill was normalized from the reviewed `mattpocock/skills teach` source profile as original Architectonic procedure text. The reusable lesson is the operating model: learner mission first, durable learning state, short practice-backed lessons, concise reference artifacts, source-aware teaching, reusable artifact boundaries, and explicit workspace-write scope. It is not an import of upstream wording, templates, lesson examples, assets, component files, command documentation, or skill body text.
