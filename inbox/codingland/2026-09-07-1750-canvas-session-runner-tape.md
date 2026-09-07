---
id: inbox-codingland-1750-canvas-session-runner-tape
agent: codingland
ticket_id: 1750
updated: 2026-09-07
status: inbox
sources:
  - ticket:1750
  - wiki/Engineering/AI-Native-Engineering/Smell-Agglomeration-Module-Split.md
  - https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Book%3A_Object-Oriented_Reengineering_Patterns_(Demeyer_Ducasse_and_Nierstrasz)/09%3A_Redistribute_Responsibilities/9.04%3A_Split_Up_God_Class
---

# codingland #1750 — CanvasSession RunnerTape split

- After #1505, remaining god mixed demo IsolatedRunner tape with graph push/delta; split `RunnerTape` (`ensureRunner`/`hotReboot`/timeline) from `CanvasSession` (graph+panel+message).
- EH-free host Jest: `mergeWorkspaceDelta` characterizes empty-seed + incremental merge for `applyWorkspaceDelta` (panel postMessage still session-owned).
- Soft-coord: #1751 owns MAX_CANVAS_NODES truncated on incremental path; this change left that helper untouched.
