---
id: inbox-codingland-296-m2-replay
agent: codingland
ticket_id: 296
updated: 2026-08-07
status: inbox
sources:
  - ticket:296
  - https://github.com/yoosungung/codingland.git
---

# codingland #296 M2 Replay sandbox shipped

- M2 core: shallow `sanitize` (depth≤3, namePatterns/astSensitiveParams), in-process `IsolatedRunner` (replay/inject/hotReboot/mock I/O), Living Spec `scenarioId`↔Jest link.
- Host Canvas: Time Bar scrub → `timeline.onChangeEnd`; Hot Reboot → `runner.hotReboot` + `timeline.cache`.
- Runner hosting locked in-process for M2 (worker = M3+). Evidence: `npm test` (37) + host `tsc`.
