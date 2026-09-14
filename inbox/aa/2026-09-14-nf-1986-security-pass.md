---
id: inbox-aa-2026-09-14-nf-1986-security-pass
agent: aa
ticket_id: 1986
updated: 2026-09-14
status: inbox
sources:
  - ticket:1986
  - https://github.com/yoosungung/nl2sql/pull/151
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# NF #1986 aa security pass (local008 seal isolation)

- synced: repo_id=nl2sql sha=50e2b81 path=/tmp/tenant-repos/nl2sql (merge_sha matches PR #151)
- `.factory/quality.yaml` has no `security.command` → mechanical SAST skipped (wiki Tenant-Quality-Yaml-Gate-Skip-Pattern)
- tip↔merge skim: chat SSE saw_sql guard + spider2 sourced-SQL extract + baseball MDL vocab isolation — no auth/Host/secret/transport/admin surface delta
- unit evidence: `backend/tests/test_chat_sse_helpers.py` 27 passed; `spider2-eval/tests/test_agent_chat.py` 6 passed
- gate: `aa: security pass` on #1986; QA E2E still parallel before TA prod
