#!/usr/bin/env python3
"""Discover candidate sources for Architectonic skills.

This script does not ingest third-party content. It creates a candidate report for later
human/agent review, license checks, risk review, and OKF normalization.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "discovery"

GITHUB_QUERIES = [
    "llm skill agent",
    "claude skills",
    "cursor rules agent",
    "codex agent instructions",
    "mcp server agent tools",
    "agent memory llm",
    "llm wiki knowledge agent",
    "ai agent workflow",
    "prompt engineering repository agents",
    "openai agents sdk examples",
]

HN_QUERIES = [
    "agent skills",
    "MCP server",
    "LLM agent workflow",
    "Claude skills",
    "Cursor rules",
    "LLM wiki",
]

WATCH_SURFACES = [
    "GitHub trending and recent repository search",
    "Hacker News search",
    "X/Twitter AI-builder roundup posts mentioning GitHub repos",
    "YouTube AI-tool roundup videos mentioning GitHub repos",
    "Reddit LocalLLaMA / OpenAI / MCP discussions",
    "Anthropic, OpenAI, Vercel, Cursor, Claude, and MCP example repositories",
]


def fetch_json(url: str) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": "architectonic-skills-discovery/0.1"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def github_search(query: str) -> list[dict[str, Any]]:
    since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=90)).strftime("%Y-%m-%d")
    full_query = f"{query} pushed:>{since}"
    params = urllib.parse.urlencode({"q": full_query, "sort": "updated", "order": "desc", "per_page": 10})
    url = f"https://api.github.com/search/repositories?{params}"
    try:
        payload = fetch_json(url)
    except Exception as exc:  # noqa: BLE001 - report discovery failures, do not crash whole run
        return [{"query": query, "error": f"{type(exc).__name__}: {exc}"}]
    out = []
    for item in payload.get("items", []):
        out.append(
            {
                "query": query,
                "name": item.get("full_name"),
                "url": item.get("html_url"),
                "description": item.get("description"),
                "stars": item.get("stargazers_count"),
                "forks": item.get("forks_count"),
                "language": item.get("language"),
                "license": (item.get("license") or {}).get("spdx_id"),
                "pushed_at": item.get("pushed_at"),
                "topics": item.get("topics", []),
                "source": "github_search",
            }
        )
    return out


def hn_search(query: str) -> list[dict[str, Any]]:
    params = urllib.parse.urlencode({"query": query, "tags": "story", "hitsPerPage": 10})
    url = f"https://hn.algolia.com/api/v1/search_by_date?{params}"
    try:
        payload = fetch_json(url)
    except Exception as exc:  # noqa: BLE001
        return [{"query": query, "error": f"{type(exc).__name__}: {exc}"}]
    out = []
    for item in payload.get("hits", []):
        out.append(
            {
                "query": query,
                "title": item.get("title"),
                "url": item.get("url") or f"https://news.ycombinator.com/item?id={item.get('objectID')}",
                "points": item.get("points"),
                "created_at": item.get("created_at"),
                "source": "hacker_news_algolia",
            }
        )
    return out


def write_report(payload: dict[str, Any]) -> None:
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / f"{today}.json"
    md_path = OUT / f"{today}.md"
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "---",
        "type: Discovery Report",
        f"title: Skill Source Discovery {today}",
        "description: Candidate external sources for Architectonic skill review.",
        "tags: [skills, discovery, candidates, github, hacker-news]",
        "okf_version: \"0.2\"",
        "status: candidate",
        "---",
        "",
        f"# Skill Source Discovery {today}",
        "",
        "## Boundaries",
        "",
        "This report is candidate discovery only. Do not copy third-party content from it. Every candidate still needs license review, risk review, usefulness review, deduplication, and OKF normalization before it becomes a skill.",
        "",
        "## Watch surfaces",
        "",
    ]
    lines += [f"- {surface}" for surface in WATCH_SURFACES]
    lines += ["", "## GitHub candidates", ""]
    for item in payload["github"][:80]:
        if item.get("error"):
            lines.append(f"- ERROR `{item['query']}`: {item['error']}")
            continue
        lines.append(f"- [{item.get('name')}]({item.get('url')}) — {item.get('description') or 'No description'}; stars={item.get('stars')}; license={item.get('license')}; pushed={item.get('pushed_at')}; query=`{item.get('query')}`")
    lines += ["", "## Hacker News candidates", ""]
    for item in payload["hacker_news"][:80]:
        if item.get("error"):
            lines.append(f"- ERROR `{item['query']}`: {item['error']}")
            continue
        lines.append(f"- [{item.get('title')}]({item.get('url')}) — points={item.get('points')}; created={item.get('created_at')}; query=`{item.get('query')}`")
    lines += ["", "## Next review action", "", "Source Reviewer should select only high-signal candidates, verify license and runtime/account/security surfaces, then create source profiles or skip notes. Publishing remains blocked unless catalog surfaces agree.", ""]
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    payload = {
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "watch_surfaces": WATCH_SURFACES,
        "github": [],
        "hacker_news": [],
    }
    for query in GITHUB_QUERIES:
        payload["github"].extend(github_search(query))
    for query in HN_QUERIES:
        payload["hacker_news"].extend(hn_search(query))
    write_report(payload)
    print(json.dumps({"github_candidates": len(payload["github"]), "hacker_news_candidates": len(payload["hacker_news"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
