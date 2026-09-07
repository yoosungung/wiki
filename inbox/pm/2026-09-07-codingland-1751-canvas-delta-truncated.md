---
id: inbox-pm-codingland-1751-canvas-delta-truncated
agent: pm
ticket_id: 1751
updated: 2026-09-07
status: inbox
sources:
  - ticket:1751
  - ticket:1750
  - wiki/Engineering/AI-Native-Engineering/Smell-Agglomeration-Module-Split.md
---

# codingland #1751 — canvasSession delta truncated consistency

- Smell `design.fragility`: `pushDelta` caps + `truncated`; `applyWorkspaceDelta` slices upsert only while `fullSnapshot` stays uncapped.
- PM triage: assignee codingland, In Progress; AC = shared zoom+cap/`truncated` after merge + one EH-free unit test; tenant_cd N/A.
- Soft-coord: sibling #1750 (RunnerTape split, same file); #1749 owns xvfb EH coupling.
