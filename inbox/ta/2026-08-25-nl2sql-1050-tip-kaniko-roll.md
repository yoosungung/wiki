---
id: inbox-ta-nl2sql-1050-tip-kaniko-roll
agent: ta
ticket_id: 1050
updated: 2026-08-25
status: inbox
sources:
  - ticket:1050
  - https://github.com/yoosungung/nl2sql
---

# nl2sql #1050 tip Kaniko + backend tip_roll

- Gate for NF #1050 Done: product tip image SHA **>** merge `53a45e1` (PR #115), not metadata git head.
- TA SA (`cursor-agent-test-ns-write`) can create/delete Jobs + patch Deployments in `nl2sql`; run `./deploy/scripts/build-tip-images-kaniko.sh test-<short> main` from synced tenant checkout.
- `tip_roll`: set **backend only** to `ghcr.io/yoosungung/nl2sql-backend:test-<short>`; do not rewrite mcp Deployment to `test-*` (verify.md / Init:Error risk).
- Evidence 2026-08-25: built `test-48e1795` (main includes `53a45e1`) · Jobs Complete · backend rolled · `/api/ready` 200 · mcp left on prior tip pin.
