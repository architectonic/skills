# Vercel AI SDK Source Profile Normalization — 2026-07-08

## Board ticket

- Ticket: `skills-normalize-vercel-ai-sdk-profile-001`
- Role: `Normalizer`
- Inspected ref: `main`
- Inspected SHA before first content write: `89590689366ba99b4cb8827063183b6df3d6067c`
- Queue item: `normalize-vercel-ai-sdk-source-profile-20260708`
- Mode: original normalization from reviewed source profile only

## Inputs reviewed

- `operations/heartbeat.md`
- `operations/board.json`
- `operations/gates.md`
- `operations/value-ledger.json`
- `operations/daily/2026-07-08/status.json`
- `operations/daily/2026-07-08/queues.json`
- `operations/daily/2026-07-08/report.md`
- `operations/log.md`
- `dist/catalog.json`
- `dist/catalog.md`
- `dist/install-manifest.json`
- `sources/profiles/2026-07-08/vercel-ai.json`
- `reports/review/2026-07-08-manual-source-review.md`

## Source boundary

The reviewed source profile records `vercel/ai` as Apache-2.0, high usefulness, medium risk, and relevant to provider abstraction, streaming, tools, UI, and sandbox boundaries. The redistribution boundary explicitly disallows copying README examples, code snippets, prompts, or implementation content.

This pass used only the reviewed source profile and internal source-review report as inputs. It did not fetch or copy third-party implementation material.

## Artifact created

- `dist/skills/ai-sdk-provider-tool-safety/SKILL.md`

The new skill is original guidance about provider, tool, sandbox, UI, approval, and failure boundaries for AI SDK-style application work.

## Metadata decision

| Field | Decision | Reason |
|---|---|---|
| `domain` | `software-engineering` | The skill is application-architecture guidance for provider/tool/sandbox boundaries. |
| `risk_level` | `medium` | The material discusses tools, sandboxes, provider routing, runtime effects, approval gates, and external mutation boundaries. |
| `requires_review` | `true` | Tool, sandbox, provider, shell/browser/account/deployment-adjacent surfaces require package-facing review before operational use. |
| `source_attribution` | `vercel/ai`, Apache-2.0 | The source profile permits use with attribution and license tracking. |

## Queue changes

Closed:

- `normalize-vercel-ai-sdk-source-profile-20260708`

Created:

- `catalog-refresh-after-vercel-ai-sdk-normalization-20260708`

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| Writes original content only | Pass | The new skill contains original boundary/checklist guidance and no copied source examples, prompts, code, or implementation content. |
| Attributes Vercel AI SDK as source metadata | Pass | Frontmatter records `source_profile` and `source_attribution` for `vercel/ai`, Apache-2.0. |
| Does not copy README examples, code snippets, prompts, or implementation | Pass | No third-party examples or implementation snippets were copied; no repository clone or code execution occurred. |
| Classifies risk and `requires_review` based on tool/sandbox surface | Pass | Frontmatter sets `risk_level: medium` and `requires_review: true`; body defines review gates for tool, sandbox, provider, UI, approval, and failure boundaries. |
| Creates catalog parity queue if dist skill content changes | Pass | Because `dist/skills/ai-sdk-provider-tool-safety/SKILL.md` was added, `skills-catalog-refresh-after-normalization-001` / `catalog-refresh-after-vercel-ai-sdk-normalization-20260708` is now the next ticket. |

## Boundaries preserved

- No online discovery was performed.
- No repository was cloned.
- No candidate code was executed.
- No third-party examples, prompts, README snippets, or implementation content were copied.
- No generated catalog surface was hand-edited in this normalization pass.
- No package, npm, registry, or publication action was attempted.

## Value delta

The reviewed Vercel AI SDK source profile is no longer only metadata. It produced one package-facing, original, review-gated skill that improves the bundle's guidance for provider abstraction and tool/sandbox safety. Catalog parity is now required before install/package/publication endorsement.

## Next action

Cataloger should consume `skills-catalog-refresh-after-normalization-001` and update or verify `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json` after the new normalized skill.
