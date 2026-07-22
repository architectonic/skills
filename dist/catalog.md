# Skills Distribution Catalog

- Package: `architectonic-skills`
- Install root: `dist/skills`
- Skill count: **1183**
- Explicit review required: **486**
- Classification overrides applied: **87**
- Deep catalog decisions applied: **11**

Classification overrides repair routing metadata without rewriting imported skill bodies. Deep catalog decisions record body-level review, lifecycle, and installation guidance. Neither grants runtime authority.

## Domains

| Domain | Count |
|---|---:|
| `agent-operations` | 122 |
| `business` | 52 |
| `cloud-security` | 42 |
| `design` | 48 |
| `forensics` | 27 |
| `media` | 10 |
| `research` | 89 |
| `runtime-tools` | 44 |
| `security-defensive` | 81 |
| `security-offensive` | 17 |
| `software-engineering` | 168 |
| `uncategorized` | 458 |
| `writing` | 25 |

## Risk Levels

| Risk | Count |
|---|---:|
| `high` | 49 |
| `low` | 35 |
| `medium` | 481 |
| `unspecified` | 618 |

## Artifact Kinds

| Artifact kind | Count |
|---|---:|
| `playbook` | 1090 |
| `reference` | 9 |
| `runbook` | 3 |
| `skill` | 54 |
| `skill-suite` | 1 |
| `workflow` | 26 |

## Classification Completeness

| Status | Count |
|---|---:|
| `complete` | 565 |
| `partial` | 160 |
| `unclassified` | 458 |

## Source Status

| Source status | Count |
|---|---:|
| `adapted` | 406 |
| `blocked-pending-redaction` | 8 |
| `blocked-redacted` | 3 |
| `classification_reviewed` | 76 |
| `distilled` | 1 |
| `distilled-reviewed` | 2 |
| `existing-package-skill-risk-reviewed` | 2 |
| `existing_package_skill_risk_reviewed` | 1 |
| `internal-normalized` | 1 |
| `metadata-backfilled` | 4 |
| `native` | 2 |
| `native-or-curated-origin-unverified` | 1 |
| `normalized` | 3 |
| `package-facing-risk-reviewed` | 3 |
| `package_body_reviewed` | 9 |
| `package_metadata_backfill` | 5 |
| `package_reviewed_blocked` | 1 |
| `package_reviewed_superseded` | 1 |
| `package_risk_reviewed` | 4 |
| `review-gated-redacted` | 1 |
| `reviewed-metadata-only` | 3 |
| `risk_reviewed` | 2 |
| `unspecified` | 644 |

## Lifecycle Status

| Lifecycle | Count |
|---|---:|
| `reviewed` | 9 |
| `superseded` | 2 |
| `unreviewed` | 1172 |

## Install Recommendation

| Recommendation | Count |
|---|---:|
| `conditional` | 9 |
| `do-not-install` | 2 |
| `inspect` | 1172 |

## Reviewed Catalog Decisions

| Skill | Lifecycle | Install | Superseded by | Decision |
|---|---|---|---|---|
| `canvas-design` | `reviewed` | `conditional` | `—` | Retain as a static visual-art procedure. Its philosophy-to-canvas workflow is distinct from interface design and UI engineering and should not route web application tasks. |
| `frontend-design` | `superseded` | `do-not-install` | `skills/interface-design.md` | The imported body mandates an external Created By Deerflow link in every generated interface, forces index.html regardless of the host project, and encourages aesthetic escalation that can override project scope and design-system intent. Preserve as evidence but do not recommend installation. |
| `frontend-ui-engineering` | `reviewed` | `conditional` | `—` | Retain for component architecture, state management, accessibility, responsive behavior, and implementation checks. It should not determine visual direction and should run after product intent and design-system boundaries are established. |
| `hyperframes` | `reviewed` | `conditional` | `skills/programmatic-video-production.md` | Reviewed against heygen-com/hyperframes@84e4eafacdaf96e8d137ba745af750448c5de0de. Retain only when the user explicitly selects HyperFrames or the existing project already uses it. The body must not make HyperFrames the universal default or authorize skill updates, website crawling, browser capture, cloud rendering, feedback, publication, or external services without separate approval. |
| `hyperframes-animation` | `reviewed` | `conditional` | `—` | Reviewed at HyperFrames revision 84e4eafacdaf96e8d137ba745af750448c5de0de. Retain for deterministic, seek-safe motion inside HyperFrames. Runtime adapters, WebGL, WebGPU, external effect skills, helper bootstrapping, and executable analysis scripts remain project-scoped and review-sensitive. |
| `hyperframes-cli` | `reviewed` | `conditional` | `—` | Reviewed at HyperFrames revision 84e4eafacdaf96e8d137ba745af750448c5de0de. The CLI can scaffold, install, capture, render, publish, authenticate, invoke hosted cloud, AWS, and GCP, send feedback, and file public reproductions. Each external, credentialed, billable, or publishing action requires explicit approval. |
| `hyperframes-core` | `reviewed` | `conditional` | `—` | Reviewed at HyperFrames revision 84e4eafacdaf96e8d137ba745af750448c5de0de. Retain as the deterministic composition contract for an explicitly selected HyperFrames project. It does not authorize project scaffolding, dependencies, rendering, media retrieval, or framework migration by itself. |
| `hyperframes-creative` | `reviewed` | `conditional` | `—` | Reviewed at HyperFrames revision 84e4eafacdaf96e8d137ba745af750448c5de0de. Retain for video-specific creative direction after the project's brand, content truth, and technical contract are known. Presets, package bootstrap, scripts, narration, music, and scene expansion are not implicit authority. |
| `hyperframes-media` | `superseded` | `do-not-install` | `media-use` | The current HyperFrames capability map routes media resolution through media-use. This packaged legacy entry contains a different credential and provider workflow and would create conflicting instructions. Preserve as evidence but do not install. |
| `hyperframes-registry` | `reviewed` | `conditional` | `—` | Reviewed at HyperFrames revision 84e4eafacdaf96e8d137ba745af750448c5de0de. Registry operations download remote blocks and components, write project files, merge HTML/CSS/JS, may touch the clipboard, and can prepare upstream pull requests. Require source, revision, license, script, filesystem, and contribution approval before use. |
| `media-use` | `reviewed` | `conditional` | `—` | Retain as the current HyperFrames media resolver only after review. It searches and downloads remote assets, writes project and global caches, uses HeyGen credentials, adopts existing media, and recommends a remote shell installer. Asset rights, provider access, retention, cache scope, executable installation, and every download require explicit approval. |

## Install Notes

- Inspect `dist/catalog.json` before selecting skills.
- Preserve complete per-skill directories during installation.
- High-risk or `requires_review=true` skills require explicit confirmation.
- `install_recommendation=do-not-install` is a package-level stop signal.
- `lifecycle_status=superseded` means a reviewed replacement exists; preserve the old body only as evidence.
- Classification and catalog decisions do not authorize tools, credentials, network access, filesystem mutation, or publication.
- `target_surfaces` is a routing hint, not an authority grant.
