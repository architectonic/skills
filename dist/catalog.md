# Skills Distribution Catalog

- Package: `architectonic-skills`
- Install root: `dist/skills`
- Skill count: **1182**

## Domains

| Domain | Count |
|---|---:|
| `agent-operations` | 106 |
| `business` | 46 |
| `cloud-security` | 42 |
| `design` | 40 |
| `forensics` | 25 |
| `media` | 1 |
| `research` | 85 |
| `runtime-tools` | 35 |
| `security-defensive` | 59 |
| `security-offensive` | 16 |
| `software-engineering` | 146 |
| `uncategorized` | 565 |
| `writing` | 16 |

## Risk Levels

| Risk | Count |
|---|---:|
| `high` | 14 |
| `low` | 9 |
| `medium` | 432 |
| `unspecified` | 727 |

## Install Notes

- GitHub/open-repo consumers should start at `README.md` and inspect `dist/catalog.json` for machine-readable discovery.
- Runtime installers should copy from `dist/skills/` and preserve per-skill directories.
- High-risk or `requires_review=true` skills should require explicit user confirmation before automatic install/use.
