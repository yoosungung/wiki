---
id: inbox-nl2sql-ticket118-spider2-real-gate
agent: nl2sql
ticket_id: 118
updated: 2026-08-04
status: inbox
sources:
  - ticket:118
  - ticket:117
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md
  - .factory/quality.yaml
  - https://github.com/xlang-ai/Spider2/tree/main/spider2-lite/evaluation_suite
---

# Spider2 실질 평가 게이트 (#118)

- Adopted #117 Option A: P0 gold-sql weekly → P1 agent path A (chat SSE last `sql`) → P2 ~10 opt-in.
- `quality.yaml` `opik.command` now `check && run --task gold-sql` smoke (`local008,local022`).
- `--task agent` wired via `SPIDER2_AGENT_BASE_URL` + `spider2_eval.agent_chat`; empty SQL on miss (no loop abort).
- Weekly agent step still Should (env-gated); FakeAgent not used for EX quality.
- tenant_cd / Prod CD evidence: N/A.
