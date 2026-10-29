#!/usr/bin/env python3
"""
Daily AI News generator — free forever.

Runs inside GitHub Actions at 6 AM ChST.
Uses only free public sources (no paid APIs).
Creates a new markdown issue in /issues/.
The workflow then also posts it as a GitHub Issue so watchers get email.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

ROOT = Path(__file__).resolve().parent.parent
ISSUES_DIR = ROOT / "issues"
DATA_DIR = ROOT / "data"
LAST_RUN_FILE = DATA_DIR / "last_run.json"

SOURCES = [
    {
        "name": "Hacker News (AI)",
        "url": "https://hn.algolia.com/api/v1/search_by_date?query=AI%20OR%20LLM%20OR%20GPT%20OR%20Claude%20OR%20Grok&tags=story&hitsPerPage=10",
        "type": "hn",
    },
]


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def chst_now() -> datetime:
    return utc_now() + timedelta(hours=10)


def next_issue_number() -> int:
    ISSUES_DIR.mkdir(exist_ok=True)
    numbers = []
    for f in ISSUES_DIR.glob("*.md"):
        m = re.match(r"(\d+)", f.stem)
        if m:
            numbers.append(int(m.group(1)))
    return max(numbers, default=0) + 1


def fetch_json(url: str):
    try:
        req = Request(url, headers={"User-Agent": "NEWS-Bot/1.0 (GitHub Actions)"})
        with urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (URLError, HTTPError, TimeoutError, json.JSONDecodeError) as e:
        print(f"Fetch failed: {e}")
        return None


def collect_stories() -> list[dict]:
    stories = []
    for src in SOURCES:
        data = fetch_json(src["url"])
        if not data:
            continue
        if src["type"] == "hn":
            for hit in data.get("hits", []):
                title = (hit.get("title") or "").strip()
                url = hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
                points = hit.get("points") or 0
                if title and points >= 8:
                    stories.append({
                        "title": title,
                        "url": url,
                        "points": points,
                        "source": src["name"],
                    })
    seen = set()
    unique = []
    for s in stories:
        key = s["title"].lower()[:55]
        if key not in seen:
            seen.add(key)
            unique.append(s)
    unique.sort(key=lambda x: x["points"], reverse=True)
    return unique[:6]


def render_issue(number: int, stories: list[dict], date_str: str) -> str:
    lines = [
        f"# NEWS — Issue #{number:03d}",
        "",
        f"**Date:** {date_str}  ",
        "**Status:** Published (auto)",
        "",
        "---",
        "",
        "## Top Stories",
        "",
    ]

    if not stories:
        lines += [
            "_No high-signal public stories matched the filter today._",
            "",
            "This issue was generated automatically.",
            "",
        ]
    else:
        for i, s in enumerate(stories, 1):
            lines += [
                f"### {i}. {s['title']}",
                f"**{s['points']} points** · {s['source']}  ",
                f"{s['url']}",
                "",
                "---",
                "",
            ]

    lines += [
        "## Closing",
        "",
        "This issue was generated automatically at 6 AM ChST.",
        "Watch the repository to receive email notifications for every new issue.",
        "",
        "— NEWS Bot",
        "",
        "https://github.com/ram133/NEWS",
        "",
    ]
    return "\n".join(lines)


def already_ran_today(today: str) -> bool:
    if not LAST_RUN_FILE.exists():
        return False
    try:
        data = json.loads(LAST_RUN_FILE.read_text())
        return data.get("date") == today
    except Exception:
        return False


def main() -> None:
    now = chst_now()
    today = now.strftime("%Y-%m-%d")
    date_str = now.strftime("%B %d, %Y")

    print(f"Running daily publisher for {date_str} (ChST)")

    if already_ran_today(today):
        print("Already published today — skipping.")
        return

    stories = collect_stories()
    print(f"Collected {len(stories)} stories")

    number = next_issue_number()
    content = render_issue(number, stories, date_str)

    ISSUES_DIR.mkdir(exist_ok=True)
    out_path = ISSUES_DIR / f"{number:03d}.md"
    out_path.write_text(content, encoding="utf-8")
    print(f"Wrote {out_path}")

    DATA_DIR.mkdir(exist_ok=True)
    LAST_RUN_FILE.write_text(json.dumps({
        "date": today,
        "issue": number,
        "stories": len(stories),
        "generated_at_utc": utc_now().isoformat(),
    }, indent=2) + "\n", encoding="utf-8")

    print("Done.")


if __name__ == "__main__":
    main()
