---
id: inbox-pm-aura-m2-object-store-intent-pass
agent: pm
ticket_id: a050691d-8fa4-4662-b439-6a066b649c78
updated: 2026-11-19
status: inbox
sources:
  - ticket:a050691d-8fa4-4662-b439-6a066b649c78
  - ticket:1d669034-018b-45e0-986f-c50b24cfd735
  - https://github.com/yoosungung/aura/pull/30
  - https://garagehq.deuxfleurs.fr/documentation/cookbook/kubernetes/
---

# Aura M2 Object Store = Garage (Intent pass)

- 제품 고정: **Garage** (S3-compatible / SigV4). MinIO CE 비채택. NCP/AWS는 endpoint 스왑 대안.
- 버킷: `aura-content` + key `tenants/{tenant_id}/refs/…`; Barman=`aura-pg` 분리.
- 256KB/PII → `content_ref` only · public ACL 금지 · `enc.kid` crypto-shred.
- 정본: `deploy/docs/object-store-content-ref.md` · gate `check-object-store-content-ref.sh`.
- Non-goals: live provision · SDK 업로드 · 고아 GC(V2.2 child). 비용/리전 택일은 `@eric` escalate 보류.
- PR#30 MERGED `e84205b2` · parent M2 next = 고아 GC 설계 `bb165a71`.
