---
id: inbox-rhwp_batch-rhwp-upstream-v0.9.1-vendor-nest
agent: rhwp_batch
ticket_id: 494e5ee5-82b0-48da-82f0-4110c87237d9
updated: 2026-11-19
status: inbox
sources:
  - ticket:494e5ee5-82b0-48da-82f0-4110c87237d9
  - https://github.com/edwardkim/rhwp/releases/tag/v0.9.1
  - https://github.com/yoosungung/rhwp_batch/pull/9
  - wiki/Engineering/Development-Environment/Cargo-Nested-Workspace-Vendor-Pattern.md
---

# rhwp v0.9.1 upstream vendor sync

- cur `0.9.0` → latest `v0.9.1`: sparse-checkout copy-set (`src`,`crates`,`saved`,`vendor`,`assets/fonts|font-rules`); drop stale `examples/` (upstream absent).
- Nest adapter unchanged from v0.9.0: strip nested `[workspace]`; flatten `vendor/svg2pdf` `{ workspace = true }` to concrete versions.
- Gate: `cargo test -p rhwp-batch` (20 passed). Tag `v0.9.1` only after PR merge (no force).
