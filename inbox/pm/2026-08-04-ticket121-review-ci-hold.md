---
id: inbox-pm-ticket121-review-ci-hold
agent: pm
ticket_id: 121
updated: 2026-08-04
status: inbox
sources:
  - ticket:121
  - https://github.com/yoosungung/nl2sql/pull/28
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #121 Review: content OK, mcp-duckdb CI hold

- PR #28 wires `quality.yaml` `opik.command` to check + gold-sql smoke (`local008,local022`); AC content-approved.
- Merge blocked only on pending `mcp-duckdb` (repo CI often ~30m on that job); backend/mcp-clippy/mcp-test already pass.
- tenant_cd N/A for this NF yaml change — after merge, Done without Deploying Test/QA/Prod lanes.
