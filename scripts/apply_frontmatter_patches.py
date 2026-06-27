#!/usr/bin/env python3
"""
Apply frontmatter proposals from reports/frontmatter-proposals.json to dist/skills.

Default mode is dry-run. Use --write to persist changes.
Supports limiting by count, path prefix, or explicit paths for safer batch rollout.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import json
import re
from typing import Iterable

import yaml

ROOT = Path("dist/skills")
PROPOSALS = Path("reports/frontmatter-proposals.json")
OUT = Path("reports")

FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)


def parse_frontmatter(text: str):
    match = FM_RE.match(text)
    if not match:
        return {}, text, False
    try:
        fm = yaml.safe_load(match.group(1))
        if not isinstance(fm, dict):
            fm = {}
    except yaml.YAMLError:
        fm = {}
    return fm, text[match.end():], True


def render_frontmatter(fm: dict) -> str:
    cleaned = {}
    for key, value in fm.items():
        if value in ("", None, [], {}):
            continue
        cleaned[key] = value
    return "---\n" + yaml.safe_dump(cleaned, sort_keys=False, allow_unicode=True).strip() + "\n---\n\n"


def normalize_type(value: str) -> str:
    text = (value or "").strip()
    return text or "Playbook"


def normalize_title(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip())


def normalize_description(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip())


def is_placeholder_description(value: str) -> bool:
    text = normalize_description(value)
    if not text:
        return True
    return text in {">", "|", ">-", "|-"} or text.startswith("<!--") or "AUTO-GENERATED" in text


def slug_to_title(value: str) -> str:
    text = value.replace("_", " ").replace("-", " ").strip()
    text = re.sub(r"\s+", " ", text)
    if not text:
        return value
    return " ".join(
        word.upper() if len(word) <= 3 and word.lower() in {"api", "cli", "sdk", "css", "html", "sql", "aws", "gcp"} else word.capitalize()
        for word in text.split()
    )


def first_heading(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return re.sub(r"\s+\([^)]*\)$", "", line[2:].strip()).strip()
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
    return normalize_description(" ".join(lines))


def dedupe_tags(tags: Iterable[str]) -> list[str]:
    out = []
    seen = set()
    for tag in tags or []:
        value = str(tag).strip().lower()
        if not value:
            continue
        if value not in seen:
            seen.add(value)
            out.append(value)
    return out


TAG_RENAMES = {
    "agent-skill": "skill",
    "software-development": "software-engineering",
}


def normalize_tags(tags: Iterable[str], domain: str) -> list[str]:
    normalized = []
    seen = set()
    for tag in tags or []:
        value = TAG_RENAMES.get(str(tag).strip().lower(), str(tag).strip().lower())
        if not value:
            continue
        if value not in seen:
            seen.add(value)
            normalized.append(value)
    if domain and domain not in seen:
        normalized.insert(0, domain)
    if "okf" not in seen:
        normalized.append("okf")
    return normalized


def load_proposals() -> list[dict]:
    return json.loads(PROPOSALS.read_text(encoding="utf-8"))


def should_include(rel_path: str, args) -> bool:
    normalized = rel_path.replace("\\", "/")
    if args.paths and normalized not in args.paths:
        return False
    if args.prefix and not normalized.startswith(args.prefix):
        return False
    return True


def apply_proposal(rel_path: str, proposal: dict, write: bool) -> dict:
    target = ROOT / Path(rel_path)
    original = target.read_text(encoding="utf-8", errors="replace")
    current_fm, body, had_frontmatter = parse_frontmatter(original)
    proposed = proposal["proposed_frontmatter"]
    heading = first_heading(body)

    merged = dict(current_fm)
    merged["name"] = current_fm.get("name") or proposed.get("name") or target.parent.name
    current_title = normalize_title(current_fm.get("title", ""))
    current_name = str(current_fm.get("name", "")).strip()
    if current_title and heading and current_name and current_title == current_name and current_title == current_title.lower():
        current_title = ""
    merged["title"] = (
        current_title
        or heading
        or normalize_title(proposed.get("title", ""))
        or slug_to_title(current_name or proposed.get("name", "") or target.parent.name)
    )
    current_desc = normalize_description(current_fm.get("description", ""))
    if is_placeholder_description(current_desc):
        current_desc = ""
    proposed_desc = normalize_description(proposed.get("description", ""))
    if is_placeholder_description(proposed_desc):
        proposed_desc = ""
    merged["description"] = (
        current_desc
        or proposed_desc
        or first_meaningful_paragraph(body)
    )
    merged["type"] = normalize_type(current_fm.get("type", "") or proposed.get("type", ""))
    merged["domain"] = current_fm.get("domain") or proposed.get("domain", "")
    merged["tags"] = normalize_tags(current_fm.get("tags") or proposed.get("tags") or [], merged["domain"])
    merged["risk_level"] = current_fm.get("risk_level") or proposed.get("risk_level", "")
    merged["requires_review"] = (
        current_fm["requires_review"]
        if "requires_review" in current_fm and current_fm["requires_review"] not in ("", None)
        else proposed.get("requires_review")
    )
    current_source_family = str(current_fm.get("source_family", "")).strip()
    proposed_source_family = str(proposed.get("source_family", "")).strip()
    merged["source_family"] = current_source_family
    if (not merged["source_family"] or merged["source_family"] == "unknown") and proposed_source_family and proposed_source_family != "unknown":
        merged["source_family"] = proposed_source_family

    if "license" in current_fm and "source_license" not in current_fm:
        merged["source_license"] = current_fm["license"]

    if "source_status" not in merged or not merged.get("source_status"):
        merged["source_status"] = "adapted" if merged.get("source_family") and merged["source_family"] != "unknown" else ""

    new_text = render_frontmatter(merged) + body.lstrip("\r\n")

    changed = new_text != original
    if changed and write:
        target.write_text(new_text, encoding="utf-8")

    return {
        "path": rel_path,
        "changed": changed,
        "had_frontmatter": had_frontmatter,
        "written": changed and write,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Persist changes to files")
    parser.add_argument("--limit", type=int, default=0, help="Apply only the first N matching proposals")
    parser.add_argument("--prefix", default="", help="Only apply to paths with this prefix, e.g. a11y-audit/")
    parser.add_argument("--paths", nargs="*", default=[], help="Explicit relative paths under dist/skills")
    args = parser.parse_args()

    proposals = load_proposals()
    selected = [p for p in proposals if should_include(p["path"], args)]
    if args.limit > 0:
        selected = selected[: args.limit]

    results = [apply_proposal(p["path"], p, args.write) for p in selected]
    changed = [r for r in results if r["changed"]]
    report = {
        "write": args.write,
        "selected_count": len(selected),
        "changed_count": len(changed),
        "results": results,
    }
    OUT.mkdir(exist_ok=True)
    (OUT / "frontmatter-apply-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Selected: {len(selected)}")
    print(f"Changed:  {len(changed)}")
    print(f"Write:    {args.write}")
    print("Wrote: reports/frontmatter-apply-report.json")


if __name__ == "__main__":
    main()
