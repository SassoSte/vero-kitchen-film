# Whole-unit dimensions — source extract

Source: `/Users/stefansassoon/projects/vero/deco/unit-blueprint/unit-dimensions.md`.
Captured 2026-10-09. This extract preserves the source from its Method section onward;
owner/parcel valuation/sale metadata is intentionally omitted. It retains source errors,
which are listed in the source register; it is not a corrected or surveyed plan.

## Method

1. Topology from the Entrata «Tallbot» render (`assets/allison-floorplans/tallbot.jpg`).
2. Pixel calibration: footprint classified from the 4× render (floor/wall vs background,
   shadows excluded); scale solved by reconciling the drawn envelope to the 1,058 sqft
   marketing area → **0.326 in/px at 4×** (±2%).
3. Independent checks: photo-locked kitchen Run A (123″) measures ≈125″ in the render (2%
   error ✓); queen-bed width (60″), 8-ft rug, balcony-chair and door scales all consistent.
4. Room spans read from the calibrated render, snapped to the 3″ construction module.
5. No published room dimensions exist for this community (checked ARMLS mirrors, Zillow,
   Realtor, Redfin, Coldwell Banker, apartments.com, theallisoncondos.com — 2026-10-07).

## Confidence

- **V** — standard-locked (appliance/fixture modules)
- **H** — photo estimate ±2–3″ (kitchen only; see kitchen-blueprint)
- **E** — render-scaled ±4–6″ (everything in this file)

These letters stay in this file. The SVG sheet does not repeat them.

## Envelope

| Element | Dim | Conf |
|---|---|---|
| Main body, width (E–W) | 262″ (21′10″) | E |
| Main body, depth (N–S) | 462″ (38′5″) | E |
| Balcony wing (east, exterior): depth × length | 94″ × 152″ (7′10″ × 12′8″) | E |
| Balcony (open, railed) | ≈53″ × 145″ (4′5″ × 12′1″) | E |
| Exterior storage closet on balcony | ≈36″ × 32″ | E |
| Kitchen ceiling 96″ flat; vaulted ceiling over living; bedrooms flat | — | H |
| Reconciliation: drawn interior ≈ 1,000–1,050 sqft vs 1,029 assessor / 1,058 marketing | ±4% | E |

## Rooms (render-scaled, snapped to 3″ module)

| Room | Dim | Area | Conf | Notes |
|---|---|---|---|---|
| Living room (open) | 13′1″ × 12′8″ | 165 sqft | E | NE corner; balcony slider on east wall; TV on south partition; vaulted |
| Dining (open zone) | ≈8′6″ × 6′8″ | 57 sqft | E | South of kitchen; clerestory window above (from #2130 photo-02) |
| Kitchen | 10′3″ runs × 8′9″ zone | 142 sqft | H | Galley; see kitchen-blueprint/dimensions.md for the locked runs |
| Bedroom 2 | 8′0″ × 11′9″ | 94 sqft | E | NE; queen fits with nightstands (render) |
| Bedroom 2 reach-in closet | 6′10″ × 2′5″ | 17 sqft | E | West of bed2, sliding/bifold |
| Hall lobby | 2′9″ × 11′9″ | 32 sqft | E | Serves bath 2 + bedroom 2 doors |
| Bath 2 (hall) | 7′4″ × 7′3″ | 53 sqft | E | Tub 60″ along north wall, toilet, vanity (render + gallery photo-07) |
| Master bedroom | 10′0″ × 10′6″ | 105 sqft | E | South-center; reach-in closet ≈6′ on north wall |
| Bath 1 (master) | 5′4″ × 5′8″ | 30 sqft | E | SW; shower over tub, toilet, vanity (gallery photo-10) |
| Laundry closet | 4′6″ × 3′1″ | 14 sqft | E | Full-size washer + dryer side-by-side, bifold, shelf over (gallery photo-11); off the corridor between master suite and kitchen |
| Entry vestibule | ≈5′2″ × 5′0″ | 26 sqft | E | SE corner; 36″ entry door on east wall (render arrow); opens to living |
| Corridor (entry → hall) | ≈3′2″ wide | — | E | Runs west between living and master |

## Suite logic (from render + gallery)

- **Bath 2** (tub) + bedroom 2 + its closet cluster at the north end, off the lobby.
- **Master suite** at the south end: bedroom, reach-in closet on its north wall, bath 1 and
  the laundry closet accessed through the short dressing corridor at its west (internal
  door arrangement approximate — ±6″).
- **Open great room**: kitchen galley (west) → dining zone → living (east) with balcony
  slider; the only interior pass-door sequence entry → living → hall → bedrooms.

## What tightens this to ±1″

Five laser numbers (kitchen checklist in kitchen-blueprint/dimensions.md) plus three more:
main-body width at the widest interior point, main-body depth along the east hall wall,
bedroom 2's two walls. 15 minutes on site with a tape/laser. Everything else then derives
by the render ratios above.
