---
id: scanbooks-m1-doctr-onnx-latency
title: "scanbooks M1: DocTr ONNX · FingerSeg · parity · latency"
status: canonical
owner: km
updated: "2026-11-17"
last_updated: "2026-11-17"
review_after: "2027-02-17"
sources:
  - inbox/scanbooks/2026-11-16-doctr-export-prototype.md
  - inbox/scanbooks/2026-11-16-scanbooks-onnx-quantize-candidates.md
  - inbox/scanbooks/2026-11-16-fingerseg-outer-cc-telea-ns.md
  - inbox/scanbooks/2026-11-16-scanbooks-m1-experiment-matrix.md
  - inbox/scanbooks/2026-11-16-scanbooks-ep-latency-bench.md
  - inbox/pm/2026-11-16-scanbooks-m1-parity-fixtures-intent-pass.md
  - inbox/pm/2026-11-16-scanbooks-m1-experiment-matrix-intent-pass.md
  - inbox/pm/2026-11-16-pm-checkpoint-scanbooks-onnx-seal-fingerseg-kick.md
  - inbox/pm/2026-11-16-pm-checkpoint-scanbooks-m1-latency-kickoff.md
  - inbox/pm/2026-11-16-pm-checkpoint-scanbooks-m1-closeout.md
  - https://github.com/fh2019ustc/DocTr
tags: ["Engineering", "scanbooks", "ONNX", "DocTr", "FingerSeg", "Latency"]
type: wiki
---

# scanbooks M1: DocTr ONNX · FingerSeg · parity · latency

Contract path: `crop → geo → finger → ill → done`. M1 closed on factory (milestone + children done); M2 not auto-enqueued until ROADMAP unchecked H2 advances.

## DocTr ONNX export

- GeoTr I/O `1×3×288×288` → `1×2×288×288` f32; IllTr patch `1×3×128×128`; U2NETP seg `1×3×288×288` → `1×1×288×288`.
- FP16 weight-only resident ≈ **75.89 MB** (GeoTr 49.11 + IllTr 24.62 + seg 2.16) ≤ 80 MB budget.
- Network ONNX **no GridSample** — warp is post-process `grid_sample`/`remap`. IllTr naive export ~123k nodes → simplify forward before mobile.
- `illOverlap` = **16 px** (`int(128*0.125)`); DocTr source comment `# 32` is wrong.
- CPU export: patch DocTr hard-coded `.cuda()` in `GeoTr.py` / `position_encoding.py`.

## Quantize candidates

- GeoTr: **dynamic_int8** preferred after latency (CPU dyn ≈188 ms ≤ WO ≈199 ms; size also favors dyn). WO MatMulNBits bits=8 still a size/accuracy alternate.
- IllTr: WO smaller/lower err than dyn, but ~123k-node load bottleneck → forward simplify first.
- Seg(U2NETP): keep FP16/FP32 (dynamic sigmoid max_abs≈0.97). **static INT8 not default** for GeoTr flow (ARCHITECTURE).

## FingerSeg post-process

- threshold 0.5 → border-touching CC only → dilate `k=0.004 * workLongEdge` → Telea default / NS alternate.
- Parity fixtures stay Telea-on-raw-mask (no CC/dilate in lock). Candidate A = custom MobileNet/U-Net binary; reject academic FingerSeg(HGR) / U2Net saliency / MediaPipe-alone.
- Evidence: `engine/benches/fingerseg_candidates.md`.

## Experiment matrix (C1/S1)

- C1: BBox+margin (`CROP_MARGIN_RATIO=0.05`) beats quad-polygon ROI on curl; keep BBox default.
- S1: stub `geo→finger→ill` beats `geo→ill→finger` (skin chroma); outer-CC keeps printed hand.
- Golden: `engine/tests/fixtures/golden/` curved_book / thumb_occlusion / printed_hand.

## Parity fixtures

- `engine/tests/fixtures/parity/` preprocess + `raw_flow→warped` + `raw_mask→inpainted`; numeric tolerance (no hash lock).
- Pitfall: milestone `@IC` comment → false Active wake; mention IC on **child** only.
- PR #4 MERGED; IC pytest 23 passed.

## EP latency

- GeoTr e2e (net 288 + remap@1024) CoreML MLProgram NE ≈0.13 s / CPU FP32 ≈0.19 s — gate ≤2.5 s **pass**.
- IllTr sequential 81 patches ≈11 s — gate ≤3.5 s **fail**; mitigate by optional IllTr / simplify+batch.
- CoreML: MLProgram + NeuralEngine; float16 graph convert → Cast/Conv errors → FP32 weights + NE FP16 compute.

## Factory seals (M1)

- ONNX PR #5 · FingerSeg PR #6 · latency PR #7 · matrix/parity Intent+merge → M1 milestone done; parent stub backlog dup closed.
- Checkpoint: kick **child** only; milestone board/progress must not `@mention` IC.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Scanbooks-Factory-Onboard.md]]
- [[wiki/Engineering/AI-Native-Engineering/Scanbooks-M2-App-Skeleton.md]]
