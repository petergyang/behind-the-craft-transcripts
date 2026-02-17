#!/usr/bin/env python3
"""Add YAML frontmatter to Behind the Craft transcripts.

Parses the existing markdown header (title, date, URL) and rewrites each
transcript file with proper YAML frontmatter including extracted guest name
and auto-generated keywords.
"""

from __future__ import annotations

import os
import re
import math
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS_DIR = REPO_ROOT / "transcripts"

# Common English stop words + filler words common in transcripts
STOP_WORDS = set("""
a about above after again against all am an and any are aren't as at be because
been before being below between both but by can't cannot could couldn't did
didn't do does doesn't doing don't down during each few for from further get got
had hadn't has hasn't have haven't having he he'd he'll he's her here here's
hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't
it it's its itself let's me more most mustn't my myself no nor not of off on
once only or other ought our ours ourselves out over own same shan't she she'd
she'll she's should shouldn't so some such than that that's the their theirs
them themselves then there there's these they they'd they'll they're they've
this those through to too under until up very was wasn't we we'd we'll we're
we've were weren't what what's when when's where where's which while who who's
whom why why's with won't would wouldn't you you'd you'll you're you've your
yours yourself yourselves
actually also always another anything around back basically because being come
could even every everyone everything first going gonna got great guys had just
kind know like literally look lot make many maybe mean much need new now okay one
people pretty really right said say see something sort still sure tell thank
thing think time trying use want way well went will work would yeah yes
""".split())

# Topic keyword mapping: canonical keyword -> related terms found in text
TOPIC_KEYWORDS = {
    "ai": ["artificial intelligence", "machine learning", "llm", "large language model",
           "chatgpt", "gpt", "claude", "generative ai", "gen ai", "ai agent", "ai agents",
           "ai product", "ai products", "ai tool", "ai tools", "ai coding", "ai native"],
    "product-management": ["product manager", "product management", "product managers",
                           "product leader", "product leaders", "pm role", "product team",
                           "product teams", "product org", "product organization"],
    "career-growth": ["career growth", "career path", "career ladder", "promotion",
                      "career advice", "career transition", "job search", "interviewing",
                      "resume", "career change", "break into"],
    "leadership": ["leadership", "managing", "management", "executive", "ceo", "cto", "cpo",
                   "vp of product", "director", "chief product", "leader"],
    "startups": ["startup", "startups", "founder", "founding", "venture", "vc",
                 "series a", "series b", "seed round", "early stage", "bootstrapped"],
    "growth": ["growth strategy", "user growth", "product-led growth", "plg", "retention",
               "acquisition", "activation", "monetization", "conversion", "funnel"],
    "design": ["ux design", "user experience", "ui design", "user interface", "figma design",
               "prototyping", "design system", "interaction design", "visual design",
               "product design"],
    "strategy": ["product strategy", "roadmap", "roadmapping", "strategic planning",
                 "competitive advantage", "positioning", "product vision"],
    "execution": ["execution", "shipping", "launch", "prioritization", "prioritize",
                  "sprint", "agile", "scrum", "velocity", "delivery"],
    "user-research": ["user research", "customer research", "user interview", "user interviews",
                      "customer interview", "customer feedback", "usability", "discovery",
                      "customer discovery"],
    "metrics": ["metrics", "okrs", "kpis", "data-driven", "analytics", "measurement",
                "north star metric", "success metrics", "data analysis"],
    "storytelling": ["storytelling", "public speaking", "content creation", "creator economy",
                     "newsletter", "youtube channel", "content creator"],
    "culture": ["culture", "team culture", "company culture", "values", "remote work",
                "hiring", "organizational", "collaboration", "meetings"],
    "pricing": ["pricing", "monetization", "freemium", "subscription", "business model",
                "revenue", "pricing strategy"],
    "platform": ["platform strategy", "marketplace", "developer platform",
                 "platform product", "two-sided market"],
    "gaming": ["gaming", "game design", "game development", "video game", "video games"],
    "productivity": ["productivity", "time management", "workflow automation",
                     "personal os", "save time", "10x productivity"],
    "entrepreneurship": ["entrepreneur", "entrepreneurship", "solopreneur", "side project",
                         "indie", "creator economy", "building in public"],
    "coding": ["coding", "programming", "vibe coding", "vibe code", "software engineer",
               "build an app", "build a full stack", "full stack app", "code editor"],
    "ai-tools": ["cursor", "claude code", "copilot", "replit", "v0", "bolt",
                 "windsurf", "lovable", "ai coding tool", "ai coding tools",
                 "google ai studio", "gemini"],
    "innovation": ["innovation", "disruption", "first principles", "creative",
                   "experimentation", "moonshot"],
    "big-tech": ["at google", "at meta", "at amazon", "at apple", "at microsoft",
                 "at netflix", "at spotify", "at shopify", "at slack", "at figma",
                 "at stripe", "google ai", "meta ai"],
}


def parse_header(content: str):
    """Parse the existing markdown header from a transcript."""
    lines = content.split("\n")

    title = ""
    date = ""
    url = ""
    body_start = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped[2:].strip()
        elif stripped.startswith("**Date:**"):
            date = stripped.replace("**Date:**", "").strip()
        elif stripped.startswith("**URL:**"):
            url = stripped.replace("**URL:**", "").strip()
        elif stripped == "---":
            body_start = i + 1
            break

    body = "\n".join(lines[body_start:])
    return title, date, url, body


def extract_guest(title: str) -> str:
    """Extract guest name from title. Returns 'Peter Yang' for solo episodes."""
    if "|" not in title:
        return "Peter Yang"

    guest_part = title.split("|")[-1].strip()
    # Remove company/role in parentheses
    guest_part = re.sub(r"\s*\(.*?\)\s*", "", guest_part).strip()
    return guest_part


def extract_keywords(title: str, body: str, max_keywords: int = 5) -> list[str]:
    """Extract 3-5 topic keywords from transcript content."""
    text = (title + " " + body).lower()

    # Score each topic by counting matches
    scores = {}
    for keyword, terms in TOPIC_KEYWORDS.items():
        score = 0
        for term in terms:
            count = text.count(term.lower())
            if count > 0:
                # Weight by term specificity (longer terms = more specific)
                weight = len(term.split())
                score += count * weight
        if score > 0:
            scores[keyword] = score

    # Sort by score descending and take top keywords
    sorted_keywords = sorted(scores, key=scores.get, reverse=True)

    # Always return 3-5 keywords
    result = sorted_keywords[:max_keywords]
    if len(result) < 3:
        # Fall back to generic keywords
        fallbacks = ["product-management", "career-growth", "leadership"]
        for fb in fallbacks:
            if fb not in result:
                result.append(fb)
            if len(result) >= 3:
                break

    return result[:max_keywords]


def build_frontmatter(title: str, guest: str, date: str, url: str, keywords: list[str]) -> str:
    """Build YAML frontmatter string."""
    # Escape quotes in title
    escaped_title = title.replace('"', '\\"')

    lines = [
        "---",
        f'title: "{escaped_title}"',
        f"guest: {guest}",
        f"publish_date: {date}",
        f"youtube_url: {url}",
        "channel: Behind the Craft",
        "keywords:",
    ]
    for kw in keywords:
        lines.append(f"- {kw}")
    lines.append("---")

    return "\n".join(lines)


def parse_existing_frontmatter(content: str):
    """Parse existing YAML frontmatter to extract title, date, url, and body."""
    lines = content.split("\n")
    # Find closing ---
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, None, None, content

    fm_lines = lines[1:end_idx]
    body = "\n".join(lines[end_idx + 1:])

    title = date = url = ""
    for line in fm_lines:
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"')
        elif line.startswith("publish_date:"):
            date = line.split(":", 1)[1].strip()
        elif line.startswith("youtube_url:"):
            url = line.split(":", 1)[1].strip()
            # Handle the case where url contains colons
            if line.count(":") > 1:
                url = ":".join(line.split(":")[1:]).strip()

    return title, date, url, body


def process_file(filepath: Path, force: bool = False) -> bool:
    """Process a single transcript file. Returns True if modified."""
    content = filepath.read_text(encoding="utf-8")

    if content.startswith("---\n"):
        if not force:
            return False
        # Re-process: extract info from existing frontmatter
        title, date, url, body = parse_existing_frontmatter(content)
    else:
        title, date, url, body = parse_header(content)

    if not title:
        print(f"  WARNING: Could not parse header in {filepath}")
        return False

    guest = extract_guest(title)
    keywords = extract_keywords(title, body)

    frontmatter = build_frontmatter(title, guest, date, url, keywords)
    new_content = frontmatter + "\n" + body

    filepath.write_text(new_content, encoding="utf-8")
    return True


def main():
    import sys
    force = "--force" in sys.argv

    processed = 0
    skipped = 0
    errors = 0

    for year_dir in sorted(TRANSCRIPTS_DIR.iterdir()):
        if not year_dir.is_dir():
            continue
        print(f"\nProcessing {year_dir.name}/")
        for md_file in sorted(year_dir.glob("*.md")):
            try:
                if process_file(md_file, force=force):
                    processed += 1
                    print(f"  ✓ {md_file.name}")
                else:
                    skipped += 1
                    print(f"  - {md_file.name} (skipped, already has frontmatter)")
            except Exception as e:
                errors += 1
                print(f"  ✗ {md_file.name}: {e}")

    print(f"\nDone: {processed} processed, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
