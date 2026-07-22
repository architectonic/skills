#!/usr/bin/env python3
"""Apply deep-review lifecycle decisions to generated skill catalog surfaces."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any
import json

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "dist" / "catalog.json"
CATALOG_MD_PATH = ROOT / "dist" / "catalog.md"
MANIFEST_PATH = ROOT / "dist" / "install-manifest.json"
DECISIONS_PATH = ROOT / "operations" / "catalog-decisions.json"
DECISIONS_DIR = ROOT / "operations" / "catalog-decisions"

ALLOWED_LIFECYCLE = {
    "unreviewed",
    "candidate",
    "review-required",
    "reviewed",
    "blocked",
    "superseded",
    "deprecated",
}
ALLOWED_RECOMMENDATIONS = {
    "inspect",
    "recommended",
    "conditional",
    "do-not-install",
}
PATCH_FIELDS = {
    "domain",
    "risk_level",
    "requires_review",
    "source_status",
    "review_status",
    "lifecycle_status",
    "install_recommendation",
    "superseded_by",
    "decision_evidence",
}


def normalize(value: Any) -> str:
    return " ".join(str(value or "").split())


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return payload


def decision_files() -> list[Path]:
    paths = [DECISIONS_PATH]
    if DECISIONS_DIR.exists():
        paths.extend(sorted(DECISIONS_DIR.glob("*.json")))
    return paths


def load_decisions() -> list[dict[str, Any]]:
    combined: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()

    for source_path in decision_files():
        payload = load_json(source_path)
        source_name = source_path.relative_to(ROOT).as_posix()
        if payload.get("schema_version") != "0.1":
            raise ValueError(f"{source_name} schema_version must be 0.1")
        decisions = payload.get("decisions")
        if not isinstance(decisions, list):
            raise ValueError(f"{source_name} decisions must be a list")

        for index, decision in enumerate(decisions):
            context = f"{source_name} decision {index}"
            if not isinstance(decision, dict):
                raise ValueError(f"{context} must be an object")
            name = normalize(decision.get("name"))
            path = normalize(decision.get("path")).replace("\\", "/")
            if not name and not path:
                raise ValueError(f"{context} requires name or path")
            identity = ("path", path) if path else ("name", name)
            if identity in seen:
                raise ValueError(
                    f"duplicate catalog decision across decision files: {identity}"
                )
            seen.add(identity)

            lifecycle = normalize(decision.get("lifecycle_status"))
            recommendation = normalize(decision.get("install_recommendation"))
            if lifecycle not in ALLOWED_LIFECYCLE - {"unreviewed"}:
                raise ValueError(
                    f"unsupported lifecycle_status {lifecycle!r} for {name or path}"
                )
            if recommendation not in ALLOWED_RECOMMENDATIONS - {"inspect"}:
                raise ValueError(
                    f"unsupported install_recommendation {recommendation!r} "
                    f"for {name or path}"
                )
            if "requires_review" in decision and not isinstance(
                decision["requires_review"], bool
            ):
                raise ValueError(f"requires_review must be boolean for {name or path}")
            unknown = set(decision) - PATCH_FIELDS - {"name", "path"}
            if unknown:
                raise ValueError(
                    f"unsupported catalog decision fields for {name or path}: "
                    f"{sorted(unknown)}"
                )
            combined.append(decision)

    return combined


def apply_decisions(
    catalog: dict[str, Any], decisions: list[dict[str, Any]]
) -> int:
    entries = catalog.get("skills")
    if not isinstance(entries, list):
        raise ValueError("dist/catalog.json skills must be a list")

    name_counts = Counter(normalize(entry.get("slug")) for entry in entries)
    by_name = {
        normalize(entry.get("slug")): entry
        for entry in entries
        if name_counts[normalize(entry.get("slug"))] == 1
    }
    by_path = {
        normalize(entry.get("path")).replace("\\", "/"): entry for entry in entries
    }

    for entry in entries:
        entry.setdefault("lifecycle_status", "unreviewed")
        entry.setdefault("install_recommendation", "inspect")
        entry.setdefault("superseded_by", "")
        entry.setdefault("decision_evidence", "")
        entry.setdefault("catalog_decision", False)

    for decision in decisions:
        path = normalize(decision.get("path")).replace("\\", "/")
        name = normalize(decision.get("name"))
        entry = by_path.get(path) if path else by_name.get(name)
        if entry is None:
            if name_counts.get(name, 0) > 1:
                raise ValueError(f"catalog decision name {name!r} is ambiguous; use path")
            raise ValueError(f"catalog decision did not match a skill: {path or name}")

        for field in PATCH_FIELDS:
            if field not in decision:
                continue
            value = decision[field]
            if field != "requires_review":
                value = normalize(value)
            entry[field] = value
        entry["catalog_decision"] = True

    summary = catalog.setdefault("summary", {})
    summary["requires_review_count"] = sum(
        bool(entry.get("requires_review")) for entry in entries
    )
    summary["risk_counts"] = count(entries, "risk_level", "unspecified")
    summary["source_status_counts"] = count(entries, "source_status", "unspecified")
    summary["review_status_counts"] = count(entries, "review_status", "unspecified")
    summary["lifecycle_status_counts"] = count(
        entries, "lifecycle_status", "unreviewed"
    )
    summary["install_recommendation_counts"] = count(
        entries, "install_recommendation", "inspect"
    )
    summary["catalog_decisions_applied"] = len(decisions)

    package = catalog.setdefault("package", {})
    package["catalog_decisions"] = "operations/catalog-decisions.json"
    package["catalog_decision_files"] = [
        path.relative_to(ROOT).as_posix() for path in decision_files()
    ]
    return len(decisions)


def count(entries: list[dict[str, Any]], field: str, fallback: str) -> dict[str, int]:
    return dict(
        sorted(Counter(normalize(entry.get(field)) or fallback for entry in entries).items())
    )


def update_manifest(manifest: dict[str, Any]) -> None:
    discovery = manifest.setdefault("discovery_files", [])
    for path in decision_files():
        decision_path = path.relative_to(ROOT).as_posix()
        if decision_path not in discovery:
            discovery.append(decision_path)

    fields = manifest.setdefault("selection_fields", [])
    for field in [
        "lifecycle_status",
        "install_recommendation",
        "superseded_by",
        "decision_evidence",
    ]:
        if field not in fields:
            fields.append(field)


def add_counts(lines: list[str], title: str, label: str, counts: dict[str, int]) -> None:
    lines.extend(["", f"## {title}", "", f"| {label} | Count |", "|---|---:|"])
    for key, value in counts.items():
        lines.append(f"| `{key}` | {value} |")


def render_catalog_markdown(catalog: dict[str, Any]) -> str:
    package = catalog.get("package", {})
    summary = catalog.get("summary", {})
    entries = catalog.get("skills", [])
    lines = [
        "# Skills Distribution Catalog",
        "",
        f"- Package: `{package.get('name', '')}`",
        f"- Install root: `{package.get('install_root', '')}`",
        f"- Skill count: **{summary.get('skill_count', len(entries))}**",
        f"- Explicit review required: **{summary.get('requires_review_count', 0)}**",
        f"- Classification overrides applied: **{summary.get('classification_overrides_applied', 0)}**",
        f"- Deep catalog decisions applied: **{summary.get('catalog_decisions_applied', 0)}**",
        "",
        "Classification overrides repair routing metadata without rewriting imported skill bodies. Deep catalog decisions record body-level review, lifecycle, and installation guidance. Neither grants runtime authority.",
    ]

    add_counts(lines, "Domains", "Domain", summary.get("domain_counts", {}))
    add_counts(lines, "Risk Levels", "Risk", summary.get("risk_counts", {}))
    add_counts(
        lines,
        "Artifact Kinds",
        "Artifact kind",
        summary.get("artifact_kind_counts", {}),
    )
    add_counts(
        lines,
        "Classification Completeness",
        "Status",
        summary.get("classification_counts", {}),
    )
    add_counts(
        lines,
        "Source Status",
        "Source status",
        summary.get("source_status_counts", {}),
    )
    add_counts(
        lines,
        "Lifecycle Status",
        "Lifecycle",
        summary.get("lifecycle_status_counts", {}),
    )
    add_counts(
        lines,
        "Install Recommendation",
        "Recommendation",
        summary.get("install_recommendation_counts", {}),
    )

    reviewed = [entry for entry in entries if entry.get("catalog_decision")]
    lines.extend(
        [
            "",
            "## Reviewed Catalog Decisions",
            "",
            "| Skill | Lifecycle | Install | Superseded by | Decision |",
            "|---|---|---|---|---|",
        ]
    )
    for entry in sorted(reviewed, key=lambda row: normalize(row.get("slug"))):
        evidence = normalize(entry.get("decision_evidence")).replace("|", "\\|")
        superseded = normalize(entry.get("superseded_by")) or "—"
        lines.append(
            f"| `{entry.get('slug', '')}` | `{entry.get('lifecycle_status', '')}` | "
            f"`{entry.get('install_recommendation', '')}` | `{superseded}` | {evidence} |"
        )

    lines.extend(
        [
            "",
            "## Install Notes",
            "",
            "- Inspect `dist/catalog.json` before selecting skills.",
            "- Preserve complete per-skill directories during installation.",
            "- High-risk or `requires_review=true` skills require explicit confirmation.",
            "- `install_recommendation=do-not-install` is a package-level stop signal.",
            "- `lifecycle_status=superseded` means a reviewed replacement exists; preserve the old body only as evidence.",
            "- Classification and catalog decisions do not authorize tools, credentials, network access, filesystem mutation, or publication.",
            "- `target_surfaces` is a routing hint, not an authority grant.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    catalog = load_json(CATALOG_PATH)
    manifest = load_json(MANIFEST_PATH)
    decisions = load_decisions()
    applied = apply_decisions(catalog, decisions)
    update_manifest(manifest)

    CATALOG_PATH.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    CATALOG_MD_PATH.write_text(render_catalog_markdown(catalog), encoding="utf-8")
    print(f"Applied {applied} catalog decisions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
