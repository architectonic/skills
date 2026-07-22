#!/usr/bin/env python3
"""Validate generated skill catalog classifications, lifecycle decisions, and working-source contracts."""
from __future__ import annotations

from pathlib import Path
from typing import Any
import json

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "dist" / "catalog.json"
MANIFEST_PATH = ROOT / "dist" / "install-manifest.json"


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return payload


def load_markdown(path: Path) -> tuple[dict[str, Any], str, str]:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        raise ValueError(f"{path.relative_to(ROOT)} missing frontmatter")
    parts = raw.split("---", 2)
    if len(parts) != 3:
        raise ValueError(f"{path.relative_to(ROOT)} has malformed frontmatter")
    frontmatter = yaml.safe_load(parts[1])
    if not isinstance(frontmatter, dict):
        raise ValueError(f"{path.relative_to(ROOT)} frontmatter must be a mapping")
    return frontmatter, parts[2], raw


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_summary(catalog: dict[str, Any], manifest: dict[str, Any]) -> None:
    summary = catalog.get("summary", {})
    require(catalog.get("schema_version") == "0.2", "catalog schema_version must be 0.2")
    require(manifest.get("schema_version") == "0.2", "install manifest schema_version must be 0.2")
    require(summary.get("classification_overrides_applied", 0) >= 60, "expected at least 60 classification overrides")
    require(summary.get("catalog_decisions_applied", 0) >= 11, "expected at least eleven deep catalog decisions")
    require(summary.get("domain_counts", {}).get("uncategorized", 10**9) <= 500, "uncategorized count remains above first-batch acceptance threshold")
    require(summary.get("risk_counts", {}).get("unspecified", 10**9) <= 650, "unspecified-risk count remains above first-batch acceptance threshold")
    require("operations/catalog-decisions.json" in manifest.get("discovery_files", []), "install manifest must expose catalog decisions")
    for field in [
        "lifecycle_status",
        "install_recommendation",
        "superseded_by",
        "decision_evidence",
    ]:
        require(field in manifest.get("selection_fields", []), f"install manifest missing selection field {field}")


def validate_classifications(entries: dict[str, dict[str, Any]]) -> None:
    expected = {
        "Building Ransomware Playbook with CISA Framework": ("security-defensive", "high", True),
        "Code Documentation Generator": ("software-engineering", "low", False),
        "hyperframes": ("media", "high", True),
        "hyperframes-cli": ("runtime-tools", "high", True),
        "ai-seo": ("business", "medium", True),
    }
    for slug, (domain, risk, review) in expected.items():
        entry = entries.get(slug)
        require(entry is not None, f"missing expected catalog entry: {slug}")
        actual = (entry.get("domain"), entry.get("risk_level"), entry.get("requires_review"))
        require(actual == (domain, risk, review), f"{slug} classification mismatch: {actual!r}")
        require(bool(entry.get("classification_override")), f"{slug} should disclose classification_override=true")


def validate_decisions(entries: dict[str, dict[str, Any]]) -> None:
    expected: dict[str, dict[str, Any]] = {
        "frontend-design": {
            "lifecycle_status": "superseded",
            "install_recommendation": "do-not-install",
            "risk_level": "medium",
            "requires_review": True,
            "source_status": "package_reviewed_blocked",
            "review_status": "blocked_for_forced_branding_and_scope",
            "superseded_by": "skills/interface-design.md",
        },
        "frontend-ui-engineering": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "risk_level": "medium",
            "requires_review": False,
            "superseded_by": "",
        },
        "canvas-design": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "risk_level": "low",
            "requires_review": False,
            "superseded_by": "",
        },
        "hyperframes": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "risk_level": "high",
            "requires_review": True,
            "review_status": "explicit_hyperframes_project_selection_required",
            "superseded_by": "",
        },
        "hyperframes-cli": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "risk_level": "high",
            "requires_review": True,
            "review_status": "command_cloud_publication_and_feedback_approval_required",
            "superseded_by": "",
        },
        "hyperframes-core": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "risk_level": "medium",
            "requires_review": False,
            "superseded_by": "",
        },
        "hyperframes-animation": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "risk_level": "medium",
            "requires_review": False,
            "superseded_by": "",
        },
        "hyperframes-creative": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "risk_level": "medium",
            "requires_review": False,
            "superseded_by": "",
        },
        "hyperframes-registry": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "risk_level": "high",
            "requires_review": True,
            "superseded_by": "",
        },
        "hyperframes-media": {
            "lifecycle_status": "superseded",
            "install_recommendation": "do-not-install",
            "risk_level": "high",
            "requires_review": True,
            "review_status": "stale_media_workflow_replaced_by_media_use",
            "superseded_by": "media-use",
        },
        "media-use": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "domain": "media",
            "risk_level": "high",
            "requires_review": True,
            "review_status": "credentials_network_filesystem_asset_rights_and_installer_review_required",
            "superseded_by": "",
        },
    }
    for slug, fields in expected.items():
        entry = entries.get(slug)
        require(entry is not None, f"missing reviewed catalog entry: {slug}")
        require(bool(entry.get("catalog_decision")), f"{slug} should disclose catalog_decision=true")
        for key, value in fields.items():
            require(entry.get(key) == value, f"{slug} decision mismatch for {key}: expected {value!r}, got {entry.get(key)!r}")


def validate_working_skills() -> None:
    required_sections = [
        "## Trigger",
        "## Inputs",
        "## Procedure",
        "## Verification",
        "## Failure Modes",
    ]
    reviewed = {
        ROOT / "skills/interface-design.md": "hallmark@aeb42fb354ff4efa36ab475773a082315a3af2ce",
        ROOT / "skills/interface-quality-audit.md": "taste-skill@98565e65bc3274ddf6eb0838734341714057178b",
        ROOT / "skills/interface-transition-review.md": "transitions.dev@047d036a79cc2ddecd868e7f1e3aa04b495644b2",
        ROOT / "skills/programmatic-video-production.md": "hyperframes@84e4eafacdaf96e8d137ba745af750448c5de0de",
    }
    for path, revision_fragment in reviewed.items():
        frontmatter, body, _ = load_markdown(path)
        require(frontmatter.get("source_status") == "distilled-reviewed", f"{path.relative_to(ROOT)} source_status must be distilled-reviewed")
        require(frontmatter.get("review_status") == "source_reviewed_utility_evaluation_pending", f"{path.relative_to(ROOT)} review_status mismatch")
        revision = str(frontmatter.get("source_revision") or "")
        require(revision_fragment in revision, f"{path.relative_to(ROOT)} missing pinned source revision")
        require("unpinned-review-required" not in revision, f"{path.relative_to(ROOT)} must not retain an unpinned revision")
        for section in required_sections:
            require(section in body, f"{path.relative_to(ROOT)} missing required section {section}")

    video_path = ROOT / "skills/programmatic-video-production.md"
    frontmatter, body, raw = load_markdown(video_path)
    require(frontmatter.get("risk_level") == "high", "programmatic-video-production must remain high risk")
    require(frontmatter.get("requires_review") is True, "programmatic-video-production must remain review gated")
    require(frontmatter.get("source_content_copied") is False, "programmatic-video-production must disclose source_content_copied=false")
    for evidence in [
        "remotion-skills@0dd76fafa3fd337b7bc6b5cd95b7db0179828a3d",
        "remotion-license@b8fdb73ae8600d011afb246a02b690bf6935f527",
        "## Output Contract",
        "Require separate explicit approval before any of:",
    ]:
        require(evidence in raw, f"programmatic video skill missing evidence: {evidence}")

    candidate_path = ROOT / "skills/recent-source-research.md"
    frontmatter, body, _ = load_markdown(candidate_path)
    require(frontmatter.get("source_status") == "distilled_candidate", "recent-source-research must remain a distilled candidate")
    require(frontmatter.get("source_revision") == "unpinned-review-required", "recent-source-research must disclose unpinned upstream revision")
    for section in required_sections:
        require(section in body, f"{candidate_path.relative_to(ROOT)} missing required section {section}")


def validate_source_reviews() -> None:
    design = (ROOT / "sources/reviewed/2026-07-22-design-quality-cluster.md").read_text(encoding="utf-8")
    for evidence in [
        "aeb42fb354ff4efa36ab475773a082315a3af2ce",
        "98565e65bc3274ddf6eb0838734341714057178b",
        "047d036a79cc2ddecd868e7f1e3aa04b495644b2",
        "No root `LICENSE` file was found",
        "do not copy or redistribute snippets",
    ]:
        require(evidence in design, f"design source review missing evidence: {evidence}")

    video = (ROOT / "sources/reviewed/2026-07-22-programmatic-video-cluster.md").read_text(encoding="utf-8")
    for evidence in [
        "84e4eafacdaf96e8d137ba745af750448c5de0de",
        "0dd76fafa3fd337b7bc6b5cd95b7db0179828a3d",
        "b8fdb73ae8600d011afb246a02b690bf6935f527",
        "License: Apache-2.0",
        "up to three employees",
        "do not copy or redistribute skill bodies",
        "Do not execute remote shell installers",
    ]:
        require(evidence in video, f"programmatic video source review missing evidence: {evidence}")


def main() -> int:
    catalog = load_json(CATALOG_PATH)
    manifest = load_json(MANIFEST_PATH)
    validate_summary(catalog, manifest)
    entries = {entry.get("slug"): entry for entry in catalog.get("skills", [])}
    validate_classifications(entries)
    validate_decisions(entries)
    validate_working_skills()
    validate_source_reviews()
    print("Catalog classifications, lifecycle decisions, and working-source contracts passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
