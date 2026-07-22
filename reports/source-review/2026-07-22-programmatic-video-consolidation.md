---
type: SourceReviewReport
title: Programmatic Video Skill Consolidation
date: 2026-07-22
status: merged_to_main
branch: agent/video-skill-consolidation
sources: [HyperFrames, Remotion Agent Skills]
tags: [skills, media, video, rendering, lifecycle, licensing, validation]
okf_version: "0.2"
---

# Programmatic Video Skill Consolidation

## Decision

Retain the HyperFrames package family as conditional, framework-specific procedures. Remove its implicit universal-default authority. Supersede the stale `hyperframes-media` workflow with `media-use`. Add one tool-neutral, high-risk first-party workflow for programmatic video production.

Keep Remotion Agent Skills reference-only because the skills package has no separate license declaration and the Remotion runtime uses a custom entity-size license.

## Changes

### First-party working source

Added `skills/programmatic-video-production.md` with:

- operation classification before framework choice;
- existing-project and framework inspection;
- asset rights and provenance requirements;
- separate approvals for dependencies, credentials, APIs, cloud, browser capture, downloads, telemetry, issue filing, publication, and deletion;
- deterministic storyboard and timing contracts;
- provider/model disclosure and no silent fallback;
- economical draft preview before final render;
- final-render approval;
- technical verification of codec, dimensions, frame rate, duration, streams, file size, and output existence;
- visual and audio inspection of encoded output;
- explicit publication separation.

The workflow is `high` risk, `requires_review: true`, source-reviewed, and not part of `core/manifest.json`.

### HyperFrames decisions

Reviewed against `heygen-com/hyperframes@84e4eafacdaf96e8d137ba745af750448c5de0de`, Apache-2.0.

| Entry | Lifecycle | Install | Risk | Decision |
|---|---|---|---|---|
| `hyperframes` | reviewed | conditional | high | Explicit HyperFrames selection required; not universal default |
| `hyperframes-cli` | reviewed | conditional | high | Commands, auth, cloud, feedback, issue filing, and publication gated |
| `hyperframes-core` | reviewed | conditional | medium | Technical contract for existing HyperFrames projects |
| `hyperframes-animation` | reviewed | conditional | medium | Deterministic HyperFrames motion only |
| `hyperframes-creative` | reviewed | conditional | medium | Project brand and truthful content remain authoritative |
| `hyperframes-registry` | reviewed | conditional | high | Remote code, scripts, filesystem, clipboard, and upstream contribution gated |
| `hyperframes-media` | superseded | do-not-install | high | Replaced by `media-use` |
| `media-use` | reviewed | conditional | high | Credentials, downloads, cache writes, asset rights, and installer review required |

### Remotion decision

Reviewed:

- skills revision: `0dd76fafa3fd337b7bc6b5cd95b7db0179828a3d`;
- package version: `4.0.496`;
- Remotion license revision: `b8fdb73ae8600d011afb246a02b690bf6935f527`.

The reviewed license allows free use for individuals, non-profits, and for-profit organizations with up to three employees. Larger for-profit organizations require a company license. The official skills repository has no separate root license and its package metadata declares no license.

No Remotion skill body or implementation content was copied.

## High-confidence findings

1. The existing top-level HyperFrames entry was under-classified. It performs or routes browser capture, website crawling, skill updates, local ML, cloud rendering, feedback, issue filing, and publication-sensitive operations.
2. The current HyperFrames source routes media resolution to `media-use`; retaining `hyperframes-media` as separately installable creates conflicting credential and provider instructions.
3. `media-use` searches and downloads remote assets, writes project/global caches, consumes credentials, adopts local assets, and recommends a remote shell installer. It cannot remain an ordinary low-friction media helper.
4. Remotion is not governed by an unrestricted permissive runtime license. Legal-entity eligibility is part of tool selection.
5. A shared Architectonic procedure should define gates and verification, not make one renderer the default.

## Boundaries

- No imported package body was edited.
- No external skill body or code template was copied.
- No remote component or media asset was downloaded.
- No package, model, runtime, browser, cloud provider, or credential was invoked.
- No remote shell installer was executed.
- No skill was promoted into the reviewed core.
- No npm publication was attempted.

## Acceptance tests

| Test | Expected |
|---|---|
| Eleven deep catalog decisions are applied | Pass in PR validation |
| HyperFrames top-level is high-risk and review-gated | Pass in PR validation |
| HyperFrames cannot claim universal default status | Pass by catalog decision and local workflow |
| Legacy `hyperframes-media` is superseded and do-not-install | Pass in PR validation |
| `media-use` is media/high/reviewed/conditional | Pass in PR validation |
| Remotion exact revisions and custom license boundary are recorded | Pass in PR validation |
| Programmatic video skill is high-risk, review-gated, and source-content-copy false | Pass in PR validation |
| Prior design and classification decisions remain intact | Pass in PR validation |

## Next justified action

After validation and merge:

1. evaluate the tool-neutral workflow against local HyperFrames and Remotion fixtures without cloud or external media;
2. continue the next source cluster with OpenSEO and marketing/SEO overlap;
3. separately inspect other HyperFrames workflow entries such as product-launch-video, website-to-video, PR-to-video, captions, and talking-head workflows before granting lifecycle decisions;
4. keep applications and runtime adapters for the later Workframe pass.
