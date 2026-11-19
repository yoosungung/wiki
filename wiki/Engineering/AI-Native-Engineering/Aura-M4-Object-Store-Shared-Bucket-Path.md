---
id: aura-m4-object-store-shared-bucket-path
title: "Aura M4: shared aura-content bucket path seal"
status: canonical
owner: km
updated: "2026-11-20"
last_updated: "2026-11-20"
review_after: "2027-02-20"
sources:
  - inbox/aura/2026-11-19-aura-object-store-shared-bucket-path.md
  - ticket:7e0b0b58-b135-400a-9bdf-9b43b1229d9f
  - https://github.com/yoosungung/aura/pull/54
  - wiki/Engineering/AI-Native-Engineering/Aura-M2-Object-Store-Garage-Gc.md
tags: ["Engineering", "Aura", "Garage", "S3"]
type: wiki
---

# Aura M4: shared aura-content bucket path seal

- App object store = **one** Garage bucket `aura-content`; prefixes `refs/` · `archive/` · `bundles/` (bundle store shares bucket).
- Per-use buckets rejected (Egress/secret duplication); sandbox isolation stays RuntimeClass+NP.
- Barman backup stays **`aura-pg`** (bucket+creds non-shared). `object_gc` lists `refs/` only.
- L0: `deploy/docs/object-store-content-ref.md` · gate `check-object-store-content-ref.sh`.

## Related

- [[wiki/Engineering/AI-Native-Engineering/Aura-M2-Object-Store-Garage-Gc.md]]
