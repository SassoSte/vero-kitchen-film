# Vero kitchen film — continuation contract

Read `HANDOFF.md` first, then `mega-prompt.md`, `docs/SOURCE-REGISTER.md` and the ordered
`docs/BACKLOG.md`. `outputs/stills-gallery.html` / `docs/asset-catalog.json` identify
assets and their status; version number alone is not approval.

Production is PAUSED by the user as of 2026-10-09. Do not generate, quote/upload through
paid job flows, buy, schedule or resume automatically. Explicit user resumption and
sufficient approved task budget are required before paid execution. Current approved
ceiling is 200 credits, recorded task cost 198.25. Proposed 205 cap is NOT approved.
`tools/run_image_job.py` contains a pre-quote pause guard; do not bypass it.

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
