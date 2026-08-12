---
id: inbox-nl2sql-metadata-git-http-user
agent: nl2sql
ticket_id: 563
updated: 2026-08-12
status: inbox
sources:
  - ticket:563
  - https://github.com/yoosungung/nl2sql/pull/72
  - inbox/ta/2026-08-12-nl2sql-metadata-git-http-oauth2.md
---

# metadata git HTTP username env

- App previously hardcoded basic-auth user `oauth2` (GitLab deploy-token). In-cluster `git-http` htpasswd only has `git` → `oauth2:token` = HTTP 401.
- Fix: `METADATA_GIT_HTTP_USER` / `MCP_GIT_HTTP_USER` (default `oauth2`). Test overlay sets both to `git` and fills remotes to `http://git-http-server.git.svc:80/git/nl2sql-metadata.git`.
- Do not restart pods until image/config with username=`git` is live — mcp `ensure_origin` would overwrite PVC URL-creds then fetch as oauth2 and CrashLoop.
