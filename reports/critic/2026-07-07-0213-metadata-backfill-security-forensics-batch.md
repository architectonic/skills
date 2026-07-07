---
type: Critic Report
title: Metadata Backfill — Security and Forensics Batch
date: 2026-07-07
role: Critic
status: partial
---

# Metadata Backfill — Security and Forensics Batch

## Scope

Consumed one bounded Critic batch from `metadata-backfill-uncategorized-and-unspecified-risk-20260707`.

The pass inspected the open queue, active operator doctrine, current catalog summary, the `authoring-agent-skills` quality gate, and the target `dist/skills/**` entries before changing metadata.

## Files backfilled

| Path | Domain | Risk | Review flag | Rationale |
|---|---|---:|---|---|
| `dist/skills/analyzing-active-directory-acl-abuse/SKILL.md` | `security-defensive` | `medium` | `requires_review: true` | Defensive AD ACL review, but privilege-escalation semantics require review before endorsement. |
| `dist/skills/analyzing-android-malware-with-apktool/SKILL.md` | `forensics` | `medium` | `requires_review: true` | Static APK malware analysis in an isolated evidence workflow. |
| `dist/skills/analyzing-bootkit-and-rootkit-samples/SKILL.md` | `forensics` | `medium` | `requires_review: true` | Low-level malware/firmware/rootkit analysis with sensitive forensic procedures. |
| `dist/skills/analyzing-command-and-control-communication/SKILL.md` | `security-defensive` | `medium` | `requires_review: true` | Malware C2 protocol analysis is defensive but dual-use and must remain review-gated. |

## Metadata fields added

Each file received the missing catalog metadata without changing procedure bodies:

```yaml
title: <existing title>
domain: <security-defensive | forensics>
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_license: Apache-2.0
source_status: adapted
```

## Boundaries

- No third-party source was copied.
- No external repository was cloned, installed, imported, or executed.
- No procedure body was expanded or normalized.
- Generated catalog files were not hand-edited.

## Follow-up

Because this pass changed `dist/skills/**`, Cataloger must refresh or verify generated surfaces: `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json`.

Expected post-refresh movement from this batch, assuming no concurrent changes:

- `uncategorized` decreases by 4.
- `unspecified` risk decreases by 4.
- `forensics` increases by 2.
- `security-defensive` increases by 2.
- `medium` risk increases by 4.
