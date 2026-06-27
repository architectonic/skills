# Skills Distribution Catalog

- Package: `@teleagent/skills`
- Install root: `dist/skills`
- Skill count: **1167**

## Domains

| Domain | Count |
|---|---:|
| `agent-operations` | 79 |
| `business` | 96 |
| `cloud-security` | 52 |
| `design` | 127 |
| `forensics` | 27 |
| `media` | 11 |
| `research` | 34 |
| `runtime-tools` | 87 |
| `security-defensive` | 201 |
| `security-offensive` | 59 |
| `software-engineering` | 328 |
| `writing` | 66 |

## Risk Levels

| Risk | Count |
|---|---:|
| `high` | 423 |
| `low` | 6 |
| `medium` | 733 |
| `unspecified` | 5 |

## Install Notes

- GitHub/open-repo consumers should start at `README.md` and inspect `dist/catalog.json` for machine-readable discovery.
- Runtime installers should copy from `dist/skills/` and preserve per-skill directories.
- High-risk or `requires_review=true` skills should require explicit user confirmation before automatic install/use.
