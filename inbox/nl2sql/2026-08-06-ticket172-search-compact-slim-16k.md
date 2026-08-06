---
id: inbox-nl2sql-ticket172-search-compact-slim-16k
agent: nl2sql
ticket_id: 172
updated: 2026-08-06
status: inbox
sources:
  - ticket:172
  - wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md
  - wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md
---

# #172 search LLM slim vs describe (local022 16K)

- After FS-tool exclude (PR #37), local022 still overflowed 16384 (requested 16676) with only `task:analyst` + one `search_tables`.
- Root cause: `slim_search_for_llm` shared describe-grade summaries including `valueDomain` members — search should stay candidate-compact; enums belong in `describe_table`.
- Fix: search drops `valueDomain`/`expression`/relation fluff; caps columns≤20, relations≤8; describe trim unchanged.
