---
id: inbox-aura-object-store-shared-bucket-path
agent: aura
ticket_id: 7e0b0b58-b135-400a-9bdf-9b43b1229d9f
updated: 2026-11-19
status: inbox
sources:
  - ticket:7e0b0b58-b135-400a-9bdf-9b43b1229d9f
  - https://github.com/yoosungung/aura/pull/54
  - wiki/Engineering/AI-Native-Engineering/Aura-M2-Object-Store-Garage-Gc.md
---

# Aura M4: shared `aura-content` bucket path seal

- App object store = **one** Garage bucket `aura-content`; prefixes `refs/` · `archive/` · `bundles/` (bundle store shares bucket).
- Per-use buckets rejected (Egress/secret duplication); sandbox isolation stays RuntimeClass+NP.
- Barman backup stays **`aura-pg`** (bucket+creds non-shared). `object_gc` lists `refs/` only.
- L0: `deploy/docs/object-store-content-ref.md` · gate `check-object-store-content-ref.sh` · ROADMAP decision log 2026-11-19.
