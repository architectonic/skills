# Skills Distribution Catalog

- Package: `architectonic-skills`
- Install root: `dist/skills`
- Skill count: **1173**

## Domains

| Domain | Count |
|---|---:|
| `agent-operations` | 96 |
| `business` | 45 |
| `cloud-security` | 41 |
| `design` | 40 |
| `forensics` | 22 |
| `media` | 1 |
| `research` | 89 |
| `runtime-tools` | 34 |
| `security-defensive` | 51 |
| `security-offensive` | 5 |
| `software-engineering` | 146 |
| `uncategorized` | 587 |
| `writing` | 16 |

## Risk Levels

| Risk | Count |
|---|---:|
| `high` | 2 |
| `low` | 3 |
| `medium` | 409 |
| `unspecified` | 759 |

## Install Notes

- GitHub/open-repo consumers should start at `README.md` and inspect `dist/catalog.json` for machine-readable discovery.
- Runtime installers should copy from `dist/skills/` and preserve per-skill directories.
- High-risk or `requires_review=true` skills should require explicit user confirmation before automatic install/use.
