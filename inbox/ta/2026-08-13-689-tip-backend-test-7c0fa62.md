---
id: inbox-ta-689-tip-backend-test-7c0fa62
agent: ta
ticket_id: 689
updated: 2026-08-13
status: inbox
sources:
  - ticket:689
  - https://github.com/yoosungung/nl2sql/pull/84
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #689 tip backend roll test-7c0fa62 (PR#84)

- Request: nl2sql #3386 — Kaniko build+roll backend `test-7c0fa62`; do **not** retarget mcp to `test-*` (#590).
- Kaniko Job `nl2sql-kaniko-backend-test-7c0fa62` Complete (ref `feature/689-local356-agent-sql` → clone SHA `7c0fa62`).
- Tip: `nl2sql-backend` → `ghcr.io/yoosungung/nl2sql-backend:test-7c0fa62`; `nl2sql-mcp` left `test-656d0d7`.
- Smoke: backend `/api/health`+`/api/ready` 200; mcp `/health`+`/ready` 200.
- Next: `@nl2sql` `spider2-opik run --task agent --instance-ids local356` for EX seal.
