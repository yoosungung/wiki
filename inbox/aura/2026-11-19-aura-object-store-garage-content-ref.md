---
id: inbox-aura-object-store-garage-content-ref
agent: aura
ticket_id: a050691d-8fa4-4662-b439-6a066b649c78
updated: 2026-11-19
status: inbox
sources:
  - ticket:a050691d-8fa4-4662-b439-6a066b649c78
  - ticket:1d669034-018b-45e0-986f-c50b24cfd735
  - https://github.com/yoosungung/aura/pull/30
---

# Aura Object Store = Garage + content_ref (M2 V2.1)

- 제품 고정: **Garage** (S3-compatible / SigV4). NCP·AWS는 동일 클라이언트·스키마로 endpoint 스왑 가능.
- 버킷: `aura-content` · 키 `tenants/{tenant_id}/refs/{yyyy}/{mm}/{content_id}`; 아카이브는 동일 버킷 `archive/` prefix; PG Barman은 **`aura-pg` 분리**.
- NATS/RPC 본문 >256KB(262144) 또는 PII → envelope에 `content_ref`만, `payload` 원문 금지.
- `content_ref` JSON: `scheme=s3`, `bucket`, `key`, `size_bytes`, optional `content_type`, `enc.alg`+`enc.kid` (crypto-shred).
- 공개 ACL 금지 · Egress allowlist to `AURA_S3_ENDPOINT` · 라이브 provision/비용은 `@eric` 보류.
- 정본: aura `deploy/docs/object-store-content-ref.md` · gate `check-object-store-content-ref.sh`.
