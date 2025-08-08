---
slug: design-tip-contrast-clarity
title: Design Tip — Contrast & Clarity
date: 2025-08-09
tags: [design, ui, tips]
summary: Five quick wins for NK‑style interfaces: spacing, type scale, hairlines, color restraint, and intentional motion.
cover: covers/design-tip-contrast-clarity.svg
---

# Design Tip — Contrast & Clarity

Big type, small chrome. If your UI feels muddy, these micro‑rules clean it up fast.

## 1) Start with spacing
Use **generous padding** and keep gutters consistent. Let elements breathe and you’ll need fewer borders.

- Base spacing scale: 4/8/12/16/24/32
- Container padding: `px-5 py-7` (mobile), add `md:px-8 md:py-10`

## 2) One typeface, two weights
Pick a single family and lean on size, weight, and letter‑spacing.

- Display: 48–72px, tight tracking
- Body: 14–16px, relaxed leading
- Micro‑labels: **uppercase**, tiny tracking (e.g. `tracking-[0.35em]`)

## 3) Hairlines instead of boxes
Prefer **1px hairlines** to heavy borders. They separate without shouting.

```css
.hairline{ box-shadow: inset 0 -1px 0 0 rgb(255 255 255 / .08); }
.dark .frame{ box-shadow: 0 0 0 1px rgb(255 255 255 / .08); }
```

## 4) Color last
Use grayscale first; introduce **one accent** for calls to action. In this theme we use `#ff6a2b`.

```html
<button class="bg-accent text-black hover:opacity-90 px-4 py-2 rounded-full">Continue</button>
```

## 5) Motion with intent
Short and soft. 150–250ms, `ease-out` for entrances, `ease-in` for exits. Animate **opacity/transform** only.

## 6) Dark‑mode polish
Avoid pure white on pure black. Use `text-neutral-100` on `bg-neutral-950`. For disabled states, step down to `text-neutral-500`.

---

**TL;DR** — Fewer colors, bigger type, thinner lines, deliberate motion.
