---
id: inbox-qa-ticket444-tool-reg-blocker
agent: qa
ticket_id: 444
updated: 2026-08-10
status: inbox
sources:
  - ticket:444
  - https://github.com/yoosungung/nl2sql/pull/51
  - inbox/nl2sql/2026-08-10-describe-ondemand-tools.md
---

# #444 QA: live test missing on-demand describe tools

- Live backend image `test-902ccf2` still has ANALYST_TOOLS = search_tables/describe_table/execute_select_query only.
- PR #51 adds get_column_values + describe_columns; prompt/docstrings align with hasValueDomain slim describe_table (unit 16 passed on PR branch).
- UI Playwright scenarios do not call LLM — cannot satisfy Eric’s Trace ask until Deploying Test rolls PR sha.
- AA security-review on PR: PASS (optional DESCRIBE_COLUMNS_MAX enforce).
