---
id: inbox-sw-factory-routertest-path-userid-from-bridge
agent: sw-factory
ticket_id: 266
updated: 2026-08-06
status: inbox
sources:
  - ticket:266
  - https://github.com/yoosungung/sw-factory/pull/4
---

# RouterTest must resolve path user id from bridge.json

- Hardcoding `pathUserId() = 6` broke when sample seed mapped aa=6 and path=102; tests then hit `cursor-agent-aa` instead of `cursor-agent-path`.
- Resolve via `BridgeConfig::agentByName('path')['leantime_user_id']` so CI bootstrap (`bridge.json.sample`) stays the fixture source of truth.
