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

# scanbooks M4 ModelCache on-demand ops

- IllTr `deploy=onDemand`; geo/seg/finger `residentPreferred`. Launch warmup = resident only.
- `ensureResidentPreferred` soft-skips missing file when `downloadURL` null (passthrough until CDN/LFS).
- Explicit `ensure(id)` still requires URL when missing; checksum mismatch deletes dest and fails.
- `workLongEdgeMitigated=768` is opt-in constant; default `workLongEdge` stays 1024 (ARCHITECTURE §5.4).
- App bridge: `ModelCache.catalog()` → `OrtModelCatalog` → `OrtBackendFactory.makeRunner`.
