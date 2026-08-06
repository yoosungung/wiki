---
id: inbox-qa-ticket262-agent-smoke-40k
agent: qa
ticket_id: 262
updated: 2026-08-06
status: inbox
sources:
  - ticket:262
  - inbox/qa/2026-08-06-ticket262-agent-smoke-32k.md
  - inbox/ta/2026-08-06-ticket262-sglang-context-40k.md
---

# #262 QA agent smoke after SGLang 40k

- Live: `max_model_len=40960`, `max_total_num_tokens=69492`, sglang 2/2 Ready (`--context-length 40960` + `fp8_e4m3`).
- Experiment `ticket262-agent-smoke-40k-20260806-082749` id `019fd62f-94fd-7404-8b0b-dbe8b1b66f4f` — pass_rate **0.0** (warehouse_sql null; EX soft).
- Gate: smoke window **no** 32768/40960 BadRequest overflow (32k-era ~33526 request cleared). SSE completed with final assistant text (no flood).
- OpikTracer: concurrent LangGraph traces `019fd62f-9573-…` / `019fd62f-9571-…` tags `nl2sql`/`deepagents`.
- Browser e2e: Playwright Chromium CDN `ENETUNREACH` (IPv6) — env blocker; config uses local Vite webServer not live ingress.
