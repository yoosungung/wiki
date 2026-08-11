---
id: inbox-ta-ticket391-prod-f9622ab-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #391 AC3 fail on prod-f9622ab tip

- Live tip `ghcr.io/yoosungung/nl2sql-backend:prod-f9622ab` (merge `f9622ab` / PR #51 #444) used for Deploying Test AC3 per Eric Ops unlock (do not use obsolete `test-902ccf2`).
- Annotation drift cleared: `nl2sql.io/image-tag=prod-f9622ab`, merge-sha=`f9622abdac97569cc5121793e4d8cfda49c1d366`.
- MCP lacked `MCP_POSTGRES_URL` (connectionRef env); injected for warehouse readiness before smoke.
- AC3 `spider2-opik run --task agent --instance-ids local008,local022` experiment `ticket391-agent-smoke-prod-f9622ab-20260811-011730` id `019fee65-6e9b-7414-aa76-01718ef6b9ff` → pass_rate **0.0**, empty SQL **2**.
- Root: analyst returns `warehouse_sql: null` (no SSE usable sql); invents `players_stats`/`table_1`; empty `task` kwargs `{}` retries precede filled analyst call. No context BadRequest/overflow in window.
