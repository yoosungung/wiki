---
id: inbox-qa-2026-08-10-ticket444-qa-blocked-not-deployed
agent: qa
ticket_id: 444
updated: 2026-08-10
status: inbox
sources:
  - ticket:444
  - https://github.com/yoosungung/nl2sql/pull/51
  - inbox/nl2sql/2026-08-10-describe-ondemand-tools.md
---

# nl2sql #444 QA blocked — #444 not on e2e-test

- synced: repo_id=nl2sql sha=902ccf2(main)/8c5171a(PR#51) path=/tmp/tenant-repos/nl2sql
- Live test image: `ghcr.io/yoosungung/nl2sql-backend:test-902ccf2` — ANALYST_TOOLS on main = search_tables, describe_table, execute_select_query only (no get_column_values/describe_columns).
- PR #51 OPEN (not merged) → Deploying Test for #444 not done; cannot verify Eric e2e-test tool registration/call sample on live.
- UI e2e (quality.yaml): 3 passed shell-nav/chat-shell/metadata-list (~1.5s); does not assert agent tools.
- AA security-review: PASS (conditional; F2 describe_columns cap follow-up).
- Next: merge #51 → TA Deploying Test → re-QA live tool list + call sample.
