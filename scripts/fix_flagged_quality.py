#!/usr/bin/env python3
"""
Apply targeted fixes for the remaining quality-gate flagged dist/skills entries.

This script handles three buckets:
- weak or placeholder descriptions
- high-risk offensive skills missing explicit authorized-use framing
- ultra-thin grill-* bodies that need minimal OKF structure
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

AUTHORIZED_USE_NOTICE = (
    "**Authorized-use only:** Use this skill only for owned systems, sanctioned lab environments, "
    "or engagements with explicit written permission. Document scope, preserve evidence, and follow "
    "applicable law, policy, and incident-response procedures."
)

GRILL_BODY_BY_NAME = {
    "grill-me": """# grill-me

Run a `/grilling` session to pressure-test a plan, design, or decision before work begins.

## When to Use

- When a plan sounds plausible but still has hidden assumptions or weak spots
- When you need a sharper problem statement, tradeoff analysis, or go/no-go call
- When a stakeholder wants a direct, adversarial review instead of polite brainstorming

## Workflow

1. Start a `/grilling` session with the current plan, draft, or decision in view.
2. Ask pointed questions that expose unclear goals, missing constraints, and fragile assumptions.
3. Push until the owner can defend the approach or agrees to revise it.
4. End with a concise summary of risks, unresolved questions, and the recommended next move.
""",
    "grill-with-docs": """# grill-with-docs

Run a `/grilling` session to pressure-test a plan or design while producing durable artifacts such as ADRs and a glossary.

Use the `/domain-modeling` skill alongside the grilling flow when the conversation exposes unclear concepts, boundaries, or vocabulary.

## When to Use

- When a design review should also produce reusable documentation
- When the team needs ADRs, terminology cleanup, or a clearer domain model as part of the critique
- When a plan is still evolving and decisions need to be captured as they harden

## Workflow

1. Start a `/grilling` session with the current proposal, design, or operating plan.
2. Record decisions, rejected alternatives, and key terms as they emerge.
3. Invoke `/domain-modeling` when entities, relationships, or boundaries need to be clarified.
4. Finish with updated ADRs, glossary entries, and a short list of follow-up actions.
""",
}


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


def render_frontmatter(fm: dict) -> str:
    cleaned = {}
    for key, value in fm.items():
        if value in ("", None, [], {}):
            continue
        cleaned[key] = value
    return "---\n" + yaml.safe_dump(cleaned, sort_keys=False, allow_unicode=True).strip() + "\n---\n\n"


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip())


def is_placeholder_description(value: str) -> bool:
    text = normalize_text(value)
    if not text:
        return True
    return text in {">", "|", ">-", "|-"} or text.startswith("<!--") or "AUTO-GENERATED" in text


def first_heading(body: str) -> str:
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("# "):
            return re.sub(r"\s+\([^)]*\)$", "", line[2:].strip()).strip()
    return ""


def first_meaningful_paragraph(body: str) -> str:
    lines = []
    seen_heading = False
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            if lines:
                break
            continue
        if line.startswith("#"):
            seen_heading = True
            continue
        if line.startswith(">") or line.startswith("```") or line.startswith("<!--"):
            continue
        if line.startswith("|") or re.match(r"^[-*]\s", line):
            continue
        if seen_heading and re.fullmatch(r"[A-Za-z0-9 /:_()'.,-]+", line) and len(line) < 80:
            heading = first_heading(body)
            if heading and line.lower() == heading.lower():
                continue
        lines.append(line)
        if len(" ".join(lines)) >= 220:
            break
    return normalize_text(" ".join(lines))


def has_authorized_use_notice(body: str) -> bool:
    lowered = body.lower()
    return "authorized-use only" in lowered or ("authorized" in lowered and "written permission" in lowered)


def inject_authorized_use_notice(body: str) -> str:
    if has_authorized_use_notice(body):
        return body
    lines = body.splitlines()
    insert_at = 0
    for idx, raw in enumerate(lines):
        if raw.startswith("# "):
            insert_at = idx + 1
            while insert_at < len(lines) and lines[insert_at].strip() == "":
                insert_at += 1
            break
    snippet = ["", AUTHORIZED_USE_NOTICE, ""]
    updated = lines[:insert_at] + snippet + lines[insert_at:]
    return "\n".join(updated).rstrip() + "\n"


def apply_fix(rel_path: str, issues: list[str]) -> dict:
    target = ROOT / rel_path
    original = target.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(original)
    changed = False

    desc = fm.get("description", "")
    if "description too short" in issues and (is_placeholder_description(desc) or len(normalize_text(str(desc))) < 20):
        candidate = first_meaningful_paragraph(body)
        if candidate:
            fm["description"] = candidate
            changed = True

    if "high-risk offensive without safety/legal framing" in issues and not has_authorized_use_notice(body):
        body = inject_authorized_use_notice(body)
        changed = True

    skill_name = Path(rel_path).parts[0]
    if "body too short (<100 chars)" in issues and skill_name in GRILL_BODY_BY_NAME:
        body = GRILL_BODY_BY_NAME[skill_name].rstrip() + "\n"
        changed = True
        if is_placeholder_description(desc) or len(normalize_text(str(desc))) < 20:
            fm["description"] = first_meaningful_paragraph(body)

    if not changed:
        return {"path": rel_path.as_posix(), "changed": False}

    new_text = render_frontmatter(fm) + body.lstrip("\r\n")
    target.write_text(new_text, encoding="utf-8")
    return {"path": rel_path.as_posix(), "changed": new_text != original}


def main():
    flagged = json.loads(FLAGGED.read_text(encoding="utf-8"))
    results = []
    for entry in flagged:
        rel_path = Path(entry["path"])
        results.append(apply_fix(rel_path, entry["issues"]))

    changed = [item for item in results if item["changed"]]
    report = {
        "selected_count": len(results),
        "changed_count": len(changed),
        "results": results,
    }
    OUT.mkdir(exist_ok=True)
    (OUT / "flagged-quality-fix-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Selected: {len(results)}")
    print(f"Changed:  {len(changed)}")
    print("Wrote: reports/flagged-quality-fix-report.json")


if __name__ == "__main__":
    main()
