---
id: inbox-qa-ticket60-kanban-dual-loop-pass
agent: qa
ticket_id: 60
updated: 2026-08-04
status: inbox
sources:
  - ticket:60
  - https://github.com/yoosungung/sw-factory/pull/2
---

# #60 QA — Kanban dual-loop stable after sessionless poison

- AC: after repeated sessionless `get_status_labels()` (empty-key poison vector), Bearer `/tickets/showKanban` still shows dual-loop columns status ids `3,1,4,2,10,11,12,13,0` (Review / Deploying Test / QA / Deploying Prod present); titles stable across interleaved poison+`project_id=5` calls.
- `get_status_labels(project_id=5)` ×8 identical 10 labels; without `project_id` still returns seed 6 (documented; agents must pass Active `projectId`).
- Cluster: CM `leantime-app-patch` includes `Tickets.Repositories.php` mounted at Tickets.php; agent STS Ready on digest `sha256:84c40f78…063f6`.
