---
id: inbox-sw-factory-agent-runner-zombie-active-run
agent: sw-factory
ticket_id: 197
updated: 2026-08-05
status: inbox
sources:
  - ticket:197
  - https://cursor.com/docs/sdk/typescript
---

# agent-runner: zombie `active_run` after worker exit

- Symptom: after SDK worker process exit, later `POST /sessions/{id}/prompt` returns 409 `skipped_active_run` / log `session.prompt.skipped` `reason=active_run` permanently for that ticket↔agent mapping.
- Soft budget, pre-lease recycle, and PM @mention do not clear SDK-side busy state.
- Likely split: parent `busyAgents` may clear on promise reject, but Cursor local agent still has an unfinished run → `Agent.resume` + `send` surfaces `already has active run`.
- Recovery direction (ticket #197 draft R1–R5): forget ticket↔agent map on crash/`active_run` fail; on consecutive skips cancel (`run.cancel` / `Agent.cancelRun`) or DELETE session then create new; log `session.recover`.
- Cite L0: `agent-runner/DESIGN.md` (Recovery section still to be written), `ARCHITECTURE.md` §2.3.1.
