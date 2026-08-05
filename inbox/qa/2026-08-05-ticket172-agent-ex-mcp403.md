---
id: inbox-qa-2026-08-05-ticket172-agent-ex-mcp403
agent: qa
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - spider2-eval/DESIGN.md
  - deploy/SETUP.md
---

# #172 agent full EX blocked — MCP 403

- Eric #454: product EX must be `--task agent` (gold-sql is scorer/PG baseline only).
- QA checkout FF to `52782f9`; seeded `SPIDER2_AGENT_BASE_URL` + AUTH_*; `spider2-opik check` OK.
- Smoke `ticket172-agent-smoke-20260805T020332Z` (local008,022): exit 0 · pass_rate 0.0.
- Live SSE: chat reaches tools then `search_tables` → backend log `403 Forbidden` to `http://nl2sql-mcp:8800/mcp`. No `sql` event.
- QA SA cannot exec pods / read `nl2sql-secrets`; cannot self-fix token. MCP auth is Bearer `MCP_SHARED_TOKEN` (401 if mismatch per mcp DESIGN).
- Resume after token align: `uv run spider2-opik run --task agent --experiment-name ticket172-local-full-agent-ex` (no instance-ids = 135) → upload agent report.
