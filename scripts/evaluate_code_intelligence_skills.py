#!/usr/bin/env python3
"""Evaluate code-intelligence skill contracts on deterministic synthetic fixtures.

This is not a model benchmark. It verifies committed skill fragments, compares
manually authored generic and skill-guided outputs against weighted rubrics, checks
unknown and mutation boundaries, and reports transparent character-based token
estimates.
"""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
from typing import Any
import json
import math

ROOT = Path(__file__).resolve().parent.parent
FIXTURE_PATH = (
    ROOT / "tests" / "fixtures" / "code-intelligence" / "contract-evaluation.json"
)
REPORT_JSON = (
    ROOT
    / "reports"
    / "evaluation"
    / "2026-07-22-code-intelligence-fixture-evaluation.json"
)
REPORT_MD = (
    ROOT
    / "reports"
    / "evaluation"
    / "2026-07-22-code-intelligence-fixture-evaluation.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(
        isinstance(payload, dict),
        f"{path.relative_to(ROOT)} must contain an object",
    )
    return payload


def estimate_tokens(text: str) -> int:
    """Estimate tokens without a provider tokenizer: ceil(UTF-8 bytes / 4)."""
    return max(1, math.ceil(len(text.encode("utf-8")) / 4))


def score(criteria: list[dict[str, Any]], field: str) -> int:
    return sum(int(row["weight"]) for row in criteria if row.get(field) is True)


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# Code-Intelligence Skill Contract Fixture Evaluation",
        "",
        f"- Date: `{report['date']}`",
        f"- Evaluation kind: `{report['evaluation_kind']}`",
        f"- Cases: **{summary['case_count']}**",
        f"- Maximum rubric score: **{summary['maximum_score']}**",
        f"- Generic baseline score: **{summary['baseline_score']}**",
        f"- Skill-guided score: **{summary['guided_score']}**",
        f"- Score delta: **+{summary['score_delta']}**",
        f"- Baseline estimated tokens: **{summary['baseline_estimated_tokens']}**",
        f"- Guided estimated tokens: **{summary['guided_estimated_tokens']}**",
        f"- Estimated token delta: **+{summary['token_delta']}**",
        f"- Promotion decision: `{summary['promotion_decision']}`",
        "",
        "> This is a deterministic synthetic contract evaluation, not a model benchmark. The outputs are authored fixtures scored against explicit rubrics. Token counts use `ceil(UTF-8 bytes / 4)` and are not provider-tokenizer measurements.",
        "",
        "## Boundaries",
        "",
    ]
    for key, value in report["boundaries"].items():
        lines.append(f"- `{key}`: `{str(value).lower()}`")

    lines.extend(
        [
            "",
            "## Results",
            "",
            "| Case | Skill | Baseline | Guided | Max | Delta | Baseline tokens | Guided tokens |",
            "|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for case in report["cases"]:
        lines.append(
            f"| `{case['id']}` | `{case['skill_path']}` | "
            f"{case['baseline_score']} | {case['guided_score']} | "
            f"{case['maximum_score']} | +{case['score_delta']} | "
            f"{case['baseline_estimated_tokens']} | "
            f"{case['guided_estimated_tokens']} |"
        )

    lines.extend(["", "## Case Findings", ""])
    for case in report["cases"]:
        lines.extend(
            [
                f"### `{case['id']}`",
                "",
                f"- Question: {case['question']}",
                f"- Score: {case['baseline_score']} → {case['guided_score']} / {case['maximum_score']}",
                f"- Estimated tokens: {case['baseline_estimated_tokens']} → {case['guided_estimated_tokens']}",
                f"- Required skill fragments verified: {case['required_skill_fragment_count']}",
                f"- Expected unknowns preserved: {case['expected_unknown_count']}",
                f"- Prohibited actions absent: {case['prohibited_action_count']}",
                "",
                "**Generic baseline fixture**",
                "",
                case["baseline_output"],
                "",
                "**Skill-guided fixture**",
                "",
                case["guided_output"],
                "",
            ]
        )

    lines.extend(
        [
            "## Interpretation",
            "",
            "The two procedures materially improve the deterministic contract score by selecting no engine when appropriate, rejecting stale and heuristic graph evidence as proof, checking configuration and generated-source relationships, preserving worktree and private-data boundaries, and separating review preparation from repository publication.",
            "",
            "The guided fixtures are longer, so the added verification and authority controls have a measurable context/output cost. This evidence closes the deterministic contract item but does not justify core promotion. Controlled model runs and real-repository tasks are still required to measure routing precision, actual defect detection, false-positive rate, tool-call behavior, and total context cost.",
            "",
            "## Verification",
            "",
            "- Every fixture is synthetic and local.",
            "- No repository was indexed and no graph engine, binary, installer, MCP server, model provider, hook, watcher, dashboard, agent configuration, CI comment, or repository mutation was used.",
            "- Every required skill fragment exists in committed working source.",
            "- Every expected unknown is preserved by the guided fixture.",
            "- No prohibited action appears in the guided action list.",
            "- Every guided score exceeds its generic baseline score.",
            "- Generated JSON and Markdown are checked for deterministic parity in CI.",
            "",
        ]
    )
    return "\n".join(lines)


def evaluate() -> dict[str, Any]:
    fixture = load_json(FIXTURE_PATH)
    require(
        fixture.get("schema_version") == "0.1",
        "fixture schema_version must be 0.1",
    )
    require(
        fixture.get("evaluation_kind")
        == "deterministic_contract_fixture_not_model_benchmark",
        "fixture must disclose deterministic non-model evaluation",
    )
    boundaries = fixture.get("boundaries")
    require(isinstance(boundaries, dict), "fixture boundaries must be an object")
    require(boundaries.get("synthetic_data_only") is True, "fixtures must be synthetic")
    for key, value in boundaries.items():
        if key == "synthetic_data_only":
            continue
        require(value is False, f"fixture boundary {key} must remain false")

    cases = fixture.get("cases")
    require(
        isinstance(cases, list) and len(cases) == 6,
        "expected exactly six code-intelligence fixture cases",
    )

    results: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for case in cases:
        require(isinstance(case, dict), "each fixture case must be an object")
        case_id = str(case.get("id") or "")
        require(
            case_id and case_id not in seen_ids,
            f"duplicate or empty case id: {case_id!r}",
        )
        seen_ids.add(case_id)

        skill_path = ROOT / str(case["skill_path"])
        require(
            skill_path.is_file(),
            f"missing skill for {case_id}: {skill_path.relative_to(ROOT)}",
        )
        skill_text = skill_path.read_text(encoding="utf-8")
        required_fragments = case.get("required_skill_fragments") or []
        require(required_fragments, f"{case_id} requires skill fragments")
        for fragment in required_fragments:
            require(
                str(fragment) in skill_text,
                f"{case_id} skill missing fragment: {fragment}",
            )

        baseline_output = str(case.get("baseline_output") or "")
        guided_output = str(case.get("guided_output") or "")
        require(
            baseline_output and guided_output,
            f"{case_id} requires both outputs",
        )

        expected_unknowns = case.get("expected_unknowns") or []
        guided_lower = guided_output.lower()
        for unknown in expected_unknowns:
            require(
                str(unknown).lower() in guided_lower,
                f"{case_id} did not preserve unknown: {unknown}",
            )

        guided_actions = {
            str(action) for action in case.get("guided_actions") or []
        }
        prohibited_actions = {
            str(action)
            for action in case.get("prohibited_guided_actions") or []
        }
        overlap = guided_actions & prohibited_actions
        require(
            not overlap,
            f"{case_id} guided actions include prohibited actions: {sorted(overlap)}",
        )

        criteria = case.get("criteria") or []
        require(criteria, f"{case_id} requires weighted criteria")
        criterion_ids: set[str] = set()
        for criterion in criteria:
            criterion_id = str(criterion.get("id") or "")
            require(
                criterion_id and criterion_id not in criterion_ids,
                f"{case_id} duplicate criterion {criterion_id!r}",
            )
            criterion_ids.add(criterion_id)
            require(
                int(criterion.get("weight", 0)) > 0,
                f"{case_id}/{criterion_id} weight must be positive",
            )
            require(
                isinstance(criterion.get("baseline_pass"), bool),
                f"{case_id}/{criterion_id} baseline_pass must be boolean",
            )
            require(
                isinstance(criterion.get("guided_pass"), bool),
                f"{case_id}/{criterion_id} guided_pass must be boolean",
            )

        maximum_score = sum(int(row["weight"]) for row in criteria)
        baseline_score = score(criteria, "baseline_pass")
        guided_score = score(criteria, "guided_pass")
        require(
            guided_score > baseline_score,
            f"{case_id} guided score must exceed baseline",
        )

        baseline_tokens = estimate_tokens(baseline_output)
        guided_tokens = estimate_tokens(guided_output)
        results.append(
            {
                "id": case_id,
                "skill_path": str(case["skill_path"]),
                "question": str(case["question"]),
                "maximum_score": maximum_score,
                "baseline_score": baseline_score,
                "guided_score": guided_score,
                "score_delta": guided_score - baseline_score,
                "baseline_estimated_tokens": baseline_tokens,
                "guided_estimated_tokens": guided_tokens,
                "token_delta": guided_tokens - baseline_tokens,
                "baseline_output": baseline_output,
                "guided_output": guided_output,
                "required_skill_fragment_count": len(required_fragments),
                "expected_unknown_count": len(expected_unknowns),
                "prohibited_action_count": len(prohibited_actions),
            }
        )

    maximum_score = sum(row["maximum_score"] for row in results)
    baseline_score = sum(row["baseline_score"] for row in results)
    guided_score = sum(row["guided_score"] for row in results)
    baseline_tokens = sum(row["baseline_estimated_tokens"] for row in results)
    guided_tokens = sum(row["guided_estimated_tokens"] for row in results)

    return {
        "schema_version": "0.1",
        "date": str(fixture["date"]),
        "evaluation_kind": str(fixture["evaluation_kind"]),
        "fixture_path": FIXTURE_PATH.relative_to(ROOT).as_posix(),
        "boundaries": boundaries,
        "summary": {
            "case_count": len(results),
            "maximum_score": maximum_score,
            "baseline_score": baseline_score,
            "guided_score": guided_score,
            "score_delta": guided_score - baseline_score,
            "baseline_estimated_tokens": baseline_tokens,
            "guided_estimated_tokens": guided_tokens,
            "token_delta": guided_tokens - baseline_tokens,
            "baseline_points_per_100_estimated_tokens": round(
                (baseline_score / baseline_tokens) * 100, 2
            ),
            "guided_points_per_100_estimated_tokens": round(
                (guided_score / guided_tokens) * 100, 2
            ),
            "promotion_decision": (
                "hold_for_controlled_model_and_real_repository_evaluation"
            ),
        },
        "cases": results,
    }


def serialize_json(report: dict[str, Any]) -> str:
    return json.dumps(
        report,
        indent=2,
        ensure_ascii=False,
        sort_keys=True,
    ) + "\n"


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="write deterministic report artifacts",
    )
    args = parser.parse_args()

    report = evaluate()
    json_text = serialize_json(report)
    markdown_text = render_markdown(report) + "\n"

    if args.write:
        REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
        REPORT_JSON.write_text(json_text, encoding="utf-8")
        REPORT_MD.write_text(markdown_text, encoding="utf-8")
        print(f"Wrote {REPORT_JSON.relative_to(ROOT)}")
        print(f"Wrote {REPORT_MD.relative_to(ROOT)}")
        return 0

    require(
        REPORT_JSON.is_file(),
        f"missing generated report: {REPORT_JSON.relative_to(ROOT)}",
    )
    require(
        REPORT_MD.is_file(),
        f"missing generated report: {REPORT_MD.relative_to(ROOT)}",
    )
    require(
        REPORT_JSON.read_text(encoding="utf-8") == json_text,
        "code-intelligence fixture JSON report is stale",
    )
    require(
        REPORT_MD.read_text(encoding="utf-8") == markdown_text,
        "code-intelligence fixture Markdown report is stale",
    )
    print("Code-intelligence deterministic fixture evaluation and report parity passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
