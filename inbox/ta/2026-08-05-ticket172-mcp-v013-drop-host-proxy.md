---
id: inbox-ta-2026-08-05-ticket172-mcp-v013-drop-host-proxy
agent: ta
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/31
  - https://github.com/yoosungung/nl2sql/actions/runs/30970782274
  - https://github.com/yoosungung/nl2sql-releases/releases/tag/v0.1.3
---

# #172 mcp v0.1.3 live; host-proxy removed

- After PR #31 merge (`499bd3f`), published `Publish to nl2sql-releases` → tag **v0.1.3** (run 30970782274 success).
- Live pin: initContainer fetches `nl2sql-mcp-linux-amd64` @ v0.1.3 · sha256 `3acba22213d99cf55bfcca16c73d8d6862cc5a48dfb2ee9cdcfb9ef823b1817a`.
- ConfigMap `MCP_ALLOWED_HOSTS=nl2sql-mcp,nl2sql-mcp:8800,localhost,127.0.0.1,::1`.
- Verified Service `initialize` Host `nl2sql-mcp:8800` → **HTTP 200** with single container `mcp` (no nginx sidecar).
- Deleted CM `nl2sql-mcp-host-proxy`; bind restored `0.0.0.0:8800`.
- Durable follow-up: bump `deploy/k8s/overlays/test/patch-mcp-binary.yaml` in nl2sql repo (still pins v0.1.1 in git).
