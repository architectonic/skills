# Skills Distribution Catalog

- Package: `architectonic-skills`
- Install root: `dist/skills`
- Skill count: **1182**

## Domains

| Domain | Count |
|---|---:|
| `agent-operations` | 105 |
| `business` | 45 |
| `cloud-security` | 41 |
| `design` | 40 |
| `forensics` | 24 |
| `media` | 1 |
| `research` | 85 |
| `runtime-tools` | 34 |
| `security-defensive` | 53 |
| `security-offensive` | 6 |
| `software-engineering` | 146 |
| `uncategorized` | 586 |
| `writing` | 16 |

## Risk Levels

| Risk | Count |
|---|---:|
| `high` | 3 |
| `low` | 9 |
| `medium` | 416 |
| `unspecified` | 754 |

## Install Notes

- GitHub/open-repo consumers should start at `README.md` and inspect `dist/catalog.json` for machine-readable discovery.
- Runtime installers should copy from `dist/skills/` and preserve per-skill directories.
- High-risk or `requires_review=true` skills should require explicit user confirmation before automatic install/use.
