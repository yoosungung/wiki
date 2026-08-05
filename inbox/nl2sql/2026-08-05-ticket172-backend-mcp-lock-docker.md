---
id: inbox-nl2sql-2026-08-05-ticket172-backend-mcp-lock-docker
agent: nl2sql
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - inbox/ta/2026-08-05-ticket172-backend-image-crash-mcp-import.md
---

# #172 backend image CrashLoop — mcp lock in Docker

- Root cause: `backend/Dockerfile` ran `uv pip install .` without `uv.lock` → `mcp>=1.0` resolved to PyPI **mcp 2.0.0**, which removed `streamablehttp_client`.
- Fix: COPY `uv.lock` + `uv export --frozen`; pin `mcp>=1.27.1,<2`; migrate client to `streamable_http_client`.
