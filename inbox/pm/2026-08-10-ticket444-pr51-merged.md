---
id: inbox-pm-ticket444-pr51-merged
agent: pm
ticket_id: 444
updated: 2026-08-10
status: inbox
sources:
  - ticket:444
  - https://github.com/yoosungung/nl2sql/pull/51
---

# #444 PR #51 merged → Deploying Test

- merge_sha `f9622abdac97569cc5121793e4d8cfda49c1d366` (squash/merge of on-demand describe tools + AA F2 `DESCRIBE_COLUMNS_REQUEST_MAX=8`).
- CI green: backend, mcp-clippy, mcp-test, mcp.
- Next: TA tenant_cd environment=test image_tag=`test-f9622ab` (or merge_sha policy), then QA live tool-list Trace.
