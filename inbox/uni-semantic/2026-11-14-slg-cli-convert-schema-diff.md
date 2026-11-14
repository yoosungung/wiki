---
id: inbox-uni-semantic-slg-cli-convert-schema-diff
agent: uni-semantic
ticket_id: 9abce257-5cad-4b93-ae94-8f11b09857a4
updated: 2026-11-14
status: inbox
sources:
  - ticket:9abce257-5cad-4b93-ae94-8f11b09857a4
  - ARCHITECTURE.md§5
---

# uni-semantic `slg` CLI (pbip→lookml · schema-diff)

- Cargo bin crate `cli/` package name `slg`: `convert --from pbip --to lookml` and `schema-diff`.
- Hub-only: `frontend_powerbi::parse_bim` → IR → `backend_looker::emit_lookml` (no spoke↔spoke).
- `--from pbip` reads BIM JSON file or dir (`model.bim` / `*.bim.json`); full PBIP/TMDL still out of frontend scope.
- `schema-diff` compares IR `fingerprint` (kind+name) only — CLI, no GUI.
- Verify: `cargo test -p slg`; fixture BIM/LookML fingerprints can be identical on shared table/metric names.
