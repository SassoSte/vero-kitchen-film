# B10 tranche T4 — execution log (2026-10-10)

Allowance: [b10-t4-authorization](../outputs/production/b10-t4-authorization.json) — ceiling 232, video sound off.

| Job | Credits | Result |
|---|---|---|
| F10-oak-v1 | 6.5 | Accepted → `stage-10-final-oak.png`; one-panel, two-stool and three-stool states built locally (`tools/build_final_states.py`) |
| 10A-v1 | 6.5 | Accepted → `10A-start.png` (lead nailing oak panel, partner pressing it; start-image take) |
| 11A-end-v1 | 6.5 | Accepted after re-compositing: the return was zoomed out with re-drawn stools; saliency now computed in return coordinates and the return's stool legs excluded. Scale checked (~1.75 m vs 0.95 m stool backrest) |
| 11A-start-v1 | 6.5 | Accepted → `11A-start.png` (lead lowering third stool, framing matched). END/START worker scale mismatch (END return was zoomed) → 11A becomes a start-image-only take; `11A-end.png` kept but unused |
| 11B/11D/11E-v1 | 19.5 | Accepted (toaster held above worktop; partner straightening rug edge; lead setting vase on bar). Start-image takes |
| 11C-v1 | 6.5 | **Rejected**: return re-framed; only a disembodied arm transferred |
| 11C-v2 | 0 (refunded) | **Void**: my take_frame bug submitted an empty prompt; provider failed the job and refunded 6.5. take_frame now refuses empty prompts/refs and never overwrites a prepared request |
| 11C-v3 | 6.5 | Accepted → `11C-start.png` (kettle held just right of range; toaster in place) |
| 10A-take-v1 | 6.25 | **Lead pass**: nailer along panel edge, partner holds panel; stable 5 s |
| 11A-take-v1 | 3.75 | **Lead pass**: stool lowered and squared, worker steps back |
| 11B-take-v1 | 3.75 | **Partial — trim**: after ~frame 14 the camera drifts, the fridge (hidden behind the worker) is hallucinated as wall ovens, and the toaster lands right of the range. Frames 0–12 clean → used slowed (0.5 s → 0.8 s slot); 11C opens with the toaster in place, so the cut implies placement. No retry |
| 11C-take-v1 | 3.75 | **Lead pass**: kettle set down right of range (nearer the range than in MASTER) |
| 11D-take-v1 | 3.75 | **Lead pass**: rug edge smoothed (small, distant) |
| 11E-take-v1 | 3.75 | **Lead pass**: vase set on bar, worker steps back |
| 12A / 13A | 0 | Local holds: slow 2% push-in on selected MASTER and FINAL |

## T4 closeout (lead)

All T4 takes produced. Generation disabled; awaiting Stefan's review. Next: B12 assembly + sound pass (local).

**User decision 2026-10-10:** T4 accepted incl. 11B trim ("Accept T4, commit, proceed to assembly with option A").
