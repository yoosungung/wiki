---
id: inbox-codingland-m2-replay-sandbox
agent: codingland
ticket_id: 296
updated: 2026-08-07
status: inbox
sources:
  - ticket:296
  - ARCHITECTURE.md
  - https://tianpan.co/blog/2026-04-12-deterministic-replay-debugging-non-deterministic-ai-agents
---

# codingland M2 Replay sandbox

- M2 Runner is **in-process** soft TTD: record call tape → `replay(entry, break)` + `inject` + `hotReboot` to last checkpoint (no VM heap rollback).
- Shallow Sanitizer: `maxDepth: 3`, namePatterns + astSensitiveParams → `[REDACTED]`; deeper nests → `[MAX_DEPTH]`; leaves stringified for RuntimeSnapshot fields.
- Living Spec sidecar frontmatter links Jest by `scenarioId` 1:1; unknown id throws (orphan Jest forbidden).
- Host Time Bar scrub emits `timeline.onChangeEnd`; Hot Reboot calls `IsolatedRunner.hotReboot` and pushes `timeline.cache`.
