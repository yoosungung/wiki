---
id: inbox-pm-ticket310-spend-tokens-100m
agent: pm
ticket_id: 310
updated: 2026-08-11
status: inbox
sources:
  - ticket:310
  - https://github.com/yoosungung/sw-factory/pull/6
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
tags: ["spend-alert", "SPEND_TOKENS_PER_CLIENT", "threshold"]
---

# Eric: SPEND_TOKENS_PER_CLIENT 20M → 100M (#310)

- Human decision on spend-alert #310: raise per-client tokens from 20M to 100M.
- Effective threshold = len(clients)×100M (5 clients → 500M).
- Manifest/default live in sw-factory PR #6; cluster CronJob apply still required after merge.
