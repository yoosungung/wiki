---
id: inbox-ta-ticket-1322-deploying-test
agent: ta
ticket_id: 1322
updated: 2026-08-26
status: inbox
sources:
  - ticket:1322
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
  - wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md
  - https://github.com/yoosungung/nl2sql/pull/127
---

# #1322 Deploying Test (Kaniko tip)

- Tip AC2/AC3 already on metadata PVC (`b8af0d92…`); product tip rolled to `test-d7109d6` (merge `d7109d6`).
- Actions `environment=` → HTTP 422; used Kaniko Job `nl2sql-kaniko-backend-test-d7109d6` backend-only; mcp left on `test-e217d63`.
- Smoke: `/api/ready` 200 ready; status → QA for @qa/@aa.
