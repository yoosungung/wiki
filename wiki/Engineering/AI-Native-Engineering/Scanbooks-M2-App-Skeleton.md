---
id: scanbooks-m2-app-skeleton
title: "scanbooks M2: UI · camera Quad · ScanSession · pipeline stub · parity hooks"
status: canonical
owner: km
updated: "2026-11-17"
last_updated: "2026-11-17"
review_after: "2027-02-17"
sources:
  - inbox/scanbooks/2026-11-17-scanbooks-m2-camera-preview-quad.md
  - inbox/scanbooks/2026-11-17-scanbooks-m2-parity-remap-inpaint-hooks.md
  - inbox/scanbooks/2026-11-16-scanbooks-m2-pipeline-stub-status.md
  - inbox/pm/2026-11-17-pm-checkpoint-scanbooks-m2-ui-kickoff.md
  - inbox/pm/2026-11-17-pm-checkpoint-scanbooks-m2-camera-quiet.md
  - inbox/pm/2026-11-17-pm-checkpoint-scanbooks-m2-scansession-kickoff.md
  - inbox/pm/2026-11-17-pm-checkpoint-scanbooks-m2-parity-quiet.md
  - inbox/pm/2026-11-17-pm-checkpoint-scanbooks-m2-parity-quiet2.md
  - inbox/pm/2026-11-17-roadmap-sync.md
  - inbox/pm/2026-11-17-roadmap-sync-0600.md
tags: ["Engineering", "scanbooks", "Mobile", "Camera", "Parity"]
type: wiki
---

# scanbooks M2: UI · camera Quad · ScanSession · pipeline stub · parity hooks

`tenant_cd` N/A for mobile M2 slices — feature Done = Intent + merge + test on ticket.

## ROADMAP / sync

- current=`## M2 — 앱 스켈레톤`; milestone `d4325e10` + children with `roadmap:scanbooks:…` markers.
- Doc lag: children may be done while ROADMAP `- [ ]` still open → sync `created=0` (dedup). Do not invent Phase invent beyond H2 gate.

## UI shell

- First `- [ ]` after M2 open = UIUX shell; kick child only (`@scanbooks`), not milestone `@IC`.

## Camera preview + rough Quad

- Live preview = **border/Quad only**; Dewarp/GeoTr never on preview frames (ARCHITECTURE §1.4).
- Quad: normalized `[0,1]` TL origin `tl/tr/br/bl` (§4.3).
- UX: undetected → gray guide + copy; stable → green Quad; permission deny → Settings CTA (no empty permission loop).
- iOS: Vision rectangles first, luminance blob fallback. Android M2: CameraX + rough luminance (ML Kit/OpenCV later).

## ScanSession + PipelineStub

- SoR: `PipelineStub` walks `crop→geo→finger→ill→done` and writes each stage to `SessionStore` `Page.status`.
- `StubProcessRunner` = UI/unit-test only (no disk). ORT/OpenCV = M3.
- Capture→Process passes `sessionId`/`pageId` so status survives cancel/reopen on same `page.json`.

## Parity remap / inpaint hooks

- Fixtures: `.rgb`/`.gray`/`.f32` under iOS/Android test resources `parity/`.
- `CvBridge.remap` = align_corners bilinear; OOB neighbors 0 (OpenCV INTER_LINEAR + BORDER_CONSTANT); vs warped ≤ `3/255`.
- `CvBridge.inpaintTelea` signature locked; body throws `openCvInpaintPending` until OpenCV M3.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Scanbooks-M1-DocTr-Onnx-Latency.md]]
- [[wiki/Engineering/AI-Native-Engineering/Scanbooks-Factory-Onboard.md]]
