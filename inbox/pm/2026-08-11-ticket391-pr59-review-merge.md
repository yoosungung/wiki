---
id: inbox-pm-ticket391-pr59-review-merge
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/59
---

# #391 PR #59 review→merge (decimal + stash emit)

- SoT tip `test-6b63138`: empty-SQL from bare MDL `decimal` + prose stop without SSE sql.
- PR #59: arrow_type decimal/numeric→Decimal128(38,10); `_to_sse` emit stash before done; CI green incl. mcp-test.
- Next: TA tip roll + AC3 local008,local022.
