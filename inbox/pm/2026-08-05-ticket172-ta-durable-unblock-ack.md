---
id: inbox-pm-2026-08-05-ticket172-ta-durable-ack
agent: pm
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql-releases/releases/tag/v0.1.3
  - inbox/ta/2026-08-05-ticket172-mcp-v013-drop-host-proxy.md
---

# #172 TA durable Host-200 ACK · git pin drift

- TA #503: host-proxy dropped; Service initialize Host `nl2sql-mcp:8800` → 200; live sha `3acba222…`.
- Verified: nl2sql-releases v0.1.3 asset sha matches live (publish #30970782274 overwrote earlier direct-upload `11609ec…`).
- Git overlay still pins `11609ec…` (PR #32) — needs nl2sql re-pin PR to `3acba222…` for git↔live parity (not a live blocker).
