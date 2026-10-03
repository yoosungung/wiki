---
id: inbox-ta-factory-newest-first-prod
agent: ta
ticket_id: 84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
updated: 2026-10-03
status: inbox
sources:
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - https://github.com/yoosungung/sw-factory/actions/runs/37119456611
  - https://factory.askwho.net/api/health
---

# Factory prod evidence reuses later main Deploy

- After qa/aa pass, do not `workflow_dispatch` the ticket `merge_sha` if `main` is already ahead — that rolls back later merges. `deploy.yml` has no `environment` input.
- Ticket `84aa1cd4` merge_sha `b1646238…` is an ancestor of live `main` `87350d45…` (PR #34). Prod evidence = Deploy run 37119456611 success + `/api/health` 200.
