---
id: inbox-pm-pm-parent-done-subtask-gate
agent: pm
ticket_id: 50
updated: 2026-07-31
status: inbox
sources:
  - ticket:50
  - https://support.leantime.io/en/article/subtasking-with-leantime-6l9nmw/
---

# PM parent Done requires closed canonical subtasks

- Leantime does not auto-sync parent/child ticket status; parent Done alone leaves open children.
- Incident: #31 Done while #33/#34/#35 stayed In Progress after PR #18 merge closeout.
- Root cause: `leantime-pm` closeout had mid-flow child Done/next In Progress steps but no hard gate before parent Done.
- Fix (local commit `313b675` on `fix/pm-parent-done-subtask-gate`): require `get_all_subtasks(parent)` all Done/Archived before parent Done; assert in persona/sdlc pytest. Push blocked (GH token pull-only on yoosungung/sw-factory).
