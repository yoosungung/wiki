---
id: inbox-nl2sql-ticket391-multi-turn-tool-budget
agent: nl2sql
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - ticket:391#1428
---

# #391 AC3: multi-turn tool payload budget

- test-ca70223: overflow 51994/48777 > 40960 after describe 12k + stash fix — accumulation across rounds.
- Caps: DESCRIBE_JSON_CHARS_MAX=2500, SEARCH_JSON_CHARS_MAX=1500, k≤2, valueDomain≤1 col×4 members, MULTI_TURN_TOOL_CHARS_MAX=12000 envelope test.
