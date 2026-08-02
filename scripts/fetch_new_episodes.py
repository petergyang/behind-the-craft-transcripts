#!/usr/bin/env python3
"""Sync published Behind the Craft videos and their YouTube transcripts.

The updater uses yt-dlp instead of youtube-transcript-api because YouTube blocks
transcript requests from GitHub-hosted runners. Run it on Peter's Mac with
``--cookies-from-browser chrome``. GitHub Actions uses ``--check-only`` so a
stale archive fails visibly instead of reporting a false success.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from add_frontmatter import build_frontmatter, extract_guest, extract_keywords


REPO_ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS_DIR = REPO_ROOT / "transcripts"
SCRIPTS_DIR = REPO_ROOT / "scripts"
README_PATH = REPO_ROOT / "README.md"
CHANNEL_URL = "https://www.youtube.com/@peteryangYT/videos"


class SyncError(RuntimeError):
    """Raised when discovery or transcript retrieval fails."""


def run_ytdlp(arguments: list[str]) -> subprocess.CompletedProcess[str]:
    command = ["yt-dlp", *arguments]
    try:
        return subprocess.run(
            command,
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError as exc:
        raise SyncError("yt-dlp is required but was not found on PATH") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or str(exc)).strip()
        raise SyncError(detail) from exc


def discover_channel_videos() -> list[dict[str, object]]:
    """Return long-form videos from the channel's Videos tab, newest first."""
    result = run_ytdlp(["--flat-playlist", "--dump-single-json", CHANNEL_URL])
    payload = json.loads(result.stdout)
    entries = []
    for entry in payload.get("entries") or []:
        if not isinstance(entry, dict) or not entry.get("id"):
            continue
        entries.append(
            {
                "video_id": str(entry["id"]),
                "title": str(entry.get("title") or "Untitled"),
                "duration": entry.get("duration"),
                "youtube_url": f"https://youtube.com/watch?v={entry['id']}",
            }
        )
    if not entries:
        raise SyncError("YouTube returned no videos for the channel")
    return entries


def get_existing_video_ids() -> set[str]:
    video_ids: set[str] = set()
    for markdown_file in TRANSCRIPTS_DIR.glob("*/*.md"):
        content = markdown_file.read_text(encoding="utf-8", errors="replace")
        match = re.search(
            r"(?:watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})",
            content,
        )
        if match:
            video_ids.add(match.group(1))
    return video_ids


def get_next_episode_number() -> int:
    numbers = []
    for markdown_file in TRANSCRIPTS_DIR.glob("*/*.md"):
        match = re.match(r"(\d+)-", markdown_file.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def slugify(title: str) -> str:
    slug = title.lower().replace("’", "").replace("'", "")
    slug = re.sub(r"[^a-z0-9\s-]", " ", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug).strip("-")
    if len(slug) > 80:
        slug = slug[:80].rsplit("-", 1)[0]
    return slug or "untitled"


def parse_metadata(stdout: str) -> dict[str, object]:
    for line in reversed(stdout.splitlines()):
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict) and payload.get("id"):
            return payload
    raise SyncError("yt-dlp did not return video metadata")


def transcript_from_json3(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    snippets: list[str] = []
    for event in payload.get("events") or []:
        text = "".join(
            str(segment.get("utf8") or "")
            for segment in event.get("segs") or []
            if isinstance(segment, dict)
        )
        text = html.unescape(text).replace("\u200b", " ")
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            snippets.append(text)

    if not snippets:
        raise SyncError(f"Downloaded caption file was empty: {path.name}")

    paragraphs: list[str] = []
    current: list[str] = []
    current_length = 0
    sentence_count = 0
    for snippet in snippets:
        current.append(snippet)
        current_length += len(snippet) + 1
        sentence_count += len(re.findall(r"[.!?](?:[\"']|$)", snippet))
        if current_length >= 900 or (current_length >= 450 and sentence_count >= 4):
            paragraph = re.sub(r"\s+([,.;!?])", r"\1", " ".join(current))
            paragraphs.append(paragraph)
            current = []
            current_length = 0
            sentence_count = 0
    if current:
        paragraphs.append(re.sub(r"\s+([,.;!?])", r"\1", " ".join(current)))
    return "\n\n".join(paragraphs)


def fetch_video(
    video: dict[str, object],
    cookies_from_browser: str,
) -> tuple[dict[str, object], str]:
    with tempfile.TemporaryDirectory(prefix="btc-transcript-") as temporary_directory:
        output_template = str(Path(temporary_directory) / "%(id)s")
        arguments = []
        if cookies_from_browser:
            arguments.extend(["--cookies-from-browser", cookies_from_browser])
        arguments.extend(
            [
                "--skip-download",
                "--write-subs",
                "--write-auto-subs",
                "--sub-langs",
                "en",
                "--sub-format",
                "json3",
                "--output",
                output_template,
                "--print-json",
                str(video["youtube_url"]),
            ]
        )
        result = run_ytdlp(arguments)
        metadata = parse_metadata(result.stdout)
        caption_files = sorted(Path(temporary_directory).glob(f"{video['video_id']}.*.json3"))
        if not caption_files:
            raise SyncError("No English manual or automatic captions were downloaded")
        return metadata, transcript_from_json3(caption_files[0])


def publish_date_from_metadata(metadata: dict[str, object]) -> str:
    raw_date = str(metadata.get("upload_date") or metadata.get("release_date") or "")
    if not re.fullmatch(r"\d{8}", raw_date):
        raise SyncError("Video metadata did not include an upload date")
    return f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"


def create_transcript_file(
    episode_number: int,
    video: dict[str, object],
    metadata: dict[str, object],
    transcript: str,
) -> Path:
    title = str(metadata.get("title") or video["title"])
    publish_date = publish_date_from_metadata(metadata)
    youtube_url = str(video["youtube_url"])
    guest = extract_guest(title)
    keywords = extract_keywords(title, transcript)
    frontmatter = build_frontmatter(title, guest, publish_date, youtube_url, keywords)

    year_directory = TRANSCRIPTS_DIR / publish_date[:4]
    year_directory.mkdir(parents=True, exist_ok=True)
    path = year_directory / f"{episode_number:03d}-{slugify(title)}.md"
    path.write_text(f"{frontmatter}\n\n{transcript}\n", encoding="utf-8")
    return path


def update_readme_count() -> None:
    if not README_PATH.exists():
        return
    episode_count = len(list(TRANSCRIPTS_DIR.glob("*/*.md")))
    content = README_PATH.read_text(encoding="utf-8")
    content = re.sub(r"\d+ episodes and counting", f"{episode_count} episodes and counting", content)
    content = re.sub(r"Q&A \d+\+ episodes", f"Q&A {episode_count}+ episodes", content)
    README_PATH.write_text(content, encoding="utf-8")


def rebuild_index() -> None:
    subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "build-index.py")],
        cwd=REPO_ROOT,
        check=True,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cookies-from-browser",
        default="",
        help="Browser profile yt-dlp should use for YouTube access, such as chrome.",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Exit nonzero when published videos are missing; do not download transcripts.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("=== Behind the Craft transcript sync ===")
    try:
        videos = discover_channel_videos()
    except (SyncError, json.JSONDecodeError) as exc:
        print(f"sync failed during discovery: {exc}", file=sys.stderr)
        return 1

    existing_ids = get_existing_video_ids()
    missing = [video for video in videos if video["video_id"] not in existing_ids]
    print(f"published={len(videos)} archived={len(existing_ids)} missing={len(missing)}")

    if not missing:
        print("Archive is current.")
        return 0
    if args.check_only:
        for video in reversed(missing):
            print(f"missing {video['video_id']} | {video['title']}")
        return 1

    next_episode_number = get_next_episode_number()
    created: list[Path] = []
    failures: list[tuple[dict[str, object], str]] = []
    for video in reversed(missing):
        print(f"\n[{next_episode_number:03d}] {video['title']}")
        try:
            metadata, transcript = fetch_video(video, args.cookies_from_browser)
            path = create_transcript_file(
                next_episode_number,
                video,
                metadata,
                transcript,
            )
        except (SyncError, json.JSONDecodeError) as exc:
            failures.append((video, str(exc)))
            print(f"  FAILED: {exc}", file=sys.stderr)
            continue
        created.append(path)
        next_episode_number += 1
        print(f"  added {path.relative_to(REPO_ROOT)}")

    if created:
        update_readme_count()
        rebuild_index()

    print(f"\ncreated={len(created)} failed={len(failures)}")
    for video, error in failures:
        print(f"failed {video['video_id']} | {video['title']} | {error}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
