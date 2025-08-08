---
slug: recall-your-ideas
title: Recall Your Ideas
date: 2025-08-08
tags: [writing, workflow, design]
summary: A lightweight workflow for publishing ideas fast — from Markdown to a live page with covers, RSS, and zero build tools.
cover: covers/recall-your-ideas.svg
---

# Recall Your Ideas

Shipping thoughts should be easier than forgetting them. This blog keeps it that way: write Markdown, drop a cover image, push. The rest (index, RSS, theme) happens for you.

## Why zero‑build still wins

- **Fast start:** no toolchain, no Node version drift, no lockfiles.  
- **Transparent:** the source you write is the source people read.  
- **Host anywhere:** plain files work on GitHub Pages, S3, or any static host.

## My writing flow

1. Create a file in `posts/` named after the slug: `recall-your-ideas.md`.
2. Add front matter (slug, title, date, tags, summary, optional cover).
3. Write. Keep sections short; use `##` headings for rhythm.
4. Commit & push to `main`.
5. The workflow updates `posts/index.json` and `feed.xml` automatically.

## Slugs and filenames

Match file and slug: it keeps routes guessable (`#/post/recall-your-ideas`) and makes imports straightforward.

## Covers that communicate

Covers are optional. If you add one, use a consistent aspect ratio (16:9). SVGs are perfect: crisp on any device and lightweight. Think of a cover like a movie poster — pick **one** strong idea, not five.

## Performance budget

- Keep images under ~200 KB when possible.
- Use SVG for abstract shapes; use JPEG/WEBP for photos.
- Prefer system fonts or a single display family.

## Accessibility quick wins

- Write descriptive alt text on images inside posts.
- Use meaningful link text (avoid “click here”).
- Break long paragraphs; 80–120 words per section is friendly.

## Roadmap ideas

- `draft: true` in front matter to keep posts local.
- `cover_alt:` for social previews.
- Automatic Open Graph image from the cover.

---

**TL;DR** — Your ideas deserve a tiny runway. This stack gives you one.