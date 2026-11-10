# Kindred — internship assignment submission

This is an interactive prototype responding to all three deliverables in `Intern_Assignment.pdf`. Open `dist/index.html` locally or use the deployed Site URL. The directory entries, course programme, and brand are illustrative. No real provider, course schedule, testimonial, or verification claim is implied.

## 1. Animal-care discovery MVP

**User problem:** A pet parent needs to identify an appropriate local service quickly, especially on a phone. The page leads with need and location, then shows six service shortcuts and concise result cards.

**MVP elements:** service and location search; service filters for clinics, hospitals, boarding, diagnostics, ambulances, and NGOs; provider cards with type, area, service summary and availability guidance; a details view; business suggestion and correction flows. The four requested CTAs are represented by **Find a vet**, **Explore all**, **List your business**, and **Submit a correction**. A production version should add species served, verified phone/website, map directions, last confirmed date, and a human-reviewed verification badge. Reviews and booking are later-phase features because they need moderation and reliable provider participation.

**Trust and safety:** The demo labels every result as illustrative. A production ingestion pipeline should require provider consent, source URL, owner claim or direct confirmation, moderation, duplicate detection, and a visible last-verified date. Corrections should enter a review queue, not change the public record immediately. For urgent care, a live listing should show whether emergency service and hours were confirmed.

**Mobile UX:** One-column search controls and cards, large tap targets, short labels, and no essential hover interactions. Search works as a prototype with local sample data.

## 2. AI education landing page

**Audience and promise:** Students and early-career professionals who want practical AI and digital skills. The structure moves from a clear promise to outcomes, four curriculum modules, and a short interest form.

**Conversion journey:** Hero CTA → programme details → name/email/role form → inline confirmation. The form intentionally says that it stores entries only in the current browser. A live implementation would add explicit communication consent, server-side validation, CRM delivery, a confirmation email, and privacy copy. Dates, pricing, instructors, certification, and outcomes are not invented; they should be supplied by the founder before launch.

## 3. Carousel and repeatable content system

The six-slide sample, **“AI is a co-pilot, not autopilot,”** is editable in the Carousel Studio. Each slide can be exported as a 1080 × 1350 PNG. The approved source is `workflow/carousel.json`; the raw brief, research note, and human review are saved beside it. The sample was AI-assisted and then checked against NIST, UNESCO and OpenAI guidance. The on-page preview loads the approved JSON and allows edits; revised copy can be downloaded as JSON.

The repeatable export is implemented in `scripts/build_carousel.py`. Running `python3 scripts/build_carousel.py` validates the slide count, copy lengths, text fit and dimensions, then writes six ready-to-publish PNGs under `dist/assets/carousel/`. A GitHub Actions workflow runs the same export when approved copy or the renderer changes and uploads the PNG set as an artifact. The founder's approval remains a human step, documented in `workflow/review.md`. This is a working export automation, not a claim that live AI research or Canva/n8n APIs are connected.

**Recommended founder workflow:**

1. Capture a raw idea with audience, goal, platform, tone, and intended CTA in a form or Notion database.
2. Use an LLM with web access to research primary sources. Save source links and dates in a short evidence note.
3. Ask the LLM for three hooks and a six-slide outline; choose one, then draft slide copy within a character budget.
4. Run a claim check: each factual statement must be backed by a source or removed. Founder approves the narrative and tone.
5. Populate a reusable Canva or Figma template. For repeat volume, Canva Bulk Create/Autofill can map structured fields into a template; plan availability must be checked before committing to API automation.
6. Check layout at phone size, proofread, export individual PNGs, and prepare platform-specific caption/alt text. Founder makes the final publication decision.

**Optional automation:** An n8n flow can watch a new brief, call the selected LLM, write structured slide data to a sheet or database, notify the founder for approval, and trigger template population only after approval. Keep publishing manual initially. The demo does not pretend this integration is connected.

## Suggested production stack

- Front end: Next.js or another accessible responsive web stack.
- Data: Supabase/Postgres tables for providers, submissions, and leads; object storage for approved provider images.
- Search: database filters first; add geospatial ranking and full-text search as records grow.
- Operations: provider claim and correction moderation dashboard; audit log and last-verified timestamps.
- Leads: a consented form connected to a CRM or email platform with spam protection.
- Content: LLM for research and structured draft; Canva/Figma template; n8n only when volume warrants it.

## Requirement checklist

| Brief requirement | Delivered here |
|---|---|
| MVP homepage/search-page design | Interactive Find Care section |
| Course landing-page design | AI Programmes section and lead form |
| One AI-generated carousel | Six-slide editable sample and PNG exports |
| Tools, stack, CTAs and workflow explanation | On-page Project Notes and this README |
| Prototype/demo link | Deployed private Site URL when available |

## Prototype limitations

This is front-end demonstration code. Form submissions use `localStorage` and are not transmitted. Provider details are fictional. The page labels those limits in the relevant flows. The generated PNGs are suitable for a sample submission, but a founder should keep editable design templates and source copy for ongoing production.

## Verification

- `node --check dist/app.js` passed.
- `python3 scripts/build_carousel.py` produced six 1080 × 1350 RGB PNGs and checked text fit.
- A headless Chrome pass at 1440 px desktop and 390 px mobile widths found no horizontal overflow or JavaScript page errors. Service filtering, carousel navigation and mobile navigation passed.
- Desktop and mobile full-page screenshots were reviewed in `qa/` locally. The mobile and desktop layouts are legible, with no observed overlaps or clipped sections.
