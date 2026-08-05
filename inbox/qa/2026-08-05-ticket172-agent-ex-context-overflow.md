---
id: inbox-qa-2026-08-05-ticket172-agent-ex-context-overflow
agent: qa
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md
---

# #172 agent EX blocked — LLM context overflow

- Durable MCP Host path verified: Service initialize Host `nl2sql-mcp:8800` → HTTP **401** (not 403 Host).
- Agent smoke `ticket172-agent-smoke-durable-20260805T084903Z` (local008,022): exit 0 · pass_rate 0.0.
- Live SSE: tools OK (`task:analyst`) then LLM **BadRequestError** — input 18445 > model context 16384; no `sql` event.
- Full 135 deferred until context ≥~20k or MDL/tool payload trim; gold-sql artifacts unchanged.
