---
type: Source Profile
title: mattpocock/skills teach
description: Reviewed reference-only profile for the mattpocock/skills teach skill delta, focused on stateful mission-grounded lesson workspaces and reusable lesson components.
tags: [source-profile, skills, teaching, learning-workspace, reusable-components, reference-only, mattpocock]
okf_version: "0.2"
source_url: https://github.com/mattpocock/skills/tree/main/skills/productivity/teach
source_name: mattpocock/skills teach
source_author: Matt Pocock
license: MIT
runtime_targets: [claude-code, generic-agent]
skill_format: user-invoked-teaching-workspace-skill
risk_level: medium
ingestion_status: reference-only_with_normalizer_follow_up
reviewed_at: 2026-07-06
---

# mattpocock/skills teach

## What It Is

The `teach` entry in `mattpocock/skills` is a public user-invoked teaching skill for turning a local workspace into durable learning state. The visible upstream metadata names the skill `teach`, describes it as teaching a new skill or concept inside the current workspace, and disables model invocation for the skill surface.

The reviewed pattern is not the upstream prose or file templates. The reusable pattern is the operating model: treat learning as a stateful project, preserve the learner's mission, accumulate resources and learning records, produce small lesson artifacts, and reuse lesson components instead of creating one-off outputs.

## Why It Matters

This source is relevant to Architectonic skills because it adds a teaching/learning loop not already represented by the repo's currently reviewed Matt Pocock set. It is not just another prompt; it defines durable learning artifacts and a progression loop:

- mission capture before lesson design;
- explicit learning state rather than stateless Q&A;
- short lesson units tied to a concrete learner goal;
- reference artifacts that outlive a single lesson;
- learning records for non-obvious lessons and future calibration;
- reusable lesson components as a default architecture choice;
- separation between knowledge acquisition, skill practice, and real-world wisdom/community exposure.

## Provenance

- Repository: `mattpocock/skills`
- Default branch inspected: `main`
- Repository visibility: public
- Repository default branch observed through GitHub connector: `main`
- Repository size observed through GitHub connector: 662 KB
- License file inspected directly: MIT, copyright Matt Pocock, 2026
- Skill file inspected directly: `skills/productivity/teach/SKILL.md`, modified date observed by GitHub connector `2026-06-17T21:26:34Z`
- Changelog inspected directly: `CHANGELOG.md`, modified date observed by GitHub connector `2026-06-17T21:26:49Z`
- Changelog evidence: version `1.0.1` records a `teach` patch change making lessons reuse-first through shared components in `./assets/`

## License

MIT license found in the upstream repository license file. That permits reuse under the license terms, but this profile remains reference-only. No upstream lesson prose, formats, examples, assets, templates, component code, or supporting files were copied into Architectonic skills.

## Runtime Targets

The source appears to target skill-aware coding/agent runtimes that can invoke a user-facing slash-command-style skill and read/write local workspace files. The reviewed behavior is filesystem-heavy by design: it creates or maintains mission, resource, lesson, reference, learning-record, asset, and notes files.

This repository should not ingest the upstream file layout as an installable template. If normalized, the safe output should be a runtime-neutral playbook that teaches when and how to structure a learning workspace, what artifacts to maintain, and what safety boundaries to enforce before agents write files.

## Candidate Capabilities

Useful concepts for future original normalization, if converted narrowly and with attribution:

1. Mission-grounded teaching: capture why the learner wants the topic before deciding lesson sequence.
2. Learning state ledger: use durable learning records and notes to calibrate future lessons instead of treating each request as stateless.
3. Small lesson artifacts: produce tightly scoped lessons that create one concrete win rather than broad surveys.
4. Reference-first retention: maintain compact reference artifacts separately from lessons.
5. Reusable lesson components: prefer shared styles, quiz widgets, diagrams, and simulators over duplicated one-off lesson code.
6. Practice loop design: require feedback loops, retrieval practice, and spaced/interleaved practice where appropriate.
7. Wisdom boundary: separate what the agent can teach from what requires community or real-world practice.

## Risks

- Filesystem mutation risk: the upstream pattern expects the agent to create and update many local files. Any normalized version must require explicit workspace scope and avoid writing outside a declared learning workspace.
- Template-copy risk: the skill references supporting format files and artifact conventions. This repo should not copy those formats or templates; it should normalize the general doctrine only.
- Asset execution/browser risk: reusable lesson components can include HTML, scripts, widgets, or simulators. Any local equivalent must distinguish static reference artifacts from executable/interactive assets and avoid unsafe script execution.
- Citation/research risk: lessons can make knowledge claims. A normalized doctrine must require current trusted sources for factual teaching and must not rely only on model memory.
- Pedagogy overclaim risk: terms like storage strength, retrieval practice, spacing, and interleaving are useful design ideas, but a normalized skill must avoid claiming guaranteed learning outcomes.
- Community recommendation risk: recommending communities, classes, or groups may become current/local/advice-like. Any implementation should verify current sources and avoid unsafe or manipulative communities.
- Runtime boundary risk: because the upstream skill is user-invoked, it should not be silently triggered by broad model heuristics or used to write a course without clear learner intent.

## Ingestion Decision

Decision: `reference-only_with_normalizer_follow_up`.

Rationale: the source is public, MIT-licensed, current enough for watchlist review, and useful as a teaching-loop pattern. The safe value is a reviewed source profile plus a narrow original Normalizer queue item for a mission-grounded learning workspace playbook. Do not copy upstream prose, supporting format files, lesson examples, asset/component files, or skill body text.

## Next Action

Queue a Normalizer pass for an original Architectonic playbook on mission-grounded learning workspaces. It should teach the artifact model, lesson loop, reusable component boundary, verification requirements, and failure modes without copying upstream wording or templates.