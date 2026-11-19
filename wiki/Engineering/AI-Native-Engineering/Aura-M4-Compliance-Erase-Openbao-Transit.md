---
id: aura-m4-compliance-erase-openbao-transit
title: "Aura M4: compliance.erase · OpenBao Transit crypto-shred"
status: canonical
owner: km
updated: "2026-11-20"
last_updated: "2026-11-20"
review_after: "2027-02-20"
sources:
  - inbox/aura/2026-11-19-compliance-erase-openbao-transit.md
  - ticket:b355e99f-374f-4bb0-b184-488d7b19cbc3
  - https://www.mongodb.com/docs/manual/core/csfle/tutorials/right-to-erasure/
tags: ["Engineering", "Aura", "Compliance", "KMS", "OpenBao"]
type: wiki
---

# Aura M4: compliance.erase · OpenBao Transit crypto-shred

- KMS product sealed: **OpenBao Transit** (`kms_product=openbao-transit`); cloud KMS deferred.
- DEK kids: `tenant:{id}:vN` · `tenant:{id}:user:{uid}:vN`. HKDF-from-MEK forbidden (re-derivable ≠ shred).
- Order fixed: shred_keys → invalidate cache → pg_redact → `aura-content` `refs/` DeleteObject → erase.done.
- erase ≠ object_gc (24h pending vs 90d orphan grace; shred vs Delete-only).
- Success smoke (draft): injectable selftest proves ciphertext undecryptable after destroy.
- L0: `deploy/docs/compliance-erase.md` · gate `check-compliance-erase.sh`.
