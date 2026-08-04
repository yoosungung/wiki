---
id: inbox-pm-ticket118-review-hold
agent: pm
ticket_id: 118
updated: 2026-08-04
status: inbox
sources:
  - ticket:118
  - ticket:117
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - https://github.com/yoosungung/nl2sql/pull/27
  - https://github.com/xlang-ai/Spider2/tree/main/spider2-lite/evaluation_suite
---

# #118 PR review hold (Spider2 real gate)

- PR #27 matches #118 AC Option A: P0 `quality.yaml` check+gold-sql smoke; P1 `--task agent` path A (`POST /api/chat` last `sql`); P2 OoS.
- Unit evidence claimed: spider2-eval pytest 10 passed + `test_quality_yaml_opik_gate.py`. Live Opik pass_rate not verified in pm env.
- Merge blocked: (1) Eric comment on #118 requires #117 complete first; #117 still Waiting for Approval; (2) CI `mcp-duckdb` still pending on PR #27 (backend/mcp-test/clippy green).
- tenant_cd / Prod CD: N/A (quality gate wiring).
