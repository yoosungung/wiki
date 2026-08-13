---
id: inbox-pm-590-mcp-incident-closeout
agent: pm
ticket_id: 590
updated: 2026-08-13
status: inbox
sources:
  - ticket:590
  - https://github.com/yoosungung/nl2sql/pull/73
  - https://github.com/yoosungung/nl2sql/pull/74
---

# nl2sql-mcp Init:Error closeout (#590)

- Tip-roll must not rewrite mcp-binary init URL to `test-*` — `publish-releases` rejects those tags → Init curl 404 / ProgressDeadlineExceeded.
- RWO PVC `nl2sql-mcp-metadata` requires Deployment strategy `Recreate` (RollingUpdate dual-mount fails).
- Published mcp `v0.1.3` ignores `MCP_GIT_HTTP_USERNAME`; credential-less remote + token alone can libgit2 Http(34). Temporary fix: Secret overrides remotes with basic-auth URL; long-term: username-aware pin (#563).
- Incident Done evidence: Ready 1/1, `/health=200`, `/ready` metadata ok; PR#73 guardrail + PR#74 Recreate/docs merged. tenant_cd N/A (no deploy.yml path for this incident).
