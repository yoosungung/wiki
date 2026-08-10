---
id: inbox-aa-ticket415-security-pass
agent: aa
ticket_id: 415
updated: 2026-08-10
status: inbox
sources:
  - ticket:415
  - https://github.com/yoosungung/nl2sql/pull/46
  - merge:9ac4c821b0f64bf3021366bee22269a0d81e8a50
  - synced:nl2sql@bede626
  - wiki/inbox/aa/2026-08-10-nl2sql-quality-yaml-security-missing.md
---

# #415 security gate (manual delta) — pass

- Tenant `.factory/quality.yaml` still has **no `security:`** command; mechanical SAST skipped (same gap as #391). Gate = manual PR #46 delta review.
- Delta scope: `chat.py` `_error_summary_from_output` / `_tool_result_payload` + ARCHITECTURE §5.1 + DESIGN + unit tests. No auth/endpoint/secret changes.
- Residual: MCP `error.message` / `isError` content is forwarded to authenticated SSE as `{code,message}` — intentional observability; no new privilege path.
- Evidence: `uv run pytest tests/test_chat.py::test_chat_tool_result_ok_false_on_mcp_error tests/test_chat_sse_helpers.py -q` → 16 passed on synced `bede626` (merge `9ac4c82` ancestor).
