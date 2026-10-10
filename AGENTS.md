# Vero kitchen film — continuation contract

Read `HANDOFF.md` first, then `mega-prompt.md`, `docs/SOURCE-REGISTER.md` and the ordered
`docs/BACKLOG.md`. `outputs/stills-gallery.html` / `docs/asset-catalog.json` identify
assets and their status; version number alone is not approval.

Current user instruction: restore photographic third view `apartment-fridge-reconstruction-v11.png`
and keep local3D work archived. User then requested three-view consistency and approved
**303 total credits for ONE view1 continuity correction**, `master-third-view-continuity-v1`,
maximum new job6.5. Authority: `outputs/production/master-third-continuity-authorization.json`.
Match view1 fridge/enclosure to selected view3; preserve north coffee station and view2.
Phone/speaker nook is kitchen-facing WEST wall: visible in view2, hidden from view3's
living-room camera. Do not relocate/duplicate it to force visibility.
No retries, purchases or video batch. Disable generation after this one job.
Use construction-state-plan.json / shotlist.html after finished-reference reconciliation.


Original photos/plans and manufacturer evidence remain separate from generated concepts.
Never modify original source drawings to fit a render. Latest explicit user design
instructions win; all projecting wine towers, posters, above-DW coffee installations
and old single-door fridge decisions are superseded/rejected.

Preserve unrelated edits, original files and historical drafts. Keep job receipts and
asset IDs stable. Rebuild the catalog after adding assets; run `tools/verify_handoff.py`
for documentation integrity. No tests or metrics establish visual/physical correctness.

Use subagents only within explicit user authorization or an applicable existing contract;
no independent spending by delegates. One lead owns the generation queue and budget.

Every commit uses per-invocation harness attribution:
`git -c user.name="Stefan Sassoon (Codex)" commit -m "..."`.
Do not persist that author identity in git config. Stage only relevant paths.
