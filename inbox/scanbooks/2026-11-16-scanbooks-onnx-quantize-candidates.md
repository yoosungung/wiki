---
id: inbox-scanbooks-onnx-quantize-candidates
agent: scanbooks
ticket_id: 0be42506-ebb3-4175-909c-3eb656a3307e
updated: 2026-11-16
status: inbox
sources:
  - ticket:0be42506-ebb3-4175-909c-3eb656a3307e
  - https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html
---

# Scanbooks ONNX 양자화 후보 (M1)

- GeoTr: dynamic INT8 ~23.5 MB (FP32 86.4) max_abs≈0.004; weight-only MatMulNBits bits=8 ~37.5 MB max_abs≈5e-4. 둘 다 후보 — latency.md 후 선택.
- IllTr: WO가 dyn보다 작고 오차 낮음; 다만 ~123k 노드 export가 로드 병목 → forward 단순화 선행.
- Seg(U2NETP): MatMulNBits no-op(Conv); dynamic은 용량↓이나 sigmoid max_abs≈0.97 → FP16/FP32 유지.
- static INT8(활성화 캘리브레이션)은 GeoTr flow 기본 배포 경로로 채택 금지 (ARCHITECTURE).
- 재현: `scanbooks-quantize-candidates --onnx-dir …` / 증거 `engine/benches/quantize_candidates.md`
