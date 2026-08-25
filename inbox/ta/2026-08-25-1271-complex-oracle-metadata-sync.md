---
id: inbox-ta-1271-complex-oracle-metadata-sync
agent: ta
ticket_id: 1271
updated: 2026-08-25
status: inbox
sources:
  - ticket:1271
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md
---

# #1271 complex_oracle seals via FS PUT on shared tip

- Tip image already `test-e7fd808` (Kaniko from #1272 stack; product SHA `a9a5c2b` ⊂ `e7fd808`). GH Actions `environment` input 422 — tip path is Kaniko + `kubectl set image`, not `build-ghcr-images.yml` env.
- Live catalog lacked 4 refSql seals; `complex_oracle_sales` was thin single-table. PUT create seals (`base_sha=null`) + update sales grain; **do not** overwrite rich live `complex_oracle_times` with thin fixture.
- Evidence gate: `/admin/metadata/push-status` `last_good_ref` + live SSE EX `exec_result match` (local067/050/060/063), not product merge SHA alone.
