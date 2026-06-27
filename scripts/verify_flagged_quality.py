#!/usr/bin/env python3
"""
Verify the current state of the previously quality-gate-flagged dist/skills set.

This is a lightweight validator for iterative cleanup work when the full
enrichment pipeline is not needed or is temporarily being debugged.
"""
from __future__ import annotations

from pathlib import Path
import json
import re

import yaml

ROOT = Path("dist/skills")
FLAGGED = Path("reports/quality-gate-flagged.json")
OUT = Path("reports")

FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)


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


def verify_entry(rel_path: str, previous_issues: list[str]) -> dict:
    target = ROOT / rel_path
    text = target.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(text)
    issues = []

    description = normalize_text(str(fm.get("description", "") or ""))
    if "description too short" in previous_issues and len(description) < 20:
        issues.append("description too short")

    if "body too short (<100 chars)" in previous_issues and len(body.strip()) < 100:
        issues.append("body too short (<100 chars)")

    if "high-risk offensive without safety/legal framing" in previous_issues:
        lowered = body.lower()
        if "authorized" not in lowered and "legal" not in lowered:
            issues.append("high-risk offensive without safety/legal framing")

    return {
        "path": rel_path,
        "issues": issues,
        "passed": not issues,
    }


def main():
    flagged = json.loads(FLAGGED.read_text(encoding="utf-8"))
    results = [verify_entry(entry["path"], entry["issues"]) for entry in flagged]
    remaining = [item for item in results if item["issues"]]

    report = {
        "verified_count": len(results),
        "remaining_count": len(remaining),
        "remaining": remaining,
    }
    OUT.mkdir(exist_ok=True)
    (OUT / "quality-gate-flagged-residual.json").write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )

    print(f"Verified:  {len(results)}")
    print(f"Remaining: {len(remaining)}")
    print("Wrote: reports/quality-gate-flagged-residual.json")


if __name__ == "__main__":
    main()
