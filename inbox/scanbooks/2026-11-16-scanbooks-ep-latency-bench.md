---
id: inbox-scanbooks-ep-latency-bench
agent: scanbooks
ticket_id: 3ad0ee61-1d56-4846-9b4b-411aa1e5a301
updated: 2026-11-16
status: inbox
sources:
  - ticket:3ad0ee61-1d56-4846-9b4b-411aa1e5a301
  - https://onnxruntime.ai/docs/execution-providers/CoreML-ExecutionProvider.html
---

# Scanbooks EP latency (M1)

- GeoTr e2e (net 288 + remap@1024) CoreML MLProgram NE ≈0.13 s / CPU FP32 ≈0.19 s — gate ≤2.5 s **pass**.
- IllTr 순차 81패치 ≈11 s — gate ≤3.5 s **fail**; ~123k-node export 단순화·batch 선행 필요 (완화: IllTr 옵션화).
- GeoTr quant 최종: **dynamic_int8** (CPU dyn ≈188 ms ≤ WO ≈199 ms; 용량도 dyn 유리).
- CoreML 기본: MLProgram + NeuralEngine; 그래프 float16 convert는 Cast/Conv 타입 오류 → FP32 가중치 + NE FP16 compute.
- NNAPI: Android ORT Mobile에서만 — macOS host deferred.
- 재현: `scanbooks-latency-bench --onnx-dir …` / 증거 `engine/benches/latency.md`
