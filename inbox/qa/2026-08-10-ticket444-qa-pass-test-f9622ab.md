---
id: inbox-qa-ticket444-qa-pass-f9622ab
agent: qa
ticket_id: 444
updated: 2026-08-10
status: inbox
sources:
  - ticket:444
  - https://github.com/yoosungung/nl2sql/pull/51
  - inbox/ta/2026-08-10-ticket444-test-f9622ab-deploy.md
---

# #444 QA pass on test-f9622ab

- Live ANALYST_TOOLS includes get_column_values + describe_columns (TA pod-exec + main@f9622ab).
- describe_table slim: hasValueDomain only; call samples via ainvoke OK; pytest 17 passed.
- UI e2e shell-nav/chat-shell/metadata-list: 3 passed (PLAYWRIGHT_CHROMIUM_PATH).
- Live SSE shows task→analyst; nested tool names not in SSE; registration gate satisfied.
- AA security-review PASS on f9622ab.
