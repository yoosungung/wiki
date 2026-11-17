---
id: inbox-sw-factory-mm-agents-wire
agent: sw-factory
ticket_id: 38cef2e7-441a-42ca-8e89-66597bc22c95
updated: 2026-11-17
status: inbox
sources:
  - ticket:38cef2e7-441a-42ca-8e89-66597bc22c95
---

# mm agents.yaml wiring

- Sample: `deploy/agents.yaml.example` — `mm` sessions + `repo_ids`; schedule `mm-topic-radar` cron `0 4 * * 1` UTC.
- Register/seed: yaml에 있으면 `./register-agent-users.sh` / `./seed-personas.sh`가 `mm` 포함. 운영 `user_id`는 macmini register 후 기입.
- Docs: `deploy/docs/schedules.md` §5.12 · `agent-workflows` §8 schedule 링크.
