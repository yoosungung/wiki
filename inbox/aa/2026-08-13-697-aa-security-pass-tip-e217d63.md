---
id: inbox-aa-697-security-pass-tip-e217d63
agent: aa
ticket_id: 697
updated: 2026-08-13
status: inbox
sources:
  - ticket:697
  - https://github.com/yoosungung/nl2sql/pull/88
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #697 aa: security pass on tip test-e217d63

- Tip backend+mcp `test-e217d63` (merge_sha `e217d63a681f22489d804e0d58002559657e64af` · nl2sql#88). Live images match TA #3555.
- synced: repo_id=nl2sql sha=e217d63 path=/tmp/tenant-repos/nl2sql
- `.factory/quality.yaml` has no `security:` — mechanical skip; scoped manual (auth/Host/secret/transport).
- #88 delta: DESIGN RCA note + mcp catalog test comment only — **no** new authz/secret/deploy/transport/Host surface.
- Unit: cargo N/A in AA pod; tip tree change is comment-only on existing `ipl_match_event_has_exactly_one_master` test.
- CM: `HOST=0.0.0.0` · `MCP_ALLOWED_HOSTS` allowlist · remotes credential-less · `*_GIT_HTTP_USERNAME=git` · `NL2SQL_MODEL=openai:gpt-5.6-luna`.
- Residual (pre-existing): same CM pattern as #699 — tip gate not failed.
