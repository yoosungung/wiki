---
id: inbox-nl2sql-spider2-quality-smoke-set
agent: nl2sql
ticket_id: 32
updated: 2026-07-29
status: inbox
sources:
  - ticket:32
  - wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md
  - spider2-eval/DESIGN.md
---

# Spider2 품질 게이트 스모크 set (nl2sql)

- 1차 스모크 instance: `local008`(Baseball), `local022`(IPL) — 상수 `QUALITY_SMOKE_INSTANCE_IDS`.
- 채점 정본은 EX/exec_result(실행 결과↔gold CSV); SQL 문자열 일치 아님.
- Preflight 순서: `spider2-load-pg` → `spider2-opik-upload-exec` → `spider2-opik check` → `gold-sql` + `--instance-ids local008,local022`.
- `--task agent`는 DESIGN §7 AC만 고정; 구현은 후속 티켓.
