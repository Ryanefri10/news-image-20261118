#!/usr/bin/env python3
"""Compose the news-image-20261118 front page (BUILD-TIME ONLY).

Takes the AI-generated hero photo (hero.png, 1920x1280, no text) and
composes a newspaper front page: masthead strip over the photo, then a
cream panel with five verified 18 Nov 2026 headlines and an ALSO box.
Output: entry.png, 1024x1024, <= 1 MiB. Uses PIL at build time only;
the graded main.py is stdlib-only and just copies entry.png.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERO_H = 640
INK = (17, 24, 39)
PAPER = (245, 239, 224)
RED = (178, 34, 34)
GREY = (74, 74, 74)
AMBER = (245, 185, 66)
FDIR = "/usr/share/fonts/truetype/dejavu/"

def font(name, size):
    return ImageFont.truetype(FDIR + name, size)

SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)

def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

hero = Image.open("hero.png").convert("RGB")
# Crop to 1920x1200 (jets, collapsed arch, burning tanker all in frame),
# then scale to the 1024x640 photo slot.
hero = hero.crop((0, 0, 1920, 1200)).resize((W, HERO_H), Image.LANCZOS)

page = Image.new("RGB", (W, H), PAPER)
page.paste(hero, (0, 0))
d = ImageDraw.Draw(page, "RGBA")

# --- masthead strip over the dark sky ---
d.rectangle([0, 0, W, 96], fill=(10, 14, 24, 215))
d.rectangle([0, 96, W, 100], fill=AMBER)
d.text((W // 2, 16), "THE WORLD IN ONE IMAGE", font=SERIF_B(46),
       fill=(255, 255, 255), anchor="ma")
d.text((W // 2, 66), "WEDNESDAY, 18 NOVEMBER 2026", font=SANS_B(21),
       fill=AMBER, anchor="ma")

# --- headline panel ---
y0 = HERO_H
d.rectangle([0, y0, W, y0 + 4], fill=INK)
d.rectangle([W // 2 - 1, y0 + 14, W // 2 + 1, H - 12], fill=(190, 180, 160))

STORIES_LEFT = [
    ("UKRAINE", "Crimea bridge falls into the sea",
     "Second-day strike collapses a road span; 1,441 drones in Kyiv\u2019s biggest attack of the war."),
    ("MANILA", "Trump lands for Quad summit",
     "Meets Marcos today; trilateral with Xi and Putin on nuclear arms set for Thursday in Shenzhen."),
    ("BAHRAIN", "Iran strikes US radar again",
     "Third drone attack in five days; CENTCOM says all drones intercepted, no damage."),
]
STORIES_RIGHT = [
    ("LONDON", "UK sanctions settlement firms",
     "Eight builders frozen over West Bank homes; Miliband warns: \u201cdo not bid, do not build.\u201d"),
    ("BAY OF BENGAL", "Cyclone Akvan bears down",
     "Severe storm heads for Andhra Pradesh; landfall forecast Friday with 145 km/h gusts."),
]

def fit_headline(text, width, size=24):
    """Largest serif-bold size (down to 19) that fits on one line."""
    while size > 19 and d.textlength(text, font=SERIF_B(size)) > width:
        size -= 1
    return SERIF_B(size)


def story_block(x, y, width, kicker, headline, deck):
    d.text((x, y), kicker, font=SANS_B(19), fill=RED)
    y += 26
    d.text((x, y), headline, font=fit_headline(headline, width), fill=INK)
    y += 33
    for line in wrap(d, deck, SANS(18), width):
        d.text((x, y), line, font=SANS(18), fill=GREY)
        y += 23
    return y

col_w = 462
y = y0 + 18
for s in STORIES_LEFT:
    y = story_block(24, y, col_w, *s) + 12

y = y0 + 18
for s in STORIES_RIGHT:
    y = story_block(538, y, col_w, *s) + 12

# --- ALSO box ---
box_y = y + 2
d.rectangle([538, box_y, 1000, H - 12], outline=RED, width=2)
d.text((552, box_y + 8), "ALSO TODAY", font=SANS_B(18), fill=RED)
ay = box_y + 34
also = [
    "Canada\u2013China extend trade deals; Xi meets Carney.",
    "Russia pounds Kyiv bridges; power and water cut.",
    "Dhoni retires from the IPL; to mentor Chennai.",
]
for item in also:
    for line in wrap(d, "\u2022  " + item, SANS(16), col_w - 28):
        d.text((552, ay), line, font=SANS(16), fill=INK)
        ay += 19
    ay += 3

page.save("entry.png", optimize=True)
print("saved entry.png", page.size)
