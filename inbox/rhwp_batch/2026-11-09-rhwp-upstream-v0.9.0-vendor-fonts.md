---
id: inbox-rhwp_batch-rhwp-upstream-v0.9.0-vendor-fonts
agent: rhwp_batch
ticket_id: 0f34dece-193b-4a93-bca5-6c8d408fb620
updated: 2026-11-09
status: inbox
sources:
  - ticket:0f34dece-193b-4a93-bca5-6c8d408fb620
  - https://github.com/edwardkim/rhwp/releases/tag/v0.9.0
  - wiki/Engineering/Development-Environment/Cargo-Nested-Workspace-Vendor-Pattern.md
---

# rhwp v0.9.0 vendor copy-set 확장

- v0.9.0부터 루트 `Cargo.toml`이 `vendor/*` path-dep(jpeg/svg2pdf/pdf-import 등)을 쓰므로 nest vendor 시 `rhwp/vendor/` 복사가 필수.
- `vendor/svg2pdf`는 `[workspace.package]`/`[workspace.dependencies]` inheritance를 쓰므로 `[workspace]` strip만으로는 부족 — 값을 인라인 flatten해야 outer workspace에서 파싱된다.
- `include_bytes!`/`include_str!`로 `assets/fonts/*`, `assets/font-rules/*`를 참조하므로 promo `assets/chrome|edge` 없이도 **fonts + font-rules**는 vendor 세트에 넣어야 `cargo test -p rhwp-batch`가 컴파일된다.
- 전체 upstream tarball(~GB) 대신 sparse-checkout(`src`,`crates`,`saved`,`samples`,`vendor`,`assets`)이 실용적.
