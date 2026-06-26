---
name: changelog-generator
description: Produce consistent, auditable release notes from Conventional Commits. Separates commit parsing, semantic-bump logic, and changelog rendering for automated releases with editorial control. Use when cutting a release, generating CHANGELOG.md from git history, computing the next semantic version, or automating release notes in CI.
type: Playbook
---

# Changelog Generator

Produce consistent, auditable release notes from Conventional Commits. Separates commit parsing, semantic bump logic, and changelog rendering so teams can automate releases without losing editorial control.

**Note:** For general changelog automation tooling (standard-version, semantic-release, git-cliff), see `software-development/changelog-automation.md`. This skill focuses on the Conventional Commits parsing and rendering pipeline.

## When to Use

- Before publishing a release tag
- During CI to generate release notes automatically
- During PR checks to block invalid commit message formats
- In monorepos where package changelogs require scoped filtering
- When converting raw git history into user-facing notes
- Planning a hotfix/rollback

## When NOT to Use

- Generating changelogs from non-Conventional Commit histories (use changelog-automation instead)
- Tracking technical debt items (use tech-debt-tracker)

## Core Capabilities

- Parse commit messages using Conventional Commit rules
- Detect semantic bump (major, minor, patch) from commit stream
- Render Keep a Changelog sections (Added, Changed, Fixed, etc.)
- Generate release entries from git ranges or provided commit input
- Enforce commit format with a dedicated linter
- Support CI integration via machine-readable JSON output

## Key Workflows

### 1. Generate Changelog Entry From Git

```bash
python3 scripts/generate_changelog.py \
  --from-tag v1.3.0 \
  --to-tag v1.4.0 \
  --next-version v1.4.0 \
  --format markdown
```

### 2. Generate Entry From stdin/File Input

```bash
git log v1.3.0..v1.4.0 --pretty=format:'%s' | \
  python3 scripts/generate_changelog.py --next-version v1.4.0 --format markdown

python3 scripts/generate_changelog.py --input commits.txt --next-version v1.4.0 --format json
```

### 3. Update CHANGELOG.md

```bash
python3 scripts/generate_changelog.py \
  --from-tag v1.3.0 \
  --to-tag HEAD \
  --next-version v1.4.0 \
  --write CHANGELOG.md
```

### 4. Compute the Next Version From Commits

```bash
git log v1.3.0..HEAD --oneline | \
  python3 scripts/version_bumper.py --current-version 1.3.0 --output-format json
```

Output JSON contains `recommended_version`, `bump_type` (major/minor/patch/none), and with `--include-commands` the exact `git tag` commands. Pre-releases: add `--prerelease alpha|beta|rc`.

### 5. Lint Commits Before Merge

```bash
python3 scripts/commit_linter.py --from-ref origin/main --to-ref HEAD --strict --format text
```

## Conventional Commit Rules

Supported types: `feat`, `fix`, `perf`, `refactor`, `docs`, `test`, `build`, `ci`, `chore`, `security`, `deprecated`, `remove`

Breaking changes: `type(scope)!: summary` or `BREAKING CHANGE:` in footer/body

SemVer mapping:
- breaking → major
- non-breaking feat → minor
- all others → patch

## Release Governance Flow

1. Lint commit history for target release range
2. Generate changelog draft from commits
3. Manually adjust wording for customer clarity
4. Validate semver bump recommendation
5. Tag release only after changelog is approved

## Hotfix Severity & SLAs

| Severity | Definition | SLA | Approval |
|---|---|---|---|
| P0 — Critical | Outage, data loss, exploited vulnerability | Fix deployed ≤ 2h; emergency deploy bypasses normal gates | Engineering Lead + On-call Manager |
| P1 — High | Major feature broken, significant user impact | Fix deployed ≤ 24h; expedited review | Engineering Lead + Product Manager |
| P2 — Medium | Minor issues, limited impact | Next release cycle | Standard PR review |

Hotfix branch comes from the last stable tag, contains the minimal fix only, and gets its own patch-bump changelog entry.

## Rollback Triggers

Pre-commit to these thresholds before tagging; roll back when any fires:

| Trigger | Threshold |
|---|---|
| Error rate spike | > 2x baseline within 30 min |
| Performance degradation | > 50% latency increase |
| Feature failure | Core functionality broken |
| Security incident | Vulnerability being exploited |
| Data corruption | Database integrity compromised |

Prefer feature-flag disable over code rollback; database rollbacks only for non-destructive migrations.

## Output Quality Checks

- Each bullet is user-meaningful, not implementation noise
- Breaking changes include migration action
- Security fixes are isolated in `Security` section
- Sections with no entries are omitted
- Duplicate bullets across sections are removed

## CI Policy

- Run `commit_linter.py --strict` on all PRs
- Block merge on invalid conventional commits
- Auto-generate draft release notes on tag push
- Require human approval before writing into CHANGELOG.md on main branch

## Monorepo Guidance

- Prefer commit scopes aligned to package names
- Filter commit stream by scope for package-specific releases
- Keep infra-wide changes in root changelog
- Store package changelogs near package roots for ownership clarity

## Common Pitfalls

1. Mixing merge commit messages with release commit parsing
2. Using vague commit summaries that cannot become release notes
3. Failing to include migration guidance for breaking changes
4. Treating docs/chore changes as user-facing features
5. Overwriting historical changelog sections instead of prepending
