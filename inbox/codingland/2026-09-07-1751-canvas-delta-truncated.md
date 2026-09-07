---
id: inbox-codingland-1751-canvas-delta-truncated
agent: codingland
ticket_id: 1751
updated: 2026-09-07
status: inbox
sources:
  - ticket:1751
  - wiki/Engineering/AI-Native-Engineering/Smell-Agglomeration-Module-Split.md
  - https://github.com/anthropics/claude-code/issues/55701
---

# codingland #1751 — canvas delta truncated consistency

- Smell: `applyWorkspaceDelta` sliced upsert-only without `truncated` while `pushDelta` capped + flagged — Canvas DOM vs uncapped `fullSnapshot` diverged.
- Fix: EH-free `buildCanvasViewDelta` (zoom + `MAX_CANVAS_NODES` + `truncated`); `applyWorkspaceDelta` → `mergeWorkspaceDelta` then `pushDelta`.
- Soft-coord: #1750 RunnerTape/`workspaceGraphMerge` landed first; #15 merge kept both (tip `6baedd3`).
- Follow-up: #15 conflict resolve dropped `extension/package.json` `ci` — restore in PR #16 (AA `clean_code` needs it).
