---
id: inbox-scanbooks-m3-pipeline-runner-ort
agent: scanbooks
ticket_id: 9b181d1d-d42b-4335-bacb-1a3d9c7d83b1
updated: 2026-11-17
status: inbox
sources:
  - ticket:9b181d1d-d42b-4335-bacb-1a3d9c7d83b1
  - ticket:a65634b1-df87-4881-bbb9-ba7fd17e4827
---

# scanbooks M3 PipelineRunner ORT skeleton

- Process uses `PipelineRunner` + injectable `StageBackend` (geo/finger/ill); order fixed `crop→geo→finger→ill→done`.
- Without on-device `.onnx`, backends are passthrough but still write stage PNGs + `PageMetrics.ortEp` (iOS CoreML / Android NNAPI selected).
- Failure → `status=failed` + `errorCode`; retry via `startFrom` (failed stage).
- Binaries stay out of git — `models/manifest.json` only; IllTr export simplify + FingerSeg weights still pending for live ORT.
