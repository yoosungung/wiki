---
id: inbox-aa-564-aa-security-pass-tip-7f519f2
agent: aa
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - https://github.com/yoosungung/nl2sql/pull/77
---

# #564 aa:security pass on tip test-7f519f2

- Tip `test-7f519f2` (merge_sha `7f519f23184071c098ee50ded2b8a2713fba978b` · nl2sql#77) Ready 1/1; prior tip `test-500a8c6` pass superseded.
- `.factory/quality.yaml` has no `security:` command — manual gate (NF residual).
- #77 delta: MCP search diversity + analyst career-SUM only — no authz/secret/deploy surface.
- CM: `NL2SQL_MODEL=openai:gpt-5.6-luna`, `OPENAI_API_BASE` absent, remotes credential-less in-cluster git-http, `*_GIT_HTTP_USERNAME=git`.
