---
id: aura-m2-object-store-garage-gc
title: "Aura M2: Garage object store · content_ref · orphan GC"
status: canonical
owner: km
updated: "2026-11-19"
last_updated: "2026-11-19"
review_after: "2027-02-19"
sources:
  - inbox/aura/2026-11-19-aura-object-store-garage-content-ref.md
  - ticket:a050691d-8fa4-4662-b439-6a066b649c78
  - ticket:1d669034-018b-45e0-986f-c50b24cfd735
  - inbox/aura/2026-11-19-aura-object-store-garage.md
  - inbox/aura/2026-11-19-aura-orphan-content-ref-gc.md
  - ticket:bb165a71-08a2-49af-828e-c5197688827e
  - inbox/pm/2026-11-19-aura-m2-object-store-intent-pass.md
  - inbox/pm/2026-11-19-aura-m2-orphan-gc-intent-m2-done.md
tags: ["Engineering", "Aura", "Garage", "S3", "GC"]
type: wiki
---

# Aura M2: Garage object store · content_ref · orphan GC

## Garage + content_ref

- Product pin: **Garage** (S3/SigV4). MinIO CE 신규 비채택; NCP/AWS = endpoint swap.
- Buckets: `aura-content` keys `tenants/{tenant_id}/refs/{yyyy}/{mm}/{content_id}` (+ `archive/`/`bundles/`); Barman **`aura-pg`** credentials separate.
- NATS/RPC body >256KiB or PII → envelope `content_ref` only (`scheme=s3`, bucket/key/size, optional `enc.alg`+`enc.kid`).
- Public ACL 금지 · Egress allowlist to `AURA_S3_ENDPOINT`. Live provision/cost = `@eric` hold.
- L0: `deploy/docs/object-store-content-ref.md` · `check-object-store-content-ref.sh`.

## Orphan GC (V2.2)

- Grace **90d** (= `AURA_EVENTS` retention); candidates only under `tenants/.../refs/` on `aura-content`.
- Task `aura.tasks.memory.object_gc` daily · batch≤100 · idempotent key; EXISTS live `metadata.content_ref` → skip; never GC archive/bundles/`aura-pg`.
- Impl = M4; gate `check-object-store-orphan-gc.sh`.
