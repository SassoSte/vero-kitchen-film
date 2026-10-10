# Research playbook — portable source extract

Source: `/Users/stefansassoon/projects/vero/deco/research-playbook.md`. Captured2026-10-09.
The local credential-routing/command section is omitted; acquisition lessons, source
matrix and dimension-derivation method are retained. This is an extract, not a byte-exact copy.

## Hurdle → solution matrix

| Hurdle | Solution that worked |
|---|---|
| `theallisoncondos.com` (Entrata) → HTTP 403 on plain fetch | **Firecrawl v2 scrape** with the Firecrawl Hermes key (1Password) — markdown format, ~7 s |
| Zillow property page (bot-walled class of site) | Firecrawl scrape returned the real `homedetails` page (not a search redirect) — verify by checking the returned title/facts before trusting |
| Coldwell Banker / Realtor.com listing pages | Firecrawl scrape — clean markdown incl. ARMLS fact blocks (appliances, interior features, subdivision) |
| Cheap facts before scraping | `web_search` snippets alone carried sold price, sqft, bed/bath, MLS #, active asks (Movoto) — search first, scrape only what search doesn't answer |
| Extracting a listing's 29–36 photos | The Firecrawl **markdown embeds the CDN image URLs** (`m1.cbhomes.com/p/246/<mls>/<id>/pdl23tp.webp`, `m.cbhomes.com` alternating) — curl them directly, keep `photo-NN` naming to preserve listing order |
| Entrata floor-plan renders | CDN is unauthenticated: `medialibrarycfo.entrata.com/...` — plain curl from the scraped markdown |
| **Room dimensions published nowhere** (verified across 7 sources: ARMLS mirrors, Zillow, Realtor, Redfin, Coldwell Banker, apartments.com, official site) | Pixel-calibrate the marketing render + photo photogrammetry (method below) |
| Reading 29–36 photo galleries reliably | PIL contact sheets: 400 px thumbs, 6-col grid, filename labels — one image read replaces 30 |
| Byte-identical duplicates in listing galleries | Detect, drop, keep original numbering (gaps documented in `assets/INDEX.md`) |
| WhatsApp media album content (assignment doc) | Desktop app media viewer + arrow keys pages every item; `screenshot({silent:true})` each step, `read()` the temp paths; AX descriptions (`el.attributes().AXDescription`) give verbatim message text when the tree truncates |

## Source matrix — The Allison / Phoenix-metro listings (2026-10-07)

| Source | Plain fetch | Firecrawl | Value |
|---|---|---|---|
| theallisoncondos.com (Entrata) | 403 | ✅ | 3 floor plans + sqft + available-unit list (confirms building/floor for a unit #) |
| zillow.com homedetails | — | ✅ | sold price/date, facts, photo set, Zestimate |
| realtor.com | — | ✅ | facts + price-history table (rental history too) |
| coldwellbankerhomes.com | — | ✅ | ARMLS fact blocks + all photo URLs in markdown |
| apartments.com | — | ✅ | rental-side plan sqft + amenity lists |
| realgeeks-platform agent sites (e.g. arizonabest.com) | ✅ plain | — | scrape clean without API (Rome St fetch used this) |
| movoto.com | — | not needed | facts surfaced via web_search snippets |

### Maricopa County Assessor — ArcGIS feature service (authoritative source)

The county live ArcGIS endpoint is the canonical source for assessed value, living area,
ownership, and parcel identifiers. No browser or auth needed — direct JSON:

```bash
curl -sS "https://gis.mcassessor.maricopa.gov/arcgis/rest/services/Parcels/MapServer/0/query\
?where=APN_DASH='217-73-750'&outFields=*&returnGeometry=false&f=json" | jq '.features[0].attributes'
```

Key fields: `APN`, `APN_DASH`, `OWNER_NAME`, `LIVING_SPACE` (sqft), `CONST_YEAR`,
`FLOOR`, `MCRNUM`, `SUBNAME`, `LAND_SIZE`, `SALE_DATE`, `SALE_PRICE`, `FCV_CUR`,
`LPV_CUR`. The geometry fields `Shape_Area` and `Shape_Length` are in **unknown units**
— do not use them. Layer schema lists all available fields: `GET [...MapServer/0?f=json]`.

Parcel-level sketch (the county's dimensional drawing): available for single-family
residential parcels via the assessor SPA's "Parcel Maps" tab, but for **condominiums**
(MCR 912-22 in this case) the assessor maps to a section-level plat only — no per-unit
interior partition sketch exists. Room-level dimensions are not published by any public
source for this community (verified 2026-10-07 across assessor ArcGIS + SPA, seven
listing platforms, and the Recorder's MCR plat).

## Dimension derivation when nothing is published

1. **Topology** from the marketing render (Entrata 3D plans are near-orthographic).
2. **Area calibration**: pixel-classify the render (floor/wall vs background; exclude
   neutral-gray shadows), solve scale by reconciling the drawn footprint to the marketed
   sqft → single in/px factor (here 0.326 in/px at 4×, ±2%).
3. **Independent validation**: measure a photo-locked span inside the render (kitchen run
   123″ measured 125″ = 2% error) plus everyday anchors (queen bed 60″, 8-ft rug, fridge 30″).
4. **Photo photogrammetry** for the graded room: lock module standards (counter 25.5″ deep /
   36″ AFF, appliances 30″/24″/33″, upper band 54–84″), derive spans from pixel ratios,
   snap to the 3″ construction module.
5. **Record confidence in the dimension markdown**, not on the drawing: V (standard-locked) /
   H (photo ±2–3″) / E (render ±4–6″), the reconciliation error vs assessor/marketing sqft,
   and the on-site measure checklist that tightens to ±1″. The plan or elevation is an SVG
   sheet — `.cursor/skills/architectural-sheet/SKILL.md`. Kitchen `plan.svg` and
   `elevations.svg` are the pattern. `unit-plan.svg` still renders black; redraw it before
   copying it.

## Housekeeping conventions that made this trackable

- `assets/INDEX.md` maps every picture to its subject; update it + regenerate the affected
  PIL contact sheet **in the same commit** as any add/remove; document deletions with the
  commit hash for recovery.
- Evidence photos committed next to the documents that cite them;MLS watermark never stripped.
- Commits stamped `git -c user.name="Stefan Sassoon (OMP)"` — per-invocation, never persisted.
