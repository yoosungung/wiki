---
id: inbox-scanbooks-m1-experiment-matrix
agent: scanbooks
ticket_id: 3817f270-425f-4ed1-927b-54f07a009cae
updated: 2026-11-16
status: inbox
sources:
  - ticket:3817f270-425f-4ed1-927b-54f07a009cae
  - repo:yoosungung/scanbooks
---

# Scanbooks M1 experiment matrix (C1/S1)

- Golden synthetics: `engine/tests/fixtures/golden/` — curved_book / thumb_occlusion / printed_hand.
- C1: BBox+margin (`CROP_MARGIN_RATIO=0.05`) content retention beats quad-polygon ROI on curl bulge; keep BBox default.
- S1: stub `geo→finger→ill` beats `geo→ill→finger` (skin chroma at detect); outer-CC keeps printed hand; keep finger-before-ill.
- Evidence: `engine/benches/experiment_matrix.md` (+ pytest C1/S1). ARCHITECTURE unchanged aside from margin constant + verification notes.
