---
id: inbox-scanbooks-m2-pipeline-stub-status
agent: scanbooks
ticket_id: c878b056-5212-47f1-a5ce-85837310325e
updated: 2026-11-16
status: inbox
sources:
  - ticket:c878b056-5212-47f1-a5ce-85837310325e
  - https://github.com/yoosungung/scanbooks/pull/11
---

# Scanbooks M2 PipelineStub status persist

- M2 stub SoR is `PipelineStub` (iOS/Android): walks `crop→geo→finger→ill→done` and writes each stage to `SessionStore` `Page.status`.
- `StubProcessRunner` stays UI/unit-test-only (no disk). ORT/OpenCV remain M3.
- Capture → Process wiring passes `sessionId`/`pageId` so status survives cancel/reopen on the same page.json.
