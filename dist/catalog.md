# Skills Distribution Catalog

- Package: `architectonic-skills`
- Install root: `dist/skills`
- Skill count: **1183**
- Explicit review required: **485**
- Classification overrides applied: **87**
- Deep catalog decisions applied: **3**

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
| `high` | 47 |
| `low` | 35 |
| `medium` | 483 |
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
| `classification_reviewed` | 84 |
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
| `package_body_reviewed` | 2 |
| `package_metadata_backfill` | 5 |
| `package_reviewed_blocked` | 1 |
| `package_risk_reviewed` | 4 |
| `review-gated-redacted` | 1 |
| `reviewed-metadata-only` | 3 |
| `risk_reviewed` | 2 |
| `unspecified` | 644 |

## Lifecycle Status

| Lifecycle | Count |
|---|---:|
| `reviewed` | 2 |
| `superseded` | 1 |
| `unreviewed` | 1180 |

## Install Recommendation

| Recommendation | Count |
|---|---:|
| `conditional` | 2 |
| `do-not-install` | 1 |
| `inspect` | 1180 |

## Reviewed Catalog Decisions

| Skill | Lifecycle | Install | Superseded by | Decision |
|---|---|---|---|---|
| `canvas-design` | `reviewed` | `conditional` | `—` | Retain as a static visual-art procedure. Its philosophy-to-canvas workflow is distinct from interface design and UI engineering and should not route web application tasks. |
| `frontend-design` | `superseded` | `do-not-install` | `skills/interface-design.md` | The imported body mandates an external Created By Deerflow link in every generated interface, forces index.html regardless of the host project, and encourages aesthetic escalation that can override project scope and design-system intent. Preserve as evidence but do not recommend installation. |
| `frontend-ui-engineering` | `reviewed` | `conditional` | `—` | Retain for component architecture, state management, accessibility, responsive behavior, and implementation checks. It should not determine visual direction and should run after product intent and design-system boundaries are established. |

## Install Notes

- Inspect `dist/catalog.json` before selecting skills.
- Preserve complete per-skill directories during installation.
- High-risk or `requires_review=true` skills require explicit confirmation.
- `install_recommendation=do-not-install` is a package-level stop signal.
- `lifecycle_status=superseded` means a reviewed replacement exists; preserve the old body only as evidence.
- Classification and catalog decisions do not authorize tools, credentials, network access, filesystem mutation, or publication.
- `target_surfaces` is a routing hint, not an authority grant.
