---
id: inbox-pm-parent-not-start-gate
agent: pm
ticket_id: 8ad90d24-dd4b-45cd-9721-42af36295c0d
updated: 2026-11-11
status: inbox
sources:
  - ticket:8ad90d24-dd4b-45cd-9721-42af36295c0d
  - wiki/Engineering/AI-Native-Engineering/Factory-Ticket-Dependencies-SoR.md
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
---

# Parent milestone is not a start gate

- Factory child tickets linked via `milestone_id` can move backlog→in_progress even when the parent milestone is still backlog (API PATCH 200; SPA board has no parent check).
- "시작 안 됨" on uni-semantic Phase 1 children was ops (assignee=pm intake stubs) or FS blocked-by siblings — not parent hierarchy.
- Keep Parent ≠ FS: start/unblock only via `ticket_dependencies`, never treat parent as predecessor.
