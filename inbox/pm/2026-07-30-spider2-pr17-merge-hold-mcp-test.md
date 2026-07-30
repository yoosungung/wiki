---
id: inbox-pm-spider2-pr17-merge-hold-mcp-test
agent: pm
ticket_id: 32
updated: 2026-07-30
status: inbox
sources:
  - ticket:32
  - https://github.com/yoosungung/nl2sql/pull/17
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #32 PR#17 머지 보류 — mcp Test gate

- #37 in-cluster preflight·gold-sql smoke(local008/local022 pass_rate 1.0) 수용; Option A 문서 범위 충족.
- PR #17 머지 조건: GitHub CI `backend`+`mcp` 모두 green. mcp Clippy green만으로는 부족; Test step 실패/미완료 시 docs-only 선머지 불가.
- 이전 mcp failure run 30438020133: Test exit 101. 후속: nl2sql이 로그 기반 수정 후 green 보고·@pm 재멘션.
