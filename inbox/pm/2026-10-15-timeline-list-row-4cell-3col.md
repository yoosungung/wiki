---
id: inbox-pm-timeline-list-row-4cell-3col
agent: pm
ticket_id: 54683314-7fe6-4d5d-8a13-f19985b89505
updated: 2026-10-15
status: inbox
sources:
  - ticket:54683314-7fe6-4d5d-8a13-f19985b89505
  - frontend/src/styles.css
  - frontend/src/pages/ProjectWorkspace.tsx
---

# Factory Timeline row: 4 cells vs `.list-row` 3-col

- Timeline rows render date | issue-key | title | status (4 children) but shared `.list-row` uses `grid-template-columns: 160px 1fr 120px`.
- Effect: key eats `1fr`, title stuck at 120px, status wraps to next line.
- Fix pattern: Timeline-only modifier (e.g. `.list-timeline`) with 4 columns; keep global 3-col for other lists.
