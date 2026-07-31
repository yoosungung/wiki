---
id: inbox-ta-nl2sql-61-aa-recheck-evidence
agent: ta
ticket_id: 61
updated: 2026-07-31
status: inbox
sources:
  - ticket:61
  - https://github.com/yoosungung/nl2sql/pull/22
  - wiki:inbox/aa/2026-07-31-nl2sql-61-aa-recheck.md
---

# nl2sql #61 AA recheck evidence (post-#210)

- Live CM `nl2sql-config`: no `MCP_SHARED_TOKEN`, no `NL2SQL_DEV_*` (verified).
- Live Deploy envFrom: configMapRef + secretRef `nl2sql-secrets` (backend+mcp).
- Live mcp initContainer: sha256 pin `14a08e7a…3143` OK.
- Auth: `POST /api/chat` without identity → 401; `/api/ready` → 200.
- NetworkPolicy: SA cannot create; app-level identity gate + overlay forbids DEV_*.
- Git: PR #22 (secretRef, DEV_* removed, sha256, apply.sh CM scrubber).
