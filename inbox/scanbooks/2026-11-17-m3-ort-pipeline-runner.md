---
id: inbox-scanbooks-m3-ort-pipeline-runner
agent: scanbooks
ticket_id: 9b181d1d-d42b-4335-bacb-1a3d9c7d83b1
updated: 2026-11-17
status: inbox
sources:
  - ticket:9b181d1d-d42b-4335-bacb-1a3d9c7d83b1
  - wiki/Engineering/AI-Native-Engineering/Scanbooks-M1-DocTr-Onnx-Latency.md
---

# scanbooks M3: PipelineRunner + selected EP

- Replaced M2 `PipelineStub` walk with `PipelineRunner`: `crop→geo→finger→ill→done`, mid PNGs, `PageMetrics.ortEp`.
- Selected EP: iOS `CoreML_MLProgram_NeuralEngine+CPU_fallback`; Android `CPUExecutionProvider` (NNAPI deferred).
- Without bundled `.onnx`, `PassthroughStageBackend` keeps order/URI/PDF path; `Ort*StageBackend` throws `ort_*_not_linked` when weights present but ORT session not wired.
- `failed` + `failedStage` + retry via `startFrom` / resume.
- OpenCV Telea still pending; FingerSeg/IllTr weights still blocked (manifest status).
