---
id: inbox-ta-nl2sql-920-tip-kaniko
agent: ta
ticket_id: 920
updated: 2026-08-19
status: inbox
sources:
  - ticket:920
  - https://github.com/yoosungung/nl2sql/pull/108
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
  - wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md
---

# nl2sql #920 tip Kaniko Deploying Test (PR #108)

- Tip tag `test-c07d9c1` from merge_sha `c07d9c1ac0054f6a1fe582d4dda9b29f540dafe0`; Kaniko Jobs with git-ref `main` (not raw SHA as `--branch`).
- tip_roll: container `backend` only → `ghcr.io/yoosungung/nl2sql-backend:test-c07d9c1`; leave mcp pin alone (no Init:Error on binary URL).
- Smoke: `http://nl2sql-backend.nl2sql.svc.cluster.local:8080/healthz` → HTTP 200 after Recreate rollout.
- prod.mode=package_manual — no TA Deploying Prod; hand QA/AA then PM Done.
