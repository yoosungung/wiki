---
id: inbox-pm-spider2-quality-gate-pm-approval
agent: pm
ticket_id: 32
updated: 2026-07-29
status: inbox
sources:
  - ticket:32
  - wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md
  - https://github.com/xlang-ai/Spider2/tree/main/spider2-lite/evaluation_suite
  - https://github.com/nodal-data/spider2-claude-code
---

# Spider2 품질 게이트 준비 — PM 승인

- 채점 정본은 EX/exec_result(실행 결과↔gold CSV). SQL 문자열 일치 아님 (`wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md`).
- #32 Option A 승인: 스모크 set 문서화 + preflight 재현 + agent 배선 **스펙/AC만**. agent 구현은 후속 티켓.
- 1차 스모크 instance는 **2건**(예: local008, local022). 외부 smoke도 `--limit` 소수(예: 3) 관행. DESIGN에 ~10 확장 경로만 남김.
