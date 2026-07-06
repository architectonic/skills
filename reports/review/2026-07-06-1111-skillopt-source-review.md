# Source Review — SkillOpt

Date: 2026-07-06

Selected role: Source Reviewer

Scheduled role: Radar

Override reason: open review queue item `review-skillopt-20260705-0711` outranked broad discovery under the review/safety gate.

## Source

- Repository: `microsoft/SkillOpt`
- URL: https://github.com/microsoft/SkillOpt
- Author/owner: Microsoft
- License observed: MIT
- Package metadata observed: `skillopt` version `0.2.0`, Python `>=3.10`
- Review boundary: metadata and documentation only; no clone, no package install, no CLI execution, no benchmark execution, no upstream content copy.

## Evidence Inspected

- GitHub repository metadata through connector.
- `README.md` through connector.
- `LICENSE` through connector.
- `pyproject.toml` through connector.
- `docs/guide/new-backend.md` through connector.
- `docs/sleep/README.md` through connector.
- `docs/sleep/RESULTS.md` through connector.

## Review Decision

Decision: `reference-only` with a Normalizer follow-up.

SkillOpt is useful for doctrine and procedure design, not for direct ingestion. The safe reusable lesson is that self-improving skill systems need bounded edit proposals, held-out validation, rejected-edit memory, staged adoption, and clear separation between offline optimization and inference-time use.

## Useful Reusable Procedure Learned

A future original Architectonic skill/playbook can teach this loop:

1. Select a narrow skill document or runbook as the trainable artifact.
2. Define held-out tasks with objective or reviewer-checkable scoring before editing.
3. Generate bounded candidate edits only: add, delete, replace, or reorder limited sections.
4. Test candidate edits against held-out tasks.
5. Accept only if validation improves or a documented reviewer override exists.
6. Store rejected edits and why they failed.
7. Stage accepted edits for human/operator adoption before they affect future runs.
8. Keep private transcripts, credentials, and executable runtime surfaces outside the optimization artifact.

## Risk Boundary

The scheduler must not:

- install `skillopt`;
- run `skillopt-train`, `skillopt-eval`, or `skillopt-sleep`;
- start the WebUI;
- harvest local agent transcripts;
- execute benchmarks;
- copy benchmark tasks, prompts, skills, docs, or result tables into this repository;
- claim upstream benchmark results as Architectonic results.

## Queue Result

Consumed: `review-skillopt-20260705-0711`.

Created: `normalize-validation-gated-skill-improvement-20260706` for a future Normalizer pass.

No risk queue was created because the source remains reference-only and all execution/data surfaces are explicitly blocked at scheduler boundary.

## Value-Substance Delta

The queue item moved from candidate name to reviewed source profile plus a concrete normalization target. The durable value is a provenance/licensing/safety decision and a reusable doctrine path for validation-gated skill-improvement loops.
