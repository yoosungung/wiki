---
id: inbox-pm-fe-agent-prompt-ui
agent: pm
ticket_id: 77497f17-3b3b-4de0-b168-ff76359bc9fa
updated: 2026-10-02
status: inbox
sources:
  - ticket:24d399f1-9f7d-43c2-912b-9092834c6227
  - ticket:77497f17-3b3b-4de0-b168-ff76359bc9fa
  - ARCHITECTURE.md§4
---

# FE workspace on-demand agent prompt UI

- Eric asked for message send in workspace UI on design parent `24d399f1-9f7d-43c2-912b-9092834c6227` (already done).
- New FE ticket `77497f17-3b3b-4de0-b168-ff76359bc9fa`: SPA compose → `POST /api/agent/prompts` (Option A); no chat/WS.
- BE/gateway already shipped; IA + FE client + e2e as needed.
