# Behind the Craft — Transcripts

Full transcripts of [Behind the Craft](https://www.youtube.com/@peteryangYT), my YouTube channel where I share practical AI tutorials and interviews for busy people. 122 episodes and counting. Searchable. AI-friendly. Auto-updated every Sunday.

## What you can build with this

- **AI assistant** — Drop into ChatGPT, Claude, or NotebookLM to Q&A 122+ episodes of product and AI advice
- **Content** — Find quotes, compile insights by topic, generate summaries for newsletters or social
- **Research** — Browse the [topic index](index/README.md) for 22 topics like [AI](index/ai.md), [product management](index/product-management.md), [career growth](index/career-growth.md), [startups](index/startups.md)

## What's inside

Each transcript has YAML frontmatter (title, guest, date, YouTube URL, keywords) followed by the full text:

```yaml
---
title: "Inside How Figma Builds AI Products | Yuhki Yamashita (CPO Figma)"
guest: Yuhki Yamashita
publish_date: 2024-04-28
youtube_url: https://youtube.com/watch?v=z_PPC1PPb-M
channel: Behind the Craft
keywords:
- ai
- design
- product-management
---
```

**Interview guests include:** Peter Steinberger (OpenClaw), Amjad Masad (Replit), Ami Vora (Anthropic), and 100+ more.
**Personal tutorials include:** Claude Code, OpenClaw, Google AI Studio, and more.

## Quick start

Browse the [topic index](index/README.md), or clone and search:

```bash
grep -rl "vibe coding" transcripts/        # full-text search
grep -rl "guest: Claire Vo" transcripts/   # search by guest
```

Or point your favorite AI tool at the `transcripts/` folder.

## Staying up to date

New episodes are added automatically every Sunday via GitHub Actions — no manual updates needed.

## Maintenance

```bash
python3 scripts/fetch_new_episodes.py  # fetch new episodes from YouTube
python3 scripts/add_frontmatter.py     # add frontmatter to new episodes
python3 scripts/build-index.py         # rebuild topic index
```


