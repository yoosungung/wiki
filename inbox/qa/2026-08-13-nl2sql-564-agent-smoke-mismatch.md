---
id: inbox-qa-nl2sql-564-agent-smoke-mismatch
agent: qa
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - ticket:391
  - ticket:562
  - ticket:563
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# nl2sql #564 agent smoke: empty SQL cleared, EX still mismatch

- On tip `test-d28fadc` + luna (`openai:gpt-5.6-luna`) + metadata git-http remote, `spider2-opik run --task agent --instance-ids local008,local022` returned **non-empty SQL for both** (empty_sql_count=0).
- Opik experiment `564-agent-smoke-20260813T020841Z` (`019ff8e0-ff08-…`): `spider2_exec_match` avg 0 · `pass_rate` 0 · score reason **result mismatch** (not empty SQL / 401).
- Chat SSE with `X-Forwarded-*` still emits usable `event: sql` (AC3 path live); AC2 EX floor remains the product gap vs #391 hard gate.
