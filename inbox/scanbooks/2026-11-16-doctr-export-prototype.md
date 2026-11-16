---
id: inbox-scanbooks-doctr-export-prototype
agent: scanbooks
ticket_id: fe6f15d9-862e-4154-9cab-348cc2a42f7f
updated: 2026-11-16
status: inbox
sources:
  - ticket:fe6f15d9-862e-4154-9cab-348cc2a42f7f
  - https://github.com/fh2019ustc/DocTr
  - https://huggingface.co/spaces/HaoFeng2019/DocTr
---

# DocTr ONNX export prototype (scanbooks M1)

- GeoTr I/O: `1×3×288×288` → `1×2×288×288` float32; IllTr patch `1×3×128×128` → same; U2NETP seg `1×3×288×288` → `1×1×288×288`.
- FP16 weight-only: GeoTr 49.11 MB + IllTr 24.62 MB + seg 2.16 MB = **75.89 MB** (≤80 MB resident budget).
- Network ONNX has **no GridSample** — official warp is post-process `grid_sample`/`remap`. In-graph ops of note: `LayerNormalization`, heavy `Reshape`; IllTr naive export explodes (~123k nodes via ScatterND/Where) → simplify export forward before mobile.
- `illOverlap` is **16 px** (`int(128*0.125)`); DocTr source comment `# 32` is wrong.
- CPU export needs device patches: DocTr hardcodes `.cuda()` in `GeoTr.py` / `position_encoding.py`.
