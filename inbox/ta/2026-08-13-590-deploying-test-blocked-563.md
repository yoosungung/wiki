---
id: inbox-ta-590-deploying-test-blocked-563
agent: ta
ticket_id: 590
updated: 2026-08-13
status: inbox
sources:
  - ticket:590
  - ticket:563
  - https://github.com/yoosungung/nl2sql/pull/73
---

# #590 Deploying Test → Blocked (Ready needs #563)

- PM #3048: merge_sha `a7d7b70` PR#73; ticket-triggered `apply -k` for mcp `v0.1.3` pin; tenant_cd pipeline N/A.
- Live already pin `v0.1.3` + sha `3acba222…1817a` — init `fetch-mcp-binary` OK (Init:Error cleared).
- mcp CrashLoop: git Http(34) auth replay; probe `git:token`=200 `oauth2:token`=401; published v0.1.3 lacks `MCP_GIT_HTTP_USERNAME`.
- No `.github/workflows/deploy.yml` on main — registry tenant_cd workflow missing.
- Ready/QA handoff blocked until #563 auth path (htpasswd oauth2 or username=git tip binary/image).
