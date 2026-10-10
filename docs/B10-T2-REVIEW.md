# B10 tranche T2 — execution log (2026-10-10)

Allowance: [b10-t2-authorization](../outputs/production/b10-t2-authorization.json) — ceiling 281, video sound off.

| Job | Credits | Result |
|---|---|---|
| W04-pre-v1 | 6.5 | Accepted → `stage-04-west-pre.png` (sink cutout empty, faucet holes, empty microwave bay, bare ledge, empty nook). Intermediate west states built locally (`tools/build_west_states.py`) |
| P05-stone-v1 | 6.5 | Accepted → `master-stone-clean.png` (hood/pot filler/toaster/kettle removed; local tone-blend composite). MASTER 04→06 states built locally (`tools/build_master_states.py`) |
| 04A-end-v1 | 6.5 | Accepted → `04A-end.png` after wider bbox + cabinet/worktop contact region (initial mask clipped lead, blotched worktop edge) |
| 04A-start-v1 | 6.5 | Accepted → `04A-start.png` (sink held level just above cutout, same worker placement as END) |
| 04B-end-v1 | 6.5 | Accepted → `04B-end.png` (lead hand-tightening faucet; faucet+dispenser from view 2) |
| 04B-start-v1 | 6.5 | Accepted → `04B-start.png` (faucet held over the drilled hole; minor seam on drawer face) |
| 04C-end-v1 | 6.5 | Accepted → `04C-end.png` (partner crouched, palm on installed microwave; bbox widened to frame edge) |
| 04C-start-v1 | 6.5 | Accepted → `04C-start.png` (microwave half into opening). Limit: held unit reads slightly plainer than installed built-in trim |
| 05A/05B/06A/06B/06C-end-v1 | 32.5 | Accepted after compositor fixes (bbox widened; solid mask threshold 70–90 + skin inclusion; every person blob kept). Limits: small blocky wall patches near hands in 05A/05B/06A; workers stand in the empty range bay for 05–06B |
| 05A/05B/06A/06B/06C-start-v1 | 32.5 | Accepted. 05B/06B needed contact regions for the held cabinet/pot filler (raw returns correct). Limits: 06C START ≈ END (range already nearly home — reads as final nudge, not a pull-in); blocky wall patch under held cabinet in 05B |
| 04A/04B/04C-take-v1 | 11.25 | **Lead pass**: sink lowered and seated; faucet seated and turned; microwave slid home |
| 05A-take-v1 | 3.75 | **Fail**: START composite had dropped the held slab (mask), so stone "wiped" onto the wall. Fixed free: slab contact region in START; new END v2 on a plate with only that one slab flat on the wall (`stage-05a-slab1.png`) |
| 05A-take-v2 | 3.75 | **Lead pass (trim to first 60 frames)**: one rigid slab held and pressed flat; last ~12 frames soften |
| 05B-take-v1 | 3.75 | **Partial — trim plan**: frames 0–24 hold the cabinet ~300 px left of its END position, then it jumps into place (START/END state mismatch; also left glass upper only in END). Frames 30–72 (drill drives screw into the installed cabinet) are coherent → use 1.75 s and retime to the 2.5 s slot at assembly. No retry: a retry can't fix a state mismatch, and rebuilding START would cost an image job plus a video |
| 06A/06B/06C-take-v1 | 11.25 | **Lead pass**: hood checked with level; pot filler arm swung out; range nudged home (06C START≈END, so the motion is small) |

## T2 closeout (lead)

All 8 T2 takes produced (05A v2, 05B trim). Generation disabled; awaiting Stefan's review.

**User decision 2026-10-10:** T2 accepted incl. 05B trim ("Accept T2, commit, approve T3 no sound").
