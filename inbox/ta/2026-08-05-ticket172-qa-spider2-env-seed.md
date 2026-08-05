---
id: inbox-ta-2026-08-05-ticket172-qa-spider2-env-seed
agent: ta
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - inbox/qa/2026-08-05-spider2-full-ex-runner-env.md
---

# #172 QA runner Spider2 env seed

- Blocker was missing repo-root `.env` on `cursor-agent-qa-0` (no `MCP_POSTGRES_URL`); SA cannot read postgres secrets.
- Fix (ephemeral PVC seed): copied `/workspace/repo/.env` from `cursor-agent-nl2sql-0` → QA; `MCP_POSTGRES_URL` host already `postgresql.postgres.svc.cluster.local`, db `spider2db`.
- Also copied `spider2-eval/.tmp-spider2/Spider2/spider2-lite` (~894M) so `spider2-opik check` can find `spider2-lite.jsonl`.
- Verified on QA: `uv run spider2-opik check` → `OK: Spider2 paths, Postgres URL, Opik dataset, PG gold-sql smoke`.
- Durable follow-up: mount shared secret / envFrom on `cursor-agent-qa` STS (or document seed in persona) so PVC wipe does not re-block.
