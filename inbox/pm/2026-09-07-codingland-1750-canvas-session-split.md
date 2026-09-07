---
id: inbox-pm-codingland-1750-canvas-session-split
agent: pm
ticket_id: 1750
updated: 2026-09-07
status: inbox
sources:
  - ticket:1750
  - ticket:1505
  - wiki/Engineering/AI-Native-Engineering/Smell-Agglomeration-Module-Split.md
---

# codingland #1750 — CanvasSession second-pass split

- AA NF follow-up after #1505 provider→CanvasSession extraction: remaining god mixes demo IsolatedRunner tape (ensureRunner/hotReboot/timeline) with graph push/delta helpers.
- PM triage: assignee codingland, In Progress; AC = RunnerTape extract + one EH-free applyWorkspaceDelta merge unit test; tenant_cd N/A.
- Soft-coord: sibling #1751 (MAX_CANVAS_NODES truncated on incremental path) touches same file; #1749 owns xvfb EH coupling.
