---
id: inbox-scanbooks-failed-stage-retry
agent: scanbooks
ticket_id: d9cd8759-c8c5-41de-8114-96ccd783ad72
updated: 2026-11-17
status: inbox
sources:
  - ticket:d9cd8759-c8c5-41de-8114-96ccd783ad72
  - wiki/Engineering/AI-Native-Engineering/Scanbooks-M2-App-Skeleton.md
---

# scanbooks M3: failed + failedStage resume

- ARCHITECTURE §1.3: `status==failed`이면 `PipelineRunner`가 명시 `startFrom` 없이도 `failedStage`부터 재개(iOS 기존 · Android 파리티).
- Process UI: `FailedRetryPresentation` — `{단계} 실패 · {errorCode}` + CTA `이 단계부터 재시도`.
- 단위: `PipelineRunnerTest(s).retryFromFailedStage` (default startFrom), `FailedRetryPresentationTest(s)`.
