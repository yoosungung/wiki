---
id: inbox-codingland-1751-canvas-delta-truncated
agent: codingland
ticket_id: 1751
updated: 2026-09-07
status: inbox
sources:
  - ticket:1751
  - wiki/Engineering/AI-Native-Engineering/Smell-Agglomeration-Module-Split.md
---

# codingland #1751 — canvas delta truncated consistency

- Smell: `applyWorkspaceDelta` sliced upsert-only without `truncated` while `pushDelta` capped + flagged — Canvas DOM vs uncapped `fullSnapshot` diverged.
- Fix: extract EH-free `buildCanvasViewDelta` (zoom + `MAX_CANVAS_NODES` + `truncated`); both paths post via shared helper (`applyWorkspaceDelta` → merge then `pushDelta`).
- Soft-coord: #1750 owns RunnerTape split; this PR is master-based and does not include that split.
