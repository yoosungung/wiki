---
id: inbox-nl2sql-ticket391-ac3-schema-hint-trim
agent: nl2sql
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - ticket:391#1181
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #391 AC3: schema hint + describe trim

- After Command/ToolMessage unwrap (#41), AC3 still failed: local008 BadRequest input 44254>40960; local022 non-empty SQL but baseball on IPL question.
- Opik dataset items already have `schema` (pg lowercased db). Agent task must prefix `[Spider2 schema: …]` into chat — question text alone is domain-ambiguous.
- Describe LLM trim needs column/relation/valueDomain caps under fixed `max_model_len=40960` (non-goal: do not retune serving context).
