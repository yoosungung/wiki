---
id: inbox-pm-ticket-fs-deps-options
agent: pm
ticket_id: dc1a8800-5609-47b1-b48f-1716695edc96
updated: 2026-09-30
status: inbox
sources:
  - ticket:dc1a8800-5609-47b1-b48f-1716695edc96
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
---

# sw-factory FS 선행 갭 (intake)

- 현재 FS SoR: description `<!-- blocked-by:uuid -->` + MCP `set_blocked_by` (A9). 1급 테이블/SPA UI/자동 unblock 없음.
- blocker `done` 시 후속 해제·전용 `agent_event_log` 이벤트가 없음 — 티켓 옵션 A(1급)+B(soft+Worker scan)+C(UI only).
- Parent는 `milestone_id`; FS와 혼동 금지 (canonical wiki 동일).
