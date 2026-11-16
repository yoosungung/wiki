---
id: inbox-scanbooks-m2-parity-remap-inpaint-hooks
agent: scanbooks
ticket_id: 4563165b-4919-41ca-9696-9cfd31ecfe74
updated: 2026-11-17
status: inbox
sources:
  - ticket:4563165b-4919-41ca-9696-9cfd31ecfe74
---

# Scanbooks M2 parity remap/inpaint hooks

- Mobile unit-test fixtures: `.rgb`/`.gray`/`.f32` subset under `ios/ScanbooksTests/Fixtures/parity/` and `android/.../test/resources/parity/` (from engine `tests/fixtures/parity`).
- `CvBridge.remap` = align_corners bilinear with OOB neighbors as 0 (OpenCV INTER_LINEAR + BORDER_CONSTANT); parity vs warped ≤ `3/255` (+1 LSB for fixture).
- `CvBridge.inpaintTelea` signature locked; Telea body = OpenCV M3 (throws `openCvInpaintPending` until then).
