from pathlib import Path
from collections import Counter, defaultdict
import re
import json

ROOT = Path("dist/skills")
OUT = Path("reports")
OUT.mkdir(exist_ok=True)

frontmatter_re = re.compile(r"^---\n(.*?)\n---\n", re.S)

def parse_frontmatter(text: str) -> dict:
    match = frontmatter_re.match(text)
    if not match:
        return {}

    data = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value.startswith("[") and value.endswith("]"):
            value = [
                item.strip().strip('"').strip("'")
                for item in value[1:-1].split(",")
                if item.strip()
            ]
        else:
            value = value.strip('"').strip("'")

        data[key] = value

    return data

def first_heading(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None

files = sorted(ROOT.rglob("*.md"))

rows = []
by_category = Counter()
by_type = Counter()
by_source_status = Counter()
by_source_name = Counter()
by_risk = Counter()
by_requires_review = Counter()
missing_frontmatter = []
missing_type = []
missing_title = []
missing_description = []

for path in files:
    rel = path.relative_to(ROOT)
    category = rel.parts[0] if len(rel.parts) > 1 else "_root"

    text = path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)

    title = fm.get("title") or first_heading(text) or path.stem
    typ = fm.get("type", "")
    source_status = fm.get("source_status", "")
    source_name = fm.get("source_name", "")
    risk_level = fm.get("risk_level", "")
    requires_review = str(fm.get("requires_review", "")).lower()

    by_category[category] += 1
    by_type[typ or "_missing"] += 1
    by_source_status[source_status or "_missing"] += 1
    by_source_name[source_name or "_missing"] += 1
    by_risk[risk_level or "_missing"] += 1
    by_requires_review[requires_review or "_missing"] += 1

    if not fm:
        missing_frontmatter.append(str(rel))
    if not typ:
        missing_type.append(str(rel))
    if not fm.get("title"):
        missing_title.append(str(rel))
    if not fm.get("description"):
        missing_description.append(str(rel))

    rows.append({
        "path": str(rel),
        "category": category,
        "type": typ,
        "title": title,
        "description": fm.get("description", ""),
        "source_status": source_status,
        "source_name": source_name,
        "source_url": fm.get("source_url", ""),
        "source_license": fm.get("source_license", ""),
        "risk_level": risk_level,
        "requires_review": requires_review,
        "tags": fm.get("tags", []),
    })

summary = {
    "total_markdown_files": len(files),
    "by_category": by_category.most_common(),
    "by_type": by_type.most_common(),
    "by_source_status": by_source_status.most_common(),
    "by_source_name_top_50": by_source_name.most_common(50),
    "by_risk_level": by_risk.most_common(),
    "by_requires_review": by_requires_review.most_common(),
    "missing_frontmatter_count": len(missing_frontmatter),
    "missing_type_count": len(missing_type),
    "missing_title_count": len(missing_title),
    "missing_description_count": len(missing_description),
}

(OUT / "dist-skills-summary.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False),
    encoding="utf-8",
)

(OUT / "dist-skills-inventory.json").write_text(
    json.dumps(rows, indent=2, ensure_ascii=False),
    encoding="utf-8",
)

def md_counter(title: str, counter: Counter, limit: int | None = None) -> str:
    items = counter.most_common(limit)
    lines = [f"## {title}", "", "| Value | Count |", "|---|---:|"]
    for key, count in items:
        lines.append(f"| `{key}` | {count} |")
    return "\n".join(lines)

report = [
    "# dist/skills Classification Report",
    "",
    f"Total Markdown files: **{len(files)}**",
    "",
    md_counter("By category", by_category),
    "",
    md_counter("By type", by_type),
    "",
    md_counter("By source status", by_source_status),
    "",
    md_counter("By risk level", by_risk),
    "",
    md_counter("By requires_review", by_requires_review),
    "",
    md_counter("Top source names", by_source_name, limit=50),
    "",
    "## Metadata gaps",
    "",
    f"- Missing frontmatter: {len(missing_frontmatter)}",
    f"- Missing `type`: {len(missing_type)}",
    f"- Missing `title`: {len(missing_title)}",
    f"- Missing `description`: {len(missing_description)}",
]

(OUT / "dist-skills-report.md").write_text("\n".join(report), encoding="utf-8")

print("\n".join(report[:80]))
print()
print("Wrote:")
print("- reports/dist-skills-summary.json")
print("- reports/dist-skills-inventory.json")
print("- reports/dist-skills-report.md")