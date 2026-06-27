#!/usr/bin/env python3
"""
Build lightweight distribution manifests for GitHub- and package-based skill installs.
"""
from __future__ import annotations

from pathlib import Path
from collections import Counter, defaultdict
import json
import re

import yaml

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SKILLS = DIST / "skills"
REPORT = ROOT / "reports" / "dist-skills-enriched-inventory.json"
FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)


def load_inventory() -> list[dict]:
    rows = json.loads(REPORT.read_text(encoding="utf-8"))
    by_path = {row["path"].replace("\\", "/"): row for row in rows}

    for skill_file in sorted(SKILLS.rglob("SKILL.md")):
        rel_path = skill_file.relative_to(SKILLS).as_posix()
        if rel_path not in by_path:
            by_path[rel_path] = synthesize_inventory_row(skill_file, rel_path)

    return list(by_path.values())


def parse_frontmatter(text: str):
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


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip())


def first_heading(body: str) -> str:
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def first_meaningful_paragraph(body: str) -> str:
    lines = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            if lines:
                break
            continue
        if line.startswith("#") or line.startswith(">") or line.startswith("```") or line.startswith("<!--"):
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


def synthesize_inventory_row(skill_file: Path, rel_path: str) -> dict:
    text = skill_file.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(text)
    tags = fm.get("tags") or []
    if not isinstance(tags, list):
        tags = [tags]
    title = fm.get("title") or first_heading(body) or skill_file.parent.name
    description = normalize_text(str(fm.get("description") or "")) or first_meaningful_paragraph(body)
    domain = fm.get("domain") or derive_domain_from_tags(tags)
    risk_level = fm.get("risk_level") or ""
    return {
        "path": rel_path,
        "name": str(fm.get("name") or skill_file.parent.name),
        "title": title,
        "description": description,
        "type": str(fm.get("type") or "Playbook"),
        "tags": tags,
        "domain": domain,
        "risk_level": risk_level,
        "requires_review": bool(fm.get("requires_review", risk_level == "high")),
        "source_family": str(fm.get("source_family") or ""),
        "source_status": str(fm.get("source_status") or ""),
    }


def skill_entry(row: dict) -> dict:
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
        "tags": row.get("tags") or [],
        "source_family": row.get("source_family", ""),
        "source_status": row.get("source_status", ""),
        "type": row.get("type") or "Playbook",
    }


def build_catalog(rows: list[dict]) -> dict:
    entries = [skill_entry(row) for row in rows]
    by_domain: dict[str, list[str]] = defaultdict(list)
    for entry in entries:
        by_domain[entry["domain"] or "uncategorized"].append(entry["slug"])

    domain_counts = Counter(entry["domain"] or "uncategorized" for entry in entries)
    risk_counts = Counter(entry["risk_level"] or "unspecified" for entry in entries)

    return {
        "schema_version": "0.1",
        "package": {
            "name": "@teleagent/skills",
            "install_root": "dist/skills",
            "entrypoint": "README.md",
        },
        "summary": {
            "skill_count": len(entries),
            "domain_counts": dict(sorted(domain_counts.items())),
            "risk_counts": dict(sorted(risk_counts.items())),
        },
        "domains": {
            domain: sorted(slugs)
            for domain, slugs in sorted(by_domain.items())
        },
        "skills": entries,
    }


def build_install_manifest(catalog: dict) -> dict:
    return {
        "schema_version": "0.1",
        "package_name": catalog["package"]["name"],
        "distribution_kind": "skill-bundle",
        "install_root": catalog["package"]["install_root"],
        "discovery_files": [
            "README.md",
            "dist/catalog.json",
            "dist/catalog.md",
            "dist/install-manifest.json",
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
            "tags",
            "requires_review",
        ],
    }


def build_catalog_markdown(catalog: dict) -> str:
    lines = [
        "# Skills Distribution Catalog",
        "",
        f"- Package: `{catalog['package']['name']}`",
        f"- Install root: `{catalog['package']['install_root']}`",
        f"- Skill count: **{catalog['summary']['skill_count']}**",
        "",
        "## Domains",
        "",
        "| Domain | Count |",
        "|---|---:|",
    ]
    for domain, count in catalog["summary"]["domain_counts"].items():
        lines.append(f"| `{domain}` | {count} |")

    lines += [
        "",
        "## Risk Levels",
        "",
        "| Risk | Count |",
        "|---|---:|",
    ]
    for risk, count in catalog["summary"]["risk_counts"].items():
        lines.append(f"| `{risk}` | {count} |")

    lines += [
        "",
        "## Install Notes",
        "",
        "- GitHub/open-repo consumers should start at `README.md` and inspect `dist/catalog.json` for machine-readable discovery.",
        "- Runtime installers should copy from `dist/skills/` and preserve per-skill directories.",
        "- High-risk or `requires_review=true` skills should require explicit user confirmation before automatic install/use.",
    ]
    return "\n".join(lines) + "\n"


def main():
    rows = load_inventory()
    catalog = build_catalog(rows)
    install_manifest = build_install_manifest(catalog)
    catalog_md = build_catalog_markdown(catalog)

    (DIST / "catalog.json").write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")
    (DIST / "install-manifest.json").write_text(
        json.dumps(install_manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (DIST / "catalog.md").write_text(catalog_md, encoding="utf-8")

    print(f"Wrote: {DIST / 'catalog.json'}")
    print(f"Wrote: {DIST / 'install-manifest.json'}")
    print(f"Wrote: {DIST / 'catalog.md'}")


if __name__ == "__main__":
    main()
