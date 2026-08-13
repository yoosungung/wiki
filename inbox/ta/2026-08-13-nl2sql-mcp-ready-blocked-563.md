---
id: inbox-ta-nl2sql-mcp-ready-blocked-563
agent: ta
ticket_id: 590
updated: 2026-08-13
status: inbox
sources:
  - ticket:590
  - ticket:563
---

# nl2sql-mcp Ready blocked on git-http auth (#563)

- Init 404 cleared: live pin `v0.1.3` + sha `3acba222…1817a` → `fetch-mcp-binary` OK.
- New RS `5657897cbb` mcp Error: metadata bootstrap `too many redirects or authentication replays` (Http 34); `git_pull_token_set=true`; remote credential-less.
- Probe: `git:token` upload-pack 200 · `oauth2:token` 401. CM has `MCP_GIT_HTTP_USERNAME=git` but release binary `v0.1.3` still fails (username path needs #563 image/roll).
- After tip/overlay roll, old Ready `7c4f85758f` scaled down → Deploy Available=0 · svc `/health` down (outage).
- #590 Ready wait: #563 Waiting for Approval (Eric) resume → Deploying Test tip/overlay with username=`git` → TA verify Ready.
