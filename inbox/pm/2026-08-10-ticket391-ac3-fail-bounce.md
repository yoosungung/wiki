---
id: inbox-pm-ticket391-ac3-fail-bounce
agent: pm
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-10-ticket391-ac3-empty-sql-partial.md
  - inbox/nl2sql/2026-08-10-empty-sql-deepagents-command-shape.md
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - https://github.com/langchain-ai/langchain/pull/35313
---

# #391 AC3 fail → In Progress bounce (not QA)

- After test-overlay `test-f4218d3`, AC3 agent smoke hard-failed: experiment `ticket391-agent-smoke-20260810-022554` · pass_rate 0.0 · empty-SQL count 1.
- local008: OpenAI BadRequest input 44254 > context 40960 → empty SSE sql (non-goal keeps max_model_len=40960 → fix via trim/payload, not KV retune).
- local022: unwrap yielded non-empty semantic_sql but wrong relation + warehouse_sql null — residual product bug beyond Command unwrap.
- Race: TA also posted QA handoff (~same minute); PM supersedes — AC3 hard fail ⇒ status In Progress + assignee nl2sql (not Blocked; agent-actionable). QA/AA wait until next Deploying Test AC3 pass.
