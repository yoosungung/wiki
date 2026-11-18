---
id: inbox-aura-object-store-garage
agent: aura
ticket_id: a050691d-8fa4-4662-b439-6a066b649c78
updated: 2026-11-19
status: inbox
sources:
  - ticket:a050691d-8fa4-4662-b439-6a066b649c78
  - https://github.com/yoosungung/aura/pull/30
  - https://www.glukhov.org/data-infrastructure/object-storage/garage-vs-minio-vs-s3/
---

# Aura Object Store = Garage (M2 V2.1)

- 제품 핀: **Garage** (S3-compatible / SigV4). MinIO CE 신규 비채택.
- 버킷: `aura-content` (`tenants/{tenant_id}/refs/…` · archive/bundles prefix 공유). Barman=`aura-pg` 자격증명 비공유.
- NATS >256KB 또는 PII → envelope `content_ref` only (`enc.kid` AES-256-GCM). 라이브 provision·NCP/AWS 비용은 보류.
- L0: `deploy/docs/object-store-content-ref.md` · `check-object-store-content-ref.sh`
