---
id: inbox-aa-685-security-pass-tip-ad563ae
agent: aa
ticket_id: 685
updated: 2026-08-13
status: inbox
sources:
  - ticket:685
  - https://github.com/yoosungung/nl2sql/pull/79
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
  - https://genai.owasp.org/initiatives/top-10-for-llm-and-genai/
---

# #685 aa: security pass on tip test-ad563ae

- Tip `test-ad563ae` (merge_sha `ad563aebf62a7860cd93bab93ada713895087c38` · nl2sql#79) backend+mcp Ready 1/1; health/ready HTTP 200.
- synced: repo_id=nl2sql sha=ad563ae path=/tmp/tenant-repos/nl2sql
- `.factory/quality.yaml` has no `security:` command — mechanical skip; scoped manual (auth/Host/secret/transport) only.
- #79 delta: analyst prompt striker join + unit test + DESIGN note — no new authz/secret/deploy/transport surface. Unit: `test_analyst_prompt_ipl_striker` 2 passed.
- CM: `NL2SQL_MODEL=openai:gpt-5.6-luna` · `OPENAI_API_BASE` absent · remotes credential-less in-cluster git-http · `*_GIT_HTTP_USERNAME=git`.
- Residual (pre-existing, not #79): deploy env `MCP_POSTGRES_URL` embeds DB userinfo — Forbidden pattern for NF follow-up; tip gate not failed (Kaniko tip doc: separate from tip fail).
