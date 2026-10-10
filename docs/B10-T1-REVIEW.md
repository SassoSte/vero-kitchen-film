# B10 tranche T1 — execution log (2026-10-10)

Allowance: [b10-t1-authorization](../outputs/production/b10-t1-authorization.json) — ceiling 249, video sound off.

| Job | Credits | Result |
|---|---|---|
| P02-bases-v1 | 6.5 | Accepted after free mask correction → `stage-02-bases.png` (worktops off, boxes exposed) |
| P02-bare-v1 | 6.5 | Accepted with local wall-texture match → `stage-02-bare.png` (no cabinets/DW; plumbing stubs) |
| 02A-end-v1 | 6.5 | Accepted → `02A-end.png` (lead trowels fresh patch, partner with bucket). Partner composited with soft cast shadow; partner reads slightly tall |
| 02A-start-v1 | 6.5 | Accepted → `02A-start.png` (patch rough; patch+hand region only re-composited onto END) |
| 02B-end-v1 | 6.5 | **Rejected**: return rebuilt the right run (continuous cabinets to the fridge, no narrow cabinet/range gap, fridge shifted); workers' hands rest on geometry that does not exist in the plate, so a worker-only composite is incoherent |
| 02B-end-v2 | 6.5 | Accepted with local fixes → `02B-end.png`: return correct layout but zoomed; worker-only composite, partner moved down 95 px onto the range-bay floor (`tools/b10_02b_partner_fix.py`). Limits: level end tucks behind lead; faint wall patch behind lead's left hand |
| 02B-start-v1 | 6.5 | Accepted → `02B-start.png`: hands/tools region only re-composited on END (drill lifted off screw, level just above cabinet) |
| 02A-take-v1 | 3.75 | **Lead pass** → `outputs/takes/02A-take-v1.mp4`: 1912×1080, 73 frames; even trowel stroke, rough→smooth patch, room/identities stable |
| 02B-take-v1 | 3.75 | **Lead pass** → `outputs/takes/02B-take-v1.mp4`: 1912×1080, 73 frames; drill drives screw, level lowered; cabinets rigid |

Shot 02 complete (pending Stefan's review). T1 spent 53.0 of 249.

## Shot 01 — paused for a decision

`references/original/ref-a-cooking-run.webp` and `ref-h-apartment-facing.webp` are 1138×640
MLS listing photos carrying a visible "©2023 ARMLS" watermark. Shot 01 (01A hold, 01B/01C/01D
edits) would build directly on them. Removing or painting over a copyright notice is not
something to do unilaterally; options are for Stefan to choose (see chat).
| P01-otr-removed-v1 | 6.5 | Accepted → `stage-01-otr-removed.png` (crop base; microwave gone, bracket/outlet exposed) |
| P01-range-removed-v1 | 6.5 | Accepted with free re-composite (larger mask, no colour gain) → `stage-01-range-removed.png` |
| P01D-lamp-removed-v1 | 6.5 | Accepted → `stage-01D-lamp-removed.png` |
| 01B-end-v1 | 6.5 | **Rejected**: partner placed behind the granite worktop (impossible footing); frame re-imagined wider |
| 01B-end-v2 | 6.5 | Accepted → `01B-end.png` (both workers in aisle carrying microwave; contact areas now survive solid mask) |
| 01B-start-v1 | 6.5 | Accepted → `01B-start.png` (reaching up to the still-mounted microwave) |
| 01C-end-v1 | 6.5 | **Rejected**: range redrawn as a front-control model (original has a raised back control panel) — would morph between START/END; frame zoomed out |
| 01C-end-v2 | 6.5 | Accepted → `01C-end.png` (correct back-panel range pulled into aisle; registration residual 18 because return zoomed — workers only transferred). Limit: faint wall tone step at far left |
| 01C-start-v1 | 6.5 | Accepted → `01C-start.png` (gripping installed range; range inside solid mask comes from return, same back-panel model) |
| 01D-end-v1 | 6.5 | Accepted → `01D-end.png` (lead carries lamp toward doorway; globes added via contact region) |
| 01D-start-v1 | 6.5 | Accepted → `01D-start.png` on lamp-removed plate with return lamp (single lamp). Limit: START lamp 3 globes vs END 2; neither matches original lamp exactly |
| 01B-take-v1 | 3.75 | **Partial**: microwave morphs (black box/flip) frames ~9–30; frames 38–72 usable as trim fallback |
| 01C-take-v1 | 3.75 | **Lead pass**: range pulled out rigidly, camera stable |
| 01D-take-v1 | 3.75 | **Fail**: worker walks away from the lamp and back; lamp not carried continuously |
| 01B-take-v2 | 3.75 | **Lead pass**: microwave stays one rigid appliance (tilts as it comes off the bracket, no morph); lowered and carried back |
| 01D-take-v2 | 3.75 | **Lead pass**: hands stay on the lamp pole; small lift/step. On side-by-side re-inspection v1 motion was similar (stride reads as wandering at tile scale); v2 preferred |

## T1 closeout (lead)

All T1 takes produced: 01A local hold on cropped original; 01B v2, 01C v1, 01D v2, 02A v1, 02B v1; 03A pilot v2 (earlier). Generation disabled; awaiting Stefan review.

**User decision 2026-10-10:** shot 01 accepted; T1 closed ("Accept shot 01, commit, approve T2 no sound").
