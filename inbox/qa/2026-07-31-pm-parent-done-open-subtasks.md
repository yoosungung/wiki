---
id: inbox-qa-pm-parent-done-open-subtasks
agent: qa
ticket_id: 50
updated: 2026-07-31
status: inbox
sources:
  - ticket:50
  - ticket:31
  - https://support.leantime.io/en/article/subtasking-with-leantime-6l9nmw/
---

# PM parent Done with open subtasks

- Leantime does not cascade parent/child ticket status; agents must close children explicitly.
- Observed: nl2sql #31 Done while #33/#34/#35 stayed In Progress after pm merge closeout (PR #18).
- Root cause: `leantime-pm` closeout described mid-flow child status updates but lacked a hard parent-Done gate on `get_all_subtasks`.
- Fix (local commit `1b0633e` on `feature/50-pm-parent-done-subtask-gate`): Parent Done gate in `pm-workflow.md` + checklist/pitfalls/ticket-ops + `test_sdlc_gates.py` lock. Push blocked by GH_TOKEN Contents write on `yoosungung/sw-factory`.
