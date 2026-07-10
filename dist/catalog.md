# Skills Distribution Catalog

- Package: `architectonic-skills`
- Install root: `dist/skills`
- Skill count: **1183**

## Domains

| Domain | Count |
|---|---:|
| `agent-operations` | 108 |
| `business` | 47 |
| `cloud-security` | 42 |
| `design` | 40 |
| `forensics` | 27 |
| `media` | 1 |
| `research` | 83 |
| `runtime-tools` | 35 |
| `security-defensive` | 72 |
| `security-offensive` | 16 |
| `software-engineering` | 152 |
| `uncategorized` | 544 |
| `writing` | 16 |

## Risk Levels

| Risk | Count |
|---|---:|
| `high` | 28 |
| `low` | 11 |
| `medium` | 440 |
| `unspecified` | 704 |

## Install Notes

- GitHub/open-repo consumers should start at `README.md` and inspect `dist/catalog.json` for machine-readable discovery.
- Runtime installers should copy from `dist/skills/` and preserve per-skill directories.
- High-risk or `requires_review=true` skills should require explicit user confirmation before automatic install/use.
