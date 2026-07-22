#!/usr/bin/env python3
"""Build package-facing skill catalog surfaces with reviewed metadata overrides."""
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
    "agent-operations", "business", "cloud-security", "design", "forensics",
    "media", "research", "runtime-tools", "security-defensive",
    "security-offensive", "software-engineering", "writing",
}
ALLOWED_RISKS = {"low", "medium", "high"}
ALLOWED_KINDS = {
    "skill", "skill-suite", "playbook", "workflow", "runbook",
    "source-profile", "reference",
}
OVERRIDE_FIELDS = {
    "domain", "risk_level", "requires_review", "artifact_kind",
    "target_surfaces", "source_family", "source_status", "review_status",
    "source_url", "source_revision", "license", "classification_evidence",
}


def text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip())


def values(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    raw = value if isinstance(value, list) else [value]
    return [text(item) for item in raw if text(item)]


def parse_frontmatter(raw: str) -> tuple[dict[str, Any], str]:
    match = FM_RE.match(raw)
    if not match:
        return {}, raw
    try:
        parsed = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        parsed = {}
    return (parsed if isinstance(parsed, dict) else {}), raw[match.end():]


def heading(body: str) -> str:
    return next(
        (line.strip()[2:] for line in body.splitlines() if line.strip().startswith("# ")),
        "",
    )


def paragraph(body: str) -> str:
    collected: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            if collected:
                break
            continue
        if line.startswith(("#", ">", "```", "<!--", "|")) or re.match(r"^[-*]\s", line):
            continue
        collected.append(line)
        if len(" ".join(collected)) >= 220:
            break
    return text(" ".join(collected))


def domain_from_tags(tags: list[str]) -> str:
    preferred = [
        "software-engineering", "security-defensive", "design", "business",
        "runtime-tools", "agent-operations", "writing", "security-offensive",
        "cloud-security", "research", "forensics", "media",
    ]
    tag_set = {tag.lower() for tag in tags}
    return next((candidate for candidate in preferred if candidate in tag_set), "")


def artifact_kind(frontmatter: dict[str, Any]) -> str:
    explicit = text(frontmatter.get("artifact_kind")).lower()
    if explicit:
        return explicit
    aliases = {
        "skill": "skill",
        "playbook": "playbook",
        "workflow": "workflow",
        "runbook": "runbook",
        "source profile": "source-profile",
        "source-profile": "source-profile",
        "reference": "reference",
    }
    return aliases.get(text(frontmatter.get("type") or "Playbook").lower(), "playbook")


def classification_status(row: dict[str, Any]) -> str:
    if row.get("domain") and row.get("risk_level"):
        return "complete"
    if row.get("domain") or row.get("risk_level"):
        return "partial"
    return "unclassified"


def synthesize(skill_file: Path, rel_path: str) -> dict[str, Any]:
    frontmatter, body = parse_frontmatter(
        skill_file.read_text(encoding="utf-8", errors="replace")
    )
    tags = values(frontmatter.get("tags"))
    risk = text(frontmatter.get("risk_level")).lower()
    row = {
        "path": rel_path,
        "name": str(frontmatter.get("name") or skill_file.parent.name),
        "title": str(frontmatter.get("title") or heading(body) or skill_file.parent.name),
        "description": text(frontmatter.get("description")) or paragraph(body),
        "type": str(frontmatter.get("type") or "Playbook"),
        "artifact_kind": artifact_kind(frontmatter),
        "tags": tags,
        "domain": text(frontmatter.get("domain")) or domain_from_tags(tags),
        "risk_level": risk,
        "requires_review": bool(frontmatter.get("requires_review", risk == "high")),
        "target_surfaces": values(frontmatter.get("target_surfaces")),
        "source_family": text(frontmatter.get("source_family")),
        "source_status": text(frontmatter.get("source_status")),
        "review_status": text(frontmatter.get("review_status")),
        "source_url": text(frontmatter.get("source_url")),
        "source_revision": text(frontmatter.get("source_revision")),
        "license": text(frontmatter.get("license")),
        "classification_evidence": text(frontmatter.get("classification_evidence")),
        "classification_override": False,
    }
    row["classification_status"] = classification_status(row)
    return row


def load_inventory() -> list[dict[str, Any]]:
    inventory = json.loads(REPORT.read_text(encoding="utf-8-sig"))
    current = {
        file.relative_to(SKILLS).as_posix(): file
        for file in sorted(SKILLS.rglob("SKILL.md"))
    }
    rows = {
        row["path"].replace("\\", "/"): row
        for row in inventory
        if row["path"].replace("\\", "/") in current
    }
    for rel_path, skill_file in current.items():
        rows[rel_path] = synthesize(skill_file, rel_path)
    return list(rows.values())


def load_overrides() -> list[dict[str, Any]]:
    if not OVERRIDES.exists():
        return []
    payload = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    if payload.get("schema_version") != "0.1":
        raise ValueError("classification override schema_version must be 0.1")
    overrides = payload.get("overrides")
    if not isinstance(overrides, list):
        raise ValueError("classification overrides must be a list")

    seen: set[tuple[str, str]] = set()
    for index, override in enumerate(overrides):
        if not isinstance(override, dict):
            raise ValueError(f"classification override {index} must be an object")
        name = text(override.get("name"))
        path = text(override.get("path")).replace("\\", "/")
        if not name and not path:
            raise ValueError(f"classification override {index} requires name or path")
        identity = ("path", path) if path else ("name", name)
        if identity in seen:
            raise ValueError(f"duplicate classification override: {identity}")
        seen.add(identity)

        domain = text(override.get("domain"))
        risk = text(override.get("risk_level")).lower()
        kind = text(override.get("artifact_kind")).lower()
        if domain and domain not in ALLOWED_DOMAINS:
            raise ValueError(f"unsupported domain {domain!r} for {name or path}")
        if risk and risk not in ALLOWED_RISKS:
            raise ValueError(f"unsupported risk_level {risk!r} for {name or path}")
        if kind and kind not in ALLOWED_KINDS:
            raise ValueError(f"unsupported artifact_kind {kind!r} for {name or path}")
        if "requires_review" in override and not isinstance(override["requires_review"], bool):
            raise ValueError(f"requires_review must be boolean for {name or path}")
        surfaces = override.get("target_surfaces", [])
        if not isinstance(surfaces, list) or not all(
            isinstance(item, str) and item.strip() for item in surfaces
        ):
            raise ValueError(f"target_surfaces must be a string list for {name or path}")
    return overrides


def apply_overrides(
    rows: list[dict[str, Any]], overrides: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], int]:
    name_counts = Counter(str(row.get("name") or "") for row in rows)
    by_path = {str(row["path"]).replace("\\", "/"): row for row in rows}
    by_name = {
        str(row["name"]): row
        for row in rows
        if name_counts[str(row.get("name") or "")] == 1
    }

    for override in overrides:
        path = text(override.get("path")).replace("\\", "/")
        name = text(override.get("name"))
        row = by_path.get(path) if path else by_name.get(name)
        if row is None:
            if name_counts.get(name, 0) > 1:
                raise ValueError(f"override name {name!r} is ambiguous; use path")
            raise ValueError(f"override did not match a packaged skill: {path or name}")

        for field in OVERRIDE_FIELDS:
            if field not in override:
                continue
            value = override[field]
            if field == "target_surfaces":
                value = values(value)
            elif field != "requires_review":
                value = text(value)
                if field in {"risk_level", "artifact_kind"}:
                    value = value.lower()
            row[field] = value
        row["classification_override"] = True
        row["classification_status"] = classification_status(row)

    return rows, len(overrides)


def catalog_entry(row: dict[str, Any]) -> dict[str, Any]:
    rel_path = row["path"].replace("\\", "/")
    directory = rel_path.rsplit("/", 1)[0]
    return {
        "slug": row["name"],
        "title": row.get("title") or row["name"],
        "description": row.get("description", ""),
        "path": f"dist/skills/{rel_path}",
        "directory": f"dist/skills/{directory}",
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


def counts(entries: list[dict[str, Any]], field: str, fallback: str) -> dict[str, int]:
    return dict(sorted(Counter(entry.get(field) or fallback for entry in entries).items()))


def build_catalog(
    rows: list[dict[str, Any]], override_count: int
) -> dict[str, Any]:
    entries = [catalog_entry(row) for row in rows]
    domains: dict[str, list[str]] = defaultdict(list)
    for entry in entries:
        domains[entry["domain"] or "uncategorized"].append(entry["slug"])
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
            "requires_review_count": sum(entry["requires_review"] for entry in entries),
            "classification_overrides_applied": override_count,
            "domain_counts": counts(entries, "domain", "uncategorized"),
            "risk_counts": counts(entries, "risk_level", "unspecified"),
            "artifact_kind_counts": counts(entries, "artifact_kind", "unspecified"),
            "classification_counts": counts(entries, "classification_status", "unclassified"),
            "source_status_counts": counts(entries, "source_status", "unspecified"),
        },
        "domains": {
            domain: sorted(slugs) for domain, slugs in sorted(domains.items())
        },
        "skills": entries,
    }


def build_manifest(catalog: dict[str, Any]) -> dict[str, Any]:
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
            "slug", "title", "domain", "risk_level", "artifact_kind",
            "target_surfaces", "source_status", "review_status", "tags",
            "requires_review",
        ],
    }


def add_table(
    lines: list[str], heading: str, label: str, table_counts: dict[str, int]
) -> None:
    lines.extend(["", f"## {heading}", "", f"| {label} | Count |", "|---|---:|"])
    lines.extend(f"| `{key}` | {count} |" for key, count in table_counts.items())


def build_markdown(catalog: dict[str, Any]) -> str:
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
        "Classification overrides repair catalog metadata without rewriting imported skill bodies. Inclusion remains untrusted until source, license, safety, and utility review pass.",
    ]
    add_table(lines, "Domains", "Domain", summary["domain_counts"])
    add_table(lines, "Risk Levels", "Risk", summary["risk_counts"])
    add_table(lines, "Artifact Kinds", "Artifact kind", summary["artifact_kind_counts"])
    add_table(
        lines, "Classification Completeness", "Status",
        summary["classification_counts"],
    )
    add_table(lines, "Source Status", "Source status", summary["source_status_counts"])
    lines.extend([
        "",
        "## Install Notes",
        "",
        "- Inspect `dist/catalog.json` before selecting skills.",
        "- Preserve complete per-skill directories during installation.",
        "- High-risk or `requires_review=true` skills require explicit confirmation.",
        "- `classification_override=true` means only the catalog metadata was separately reviewed.",
        "- `target_surfaces` is a routing hint, not an authority grant.",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = load_inventory()
    rows, override_count = apply_overrides(rows, load_overrides())
    catalog = build_catalog(rows, override_count)
    (DIST / "catalog.json").write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (DIST / "install-manifest.json").write_text(
        json.dumps(build_manifest(catalog), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (DIST / "catalog.md").write_text(build_markdown(catalog), encoding="utf-8")
    print(f"Applied classification overrides: {override_count}")


if __name__ == "__main__":
    main()
