---
id: scanbooks-m3-pipeline-ort-temp-smoke
title: "scanbooks M3: PipelineRunner · ORT EP · failedStage retry · temp device smoke"
status: canonical
owner: km
updated: "2026-11-18"
last_updated: "2026-11-18"
review_after: "2027-02-18"
sources:
  - inbox/scanbooks/2026-11-17-m3-ort-pipeline-runner.md
  - inbox/scanbooks/2026-11-17-scanbooks-m3-pipeline-runner-ort.md
  - inbox/scanbooks/2026-11-17-failed-stage-retry.md
  - inbox/scanbooks/2026-11-17-scanbooks-m3-page-progress-metrics-ui.md
  - inbox/scanbooks/2026-11-18-m3-temp-device-smoke-option2.md
  - inbox/pm/2026-11-17-intent-pass-failed-stage-retry.md
  - inbox/pm/2026-11-17-scanbooks-m3-pagemetrics-ui-intent-pass.md
  - inbox/pm/2026-11-17-scanbooks-m2-done-roadmap-lag-blocks-m3.md
  - inbox/pm/2026-11-17-scanbooks-m2-m3-pass-approved.md
  - inbox/pm/2026-11-17-scanbooks-m2-pass-gate-manual.md
  - inbox/pm/2026-11-17-scanbooks-m3-device-smoke-approval.md
  - inbox/pm/2026-11-18-scanbooks-m3-intent-pass-option2.md
  - inbox/pm/2026-11-18-scanbooks-m3-pr19-roadmap-clarify-intent.md
  - inbox/pm/2026-11-18-scanbooks-m3-temp-evidence-option2.md
  - ticket:9b181d1d-d42b-4335-bacb-1a3d9c7d83b1
  - ticket:d9cd8759-c8c5-41de-8114-96ccd783ad72
  - ticket:27d8afbd-379e-4395-9753-e330ec6b34a1
  - ticket:377c50be-63b7-4293-927b-8886b69c5ce3
  - ticket:de05921c-ffdf-41ef-88d7-2053f9a7dd9c
tags: ["Engineering", "scanbooks", "ONNX", "ORT", "Mobile"]
type: wiki
---

# scanbooks M3: PipelineRunner · ORT EP · failedStage retry · temp device smoke

Builds on [[wiki/Engineering/AI-Native-Engineering/Scanbooks-M2-App-Skeleton.md]]. `tenant_cd` N/A for mobile slices — feature Done = Intent + merge + test evidence on ticket.

## PipelineRunner + selected EP

- Replaces M2 `PipelineStub` with `PipelineRunner`: order `crop→geo→finger→ill→done`, mid PNGs, `PageMetrics.ortEp`.
- Selected EP: iOS `CoreML_MLProgram_NeuralEngine+CPU_fallback`; Android `CPUExecutionProvider` (NNAPI deferred).
- Without bundled `.onnx`, `PassthroughStageBackend` keeps order/URI/PDF; `Ort*StageBackend` throws `ort_*_not_linked` when weights present but session not linked.
- Binaries stay out of git — `models/manifest.json` only; IllTr export simplify + FingerSeg weights still pending for live ORT.

## failed + failedStage resume

- ARCHITECTURE §1.3: `status==failed` → resume from `failedStage` even without explicit `startFrom` (iOS existing · Android parity).
- Process UI: `FailedRetryPresentation` — `{단계} 실패 · {errorCode}` + CTA `이 단계부터 재시도`.
- Unit: `PipelineRunnerTest(s).retryFromFailedStage`, `FailedRetryPresentationTest(s)`. PR #17 merged for this slice.

## Process UI + PageMetrics contract line

- Stage list + per-stage ms + contract line `workLongEdge · geoNet · EP(ortEp)` via `PageMetricsPresentation` (iOS/Android parity).
- Metrics reload from SessionStore on each PipelineStage update.
- Out of scope this spoke: live OrtSession device smoke · M4 batch.

## Temp device smoke (option 2)

- Eric 2026-11-17: USB mid-range absent → **sim/emu + fixture 3 pages → done+PDF** as **temporary** M3 device AC; physical USB remains follow-up.
- Intent must state `drift: sim/emu temporary evidence` (ROADMAP 「실기기(중급기)」와 의도적 불일치).
- Evidence: iOS `iPhone 17` Simulator `DeviceSmokeTempEvidenceTests` PASS; Android host JVM `DeviceSmokeTempEvidenceTest` PASS; AVD inventory OK (adb boot hang ≠ full install run).
- PR #18 merge `3b929e04`; PR #19 docs-only ROADMAP Android clarify `fa293cb8`.

## M2→M3 gate notes

- M2 checkbox lag can block M3 invent until roadmap sync closes M2 / markers exist.
- Manual pass-gate / Approval KEEP on USB mid-range child until option 2 supersedes.

## 🔗 Related

- [[wiki/Engineering/AI-Native-Engineering/Scanbooks-Factory-Onboard.md]]
- [[wiki/Engineering/AI-Native-Engineering/Scanbooks-M1-DocTr-Onnx-Latency.md]]
- [[wiki/Engineering/AI-Native-Engineering/Scanbooks-M2-App-Skeleton.md]]
- [[wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md]]
