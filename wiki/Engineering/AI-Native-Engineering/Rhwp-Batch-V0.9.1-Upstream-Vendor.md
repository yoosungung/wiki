---
id: rhwp-batch-v091-upstream-vendor
title: "rhwp_batch v0.9.1: upstream tag · nested vendor"
status: canonical
owner: km
updated: "2026-11-19"
last_updated: "2026-11-19"
review_after: "2027-02-19"
sources:
  - inbox/rhwp_batch/2026-11-19-rhwp-upstream-v0.9.1-tag-release.md
  - ticket:494e5ee5-82b0-48da-82f0-4110c87237d9
  - inbox/rhwp_batch/2026-11-19-rhwp-upstream-v0.9.1-vendor-nest.md
  - inbox/pm/2026-11-19-pm-checkpoint-aura-inflight-under30-rhwp-ci-wait.md
  - ticket:5f299c68-2d2d-458f-a055-86cbe2ec91b9
  - ticket:6a457aa6-1c75-4e0f-ace3-f6cb01baa104
  - inbox/pm/2026-11-19-pm-checkpoint-aura-rl-rhwp-ciwait.md
  - ticket:605ca218-b321-437f-99b6-429b2f13dc67
  - ticket:c2b44645-3a15-4e5c-a37a-b4882e3a9668
tags: ["Engineering", "rhwp_batch", "Cargo", "Vendor"]
type: wiki
---

# rhwp_batch v0.9.1: upstream tag · nested vendor

Extends [[wiki/Engineering/Development-Environment/Cargo-Nested-Workspace-Vendor-Pattern.md]].

## v0.9.1

- - Annotated tag `v0.9.1` on main tip `bcd84ba` (PR #9 merge); no force.
- - Release run success: linux + darwin binaries + GHCR `ghcr.io/yoosungung/rhwp-batch:v0.9.1` (also `:0.9.1`, `:latest`) digest `sha256:c46da701f1949372cf2fecf77fb7dfcf10cf2b9691896834e76de2b7535c5f08`.
- - cur `0.9.0` → latest `v0.9.1`: sparse-checkout copy-set (`src`,`crates`,`saved`,`vendor`,`assets/fonts|font-rules`); drop stale `examples/` (upstream absent).
- - Nest adapter unchanged from v0.9.0: strip nested `[workspace]`; flatten `vendor/svg2pdf` `{ workspace = true }` to concrete versions.
- - Gate: `cargo test -p rhwp-batch` (20 passed). Tag `v0.9.1` only after PR merge (no force).
