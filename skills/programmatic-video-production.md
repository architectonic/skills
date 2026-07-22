---
type: Workflow
title: Programmatic Video Production
description: Use when creating, editing, captioning, converting, or rendering video through code or an agent-driven video framework, especially when assets, dependencies, credentials, external services, compute costs, or publication require explicit control.
tags: [workflow, media, video, animation, rendering, captions, provenance, accessibility, verification, high-risk, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled-reviewed
source_name: Architectonic synthesis of reviewed HyperFrames and Remotion Agent Skills patterns
source_url: https://github.com/architectonic/skills/blob/main/sources/reviewed/2026-07-22-programmatic-video-cluster.md
source_revision: hyperframes@84e4eafacdaf96e8d137ba745af750448c5de0de; remotion-skills@0dd76fafa3fd337b7bc6b5cd95b7db0179828a3d; remotion-license@b8fdb73ae8600d011afb246a02b690bf6935f527
license: Apache-2.0
source_license_status: hyperframes-apache-2.0; remotion-custom-conditional-reference-only
source_content_copied: false
domain: media
artifact_kind: workflow
target_surfaces: [skills, workframe, click-blue, design-system]
risk_level: high
requires_review: true
review_status: source_reviewed_utility_evaluation_pending
---

# Programmatic Video Production

## Trigger

Use when creating, editing, captioning, converting, or rendering video through code or an agent-driven video framework, especially when assets, dependencies, credentials, external services, compute costs, or publication require explicit control.

Do not use this workflow merely to inspect or summarize an existing video. Use a grounded video-analysis procedure instead. Do not use it for ordinary non-linear editing when the selected framework cannot perform the requested cut, re-time, colour, audio-repair, or footage-reordering operation.

## Purpose

Produce a verifiable video artifact while preserving:

- the user's chosen framework and existing project;
- asset rights and provenance;
- deterministic timing and rendering;
- privacy and credential boundaries;
- explicit approval before costly or external actions;
- accessible captions and readable visual composition;
- technical and visual output verification.

Programmatic video is not a reason to default every request to one framework, install arbitrary tooling, crawl external sources, or publish automatically.

## Inputs

- Requested operation: create, edit, caption, convert, render, batch, or publish.
- Existing project and selected framework, if any.
- Source brief, script, footage, audio, images, brand assets, data, or URLs.
- Ownership, license, and permitted use for every source asset.
- Intended audience and distribution destination.
- Required aspect ratio, dimensions, frame rate, duration, language, and output format.
- Narration, captions, audio-description, and accessibility requirements.
- Local compute, GPU, browser, FFmpeg, storage, and time constraints.
- Privacy and retention requirements.
- Approved credentials, APIs, cloud providers, and budget when external services are allowed.

## Procedure

### 1. Classify the operation

Choose the smallest accurate category:

- **new composition** — create a video from a brief, script, data, or assets;
- **existing composition edit** — modify a project already using a programmatic framework;
- **footage packaging** — add captions, overlays, lower-thirds, or graphics without changing the underlying edit;
- **non-linear edit** — cut, reorder, re-time, reframe, colour, or repair footage;
- **conversion** — transcode, resize, extract audio, generate thumbnails, or change container/codec;
- **batch rendering** — render one composition against multiple approved data rows;
- **publication** — upload or distribute an already verified artifact.

If the framework does not support the requested operation, say so and route to an appropriate editor or media tool rather than forcing a programmatic composition.

### 2. Inspect the existing project first

When a project exists, inspect:

1. framework and version;
2. package and runtime requirements;
3. composition entrypoints;
4. media directories and manifests;
5. variables, data schema, and render configuration;
6. design or frame specification;
7. existing timing and animation contract;
8. local and cloud rendering configuration;
9. output and cache directories;
10. repository instructions and validation scripts.

Do not migrate between HyperFrames, Remotion, or another renderer unless the user explicitly requests and approves the migration.

### 3. Resolve legal and provenance boundaries

For every input asset, record:

- source;
- owner or licensor;
- permitted use;
- attribution requirement;
- modification rights;
- redistribution rights;
- retention requirement;
- whether it contains private, biometric, personal, confidential, or customer data.

Do not scrape, download, synthesize, or retrieve assets from a remote service without authorization. Do not treat search availability as a license.

When the selected runtime has entity-size or commercial-use restrictions, verify eligibility for the actual legal entity before using it. Do not represent source-available software as unrestricted open source.

### 4. Declare external-action gates

Require separate explicit approval before any of:

- installing or upgrading packages;
- running a remote shell installer;
- signing in or changing stored credentials;
- invoking a paid API;
- using cloud rendering;
- crawling or capturing a website;
- downloading remote media;
- submitting private media to transcription, TTS, generation, or analysis providers;
- sending telemetry or feedback;
- filing a public issue or uploading a reproduction;
- publishing or distributing the final artifact;
- deleting source media, caches, or rendered outputs.

Approval for one action does not authorize the others.

### 5. Establish the production contract

Record:

- output purpose and destination;
- aspect ratio and pixel dimensions;
- frame rate;
- target duration and acceptable variance;
- delivery codec, container, alpha, and audio requirements;
- language and caption format;
- brand and design-system constraints;
- safe areas and text-size minimums;
- maximum file size;
- draft and final quality levels;
- local or approved cloud execution path;
- cost ceiling;
- review checkpoints.

Do not ask for every value when the project already defines it. Surface inherited defaults and let the user correct consequential assumptions.

### 6. Plan before authoring

Create a storyboard or scene plan containing:

1. scene or beat purpose;
2. start time and duration;
3. narration or on-screen text;
4. visual source and asset provenance;
5. animation or transition purpose;
6. audio and caption requirements;
7. data or variable dependencies;
8. unresolved content or rights questions.

Keep narration, visual timing, and captions linked through stable identifiers. Do not invent product claims, metrics, quotations, testimonials, or customer proof.

### 7. Build deterministically

- Use the selected framework's supported timing and composition model.
- Avoid render-time clocks, unseeded randomness, uncontrolled network fetches, and input-state dependencies.
- Pre-resolve remote assets before final rendering.
- Pin dependency versions required for reproducibility.
- Keep generated files distinguishable from hand-authored source.
- Preserve unrelated composition IDs, timing, variables, tracks, and media paths during edits.
- Keep animation seekable and bounded.
- Use shared design and motion tokens where the project defines them.

### 8. Handle media and models explicitly

For TTS, transcription, background removal, generation, or media retrieval:

1. identify the provider or local model;
2. disclose whether data leaves the machine;
3. confirm credential source and account;
4. estimate cost and runtime;
5. select language and model explicitly;
6. preserve original media;
7. record generated or retrieved asset provenance;
8. verify fallback behavior rather than allowing silent provider drift.

Do not silently replace a requested provider with another. Do not download model weights or invoke detached background generation without approval.

### 9. Produce a draft preview

Render or preview at an economical quality before final delivery.

Inspect representative frames including:

- opening;
- scene transitions;
- dense text;
- captions;
- visual peaks;
- media boundaries;
- ending;
- each sub-composition or reusable scene.

Check narration, captions, graphics, and audio synchronization. A storyboard approval is not final-render approval.

### 10. Run pre-render checks

Verify:

- build and framework validation;
- missing assets and failed requests;
- deterministic duration;
- composition dimensions;
- text fit and safe areas;
- contrast and caption readability;
- duplicate IDs or scene keys;
- unavailable fonts;
- audio clipping and silence;
- caption timing and language;
- unsupported codecs or alpha settings;
- output and temporary disk capacity;
- expected local or cloud cost.

Stop on persistent defects. Do not render merely because a lint command exits successfully.

### 11. Obtain final-render approval

Show or link the final preview and summarize:

- planned output;
- unresolved limitations;
- selected renderer;
- local or cloud execution;
- expected cost;
- private data or external-service exposure;
- intended output path.

Final rendering, batch rendering, or cloud rendering requires explicit approval unless the user already authorized that exact action and scope.

### 12. Render and verify technically

After approval:

1. render to a non-destructive output path;
2. confirm the output exists and is non-empty;
3. inspect container, codec, dimensions, frame rate, duration, audio streams, and alpha when applicable;
4. compare actual duration and format with the production contract;
5. extract representative verification frames;
6. inspect logs for fallbacks, dropped assets, warnings, and external calls;
7. retain the exact command and dependency versions used.

Do not overwrite the only known-good output without preserving a rollback copy.

### 13. Verify visually and audibly

Inspect the rendered artifact, not only source code or preview state.

Check:

- black, blank, frozen, duplicated, or corrupt frames;
- clipping, overflow, and off-canvas content;
- transition continuity;
- text legibility at delivery resolution;
- caption accuracy and timing;
- narration intelligibility;
- music and effects balance;
- visual-content truthfulness;
- brand and design adherence;
- ending and loop behavior.

Record evidence for any issue that remains.

### 14. Deliver without implicit publication

Return:

- artifact path;
- technical media summary;
- source and asset manifest;
- render command and versions;
- verification evidence;
- known limitations;
- cost or provider usage;
- required attribution;
- publication status.

A local render is not authorization to upload it. Publication requires a separate explicit action naming the destination and account.

## Output Contract

Record:

1. operation classification;
2. framework and project inspected;
3. production contract;
4. source and asset provenance;
5. external-action approvals;
6. storyboard or scene plan;
7. provider and model decisions;
8. preview evidence;
9. final-render approval;
10. render command and versions;
11. technical and visual verification;
12. artifact path and publication status;
13. unresolved limitations.

## Verification

- The chosen framework matches the existing project or explicit user choice.
- Every source asset has a known or explicitly unresolved rights status.
- Private media was not sent to an external provider without approval.
- Dependencies, credentials, cloud use, downloads, telemetry, feedback, issue filing, and publication were individually gated.
- The composition is deterministic and reproducible within documented dependencies.
- A draft preview was reviewed before final rendering.
- The final artifact was checked for codec, dimensions, frame rate, duration, streams, file size, and non-empty output.
- Representative rendered frames and audio were inspected.
- Captions and accessible presentation requirements were verified.
- Delivery did not silently publish, overwrite, delete, or expose data.

## Failure Modes

- Treating one installed framework as the universal video default.
- Forcing a motion-graphics renderer to perform unsupported non-linear editing.
- Copying source-available implementation material without license authority.
- Ignoring entity-size or commercial-use license conditions.
- Scraping websites or downloading media without authorization.
- Treating an available image, track, icon, or clip as licensed.
- Installing packages or running remote shell scripts from an upstream skill without review.
- Silent API, model, voice, or cloud-provider fallback.
- Sending private source media to external services without disclosure.
- Rendering at final quality before reviewing a draft.
- Trusting preview or lint while the encoded output is blank or corrupt.
- Publishing, sending feedback, or filing a public issue automatically.
- Deleting source material or overwriting the only valid render.

## Provenance Boundary

This is an original first-party workflow distilled from reviewed HyperFrames and Remotion Agent Skills patterns. No upstream skill body, code template, media asset, registry component, or implementation snippet was copied. Exact source revisions, licenses, retained procedures, and blocked actions are recorded in `sources/reviewed/2026-07-22-programmatic-video-cluster.md`.