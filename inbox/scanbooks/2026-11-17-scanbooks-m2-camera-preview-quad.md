---
id: inbox-scanbooks-m2-camera-preview-quad
agent: scanbooks
ticket_id: 1113c912-ea26-44c5-9411-ea04e2450e52
updated: 2026-11-17
status: inbox
sources:
  - ticket:1113c912-ea26-44c5-9411-ea04e2450e52
  - https://github.com/yoosungung/scanbooks
---

# Scanbooks M2 — camera preview + rough Quad

- Live preview runs **border/Quad only**; Dewarp/GeoTr never on preview frames (ARCHITECTURE §1.4).
- Quad schema: normalized `[0,1]` TL origin with `tl/tr/br/bl` (ARCHITECTURE §4.3).
- UX: undetected → thin gray guide + `문서를 화면에 맞춰 주세요`; stable → green Quad; permission deny → Settings CTA only (no empty permission loop).
- iOS path: Vision rectangles first, rough luminance blob fallback; Android M2: CameraX + rough luminance blob (ML Kit/OpenCV later).
- Stability: require N consecutive similar hits before green overlay (`EdgeStabilityTracker`).
