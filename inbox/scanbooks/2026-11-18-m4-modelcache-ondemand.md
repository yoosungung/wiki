---
id: inbox-scanbooks-m4-modelcache-ondemand
agent: scanbooks
ticket_id: 5f79ae5a-0ecb-4c81-b8f3-ebf35ce3b4c6
updated: 2026-11-18
status: inbox
sources:
  - ticket:5f79ae5a-0ecb-4c81-b8f3-ebf35ce3b4c6
  - wiki/Engineering/AI-Native-Engineering/Scanbooks-M1-DocTr-Onnx-Latency.md
---

# scanbooks M4: ModelCache on-demand ops

- `models/manifest.json` `deploy`: `residentPreferred` (geo/seg/finger) · `onDemand` (illtr). Optional `downloadURL`/`checksumSha256`.
- App `ModelCache.ensure` / `ensureResidentPreferred` → `OrtModelCatalog`; IllTr absent → ill passthrough (pipeline order intact).
- Missing resident file + null URL → soft-skip (no launch crash until CDN/LFS).
- `workLongEdgeMitigated=768` constant only; default remains 1024 (ARCHITECTURE §5.4).
