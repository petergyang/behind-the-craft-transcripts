#!/usr/bin/env python3
"""Fetch new Behind the Craft episodes from YouTube.

Checks the channel RSS feed for new videos, fetches their transcripts,
and creates properly formatted transcript files. Then runs add_frontmatter.py
and build-index.py to complete the pipeline.
"""

from __future__ import annotations

import re
import subprocess
import sys
import urllib.request
import ssl
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS_DIR = REPO_ROOT / "transcripts"
SCRIPTS_DIR = REPO_ROOT / "scripts"

CHANNEL_ID = "UCnpBg7yqNauHtlNSpOl5-cg"
FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

ATOM_NS = {"atom": "http://www.w3.org/2005/Atom",
           "yt": "http://www.youtube.com/xml/schemas/2015"}


def fetch_rss_feed() -> list[dict]:
    """Fetch and parse YouTube RSS feed. Returns list of video entries."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(FEED_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx) as resp:
        xml_data = resp.read()

    root = ET.fromstring(xml_data)

    entries = []
    for entry in root.findall("atom:entry", ATOM_NS):
        video_id_el = entry.find("yt:videoId", ATOM_NS)
        title_el = entry.find("atom:title", ATOM_NS)
        published_el = entry.find("atom:published", ATOM_NS)

        if video_id_el is None or title_el is None:
            continue

        pub_date = ""
        if published_el is not None and published_el.text:
            pub_date = published_el.text[:10]

        entries.append({
            "video_id": video_id_el.text,
            "title": title_el.text,
            "publish_date": pub_date,
            "youtube_url": f"https://youtube.com/watch?v={video_id_el.text}",
        })

    return entries


def get_existing_video_ids() -> set[str]:
    """Collect all YouTube video IDs already in the repo."""
    video_ids = set()
    for year_dir in TRANSCRIPTS_DIR.iterdir():
        if not year_dir.is_dir():
            continue
        for md_file in year_dir.glob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            match = re.search(r"youtube_url:.*watch\?v=([^\s]+)", content)
            if match:
                video_ids.add(match.group(1))
    return video_ids


def get_next_episode_number() -> int:
    """Find the next sequential episode number."""
    max_num = 0
    for year_dir in TRANSCRIPTS_DIR.iterdir():
        if not year_dir.is_dir():
            continue
        for md_file in year_dir.glob("*.md"):
            match = re.match(r"(\d+)-", md_file.name)
            if match:
                max_num = max(max_num, int(match.group(1)))
    return max_num + 1


def slugify(title: str) -> str:
    """Convert title to URL-friendly slug matching existing file naming."""
    slug = title.lower()
    slug = re.sub(r"[''']", "", slug)
    slug = re.sub(r"[^a-z0-9\s-]", " ", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    if len(slug) > 80:
        slug = slug[:80].rsplit("-", 1)[0]
    return slug


def fetch_transcript(video_id: str) -> str | None:
    """Fetch and format YouTube transcript for a video."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi

        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id, languages=["en"])
        return format_transcript(transcript.snippets)
    except Exception as e:
        print(f"        ⚠ Could not fetch transcript: {e}")
        return None


def format_transcript(snippets) -> str:
    """Format transcript snippets into readable paragraphs."""
    if not snippets:
        return ""

    paragraphs = []
    current_sentences = []
    sentence_count = 0

    for snippet in snippets:
        text = snippet.text.replace("\n", " ").strip()
        if not text:
            continue

        current_sentences.append(text)
        sentence_count += text.count(".") + text.count("!") + text.count("?")

        if sentence_count >= 6:
            paragraphs.append(" ".join(current_sentences))
            current_sentences = []
            sentence_count = 0

    if current_sentences:
        paragraphs.append(" ".join(current_sentences))

    return "\n\n".join(paragraphs)


def create_transcript_file(episode_num: int, video: dict, transcript_text: str) -> Path:
    """Create a transcript markdown file with header format for add_frontmatter.py."""
    title = video["title"]
    slug = slugify(title)
    filename = f"{episode_num:03d}-{slug}.md"

    year = video["publish_date"][:4] if video["publish_date"] else str(datetime.now().year)
    year_dir = TRANSCRIPTS_DIR / year
    year_dir.mkdir(parents=True, exist_ok=True)

    filepath = year_dir / filename

    # Write in the raw header format that add_frontmatter.py expects
    content = (
        f"# {title}\n\n"
        f"**Date:** {video['publish_date']}\n\n"
        f"**URL:** {video['youtube_url']}\n\n"
        f"---\n\n"
        f"{transcript_text}\n"
    )
    filepath.write_text(content, encoding="utf-8")
    return filepath


def main():
    print("=== Behind the Craft — Transcript Updater ===\n")

    # Fetch RSS feed
    print("Fetching RSS feed...")
    videos = fetch_rss_feed()
    print(f"  Found {len(videos)} videos in feed")

    # Filter out existing episodes
    existing_ids = get_existing_video_ids()
    new_videos = [v for v in videos if v["video_id"] not in existing_ids]
    print(f"  {len(new_videos)} new episode(s) to process")

    if not new_videos:
        print("\nAll caught up — no new episodes.")
        return

    # Sort oldest-first so numbering stays chronological
    new_videos.sort(key=lambda v: v["publish_date"])

    # Fetch transcripts and create files
    next_num = get_next_episode_number()
    created = []

    for i, video in enumerate(new_videos):
        num = next_num + i
        print(f"\n  [{num:03d}] {video['title']}")
        print(f"        {video['youtube_url']} ({video['publish_date']})")

        transcript = fetch_transcript(video["video_id"])
        if transcript is None:
            print("        Skipping (no transcript available)")
            # Adjust numbering so we don't leave gaps
            next_num -= 1
            continue

        filepath = create_transcript_file(num, video, transcript)
        created.append(filepath)
        print(f"        ✓ {filepath.relative_to(REPO_ROOT)}")

    if not created:
        print("\nNo transcripts could be fetched.")
        return

    # Run add_frontmatter.py
    print("\nAdding frontmatter...")
    subprocess.run([sys.executable, str(SCRIPTS_DIR / "add_frontmatter.py")],
                   cwd=REPO_ROOT, check=True)

    # Rebuild topic index
    print("\nRebuilding topic index...")
    subprocess.run([sys.executable, str(SCRIPTS_DIR / "build-index.py")],
                   cwd=REPO_ROOT, check=True)

    print(f"\n=== Done! {len(created)} new transcript(s) added. ===")


if __name__ == "__main__":
    main()
