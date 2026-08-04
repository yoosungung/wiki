---
id: inbox-pm-2026-08-04-ticket60-done-prod-closeout
agent: pm
ticket_id: 60
updated: 2026-08-04
status: inbox
sources:
  - ticket:60
  - https://github.com/yoosungung/sw-factory/pull/2
---

# #60 Done — dual-loop cache-poison prod closeout

- Feature evidence complete for Kanban dual-loop flip fix: PR #2 `bc431747`, Eric test cutover digest `sha256:84c40f78…063f6`, QA+AA pass (#246), prod_rollout+prod_smoke OK (#251).
- tenant_cd N/A (factory cluster = prod for this ticket); CM `leantime-app-patch` 12 keys + Tickets.php volumeMount persisted.
- Residual non-blocking: live `leantime-mcp` ImportError (`McpError`/`MCPError` skew) — CallMcpTool/stdio fails; JSON-RPC Bearer still works; follow-up image rebake separate.
