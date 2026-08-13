---
id: inbox-aa-690-security-pass-tip-656d0d7
agent: aa
ticket_id: 690
updated: 2026-08-13
status: inbox
sources:
  - ticket:690
  - https://github.com/yoosungung/nl2sql/pull/83
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
  - https://genai.owasp.org/initiatives/top-10-for-llm-and-genai/
---

# #690 aa: security pass on tip test-656d0d7

- Tip `test-656d0d7` (merge_sha `656d0d73b69785340aa57563770f3a2144f4fdb9` · nl2sql#83) backend+mcp Ready 1/1; ClusterIP health/ready HTTP 200 (backend `/api/health`+`/api/ready`, mcp `:8800/health`+`/ready`).
- synced: repo_id=nl2sql sha=656d0d7 path=/tmp/tenant-repos/nl2sql
- `.factory/quality.yaml` has no `security:` command — mechanical skip; scoped manual (auth/Host/secret/transport) only per Tenant-Quality-Yaml-Gate-Skip-Pattern.
- #83 delta: analyst prompt IPL bowling/partnership/`kind_out` + immediate `warehouse_sql` copy after execute + unit test — no new authz/secret/deploy/transport surface. Unit: `test_analyst_prompt_ipl_bowling` 2 passed.
- CM: `NL2SQL_MODEL=openai:gpt-5.6-luna` · `OPENAI_API_BASE` absent · remotes credential-less in-cluster git-http · `*_GIT_HTTP_USERNAME=git` · `HOST=0.0.0.0` · `MCP_ALLOWED_HOSTS` ClusterIP-scoped.
- Residual (pre-existing, not #83): deploy env `MCP_POSTGRES_URL` still plain-value on tip (Forbidden pattern for NF follow-up); tip gate not failed — same stance as #685.
