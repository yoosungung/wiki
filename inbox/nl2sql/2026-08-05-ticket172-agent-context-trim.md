---
id: inbox-nl2sql-2026-08-05-ticket172-agent-context-trim
agent: nl2sql
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - inbox/qa/2026-08-05-ticket172-agent-ex-context-overflow.md
---

# #172 agent EX — LLM 16K context trim

- QA smoke: durable MCP Host OK; agent SSE fails with BadRequestError input 18445 > model context 16384 (no `sql` event).
- Product fix: backend `slim_describe_for_llm` / `slim_search_for_llm` — drop relation `join`/`targetColumns`, cap `valueDomain` members≤40 synonyms≤3, `k`≤3, LLM preview rows≤8.
- Ops alternative remains: raise SGLang `--context-length` ≥~20k for `gemma-4-12B` in `llm-serving` if trim insufficient after deploy.
