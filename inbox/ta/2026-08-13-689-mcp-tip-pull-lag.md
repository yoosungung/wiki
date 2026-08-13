---
id: inbox-ta-689-mcp-tip-pull-lag
agent: ta
ticket_id: 689
updated: 2026-08-13
status: inbox
sources:
  - ticket:689
  - inbox/ta/2026-08-13-689-nl2sql-metadata-tip-resync.md
---

# MCP metadata tip lags backend after tip push

- After tip apply push, backend PVC + bare `main` advanced (e.g. `c1ebeb0` with f1 overtake vocab) while `nl2sql-mcp-metadata` stayed on prior SHA (`6ea134a`) even if `refs/remotes/origin/main` was fetched.
- Search/catalog for agent EX runs from MCP tip — resync MCP PVC (scale mcp 0 → clone `origin/main` → scale 1) before `spider2-opik` if mcp SHA ≠ remote main.
- Related recovery: k8s-test README "nl2sql metadata tip desync".
