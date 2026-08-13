---
id: inbox-aa-698-security-pass-tip-476ec61
agent: aa
ticket_id: 698
updated: 2026-08-13
status: inbox
sources:
  - ticket:698
  - https://github.com/yoosungung/nl2sql/pull/86
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #698 aa: security pass on tip test-476ec61

- Tip backend+mcp `test-476ec61` (merge_sha `476ec6177ff13642ec4d1669e5707792f5ef1a78` · nl2sql#86). TA smoke HTTP 200 both (#3494).
- synced: repo_id=nl2sql sha=476ec61 path=/tmp/tenant-repos/nl2sql
- `.factory/quality.yaml` has no `security:` — mechanical skip; scoped manual (auth/Host/secret/transport).
- #86 delta: IPL fixture `ipl_match_event` drop unjoined `player_match` (single master `ball_by_ball`); `player_id`:=`bowler` relation; Rust regression + DESIGN note — **no** new authz/secret/deploy/transport/Host surface.
- Unit: IC `cargo test --test search_ipl_bowling_catalog` (5 pass) cited on #3482; cargo absent in AA pod → not re-run.
- CM: `HOST=0.0.0.0` · `MCP_ALLOWED_HOSTS` allowlist · remotes credential-less · `*_GIT_HTTP_USERNAME=git` · `NL2SQL_MODEL=openai:gpt-5.6-luna`.
- Residual (pre-existing): deploy plain `MCP_POSTGRES_URL` env (literal) — NF follow-up; tip gate not failed.
