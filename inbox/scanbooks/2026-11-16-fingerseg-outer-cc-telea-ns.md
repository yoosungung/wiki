---
id: inbox-scanbooks-fingerseg-outer-cc-telea-ns
agent: scanbooks
ticket_id: 2b22debc-12fa-4af6-b459-4d4a8a6e94b8
updated: 2026-11-16
status: inbox
sources:
  - ticket:2b22debc-12fa-4af6-b459-4d4a8a6e94b8
  - https://www.insticc.org/node/TechnicalProgram/visigrapp/2024/presentationDetails/125750
---

# FingerSeg post-process + candidates (scanbooks)

- Contract path: threshold 0.5 → border-touching CC only → dilate `k=0.004 * workLongEdge` → Telea default / NS alternate.
- Parity fixtures stay Telea-on-raw-mask (no CC/dilate in lock); pipeline covered by unit + golden printed_hand.
- Candidate A (custom MobileNet/U-Net binary) primary; reject academic FingerSeg (HGR), U2Net saliency, MediaPipe-alone.
- Evidence: `engine/benches/fingerseg_candidates.md`, `finger_pipeline.py`.
