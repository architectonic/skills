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


def require_text(path: Path, evidence_items: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for evidence in evidence_items:
        require(evidence in text, f"{path.relative_to(ROOT)} missing evidence: {evidence}")


def validate_summary(catalog: dict[str, Any], manifest: dict[str, Any]) -> None:
    summary = catalog.get("summary", {})
    require(catalog.get("schema_version") == "0.2", "catalog schema_version must be 0.2")
    require(manifest.get("schema_version") == "0.2", "install manifest schema_version must be 0.2")
    require(
        summary.get("classification_overrides_applied", 0) >= 60,
        "expected at least 60 classification overrides",
    )
    require(
        summary.get("catalog_decisions_applied", 0) >= 16,
        "expected at least sixteen deep catalog decisions",
    )
    require(
        summary.get("domain_counts", {}).get("uncategorized", 10**9) <= 500,
        "uncategorized count remains above first-batch acceptance threshold",
    )
    require(
        summary.get("risk_counts", {}).get("unspecified", 10**9) <= 650,
        "unspecified-risk count remains above first-batch acceptance threshold",
    )
    discovery_files = manifest.get("discovery_files", [])
    for path in [
        "operations/catalog-decisions.json",
        "operations/catalog-decisions/code-intelligence.json",
    ]:
        require(path in discovery_files, f"install manifest must expose {path}")
    for field in [
        "lifecycle_status",
        "install_recommendation",
        "superseded_by",
        "decision_evidence",
    ]:
        require(
            field in manifest.get("selection_fields", []),
            f"install manifest missing selection field {field}",
        )


def validate_fields(
    entries: dict[str, dict[str, Any]],
    slug: str,
    expected: dict[str, Any],
    *,
    classification_override: bool = False,
    catalog_decision: bool = False,
) -> None:
    entry = entries.get(slug)
    require(entry is not None, f"missing expected catalog entry: {slug}")
    if classification_override:
        require(
            bool(entry.get("classification_override")),
            f"{slug} should disclose classification_override=true",
        )
    if catalog_decision:
        require(
            bool(entry.get("catalog_decision")),
            f"{slug} should disclose catalog_decision=true",
        )
    for key, value in expected.items():
        require(
            entry.get(key) == value,
            f"{slug} mismatch for {key}: expected {value!r}, got {entry.get(key)!r}",
        )


def validate_classifications(entries: dict[str, dict[str, Any]]) -> None:
    expected = {
        "Building Ransomware Playbook with CISA Framework": {
            "domain": "security-defensive",
            "risk_level": "high",
            "requires_review": True,
        },
        "Code Documentation Generator": {
            "domain": "software-engineering",
            "risk_level": "low",
            "requires_review": False,
        },
        "hyperframes": {
            "domain": "media",
            "risk_level": "high",
            "requires_review": True,
        },
        "hyperframes-cli": {
            "domain": "runtime-tools",
            "risk_level": "high",
            "requires_review": True,
        },
        "ai-seo": {
            "domain": "business",
            "risk_level": "medium",
            "requires_review": True,
        },
    }
    for slug, fields in expected.items():
        validate_fields(entries, slug, fields, classification_override=True)


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
        "ai-seo": {
            "lifecycle_status": "superseded",
            "install_recommendation": "do-not-install",
            "risk_level": "medium",
            "requires_review": True,
            "source_status": "package_reviewed_superseded",
            "review_status": "volatile_unverified_claims_and_missing_dependencies",
            "superseded_by": "skills/ai-search-visibility-audit.md",
        },
        "competitive-intel": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "domain": "business",
            "risk_level": "medium",
            "requires_review": True,
            "source_status": "package_body_reviewed",
            "review_status": "retained_for_business_intelligence_not_seo_competitive_research",
            "superseded_by": "",
        },
        "Graphify Onboarding": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "domain": "agent-operations",
            "risk_level": "medium",
            "requires_review": True,
            "source_status": "package_body_reviewed",
            "review_status": "retained_as_derived_graph_onboarding_not_canonical_truth",
            "superseded_by": "",
        },
        "monorepo-navigator": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "domain": "software-engineering",
            "risk_level": "high",
            "requires_review": True,
            "source_status": "package_body_reviewed",
            "review_status": "ci_history_cache_migration_and_publication_approval_required",
            "superseded_by": "",
        },
        "codebase-design": {
            "lifecycle_status": "reviewed",
            "install_recommendation": "conditional",
            "domain": "software-engineering",
            "risk_level": "low",
            "requires_review": False,
            "source_status": "package_body_reviewed",
            "review_status": "retained_as_optional_deep_module_doctrine",
            "superseded_by": "",
        },
    }
    for slug, fields in expected.items():
        validate_fields(entries, slug, fields, catalog_decision=True)


def validate_reviewed_skill(
    path: Path,
    revision_fragment: str,
    required_sections: list[str],
) -> tuple[dict[str, Any], str, str]:
    frontmatter, body, raw = load_markdown(path)
    require(
        frontmatter.get("source_status") == "distilled-reviewed",
        f"{path.relative_to(ROOT)} source_status must be distilled-reviewed",
    )
    require(
        frontmatter.get("review_status")
        == "source_reviewed_utility_evaluation_pending",
        f"{path.relative_to(ROOT)} review_status mismatch",
    )
    revision = str(frontmatter.get("source_revision") or "")
    require(
        revision_fragment in revision,
        f"{path.relative_to(ROOT)} missing pinned source revision",
    )
    require(
        "unpinned-review-required" not in revision,
        f"{path.relative_to(ROOT)} must not retain an unpinned revision",
    )
    require(
        frontmatter.get("source_content_copied") is not True,
        f"{path.relative_to(ROOT)} must not disclose copied source content",
    )
    for section in required_sections:
        require(section in body, f"{path.relative_to(ROOT)} missing {section}")
    return frontmatter, body, raw


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
        ROOT / "skills/seo-project-context.md": "seo-project-setup@9101f1479e128fb08296348b8041df03a9a654d8",
        ROOT / "skills/seo-keyword-opportunity-research.md": "keyword-research@4bdfc40dd4a27756f3abbc291b7b1bfe1176699c",
        ROOT / "skills/seo-keyword-page-mapping.md": "keyword-clustering@0fbadf7564b3127dd9f87f4fd14f7e17c9bc4b39",
        ROOT / "skills/seo-competitive-research.md": "competitive-landscape@0883708810e7fae718da8bb8b12200d759efacb5",
        ROOT / "skills/seo-link-prospecting.md": "link-prospecting@e9b9fb7114c092e41dd06c6b6d0e0e77f3afd4eb",
        ROOT / "skills/ai-search-visibility-audit.md": "packaged-ai-seo@62339de9a8c7ff51f3e8ff682e4c5e80a3dbc89d",
        ROOT / "skills/codebase-structural-map.md": "code-review-graph@6ce25b4e53f9df397f5136e86a59e17c02a610fe",
        ROOT / "skills/change-impact-review.md": "codebase-memory-mcp@7d6cdb23ef5ca2fd51f5d5b7509b33e112ef15f3",
    }
    loaded = {
        path: validate_reviewed_skill(path, revision, required_sections)
        for path, revision in reviewed.items()
    }

    video_path = ROOT / "skills/programmatic-video-production.md"
    frontmatter, _, raw = loaded[video_path]
    require(
        frontmatter.get("risk_level") == "high"
        and frontmatter.get("requires_review") is True,
        "programmatic-video-production must remain high risk and review gated",
    )
    require(
        frontmatter.get("source_content_copied") is False,
        "programmatic-video-production must disclose source_content_copied=false",
    )
    for evidence in [
        "remotion-skills@0dd76fafa3fd337b7bc6b5cd95b7db0179828a3d",
        "remotion-license@b8fdb73ae8600d011afb246a02b690bf6935f527",
        "## Output Contract",
        "Require separate explicit approval before any of:",
    ]:
        require(evidence in raw, f"programmatic video skill missing: {evidence}")

    link_path = ROOT / "skills/seo-link-prospecting.md"
    frontmatter, _, raw = loaded[link_path]
    require(
        frontmatter.get("requires_review") is True,
        "seo-link-prospecting must remain review gated",
    )
    for evidence in [
        "Do not collect unrelated personal information",
        "Separate sending from drafting",
        "No contact enrichment, CRM write, sequence, message, follow-up, tracking pixel, or publication occurred without explicit approval",
    ]:
        require(evidence in raw, f"SEO link prospecting missing: {evidence}")

    visibility_path = ROOT / "skills/ai-search-visibility-audit.md"
    _, _, raw = loaded[visibility_path]
    for evidence in [
        "current official source",
        "Observed citations are separated from hypotheses",
        "does not guarantee citation, ranking, inclusion, or traffic impact",
        "preserves no static platform statistics",
    ]:
        require(evidence in raw, f"AI search visibility missing: {evidence}")

    for path in [
        ROOT / "skills/seo-keyword-opportunity-research.md",
        ROOT / "skills/seo-keyword-page-mapping.md",
    ]:
        _, _, raw = loaded[path]
        require(
            "explicit confirmation" in raw or "without approval" in raw,
            f"{path.relative_to(ROOT)} must gate connector mutations",
        )
        require(
            "unknown" in raw.lower(),
            f"{path.relative_to(ROOT)} must preserve unknown evidence",
        )

    structural_path = ROOT / "skills/codebase-structural-map.md"
    frontmatter, _, raw = loaded[structural_path]
    require(
        frontmatter.get("risk_level") == "medium"
        and frontmatter.get("requires_review") is True,
        "codebase-structural-map must remain medium risk and review gated",
    )
    for evidence in [
        "Separate installation from analysis",
        "Generated graph outputs do not overwrite canonical architecture",
        "Do not install all three by default",
        "codebase-memory-mcp@7d6cdb23ef5ca2fd51f5d5b7509b33e112ef15f3",
        "understand-anything@6ae71878beb50226a1e4b7e2f52ac6468c86f74b",
    ]:
        require(evidence in raw or evidence in (ROOT / "sources/reviewed/2026-07-22-code-intelligence-cluster.md").read_text(encoding="utf-8"), f"codebase structural map missing: {evidence}")

    impact_path = ROOT / "skills/change-impact-review.md"
    _, _, raw = loaded[impact_path]
    for evidence in [
        "Every reported impact or defect is supported by source, configuration, history, test, or runtime evidence",
        "Posting a PR comment",
        "Graph coverage, freshness, exclusions, and engine revision are disclosed",
    ]:
        require(evidence in raw, f"change impact review missing: {evidence}")

    candidate_path = ROOT / "skills/recent-source-research.md"
    frontmatter, body, _ = load_markdown(candidate_path)
    require(
        frontmatter.get("source_status") == "distilled_candidate",
        "recent-source-research must remain a distilled candidate",
    )
    require(
        frontmatter.get("source_revision") == "unpinned-review-required",
        "recent-source-research must disclose unpinned upstream revision",
    )
    for section in required_sections:
        require(section in body, f"{candidate_path.relative_to(ROOT)} missing {section}")


def validate_source_reviews() -> None:
    reviews = {
        ROOT / "sources/reviewed/2026-07-22-design-quality-cluster.md": [
            "aeb42fb354ff4efa36ab475773a082315a3af2ce",
            "98565e65bc3274ddf6eb0838734341714057178b",
            "047d036a79cc2ddecd868e7f1e3aa04b495644b2",
            "No root `LICENSE` file was found",
            "do not copy or redistribute snippets",
        ],
        ROOT / "sources/reviewed/2026-07-22-programmatic-video-cluster.md": [
            "84e4eafacdaf96e8d137ba745af750448c5de0de",
            "0dd76fafa3fd337b7bc6b5cd95b7db0179828a3d",
            "b8fdb73ae8600d011afb246a02b690bf6935f527",
            "License: Apache-2.0",
            "up to three employees",
            "do not copy or redistribute skill bodies",
            "Do not execute remote shell installers",
        ],
        ROOT / "sources/reviewed/2026-07-22-seo-evidence-cluster.md": [
            "95e95d48cb88e60e1277422254e59c59b3e7e2e2",
            "License: MIT",
            "d7d884f16474e989ff443e080f6e0d1ddb42c444",
            "4bdfc40dd4a27756f3abbc291b7b1bfe1176699c",
            "0fbadf7564b3127dd9f87f4fd14f7e17c9bc4b39",
            "e9b9fb7114c092e41dd06c6b6d0e0e77f3afd4eb",
            "Keyword saving is a connector mutation",
            "No OpenSEO skill body",
        ],
        ROOT / "sources/reviewed/2026-07-22-code-intelligence-cluster.md": [
            "6ce25b4e53f9df397f5136e86a59e17c02a610fe",
            "83c1ad6884340e94ff27816b4191ea6a23139cb4",
            "7d6cdb23ef5ca2fd51f5d5b7509b33e112ef15f3",
            "0b95352746a97a8cf2d1f3ba568bc7bb5e514d1f",
            "6ae71878beb50226a1e4b7e2f52ac6468c86f74b",
            "5df102e8a2e29cdfb881ae7ec5040f2766564680",
            "Do not install all three by default",
            "A parser edge or risk score is evidence for inspection, not proof",
            "Generated graph and onboarding artifacts must not overwrite canonical architecture",
        ],
    }
    for path, evidence_items in reviews.items():
        require_text(path, evidence_items)


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
