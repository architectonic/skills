---
type: SourceReview
title: Programmatic Video Skill Cluster Review
date: 2026-07-22
status: reviewed_for_distillation
sources: [HyperFrames, Remotion Agent Skills]
tags: [skills, media, video, rendering, source-review, provenance, licensing, deduplication]
okf_version: "0.2"
---

# Programmatic Video Skill Cluster Review

## Decision

Retain the existing HyperFrames package family conditionally with corrected lifecycle and risk decisions. Supersede the stale `hyperframes-media` entry with the current `media-use` entry. Distill a smaller first-party, tool-neutral `programmatic-video-production` procedure.

Do not vendor the Remotion Agent Skills into Architectonic. Keep Remotion reference-only until its skills package has an explicit redistribution license and the selected runtime use satisfies Remotion's entity-size license.

## HyperFrames

- Repository: https://github.com/heygen-com/hyperframes
- Reviewed revision: `84e4eafacdaf96e8d137ba745af750448c5de0de`
- Release observed at review: `0.7.68`
- License: Apache-2.0
- Decision: retain package family conditionally; do not make it the universal video default.

### Reviewed bodies

- `hyperframes` package body: `f24ba819d8cf82893051f16e7c67e0d66d0c93cb`
- `hyperframes-cli`: `938a3b5403945606aadaa63df45b1e87e58cdd33`
- `hyperframes-core`: `74d21fb81bc40495f2fb808fe7555f70852b3857`
- `hyperframes-animation`: `00aaaeed5c5f216b593781b9905c97b83bef3695`
- `hyperframes-creative`: `293067cbafc4704a930757d35926d29cfd39484c`
- `hyperframes-registry`: `5fd897bc71ced67dae08f3e5a6e8b3915966bd09`
- packaged legacy `hyperframes-media`: `f21d5134b28d0f9c26c5b9daa7a29fca43581a93`
- packaged current `media-use`: `8462c44f9aa01f2d23b9875908eb7e191d94fa8c`

### Retain

- HTML-native deterministic composition model.
- Explicit separation of technical composition, animation, creative direction, media resolution, registry operations, and CLI execution.
- One paused seekable timeline and deterministic-render constraints.
- Plan → preview → approval → render → output verification sequence.
- Draft-versus-final quality distinction.
- Snapshot and sub-composition smoke tests.
- Explicit approval before final render.
- Provenance-aware local media manifests.

### Correct or constrain

- HyperFrames must not override another framework merely because its skill is installed. Use it only when the user selected HyperFrames or the existing project is a HyperFrames project.
- Skill updates, registry installation, dependency bootstrap, cloud rendering, browser capture, website crawling, authentication, credential storage, feedback submission, issue filing, publication, and upstream contribution are separate external actions requiring explicit approval.
- Do not send feedback automatically after successful renders.
- Do not use `--file-issue` or publish reproduction material without explicit consent and redaction review.
- Do not silently switch between paid APIs and local model fallbacks.
- Do not execute remote shell installers from a skill instruction. Package installation must use a reviewed, pinned installation route.
- Media assets require rights, provenance, retention, and redistribution checks before use.
- Cloud rendering requires cost, region, credential, data-transfer, and artifact-retention review.
- Browser capture and URL ingestion require authorization and privacy review.

### Lifecycle decisions

- `hyperframes` — reviewed, conditional, high risk, explicit project/framework selection required.
- `hyperframes-cli` — reviewed, conditional, high risk, command/cloud/publication approval required.
- `hyperframes-core` — reviewed, conditional, medium risk, retained as the technical contract.
- `hyperframes-animation` — reviewed, conditional, medium risk, retained for deterministic HyperFrames motion only.
- `hyperframes-creative` — reviewed, conditional, medium risk, project design and content truth remain authoritative.
- `hyperframes-registry` — reviewed, conditional, high risk, remote code and filesystem review required.
- `hyperframes-media` — superseded, do not install; replaced by `media-use`.
- `media-use` — reviewed, conditional, high risk, credentials/network/filesystem/license review required.

## Remotion Agent Skills

- Skills repository: https://github.com/remotion-dev/skills
- Reviewed revision: `0dd76fafa3fd337b7bc6b5cd95b7db0179828a3d`
- Skills package version: `4.0.496`
- Skills package metadata points to: https://github.com/remotion-dev/remotion/tree/main/packages/skills
- Separate skills-repository license: not found
- Skills package license declaration: absent
- Remotion monorepo license reviewed at: `b8fdb73ae8600d011afb246a02b690bf6935f527`
- Runtime license: custom two-tier Remotion License
- Decision: reference only; do not copy or redistribute skill bodies.

### License boundary

The reviewed Remotion license permits free use for individuals, non-profits, and for-profit organizations with up to three employees. Larger for-profit organizations require a company license. It permits eligible users to create videos and images and modify Remotion for their use case, but prohibits copying or modifying Remotion code to sell, rent, license, relicense, or sublicense a derivative of Remotion.

Architectonic must not represent Remotion as Apache, MIT, or unrestricted open source. Runtime eligibility must be evaluated for the actual legal entity using it.

### Reviewed skill surfaces

- `remotion-best-practices` body: `83899db253a911d70a8fca1a8543f3bea05bde52`
- `remotion-create` body: `f0f8f62bc2ca2a847b33242f312711f6b6a2172b`
- additional official skill paths observed: `remotion-markup`, `remotion-docs`, and references for rendering, captions, interactivity, SaaS, and upgrades.

### Retain as general principles

- Prefer the existing video framework and project before scaffolding a new one.
- Separate project creation, markup, rendering, captions, interactivity, SaaS integration, documentation lookup, and upgrades.
- Preview before final rendering.
- Inspect dependencies and runtime requirements before scaffolding or rendering.

### Do not copy

- Remotion skill bodies or reference files.
- Remotion implementation code, templates, or package internals.
- Commands represented as universally licensed or universally eligible.

## Local first-party procedure

Create `skills/programmatic-video-production.md` as a tool-neutral high-risk workflow that:

- inspects the existing project and framework first;
- distinguishes creation, editing, captioning, analysis, and conversion;
- records asset rights and provenance;
- sets output, duration, aspect, distribution, accessibility, compute, and privacy constraints;
- builds a deterministic storyboard and timing contract;
- uses draft previews and explicit final-render approval;
- verifies media outputs technically and visually;
- prohibits automatic publication, feedback, issue filing, cloud use, dependency installation, credential changes, or remote installers.

## Promotion gates

The first-party procedure remains outside `core/manifest.json` until it passes:

1. a local deterministic motion graphic task;
2. an existing HyperFrames project edit without framework migration;
3. an existing Remotion project task without copying upstream skills;
4. a caption or media task involving private source material;
5. a cloud-render request where cost and credential gates remain intact;
6. an asset-rights failure case;
7. a preview rejection followed by bounded revision;
8. output verification using duration, codec, frame, audio, and visual evidence.

## Boundary

No Remotion skill body, HyperFrames skill body, implementation snippet, registry component, media asset, or remote installer was copied into the first-party procedure. Existing imported HyperFrames bodies remain unchanged. Catalog decisions alter routing and installation guidance only.