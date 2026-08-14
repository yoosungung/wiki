---
id: inbox-ta-753-skip-product-sha-pvc
agent: ta
ticket_id: 753
updated: 2026-08-14
status: inbox
sources:
  - ticket:753
  - ticket:752
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md
---

# #753 do not PVC-resync to product SHA

- Metadata git SHA ≠ product-repo merge SHA. #753 merge `251af64c` is nl2sql product; tip catalog lives on `nl2sql-metadata.git` (`44d30eb8`).
- After #752/#3701 re-clone, both tip PVCs and MCP `/ready` already match `origin/main` @ `44d30eb8` including modern_data seals. A second scale-0 to chase the product SHA is wrong.
- Keep published MCP image/binary (`test-*` image OK; do not rewrite init binary URL to `test-*`).
