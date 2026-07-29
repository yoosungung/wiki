---
id: inbox-qa-spider2-quality-gate-intake
agent: qa
ticket_id: 32
updated: 2026-07-29
status: inbox
sources:
  - ticket:32
  - wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md
  - https://github.com/xlang-ai/Spider2/tree/main/spider2-lite/evaluation_suite
---

# Spider2-Lite local* → nl2sql 품질 게이트 (intake)

- 채점 정본은 SQL 문자열 일치가 아니라 **exec_result**(예측 SQL 실행 결과 ↔ gold CSV).
- 이 repo `spider2-eval`은 PG 적재·Opik Dataset `spider2-lite-local-exec`(local* 135)·`--task gold-sql` 스모크까지 있음. `--task agent`는 미배선(`tasks.py`).
- 품질 테스트 "준비"의 최소 완료선: 스모크 instance set 문서화 + preflight(check/gold-sql) 재현 + agent 배선 AC. UI Playwright(#31)와 축이 다름.
