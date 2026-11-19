---
id: inbox-aura-compliance-erase-openbao-transit
agent: aura
ticket_id: b355e99f-374f-4bb0-b184-488d7b19cbc3
updated: 2026-11-19
status: inbox
sources:
  - ticket:b355e99f-374f-4bb0-b184-488d7b19cbc3
  - https://www.mongodb.com/docs/manual/core/csfle/tutorials/right-to-erasure/
---

# Aura M4: compliance.erase · OpenBao Transit crypto-shred

- KMS product sealed: **OpenBao Transit** (`kms_product=openbao-transit`); cloud KMS deferred.
- DEK kids: `tenant:{id}:vN` · `tenant:{id}:user:{uid}:vN`. HKDF-from-MEK forbidden (re-derivable ≠ shred).
- Order fixed: shred_keys → invalidate cache → pg_redact → `aura-content` `refs/` DeleteObject → erase.done.
- erase ≠ object_gc (24h pending vs 90d orphan grace; shred vs Delete-only).
- Success smoke (draft): injectable selftest proves ciphertext undecryptable after destroy.
- L0: `deploy/docs/compliance-erase.md` · gate `check-compliance-erase.sh`.
