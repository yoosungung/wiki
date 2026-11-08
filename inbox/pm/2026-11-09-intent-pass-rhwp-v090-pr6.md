---
id: inbox-pm-intent-pass-rhwp-v090-pr6
agent: pm
ticket_id: 0f34dece-193b-4a93-bca5-6c8d408fb620
updated: 2026-11-09
status: inbox
sources:
  - ticket:0f34dece-193b-4a93-bca5-6c8d408fb620
  - https://github.com/yoosungung/rhwp_batch/pull/6
  - wiki/Engineering/Development-Environment/Cargo-Nested-Workspace-Vendor-Pattern.md
---

# rhwp_batch v0.9.0 Intent pass + merge

- Intent pass on lean nest PR #6 (prefer over fat #5); squash merge `394534c`.
- v0.9.0 vendor set needs `rhwp/vendor/*` + fonts/font-rules; promo chrome/edge optional.
- Repo CI is tag-only `release.yml` — PR checks absent; local `cargo test -p rhwp-batch` is the Intent gate.
- Post-merge remaining: annotated tag `v0.9.0` (no force) to trigger Release.
