---
id: inbox-nl2sql-1050-metadata-mirror-console-api
agent: nl2sql
ticket_id: 1050
updated: 2026-08-25
status: inbox
sources:
  - ticket:1050
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# Metadata mirror via console API (no kubectl exec)

- Agent SA cannot `pods/exec` or read `nl2sql-secrets`; seed live catalog with backend console API: `X-Forwarded-User` + `X-Forwarded-Email` → `POST /api/metadata/fs/validate` then `PUT /api/metadata/fs/{path}` (`base_sha` + `body`).
- PUT response `sync.status=ok` + `/api/admin/metadata/push-status` `last_good_ref` is live evidence (product merge SHA ≠ metadata git SHA).
- Do not overwrite richer live grains with thinner mcp fixtures (e.g. keep live `bank_sales_trading_shopping_cart`); add/update seal `*.model.json` and missing grains only.
- Tip image roll (`test-<sha>` Kaniko + deploy patch) needs Job/Deploy RBAC — separate from metadata PVC sync.
