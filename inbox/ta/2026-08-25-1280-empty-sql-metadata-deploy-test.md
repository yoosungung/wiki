---
id: inbox-ta-1280-empty-sql-metadata-deploy-test
agent: ta
ticket_id: 1280
updated: 2026-08-25
status: inbox
sources:
  - ticket:1280
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #1280 Deploying Test — metadata seals PUT + SSE

- Product merge_sha `88c12f0` (PR #122). Delta is mcp fixtures/catalog TDD only — no backend runtime change.
- Tip image kept `nl2sql-backend:test-e7fd808` (prior Kaniko). Do not thin-overwrite live `bowlingleague_bowler_score` / `e_commerce_sale` grains with tip fixtures (live richer).
- AC3: FS validate+PUT create (no base_sha) for new seals; `integer`→`bigint` coerce for bowlingleague/wwe_match. `last_good_ref=42dd54eb…` sync ok.
- AC2: live SSE local197 + local128 → non-empty SQL + `sql_result`; meta_ref matches push-status. local128 used `__refsql_bowlingleague_triple_venue_handicap_wins`.
- GH `build-ghcr-images` `environment` input 422; tag=`test-88c12f0` backend-only dispatch optional (metadata path does not require tip rebuild).
