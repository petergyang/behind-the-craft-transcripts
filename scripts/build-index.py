#!/usr/bin/env python3
"""Build topic index from transcript frontmatter keywords.

Reads all transcript YAML frontmatter, collects keywords, and generates:
  - index/README.md — main entry point listing all topics with episode counts
  - index/{topic}.md — one file per keyword, listing relevant episodes
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS_DIR = REPO_ROOT / "transcripts"
INDEX_DIR = REPO_ROOT / "index"


def parse_frontmatter(filepath: Path) -> dict:
    """Parse YAML frontmatter from a transcript file."""
    content = filepath.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        return {}

    end = content.index("\n---\n", 4)
    fm_block = content[4:end]

    result = {}
    keywords = []
    in_keywords = False

    for line in fm_block.split("\n"):
        if line.startswith("- ") and in_keywords:
            keywords.append(line[2:].strip())
            continue
        in_keywords = False

        if line.startswith("keywords:"):
            in_keywords = True
            continue

        if ":" in line:
            key, val = line.split(":", 1)
            val = val.strip().strip('"')
            result[key.strip()] = val

    result["keywords"] = keywords
    return result


def get_episode_number(filename: str) -> str:
    """Extract episode number from filename like '001-title.md'."""
    match = re.match(r"(\d+)-", filename)
    return match.group(1) if match else ""


DISPLAY_OVERRIDES = {
    "ai": "AI",
    "ai-tools": "AI Tools",
    "big-tech": "Big Tech",
    "career-growth": "Career Growth",
    "product-management": "Product Management",
    "user-research": "User Research",
}


def topic_display_name(topic: str) -> str:
    """Human-readable display name for a topic."""
    return DISPLAY_OVERRIDES.get(topic, topic.replace("-", " ").title())


def build_topic_file(topic: str, episodes: list[dict]) -> str:
    """Generate markdown content for a single topic file."""
    lines = [
        f"# {topic_display_name(topic)}",
        "",
        f"{len(episodes)} episode{'s' if len(episodes) != 1 else ''}",
        "",
        "| # | Episode | Guest | Date |",
        "|---|---------|-------|------|",
    ]

    for ep in sorted(episodes, key=lambda e: e.get("publish_date", "")):
        num = ep["number"]
        title = ep.get("title", "")
        guest = ep.get("guest", "")
        date = ep.get("publish_date", "")
        rel_path = ep["rel_path"]
        lines.append(f"| {num} | [{title}](../{rel_path}) | {guest} | {date} |")

    lines.append("")
    return "\n".join(lines)


def build_readme(topic_counts: dict[str, int]) -> str:
    """Generate the index README.md."""
    lines = [
        "# Topic Index",
        "",
        "Browse Behind the Craft episodes by topic.",
        "",
        "| Topic | Episodes |",
        "|-------|----------|",
    ]

    for topic in sorted(topic_counts):
        count = topic_counts[topic]
        display = topic_display_name(topic)
        lines.append(f"| [{display}]({topic}.md) | {count} |")

    lines.append("")
    return "\n".join(lines)


def main():
    # Collect all episodes by keyword
    topic_episodes: dict[str, list[dict]] = defaultdict(list)

    for year_dir in sorted(TRANSCRIPTS_DIR.iterdir()):
        if not year_dir.is_dir():
            continue
        for md_file in sorted(year_dir.glob("*.md")):
            fm = parse_frontmatter(md_file)
            if not fm:
                print(f"  WARNING: No frontmatter in {md_file}")
                continue

            ep = {
                "number": get_episode_number(md_file.name),
                "title": fm.get("title", ""),
                "guest": fm.get("guest", ""),
                "publish_date": fm.get("publish_date", ""),
                "rel_path": f"transcripts/{year_dir.name}/{md_file.name}",
            }

            for kw in fm.get("keywords", []):
                topic_episodes[kw].append(ep)

    # Generate index files
    INDEX_DIR.mkdir(exist_ok=True)

    topic_counts = {}
    for topic, episodes in sorted(topic_episodes.items()):
        content = build_topic_file(topic, episodes)
        (INDEX_DIR / f"{topic}.md").write_text(content, encoding="utf-8")
        topic_counts[topic] = len(episodes)
        print(f"  ✓ {topic}.md ({len(episodes)} episodes)")

    # Generate README
    readme = build_readme(topic_counts)
    (INDEX_DIR / "README.md").write_text(readme, encoding="utf-8")
    print(f"\n  ✓ README.md ({len(topic_counts)} topics)")

    print(f"\nDone: {len(topic_counts)} topic files + README.md generated in index/")


if __name__ == "__main__":
    main()
