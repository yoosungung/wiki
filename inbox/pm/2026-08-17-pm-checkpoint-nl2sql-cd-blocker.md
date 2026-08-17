---
id: inbox-pm-2026-08-17-pm-checkpoint-nl2sql-cd-blocker
agent: pm
ticket_id: 920
updated: 2026-08-17
status: inbox
sources:
  - ticket:918
  - ticket:920
  - inbox/ta/2026-08-17-nl2sql-920-deploy-yml-missing.md
---

# pm-checkpoint: nl2sql CD contract blocker (918/920)

- Flow scan (IP/Review/DeployTest/QA/DeployProd): empty after TA escalated #920; only Approval misroute candidates #918+#920.
- Both Keep Approval@eric: tenant-cd-registry expects `deploy.yml`+`image_tag`; product main has ci/build-ghcr/publish only — same class human CD contract.
- Silence/ladder: no HC/ARC; TA blocker comments count as silence-reset. Status-board upsert only (edit_comment); actionable add_comment=0.
- Dual-loop Done blocked until test_* after contract fix; do not invent alternate CD.
