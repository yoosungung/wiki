---
id: inbox-qa-2026-11-16-qa-bulk-weekly
agent: qa
ticket_id: 462941ab-79a3-4044-9178-07727c2d99c3
updated: 2026-11-16
status: inbox
sources:
  - ticket:462941ab-79a3-4044-9178-07727c2d99c3
  - schedule:qa-bulk-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# qa-bulk-weekly 2026-11-16

- Registry 7 repo tip sync 후 Discover: 전부 `.factory/quality.yaml` 없음 → `bulk_api`/`opik` skip (NF New=0).
- Factory smoke: `GET https://factory.askwho.net/api/health` → 200 `{"ok":true,"service":"sw-factory-workers"}` (`qa: pass`).
- `opik-eval` 스킬 파일 부재·테넌트 `opik:` 키 없음 → Opik N/A. 장시간 detach/`nf-progress:` 하트비트 불필요(명령 미기동) → outcome에 `nf-progress: complete`.
- skip ≠ 실패; quality.yaml 게이트 키 온보딩 전까지 영구 skip 가능 (canonical: Tenant-Quality-Yaml-Gate-Skip-Pattern).
