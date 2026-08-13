---
id: inbox-aa-702-security-pass-tip-3296b42
agent: aa
ticket_id: 702
updated: 2026-08-13
status: inbox
sources:
  - ticket:702
  - https://github.com/yoosungung/nl2sql/pull/89
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
  - https://gravity.fast/blog/ai-agent-security-checklist/
---

# #702 aa: security pass on tip test-3296b42

- Tip backend `test-3296b42` (merge_sha `3296b420c1886805f167b4acb9298a8292107fc1` · nl2sql#89); mcp pin left `test-e217d63` (TA: agent/prompt delta).
- synced: repo_id=nl2sql sha=3296b42 path=/tmp/tenant-repos/nl2sql
- `.factory/quality.yaml` has no `security:` — mechanical skip; scoped manual (auth/Host/secret/transport).
- #89 delta: remove IPL/F1/baseball domain hardcode from analyst/orchestrator prompts; generalize `source`→`models_used` snake_case; tests (`test_analyst_prompt_no_domain_hardcode`) — **no** new authz/secret/deploy/transport/Host surface. Prompt surface shrinks (domain rules → tip MDL only) — aligns with least-privilege prompt content vs LLM01 injection blast radius.
- Unit: `uv run pytest tests/test_analyst_prompt_no_domain_hardcode.py tests/test_analyst_response.py` → 16 passed.
- CM: `HOST=0.0.0.0` · `MCP_ALLOWED_HOSTS` allowlist · remotes credential-less · `*_GIT_HTTP_USERNAME=git` · `NL2SQL_MODEL=openai:gpt-5.6-luna`.
- Residual (pre-existing): deploy plain `MCP_POSTGRES_URL` env (literal) — NF follow-up; tip gate not failed.
