---
id: inbox-rhwp_batch-rhwp-upstream-v0.9.0-vendor-nest
agent: rhwp_batch
ticket_id: 0f34dece-193b-4a93-bca5-6c8d408fb620
updated: 2026-11-09
status: inbox
sources:
  - ticket:0f34dece-193b-4a93-bca5-6c8d408fb620
  - https://github.com/edwardkim/rhwp/releases/tag/v0.9.0
  - wiki/Engineering/Development-Environment/Cargo-Nested-Workspace-Vendor-Pattern.md
---

# rhwp v0.9.0 vendor path deps + nest adapter

- edwardkim/rhwp **v0.9.0** default features pull path vendors (`vendor/rhwp-pdf-import-backend`, `rhwp-zune-jpeg`, `rhwp-jpeg-encoder`, `svg2pdf`, hayro/qcms/codec) — copy set must include `vendor/` (+ `assets/` for `include_bytes!` fonts).
- Nest adapter beyond stripping root `[workspace]`: vendor crates that ship `[workspace]` / `{ workspace = true }` must be flattened to concrete package/dep versions, or the outer `rhwp_batch` workspace hits multiple-root / missing `workspace.package` errors.
- Full upstream tarball is multi-GB (samples etc.); use sparse clone of crate subset. Omit `tools/` (~580MB) for `rhwp-batch` — bins unused; 0.8.7 also shipped without `tools/` on disk.
- After merge only: annotated tag `v0.9.0` → `.github/workflows/release.yml` (no force/retag).
