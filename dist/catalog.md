# Skills Distribution Catalog

- Package: `architectonic-skills`
- Install root: `dist/skills`
- Skill count: **1182**

## Domains

| Domain | Count |
|---|---:|
| `agent-operations` | 104 |
| `business` | 46 |
| `cloud-security` | 42 |
| `design` | 40 |
| `forensics` | 25 |
| `media` | 1 |
| `research` | 85 |
| `runtime-tools` | 35 |
| `security-defensive` | 58 |
| `security-offensive` | 12 |
| `software-engineering` | 146 |
| `uncategorized` | 572 |
| `writing` | 16 |

## Risk Levels

| Risk | Count |
|---|---:|
| `high` | 9 |
| `low` | 9 |
| `medium` | 429 |
| `unspecified` | 735 |

## Install Notes

- GitHub/open-repo consumers should start at `README.md` and inspect `dist/catalog.json` for machine-readable discovery.
- Runtime installers should copy from `dist/skills/` and preserve per-skill directories.
- High-risk or `requires_review=true` skills should require explicit user confirmation before automatic install/use.
