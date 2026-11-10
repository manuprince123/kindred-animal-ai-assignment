#!/usr/bin/env python3
"""Validate approved slide data and export a repeatable PNG carousel."""
import json
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "workflow" / "carousel.json"
OUT = ROOT / "dist" / "assets" / "carousel"
FONT = Path("/System/Library/Fonts/Avenir Next.ttc")
if not FONT.exists():
    FONT = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")

def font(size, bold=False):
    return ImageFont.truetype(str(FONT), size, index=1 if bold and FONT.suffix == ".ttc" else 0)

def wrap(draw, text, face, width):
    lines, line = [], ""
    for word in text.split():
        candidate = f"{line} {word}".strip()
        if line and draw.textbbox((0, 0), candidate, font=face)[2] > width:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines

data = json.loads(SOURCE.read_text())
slides = data.get("slides", [])
if len(slides) != 6:
    sys.exit("Expected exactly six approved slides")
OUT.mkdir(parents=True, exist_ok=True)
for n, slide in enumerate(slides, 1):
    for key, limit in (("overline", 45), ("title", 70), ("body", 170)):
        value = slide.get(key, "")
        if not isinstance(value, str) or not value.strip() or len(value) > limit:
            sys.exit(f"Slide {n}: invalid {key} (limit {limit})")
    image = Image.new("RGB", (1080, 1350), "#d8f267")
    draw = ImageDraw.Draw(image)
    ink = "#16251d"
    draw.ellipse((765, 1000, 1390, 1625), fill="#c8e65c")
    draw.text((65, 55), "kindred.", font=font(54, True), fill=ink)
    draw.text((330, 78), "AI FIELD NOTES", font=font(18, True), fill=ink)
    draw.text((975, 76), f"{n:02d}", font=font(22, True), fill=ink)
    draw.text((65, 390), slide["overline"].upper(), font=font(24, True), fill=ink)
    title_font = font(100 if len(slide["title"]) < 44 else 86, True)
    title_lines = wrap(draw, slide["title"], title_font, 950)
    if len(title_lines) > 4:
        sys.exit(f"Slide {n}: title overflows")
    y = 475
    for line in title_lines:
        draw.text((65, y), line, font=title_font, fill=ink)
        y += 116 if len(slide["title"]) < 44 else 103
    body_font = font(36)
    body_lines = wrap(draw, slide["body"], body_font, 920)
    if len(body_lines) > 5 or max(y + 70, 930) + len(body_lines) * 55 > 1210:
        sys.exit(f"Slide {n}: body overflows")
    body_y = max(y + 70, 930)
    for line in body_lines:
        draw.text((65, body_y), line, font=body_font, fill=ink)
        body_y += 55
    draw.line((65, 1235, 1015, 1235), fill="#6a923d", width=2)
    draw.text((65, 1260), "Practical ideas for curious minds", font=font(20, True), fill=ink)
    footer = "SAVE & SHARE" if n == len(slides) else "SWIPE TO LEARN"
    draw.text((830, 1260), footer, font=font(18, True), fill=ink)
    dest = OUT / f"slide-{n:02d}.png"
    image.save(dest, optimize=True)
    check = Image.open(dest)
    assert check.size == (1080, 1350) and check.mode == "RGB"
    print(dest.relative_to(ROOT))
