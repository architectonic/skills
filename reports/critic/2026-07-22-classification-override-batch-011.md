---
type: CriticReport
title: Classification Override Batch 011
date: 2026-07-22
status: validation_passed
board_ticket: skills-metadata-backfill-batch-011
selected_role: Critic
branch: agent/skills-catalog-repair
pull_request: 4
validation_workflow_run: 29952399864
---

# Classification Override Batch 011

## Decision

Replace ad hoc mutation of imported skill files with a reviewed classification-override layer, then apply a first bounded metadata batch to obvious package-facing misclassifications and unspecified-risk entries.

The batch also records newly discovered high-signal sources and adds three original working-source skills. None of the new working skills is promoted into `core/` or `dist/`.

## Root finding

The registry contains useful material, but raw volume concealed three different problems:

1. imported skills with blank domain and risk metadata;
2. skills assigned to a technically valid but semantically weak domain;
3. external sources that yield several artifact kinds—skills, applications, runtimes, connectors, components, or references—but were being flattened into one candidate type.

Examples found during this batch:

- the HyperFrames family already existed but was buried in `uncategorized`;
- `ai-seo` already existed but lacked sufficient risk and target-surface metadata;
- offensive authentication coercion, defensive ransomware response, browser testing, authentication implementation, MCP construction, media generation, meeting analysis, and production recovery cannot share an unspecified risk state;
- design and research candidates must be semantically compared with existing `frontend-design`, `canvas-design`, `litreview`, `github-deep-research`, and related entries before new package slugs are created.

## Changes made

### Catalog architecture

- Added `operations/classification-overrides.json`.
- Updated `scripts/build_distribution_catalog.py` to validate and apply exact name/path overrides.
- Preserved imported `SKILL.md` bodies unchanged.
- Added catalog schema `0.2` fields for:
  - classification completeness;
  - classification evidence;
  - artifact kind;
  - target surfaces;
  - override disclosure;
  - source and review status;
  - source URL, revision, and license when available.
- Extended catalog summaries with review, artifact-kind, classification, and source-status counts.

### First metadata batch

The override batch classifies a broad but bounded set of obvious entries across:

- defensive and offensive security;
- software engineering and runtime tooling;
- agent operations;
- design and media;
- research and writing;
- business workflows.

High-risk entries are explicitly review-gated where they can touch production systems, credentials, external services, authenticated browsers, private data, executable plugins, MCP authority, publication, recovery, or deliberate fault injection.

### New source discovery

Expanded `operations/source-watchlist.json` with high-signal sources covering:

- Remotion;
- Transitions.dev;
- Taste Skill;
- Hallmark;
- Tushar Skills;
- PixelRAG;
- Design Judge Skills;
- OpenSEO;
- HyperFrames;
- Last30Days;
- Claude Video;
- Code Review Graph;
- Codebase Memory MCP;
- BMAD Method;
- `integrations.sh`;
- the WebMCP directory.

Added `sources/candidates/2026-07-22-curated-sources.md` with deduplication findings and promotion gates.

### New working-source skills

Added original local candidate procedures:

- `skills/interface-quality-audit.md`;
- `skills/interface-transition-review.md`;
- `skills/recent-source-research.md`.

These remain `distilled_candidate`, disclose unpinned upstream inspiration, and are not part of the reviewed core.

### Validation

- Added `.github/workflows/catalog-validation.yml` for pull-request validation.
- Updated catalog refresh workflows to rebuild when classification overrides change.
- Workflow run `29952399864` completed successfully.
- Passed checks:
  - package validation;
  - Python compilation;
  - catalog generation;
  - exact matching for all 87 overrides;
  - representative classification assertions;
  - first-batch classification thresholds;
  - required structure and candidate status for the three new working skills.

## Generated result

| Metric | Before | After |
|---|---:|---:|
| Skill count | 1,183 | 1,183 |
| Classification overrides | 0 | 87 |
| Uncategorized | 544 | 458 |
| Unspecified risk | 704 | 618 |
| Media | 1 | 10 |
| Software engineering | 152 | 168 |
| Security defensive | 72 | 81 |

Additional generated state:

- explicit review required: 484;
- complete classification: 565;
- partial classification: 160;
- unclassified: 458.

## Boundary result

- No imported third-party skill body was rewritten.
- No external repository was cloned or executed.
- No new source was promoted into `core/manifest.json`.
- No npm publication was attempted.
- No application, connector, MCP server, credential, browser session, or external system was invoked.
- Target surfaces are routing hints only and grant no authority.

## Acceptance tests

| Test | Result |
|---|---|
| Override file parses and uses allowed taxonomy | Pass |
| Every override matches exactly one packaged skill | Pass |
| Catalog builder compiles and generates schema 0.2 | Pass |
| Uncategorized count falls below first-batch threshold | Pass |
| Unspecified-risk count falls below first-batch threshold | Pass |
| HyperFrames and `ai-seo` are deduplicated and classified rather than re-added | Pass |
| New candidate skills retain required structure and unpinned-source disclosure | Pass |
| Imported skill bodies remain unchanged | Pass by construction of override approach |

## Next justified action

1. Review and merge draft pull request 4 when approved.
2. Run source review on Transitions/Hallmark/Taste, Remotion/HyperFrames, OpenSEO, Last30Days/Claude Video, and Code Review Graph/Codebase Memory in that order.
3. Continue metadata repair in bounded semantic clusters instead of alphabetical bulk backfill.
4. Promote no candidate into the reviewed core until provenance, license, safety, and measured utility gates pass.
