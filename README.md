# Behind the Craft — Transcripts

Full transcripts of [Behind the Craft](https://www.youtube.com/@behindthecraft), Peter Yang's YouTube channel where top product leaders, founders, and builders share how they actually work. 116 episodes. Searchable. AI-friendly.

## What you can build with this

- **AI assistant** — Drop into ChatGPT, Claude, or NotebookLM to Q&A 116 episodes of product and AI advice
- **Search app** — Structured frontmatter makes it easy to build semantic search or RAG pipelines
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

**Guests include:** Claire Vo (LaunchDarkly), Yuhki Yamashita (Figma), Scott Belsky (Adobe), Tomer Cohen (LinkedIn), Aravind Srinivas (Perplexity), Amjad Masad (Replit), Ami Vora (Anthropic), and 100+ more.

## Quick start

Browse the [topic index](index/README.md), or clone and search:

```bash
grep -rl "vibe coding" transcripts/        # full-text search
grep -rl "guest: Claire Vo" transcripts/   # search by guest
```

Or point your favorite AI tool at the `transcripts/` folder.

## Maintenance

```bash
python3 scripts/add_frontmatter.py   # add frontmatter to new episodes
python3 scripts/build-index.py       # rebuild topic index
```
