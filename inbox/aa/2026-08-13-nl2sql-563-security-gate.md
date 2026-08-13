---
id: inbox-aa-nl2sql-563-security-gate
agent: aa
ticket_id: 563
updated: 2026-08-13
status: inbox
sources:
  - ticket:563
  - https://github.com/yoosungung/nl2sql/pull/71
  - https://kubernetes.io/docs/concepts/configuration/secret/
---

# nl2sql #563 security gate (tip d28fadc)

- Tenant `.factory/quality.yaml` has **no `security:` command** (factory example stub exists; gate ran as manual code+CM review).
- PR #71: HTTP basic username configurable (`METADATA_GIT_HTTP_USERNAME` / `MCP_GIT_HTTP_USERNAME`, default `oauth2`); tokens stay in Secret env keys; overlay remotes are credential-less in-cluster URLs + username=`git`.
- Live CM (read): both remotes = `http://git-http-server.git.svc:80/git/nl2sql-metadata.git` (no URL-embedded creds); both `*_GIT_HTTP_USERNAME=git`.
- Tip images `*:test-d28fadc` Ready; unit `test_push_uses_configurable_http_username` pass.
- Residual NF: add real `security:` command to nl2sql quality.yaml (SAST/policy), not a stub.
