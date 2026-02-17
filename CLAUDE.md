# CLAUDE.md

## Repository overview
Behind the Craft is a collection of 116 podcast/YouTube transcript files from Peter Yang's "Behind the Craft" channel, covering product management, AI, career growth, and leadership.

## Structure
- `transcripts/YYYY/*.md` — Episode transcripts with YAML frontmatter (title, guest, date, URL, keywords)
- `index/` — Auto-generated topic index built from frontmatter keywords
- `scripts/` — Maintenance scripts

## Key conventions
- Transcripts are numbered sequentially (001–116) and organized by year (2024, 2025, 2026)
- Each transcript has YAML frontmatter with: title, guest, publish_date, youtube_url, channel, keywords
- Solo episodes (no `|` in title) have `guest: Peter Yang`
- Keywords are drawn from a fixed topic taxonomy defined in `scripts/add_frontmatter.py`

## Common tasks
- **Regenerate frontmatter**: `python3 scripts/add_frontmatter.py --force`
- **Rebuild topic index**: `python3 scripts/build-index.py`
- **Search transcripts**: Use grep/ripgrep across `transcripts/` — frontmatter fields make structured search easy

## Adding new episodes
1. Add the transcript `.md` file to the appropriate `transcripts/YYYY/` folder with the standard header format (# Title, **Date:**, **URL:**)
2. Run `python3 scripts/add_frontmatter.py` to add frontmatter
3. Run `python3 scripts/build-index.py` to update the topic index
