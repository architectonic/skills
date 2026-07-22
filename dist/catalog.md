# Skills Distribution Catalog

- Package: `architectonic-skills`
- Install root: `dist/skills`
- Skill count: **1183**
- Explicit review required: **487**
- Classification overrides applied: **87**
- Deep catalog decisions applied: **16**

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
| `high` | 50 |
| `low` | 36 |
| `medium` | 481 |
| `unspecified` | 616 |

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
| `adapted` | 405 |
| `blocked-pending-redaction` | 8 |
| `blocked-redacted` | 3 |
| `classification_reviewed` | 74 |
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
| `package_body_reviewed` | 13 |
| `package_metadata_backfill` | 5 |
| `package_reviewed_blocked` | 1 |
| `package_reviewed_superseded` | 2 |
| `package_risk_reviewed` | 4 |
| `review-gated-redacted` | 1 |
| `reviewed-metadata-only` | 3 |
| `risk_reviewed` | 2 |
| `unspecified` | 642 |

## Lifecycle Status

| Lifecycle | Count |
|---|---:|
| `reviewed` | 13 |
| `superseded` | 3 |
| `unreviewed` | 1167 |

## Install Recommendation

| Recommendation | Count |
|---|---:|
| `conditional` | 13 |
| `do-not-install` | 3 |
| `inspect` | 1167 |

## Reviewed Catalog Decisions

| Skill | Lifecycle | Install | Superseded by | Decision |
|---|---|---|---|---|
| `Graphify Onboarding` | `reviewed` | `conditional` | `—` | Retain the source hierarchy, ignore rules, private-data caveats, review-before-commit, and derived-not-canonical boundaries. Use it with an explicitly approved graph engine or no engine; it does not authorize installation, repository scanning, global configuration, hooks, watchers, dashboards, or canonical memory writes. |
| `ai-seo` | `superseded` | `do-not-install` | `skills/ai-search-visibility-audit.md` | The imported reference has unverified origin and embeds date-sensitive platform behavior, crawler names, prevalence percentages, traffic-loss claims, citation multipliers, optimization gains, and source-share statistics without recoverable current evidence. It also refers to content-strategy and copywriting package skills that are not present. Preserve as evidence but use the current-source AI search visibility audit instead. |
| `canvas-design` | `reviewed` | `conditional` | `—` | Retain as a static visual-art procedure. Its philosophy-to-canvas workflow is distinct from interface design and UI engineering and should not route web application tasks. |
| `codebase-design` | `reviewed` | `conditional` | `—` | Retain as an optional module/interface design vocabulary. It is not a structural graph or impact-analysis tool and its exact terminology and universal-sounding rules should be applied only when the deep-module model fits the project, not as mandatory architecture language. |
| `competitive-intel` | `reviewed` | `conditional` | `—` | Retain for broad business intelligence, sales battlecards, positioning, product, and leadership decisions. Current funding, hiring, customer, pricing, partnership, social, CRM, win/loss, and churn evidence requires source, privacy, confidentiality, and authorization review. Use skills/seo-competitive-research.md for search-market and ranking analysis. |
| `frontend-design` | `superseded` | `do-not-install` | `skills/interface-design.md` | The imported body mandates an external Created By Deerflow link in every generated interface, forces index.html regardless of the host project, and encourages aesthetic escalation that can override project scope and design-system intent. Preserve as evidence but do not recommend installation. |
| `frontend-ui-engineering` | `reviewed` | `conditional` | `—` | Retain for component architecture, state management, accessibility, responsive behavior, and implementation checks. It should not determine visual direction and should run after product intent and design-system boundaries are established. |
| `hyperframes` | `reviewed` | `conditional` | `—` | Reviewed against heygen-com/hyperframes@84e4eafacdaf96e8d137ba745af750448c5de0de. Retain only when the user explicitly selects HyperFrames or the existing project already uses it. The body must not make HyperFrames the universal default or authorize skill updates, website crawling, browser capture, cloud rendering, feedback, publication, or external services without separate approval. Use skills/programmatic-video-production.md as the framework-neutral governing workflow. |
| `hyperframes-animation` | `reviewed` | `conditional` | `—` | Reviewed at HyperFrames revision 84e4eafacdaf96e8d137ba745af750448c5de0de. Retain for deterministic, seek-safe motion inside HyperFrames. Runtime adapters, WebGL, WebGPU, external effect skills, helper bootstrapping, and executable analysis scripts remain project-scoped and review-sensitive. |
| `hyperframes-cli` | `reviewed` | `conditional` | `—` | Reviewed at HyperFrames revision 84e4eafacdaf96e8d137ba745af750448c5de0de. The CLI can scaffold, install, capture, render, publish, authenticate, invoke hosted cloud, AWS, and GCP, send feedback, and file public reproductions. Each external, credentialed, billable, or publishing action requires explicit approval. |
| `hyperframes-core` | `reviewed` | `conditional` | `—` | Reviewed at HyperFrames revision 84e4eafacdaf96e8d137ba745af750448c5de0de. Retain as the deterministic composition contract for an explicitly selected HyperFrames project. It does not authorize project scaffolding, dependencies, rendering, media retrieval, or framework migration by itself. |
| `hyperframes-creative` | `reviewed` | `conditional` | `—` | Reviewed at HyperFrames revision 84e4eafacdaf96e8d137ba745af750448c5de0de. Retain for video-specific creative direction after the project's brand, content truth, and technical contract are known. Presets, package bootstrap, scripts, narration, music, and scene expansion are not implicit authority. |
| `hyperframes-media` | `superseded` | `do-not-install` | `media-use` | The current HyperFrames capability map routes media resolution through media-use. This packaged legacy entry contains a different credential and provider workflow and would create conflicting instructions. Preserve as evidence but do not install. |
| `hyperframes-registry` | `reviewed` | `conditional` | `—` | Reviewed at HyperFrames revision 84e4eafacdaf96e8d137ba745af750448c5de0de. Registry operations download remote blocks and components, write project files, merge HTML/CSS/JS, may touch the clipboard, and can prepare upstream pull requests. Require source, revision, license, script, filesystem, and contribution approval before use. |
| `media-use` | `reviewed` | `conditional` | `—` | Retain as the current HyperFrames media resolver only after review. It searches and downloads remote assets, writes project and global caches, uses HeyGen credentials, adopts existing media, and recommends a remote shell installer. Asset rights, provider access, retention, cache scope, executable installation, and every download require explicit approval. |
| `monorepo-navigator` | `reviewed` | `conditional` | `—` | Retain for monorepo structure, package impact, selective builds, migrations, and coordinated releases. The body reaches executable analyzers, CI filters, remote cache credentials, history rewriting, package moves, versioning, and publication; absolute tool preferences and bundled-script paths are advisory and every mutation requires repository-specific review. |

## Install Notes

- Inspect `dist/catalog.json` before selecting skills.
- Preserve complete per-skill directories during installation.
- High-risk or `requires_review=true` skills require explicit confirmation.
- `install_recommendation=do-not-install` is a package-level stop signal.
- `lifecycle_status=superseded` means a reviewed replacement exists; preserve the old body only as evidence.
- Classification and catalog decisions do not authorize tools, credentials, network access, filesystem mutation, or publication.
- `target_surfaces` is a routing hint, not an authority grant.
