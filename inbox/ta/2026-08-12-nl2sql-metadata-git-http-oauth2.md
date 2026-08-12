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

# nl2sql metadata ↔ git-http: oauth2 username mismatch

- Live test CM remotes can point at `http://git-http-server.git.svc:80/git/nl2sql-metadata.git` (no URL creds).
- Secret tokens `METADATA_GIT_PUSH_TOKEN` / `MCP_GIT_PULL_TOKEN` match test default `gitpassword`.
- App code hardcodes basic-auth user `oauth2` (GitLab deploy-token convention); git-http htpasswd only has user `git` → `oauth2:gitpassword` returns HTTP 401.
- PVC origin with URL-embedded `git:…` works for manual fetch/push; mcp `ensure_origin` overwrites that URL from CM on bootstrap — do not restart with remotes+tokens until htpasswd has `oauth2` or product username is `git`.
- Bare repo needed both `refs/heads/master` and `refs/heads/main` when `METADATA_GIT_BRANCH=main`.
