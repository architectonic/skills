#!/usr/bin/env python3
"""
Select a bounded batch of dist/skills paths for frontmatter normalization.

Uses the enriched inventory and quality-gate report to avoid high-risk or noisy entries
 unless explicitly requested.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import json

REPORTS = Path("reports")
INVENTORY = REPORTS / "dist-skills-enriched-inventory.json"
QUALITY = REPORTS / "quality-gate-flagged.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--risk", choices=["low", "medium", "high", "any"], default="medium")
    parser.add_argument("--allow-flagged", action="store_true")
    parser.add_argument("--allow-unknown-source", action="store_true")
    parser.add_argument("--min-source-confidence", type=float, default=0.2)
    parser.add_argument("--min-domain-confidence", type=float, default=0.0)
    parser.add_argument("--domain")
    parser.add_argument("--missing-frontmatter-only", action="store_true")
    parser.add_argument("--missing-source-status-only", action="store_true")
    parser.add_argument("--out", default="reports/selected-frontmatter-batch.json")
    args = parser.parse_args()

    rows = load_json(INVENTORY)
    flagged = {entry["path"] for entry in load_json(QUALITY)}

    selected = []
    for row in rows:
        if args.risk != "any" and row.get("risk_level") != args.risk:
            continue
        if not args.allow_flagged and row.get("path") in flagged:
            continue
        if args.domain and row.get("domain") != args.domain:
            continue
        if row.get("source_confidence", 0.0) < args.min_source_confidence:
            continue
        if row.get("domain_confidence", 0.0) < args.min_domain_confidence:
            continue
        if not args.allow_unknown_source and row.get("source_family") == "unknown":
            continue
        if args.missing_frontmatter_only and row.get("type"):
            continue
        if args.missing_source_status_only and row.get("source_status"):
            continue
        selected.append(row)
        if len(selected) >= args.limit:
            break

    out_path = Path(args.out)
    out_path.write_text(json.dumps(selected, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Selected: {len(selected)}")
    print(f"Wrote: {out_path}")
    for row in selected[:10]:
        print(f"- {row['path']} | risk={row['risk_level']} | source={row['source_family']} | domain={row['domain']}")


if __name__ == "__main__":
    main()
