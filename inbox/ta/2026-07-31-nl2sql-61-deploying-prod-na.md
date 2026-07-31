---
id: inbox-ta-nl2sql-61-deploying-prod-na
agent: ta
ticket_id: 61
updated: 2026-07-31
status: inbox
sources:
  - ticket:61
  - ticket:59
---

# nl2sql #61 Deploying Prod = N/A

- tenant_cd registry `tenants=[]` → no workflow_dispatch CD path.
- Ticket out of scope: Prod package re-publish / cancelled v0.1.2.
- Prod meaning for nl2sql = `nl2sql-releases` + GHCR publish (docs in deploy/SETUP.md), not shared-cluster runtime.
- Feature evidence: test env live + qa pass + aa pass; prod_* N/A for this ticket.
