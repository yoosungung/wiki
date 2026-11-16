---
id: inbox-pm-scanbooks-m1-experiment-matrix-intent-pass
agent: pm
ticket_id: 3817f270-425f-4ed1-927b-54f07a009cae
updated: 2026-11-16
status: inbox
sources:
  - ticket:3817f270-425f-4ed1-927b-54f07a009cae
  - https://github.com/yoosungung/scanbooks/pull/3
---

# scanbooks M1 experiment matrix — intent pass

- C1: BBox+margin content retention beats straight-edge quad/homography ROI on curled pages; keep `CROP_MARGIN_RATIO=0.05`.
- S1: stub proxies show `geo→finger→ill` beats `geo→ill→finger` (chroma wash at detect); outer-CC keeps interior printed hands.
- Contract path unchanged: `crop → geo → finger → ill → done`; evidence `engine/benches/experiment_matrix.md`.
- Non-goals held: no M2+/GeoTr-1024/static INT8 default.
- Next M1 slice after merge: parity fixtures (`raw_flow→warped`, `raw_mask→inpainted`).
