---
id: inbox-ta-ticket391-test-eb4bc95-mcp-pending
agent: ta
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/59
  - https://github.com/yoosungung/nl2sql/actions/runs/31460241537
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# #391 tip test-eb4bc95 — backend OK, MCP duckdb build pending

- PR #59 merged `eb4bc95`; registry `deploy.yml` absent → Test-Overlay via `publish-releases` `tag=test-eb4bc95`.
- Backend tip rolled: `ghcr.io/yoosungung/nl2sql-backend:test-eb4bc95`; smoke `/api/health`+`/api/ready` = 200.
- Live MCP still init-fetches `nl2sql-releases` **v0.1.3** binary (not tip). SoT 1870 residual `dialect_unparse` needs MCP tip (`ghcr.io/yoosungung/nl2sql-mcp:test-eb4bc95` after `build-mcp-linux`).
- `build-mcp-linux` bookworm+duckdb compile often 30–60m; do **not** cancel until artifact/image push if AC3 needs decimal fix.
- Next: MCP image ready → switch mcp Deployment to GHCR tip (drop ubuntu fetch init) → AC3 `local008,local022` → QA/@qa/@aa or bounce.
