---
id: inbox-rhwp_batch-rhwp-upstream-v0.8.7-nest
agent: rhwp_batch
ticket_id: 2802d700-87fe-4f67-81b9-877a44fdbe08
updated: 2026-11-03
status: inbox
sources:
  - ticket:2802d700-87fe-4f67-81b9-877a44fdbe08
  - https://github.com/edwardkim/rhwp/releases/tag/v0.8.7
  - https://github.com/yoosungung/rhwp_batch/pull/4
---

# rhwp v0.8.7 vendor under rhwp_batch workspace

- Upstream `rhwp` root now declares `[workspace]` + path deps `crates/rhwp-{contracts,ooxml-chart,password-crypto}`.
- Vendor copy set: `src/`, `Cargo.toml`, `examples/`, `saved/`, plus `crates/*` and `build.rs`.
- Nest adapter (not `.rs` patch): strip nested `[workspace]` from vendored `rhwp/Cargo.toml`; parent `Cargo.toml` members include `rhwp/crates/*`.
- `cargo test -p rhwp-batch` needs gitignored fixtures (`rhwp-batch/samples/from_rhwp/*`, `rhwp/samples/basic/english.hwp`) from upstream `samples/`.
- Invalid env `GH_TOKEN` → use `env -u GH_TOKEN` / keyring for `gh` against public edwardkim/rhwp.
