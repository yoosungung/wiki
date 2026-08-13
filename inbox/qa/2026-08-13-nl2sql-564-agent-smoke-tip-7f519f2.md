---
id: inbox-qa-nl2sql-564-agent-smoke-tip-7f519f2
agent: qa
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - tip:test-7f519f2
  - experiment:564-agent-smoke-20260813T031336Z
---

# #564 agent smoke tip test-7f519f2

- Tip `test-7f519f2` (merge_sha `7f519f2…` / nl2sql#77): AC2 `spider2-opik … local008,local022` → empty_sql=0 · pass_rate=0.5.
- local008 pass after career SUM analyst fix; local022 still result mismatch (incomplete player SELECT) — residual, not AC2 blocker.
- Opik LangGraph traces tagged `nl2sql`/`deepagents`; CM model `openai:gpt-5.6-luna`.
- Prior tip `test-500a8c6` had pass_rate=0 (both mismatch); do not reuse that evidence for this tip.
