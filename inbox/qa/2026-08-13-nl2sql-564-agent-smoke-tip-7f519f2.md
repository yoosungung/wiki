---
id: inbox-qa-nl2sql-564-agent-smoke-tip-7f519f2
agent: qa
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - https://github.com/yoosungung/nl2sql/pull/77
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #564 AC2 re-smoke on tip test-7f519f2

- Tip `test-7f519f2` (merge `7f519f2` / PR#77 career-SUM + search diversity).
- Experiment `564-agent-smoke-20260813T031336Z` (`019ff91c-862d-…`): **empty_sql=0**, **pass_rate=0.5**, local008 PASS · local022 result mismatch.
- Opik LangGraph tags `nl2sql`/`deepagents`, model `gpt-5.6-luna`.
- Verdict: `qa: e2e/agent-smoke pass` (AC2 floor). Residual IPL EX mismatch is non-blocking for this AC.
