---
id: inbox-scanbooks-m3-page-progress-metrics-ui
agent: scanbooks
ticket_id: 27d8afbd-379e-4395-9753-e330ec6b34a1
updated: 2026-11-17
status: inbox
sources:
  - ticket:27d8afbd-379e-4395-9753-e330ec6b34a1
  - wiki/Engineering/AI-Native-Engineering/Scanbooks-M2-App-Skeleton.md
---

# scanbooks M3: Process UI + PageMetrics contract line

- Process shows stage list + per-stage ms + contract line `workLongEdge · geoNet · EP(ortEp)` via `PageMetricsPresentation` (iOS/Android parity).
- Metrics reload from SessionStore on each PipelineStage update; PipelineRunner order `crop→geo→finger→ill` unchanged.
- Out of scope this slice: failed-stage retry UX polish · live OrtSession device smoke · M4 batch.
