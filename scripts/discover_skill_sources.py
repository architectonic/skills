#!/usr/bin/env python3
"""Discover candidate sources for Architectonic skills.

This script does not ingest third-party content. It creates candidate reports for
later human/agent review, license checks, risk review, and OKF normalization.

The broad search surfaces find new sources. The source watchlist checks known
high-signal upstream repositories and registries for additions or material
changes so already-distilled sources do not silently drift.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "discovery"
WATCHLIST_PATH = ROOT / "operations" / "source-watchlist.json"

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
    "Repo-controlled source watchlist in operations/source-watchlist.json",
]


def fetch_json(url: str) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": "architectonic-skills-discovery/0.2"})
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


def load_watchlist() -> dict[str, Any]:
    if not WATCHLIST_PATH.exists():
        return {"repositories": [], "registries": []}
    return json.loads(WATCHLIST_PATH.read_text(encoding="utf-8"))


def github_contents_url(repo: str, path: str) -> str:
    encoded_path = "/".join(urllib.parse.quote(part) for part in path.strip("/").split("/") if part)
    return f"https://api.github.com/repos/{repo}/contents/{encoded_path}"


def github_repo_url(repo: str) -> str:
    return f"https://api.github.com/repos/{repo}"


def get_repo_metadata(repo: str) -> dict[str, Any]:
    try:
        payload = fetch_json(github_repo_url(repo))
    except Exception as exc:  # noqa: BLE001
        return {"error": f"{type(exc).__name__}: {exc}"}
    return {
        "stars": payload.get("stargazers_count"),
        "forks": payload.get("forks_count"),
        "license": (payload.get("license") or {}).get("spdx_id"),
        "pushed_at": payload.get("pushed_at"),
        "default_branch": payload.get("default_branch"),
        "topics": payload.get("topics", []),
        "description": payload.get("description"),
    }


def include_path(path: str, rule: dict[str, Any]) -> bool:
    extensions = rule.get("include_extensions") or []
    if extensions and not any(path.endswith(ext) for ext in extensions):
        return False
    pattern = rule.get("include_path_regex")
    if pattern and not re.search(str(pattern), path):
        return False
    return True


def skill_slug_from_path(path: str) -> str | None:
    parts = path.split("/")
    if len(parts) >= 3 and parts[-1] == "SKILL.md":
        return parts[-2]
    return None


def list_watch_path(repo: str, rule: dict[str, Any], repo_meta: dict[str, Any]) -> list[dict[str, Any]]:
    start_path = str(rule.get("path") or "").strip("/")
    max_depth = int(rule.get("max_depth", 0))
    queue: list[tuple[str, int]] = [(start_path, 0)]
    out: list[dict[str, Any]] = []
    seen: set[str] = set()

    while queue:
        path, depth = queue.pop(0)
        if path in seen:
            continue
        seen.add(path)
        try:
            payload = fetch_json(github_contents_url(repo, path))
        except Exception as exc:  # noqa: BLE001
            out.append(
                {
                    "source": "github_watchlist",
                    "source_family": "repository_watch_error",
                    "name": f"{repo}:{path}",
                    "url": f"https://github.com/{repo}/tree/main/{path}",
                    "description": f"Watch path could not be inspected: {type(exc).__name__}: {exc}",
                    "query": "source_watchlist",
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )
            continue

        entries = payload if isinstance(payload, list) else [payload]
        for entry in entries:
            entry_type = entry.get("type")
            entry_path = entry.get("path") or path
            if entry_type == "dir" and depth < max_depth:
                queue.append((entry_path, depth + 1))
                continue
            if entry_type != "file" or not include_path(entry_path, rule):
                continue
            slug = skill_slug_from_path(entry_path)
            html_url = entry.get("html_url") or f"https://github.com/{repo}/blob/main/{entry_path}"
            out.append(
                {
                    "source": "github_watchlist",
                    "source_family": "watched_repository_file",
                    "name": f"{repo}:{entry_path}",
                    "url": html_url,
                    "description": "Watched upstream skill-source path; metadata-only candidate for source review if new or materially changed.",
                    "query": "source_watchlist",
                    "repo": repo,
                    "path": entry_path,
                    "skill_slug": slug,
                    "stars": repo_meta.get("stars"),
                    "forks": repo_meta.get("forks"),
                    "license": repo_meta.get("license"),
                    "pushed_at": repo_meta.get("pushed_at"),
                    "topics": repo_meta.get("topics", []),
                    "review_boundary": "metadata_only_no_content_copy_no_code_execution",
                }
            )
    return out


def watchlist_repository_scan(watchlist: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for repo_cfg in watchlist.get("repositories", []):
        repo = repo_cfg.get("full_name")
        if not repo:
            continue
        repo_meta = get_repo_metadata(repo)
        if repo_meta.get("error"):
            out.append(
                {
                    "source": "github_watchlist",
                    "source_family": "repository_watch_error",
                    "name": repo,
                    "url": repo_cfg.get("url") or f"https://github.com/{repo}",
                    "description": repo_meta["error"],
                    "query": "source_watchlist",
                    "error": repo_meta["error"],
                }
            )
            continue
        known = set(repo_cfg.get("known_reviewed_or_distilled_slugs") or [])
        for rule in repo_cfg.get("watch_paths", []):
            for item in list_watch_path(repo, rule, repo_meta):
                slug = item.get("skill_slug")
                item["watch_priority"] = repo_cfg.get("priority")
                item["watch_reason"] = repo_cfg.get("reason")
                item["watch_status"] = "known_reviewed_or_distilled" if slug in known else "needs_delta_review"
                if slug in known:
                    item["description"] = "Known reviewed/distilled upstream skill path; watch for material changes rather than immediate normalization."
                out.append(item)
    return out


def registry_watch_candidates(watchlist: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for registry in watchlist.get("registries", []):
        out.append(
            {
                "source": "registry_watchlist",
                "source_family": registry.get("source_family") or "registry_watch",
                "name": registry.get("name"),
                "url": registry.get("url"),
                "description": registry.get("reason"),
                "query": "source_watchlist_registry",
                "watch_priority": registry.get("priority"),
                "review_boundary": registry.get("review_boundary") or "metadata_only_no_content_copy_no_bulk_registry_scrape",
                "decision_hint": "watch",
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
        "tags: [skills, discovery, candidates, github, hacker-news, watchlist]",
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
    lines += ["", "## Watched repository candidates", ""]
    for item in payload.get("watched_repositories", [])[:80]:
        if item.get("error"):
            lines.append(f"- ERROR `{item.get('name')}`: {item['error']}")
            continue
        lines.append(
            f"- [{item.get('name')}]({item.get('url')}) — status={item.get('watch_status') or 'candidate'}; "
            f"license={item.get('license')}; pushed={item.get('pushed_at')}; boundary={item.get('review_boundary')}"
        )
    lines += ["", "## Registry watch candidates", ""]
    for item in payload.get("registries", [])[:40]:
        lines.append(f"- [{item.get('name')}]({item.get('url')}) — {item.get('description')}; boundary={item.get('review_boundary')}")
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
    watchlist = load_watchlist()
    payload = {
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "watch_surfaces": WATCH_SURFACES,
        "watchlist_path": str(WATCHLIST_PATH.relative_to(ROOT)) if WATCHLIST_PATH.exists() else None,
        "github": [],
        "hacker_news": [],
        "watched_repositories": [],
        "registries": [],
    }
    payload["watched_repositories"].extend(watchlist_repository_scan(watchlist))
    payload["registries"].extend(registry_watch_candidates(watchlist))
    for query in GITHUB_QUERIES:
        payload["github"].extend(github_search(query))
    for query in HN_QUERIES:
        payload["hacker_news"].extend(hn_search(query))
    write_report(payload)
    print(
        json.dumps(
            {
                "github_candidates": len(payload["github"]),
                "hacker_news_candidates": len(payload["hacker_news"]),
                "watched_repository_candidates": len(payload["watched_repositories"]),
                "registry_watch_candidates": len(payload["registries"]),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
