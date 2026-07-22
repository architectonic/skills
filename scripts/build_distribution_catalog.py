#!/usr/bin/env python3
"""
Build lightweight distribution manifests for GitHub- and package-based skill installs.

Imported skill files are preserved as source artifacts. Reviewed catalog corrections
are applied from operations/classification-overrides.json so classification can evolve
without silently rewriting third-party material.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json
import re
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SKILLS = DIST / "skills"
REPORT = ROOT / "reports" / "dist-skills-enriched-inventory.json"
OVERRIDES = ROOT / "operations" / "classification-overrides.json"
FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)

ALLOWED_DOMAINS = {
    "agent-operations",
    "business",
    "cloud-security",
    "design",
    "forensics",
    "media",
    "research",
    "runtime-tools",
    "security-defensive",
    "security-offensive",
    "software-engineering",
    "writing",
}
ALLOWED_RISK_LEVELS = {"low", "medium", "high"}
ALLOWED_ARTIFACT_KINDS = {
    "skill",
    "skill-suite",
    "playbook",
    "workflow",
    "runbook",
    "source-profile",
    "reference",
}


def load_inventory() -> list[dict[str, Any]]:
    rows = json.loads(REPORT.read_text(encoding="utf-8-sig"))
    current_paths = {
        skill_file.relative_to(SKILLS).as_posix()
        for skill_file in sorted(SKILLS.rglob("SKILL.md"))
    }
    by_path = {
        row["path"].replace("\\", "/"): row
        for row in rows
        if row["path"].replace("\\", "/") in current_paths
    }

    for skill_file in sorted(SKILLS.rglob("SKILL.md")):
        rel_path = skill_file.relative_to(SKILLS).as_posix()
        by_path[rel_path] = synthesize_inventory_row(skill_file, rel_path)

    return list(by_path.values())


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = FM_RE.match(text)
    if not match:
        return {}, text
    try:
        fm = yaml.safe_load(match.group(1))
        if not isinstance(fm, dict):
            fm = {}
    except yaml.YAMLError:
        fm = {}
    return fm, text[match.end():]


def normalize_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip())


def normalize_list(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    values = value if isinstance(value, list) else [value]
    return [
        normalize_text(item)
        for item in values
        if normalize_text(item)
    ]


def first_heading(body: str) -> str:
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def first_meaningful_paragraph(body: str) -> str:
    lines: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            if lines:
                break
            continue
        if (
            line.startswith("#")
            or line.startswith(">")
            or line.startswith("```")
            or line.startswith("<!--")
        ):
            continue
        if line.startswith("|") or re.match(r"^[-*]\s", line):
            continue
        lines.append(line)
        if len(" ".join(lines)) >= 220:
            break
    return normalize_text(" ".join(lines))


def derive_domain_from_tags(tags: list[str]) -> str:
    preferred = [
        "software-engineering",
        "security-defensive",
        "design",
        "business",
        "runtime-tools",
        "agent-operations",
        "writing",
        "security-offensive",
        "cloud-security",
        "research",
        "forensics",
        "media",
    ]
    tag_set = {str(tag).strip().lower() for tag in tags or []}
    for candidate in preferred:
        if candidate in tag_set:
            return candidate
    return ""


def derive_artifact_kind(fm: dict[str, Any]) -> str:
    explicit = normalize_text(fm.get("artifact_kind")).lower()
    if explicit:
        return explicit
    raw_type = normalize_text(fm.get("type") or "Playbook").lower()
    aliases = {
        "skill": "skill",
        "playbook": "playbook",
        "workflow": "workflow",
        "runbook": "runbook",
        "source profile": "source-profile",
        "source-profile": "source-profile",
        "reference": "reference",
    }
    return aliases.get(raw_type, "playbook")


def classification_status(row: dict[str, Any]) -> str:
    if row.get("domain") and row.get("risk_level"):
        return "complete"
    if row.get("domain") or row.get("risk_level"):
        return "partial"
    return "unclassified"


def synthesize_inventory_row(skill_file: Path, rel_path: str) -> dict[str, Any]:
    text = skill_file.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(text)
    tags = normalize_list(fm.get("tags"))
    title = fm.get("title") or first_heading(body) or skill_file.parent.name
    description = normalize_text(fm.get("description")) or first_meaningful_paragraph(body)
    domain = normalize_text(fm.get("domain")) or derive_domain_from_tags(tags)
    risk_level = normalize_text(fm.get("risk_level")).lower()
    artifact_kind = derive_artifact_kind(fm)
    row = {
        "path": rel_path,
        "name": str(fm.get("name") or skill_file.parent.name),
        "title": str(title),
        "description": description,
        "type": str(fm.get("type") or "Playbook"),
        "artifact_kind": artifact_kind,
        "tags": tags,
        "domain": domain,
        "risk_level": risk_level,
        "requires_review": bool(fm.get("requires_review", risk_level == "high")),
        "target_surfaces": normalize_list(fm.get("target_surfaces")),
        "source_family": normalize_text(fm.get("source_family")),
        "source_status": normalize_text(fm.get("source_status")),
        "review_status": normalize_text(fm.get("review_status")),
        "source_url": normalize_text(fm.get("source_url")),
        "source_revision": normalize_text(fm.get("source_revision")),
        "license": normalize_text(fm.get("license")),
        "classification_evidence": normalize_text(fm.get("classification_evidence")),
        "classification_override": false,
    }
    row["classification_status"] = classification_status(row)
    return row


def load_classification_overrides() -> list[dict[str, Any]]:
    if not OVERRIDES.exists():
        return []

    payload = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    if payload.get("schema_version") != "0.1":
        raise ValueError(f"{OVERRIDES.relative_to(ROOT)} schema_version must be 0.1")

    overrides = payload.get("overrides")
    if not isinstance(overrides, list):
        raise ValueError(f"{OVERRIDES.relative_to(ROOT)} overrides must be a list")

    seen: set[tuple[str, str]] = set()
    for index, override in enumerate(overrides):
        if not isinstance(override, dict):
            raise ValueError(f"classification override {index} must be an object")
        name = normalize_text(override.get("name"))
        path = normalize_text(override.get("path")).replace("\\", "/")
        if not name and not path:
            raise ValueError(f"classification override {index} requires name or path")
        identity = ("path", path) if path else ("name", name)
        if identity in seen:
            raise ValueError(f"duplicate classification override for {identity[0]}={identity[1]!r}")
        seen.add(identity)

        domain = normalize_text(override.get("domain"))
        if domain and domain not in ALLOWED_DOMAINS:
            raise ValueError(f"unsupported domain {domain!r} for override {name or path}")

        risk_level = normalize_text(override.get("risk_level")).lower()
        if risk_level and risk_level not in ALLOWED_RISK_LEVELS:
            raise ValueError(f"unsupported risk_level {risk_level!r} for override {name or path}")

        artifact_kind = normalize_text(override.get("artifact_kind")).lower()
        if artifact_kind and artifact_kind not in ALLOWED_ARTIFACT_KINDS:
            raise ValueError(f"unsupported artifact_kind {artifact_kind!r} for override {name or path}")

        if "requires_review" in override and not isinstance(override["requires_review"], bool):
            raise ValueError(f"requires_review must be boolean for override {name or path}")

        surfaces = override.get("target_surfaces", [])
        if not isinstance(surfaces, list) or not all(
            isinstance(item, str) and item.strip() for item in surfaces
        ):
            raise ValueError(f"target_surfaces must be a non-empty-string list for override {name or path}")

    return overrides


def apply_classification_overrides(
    rows: list[dict[str, Any]],
    overrides: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], int]:
    if not overrides:
        return rows, 0

    name_counts = Counter(str(row.get("name") or "") for row in rows)
    by_path = {
        str(row["path"]).replace("\\", "/"): row
        for row in rows
    }
    by_name = {
        str(row["name"]): row
        for row in rows
        if name_counts[str(row.get("name") or "")] == 1
    }

    override_fields = {
        "domain",
        "risk_level",
        "requires_review",
        "artifact_kind",
        "target_surfaces",
        "source_family",
        "source_status",
        "review_status",
        "source_url",
        "source_revision",
        "license",
        "classification_evidence",
    }

    matched = 0
    for override in overrides:
        path = normalize_text(override.get("path")).replace("\\", "/")
        name = normalize_text(override.get("name"))
        row = by_path.get(path) if path else by_name.get(name)
        if row is None:
            if name and name_counts.get(name, 0) > 1:
                raise ValueError(f"classification override name {name!r} is ambiguous; use path")
            raise ValueError(f"classification override did not match a packaged skill: {path or name}")

        for field in override_fields:
            if field not in override:
                continue
            value = override[field]
            if field == "target_surfaces":
                value = normalize_list(value)
            elif field in {
                "domain",
                "risk_level",
                "artifact_kind",
                "source_family",
                "source_status",
                "review_status",
                "source_url",
                "source_revision",
                "license",
                "classification_evidence",
            }:
                value = normalize_text(value)
                if field in {"risk_level", "artifact_kind"}:
                    value = value.lower()
            row[field] = value

        row["classification_override"] = True
        row["classification_status"] = classification_status(row)
        matched += 1

    return rows, matched


def skill_entry(row: dict[str, Any]) -> dict[str, Any]:
    rel_path = row["path"].replace("\\", "/")
    skill_dir = rel_path.rsplit("/", 1)[0]
    return {
        "slug": row["name"],
        "title": row.get("title") or row["name"],
        "description": row.get("description", ""),
        "path": f"dist/skills/{rel_path}",
        "directory": f"dist/skills/{skill_dir}",
        "domain": row.get("domain", ""),
        "risk_level": row.get("risk_level", ""),
        "requires_review": bool(row.get("requires_review")),
        "classification_status": row.get("classification_status", ""),
        "classification_override": bool(row.get("classification_override")),
        "classification_evidence": row.get("classification_evidence", ""),
        "artifact_kind": row.get("artifact_kind", "playbook"),
        "target_surfaces": row.get("target_surfaces") or [],
        "tags": row.get("tags") or [],
        "source_family": row.get("source_family", ""),
        "source_status": row.get("source_status", ""),
        "review_status": row.get("review_status", ""),
        "source_url": row.get("source_url", ""),
        "source_revision": row.get("source_revision", ""),
        "license": row.get("license", ""),
        "type": row.get("type") or "Playbook",
    }


def build_catalog(rows: list[dict[str, Any]], overrides_applied: int) -> dict[str, Any]:
    entries = [skill_entry(row) for row in rows]
    by_domain: dict[str, list[str]] = defaultdict(list)
    for entry in entries:
        by_domain[entry["domain"] or "uncategorized"].append(entry["slug"])

    domain_counts = Counter(entry["domain"] or "uncategorized" for entry in entries)
    risk_counts = Counter(entry["risk_level"] or "unspecified" for entry in entries)
    artifact_kind_counts = Counter(entry["artifact_kind"] or "unspecified" for entry in entries)
    classification_counts = Counter(entry["classification_status"] or "unclassified" for entry in entries)
    source_status_counts = Counter(entry["source_status"] or "unspecified" for entry in entries)

    return {
        "schema_version": "0.2",
        "package": {
            "name": "architectonic-skills",
            "install_root": "dist/skills",
            "entrypoint": "README.md",
            "classification_overrides": "operations/classification-overrides.json",
        },
        "summary": {
            "skill_count": len(entries),
            "requires_review_count": sum(1 for entry in entries if entry["requires_review"]),
            "classification_overrides_applied": overrides_applied,
            "domain_counts": dict(sorted(domain_counts.items())),
            "risk_counts": dict(sorted(risk_counts.items())),
            "artifact_kind_counts": dict(sorted(artifact_kind_counts.items())),
            "classification_counts": dict(sorted(classification_counts.items())),
            "source_status_counts": dict(sorted(source_status_counts.items())),
        },
        "domains": {
            domain: sorted(slugs)
            for domain, slugs in sorted(by_domain.items())
        },
        "skills": entries,
    }


def build_install_manifest(catalog: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "0.2",
        "package_name": catalog["package"]["name"],
        "distribution_kind": "skill-bundle",
        "install_root": catalog["package"]["install_root"],
        "discovery_files": [
            "README.md",
            "dist/catalog.json",
            "dist/catalog.md",
            "dist/install-manifest.json",
            "operations/classification-overrides.json",
        ],
        "recommended_entrypoints": {
            "github_repo": "README.md",
            "installer_catalog": "dist/catalog.json",
        },
        "selection_fields": [
            "slug",
            "title",
            "domain",
            "risk_level",
            "artifact_kind",
            "target_surfaces",
            "source_status",
            "review_status",
            "tags",
            "requires_review",
        ],
    }


def append_count_table(
    lines: list[str],
    heading: str,
    label: str,
    counts: dict[str, int],
) -> None:
    lines += [
        "",
        f"## {heading}",
        "",
        f"| {label} | Count |",
        "|---|---:|",
    ]
    for key, count in counts.items():
        lines.append(f"| `{key}` | {count} |")


def build_catalog_markdown(catalog: dict[str, Any]) -> str:
    summary = catalog["summary"]
    lines = [
        "# Skills Distribution Catalog",
        "",
        f"- Package: `{catalog['package']['name']}`",
        f"- Install root: `{catalog['package']['install_root']}`",
        f"- Skill count: **{summary['skill_count']}**",
        f"- Explicit review required: **{summary['requires_review_count']}**",
        f"- Classification overrides applied: **{summary['classification_overrides_applied']}**",
        "",
        "Classification overrides repair catalog metadata without rewriting imported skill bodies. Inclusion remains untrusted until the skill passes source, license, safety, and utility review.",
    ]

    append_count_table(lines, "Domains", "Domain", summary["domain_counts"])
    append_count_table(lines, "Risk Levels", "Risk", summary["risk_counts"])
    append_count_table(lines, "Artifact Kinds", "Artifact kind", summary["artifact_kind_counts"])
    append_count_table(lines, "Classification Completeness", "Status", summary["classification_counts"])
    append_count_table(lines, "Source Status", "Source status", summary["source_status_counts"])

    lines += [
        "",
        "## Install Notes",
        "",
        "- GitHub/open-repo consumers should start at `README.md` and inspect `dist/catalog.json` for machine-readable discovery.",
        "- Runtime installers should copy from `dist/skills/` and preserve per-skill directories.",
        "- High-risk or `requires_review=true` skills require explicit user confirmation before installation or use.",
        "- `classification_override=true` means metadata was reviewed separately from the imported skill body; it does not mean the procedure itself is approved.",
        "- Filter by `target_surfaces` only as a routing hint, never as an authority grant.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = load_inventory()
    overrides = load_classification_overrides()
    rows, overrides_applied = apply_classification_overrides(rows, overrides)
    catalog = build_catalog(rows, overrides_applied)
    install_manifest = build_install_manifest(catalog)
    catalog_md = build_catalog_markdown(catalog)

    (DIST / "catalog.json").write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (DIST / "install-manifest.json").write_text(
        json.dumps(install_manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (DIST / "catalog.md").write_text(catalog_md, encoding="utf-8")

    print(f"Wrote: {DIST / 'catalog.json'}")
    print(f"Wrote: {DIST / 'install-manifest.json'}")
    print(f"Wrote: {DIST / 'catalog.md'}")
    print(f"Applied classification overrides: {overrides_applied}")


if __name__ == "__main__":
    main()
