# Skills Distribution Catalog

- Package: `architectonic-skills`
- Install root: `dist/skills`
- Skill count: **1183**
- Explicit review required: **484**
- Classification overrides applied: **87**

Classification overrides repair catalog metadata without rewriting imported skill bodies. Inclusion remains untrusted until source, license, safety, and utility review pass.

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
| `classification_reviewed` | 87 |
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
| `package_metadata_backfill` | 5 |
| `package_risk_reviewed` | 4 |
| `review-gated-redacted` | 1 |
| `reviewed-metadata-only` | 3 |
| `risk_reviewed` | 2 |
| `unspecified` | 644 |

## Install Notes

- Inspect `dist/catalog.json` before selecting skills.
- Preserve complete per-skill directories during installation.
- High-risk or `requires_review=true` skills require explicit confirmation.
- `classification_override=true` means only the catalog metadata was separately reviewed.
- `target_surfaces` is a routing hint, not an authority grant.
