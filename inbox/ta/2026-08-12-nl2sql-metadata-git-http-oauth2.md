---
id: inbox-ta-nl2sql-metadata-git-http-oauth2
agent: ta
ticket_id: 563
updated: 2026-08-12
status: inbox
sources:
  - ticket:563
  - https://github.com/yoosungung/nl2sql/pull/71
---

# nl2sql metadata ↔ git-http: prefer configurable HTTP username

- Decision (pm #2149): do not wait on htpasswd `oauth2` alias; align app to username `git`.
- PR #71 adds `METADATA_GIT_HTTP_USERNAME` / `MCP_GIT_HTTP_USERNAME` (default `oauth2`); test overlay sets `git`.
- Live CM remotes + username keys patched; do not restart until new image with code lands (old binaries ignore username env; oauth2 would still 401).
- Bare repo has both `main` and `master` at same tip.
