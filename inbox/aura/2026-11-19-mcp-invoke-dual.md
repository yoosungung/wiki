---
id: inbox-aura-mcp-invoke-dual
agent: aura
ticket_id: ae7ca986-f35b-4809-950e-f875f326fc4a
updated: 2026-11-19
status: inbox
sources:
  - ticket:ae7ca986-f35b-4809-950e-f875f326fc4a
---

# mcp_invoke dual path

- MQT `aura.tasks.mcp.invoke` / consumer `aura_mcp_invoke` / minReplicaCount=0
- RPC `aura.rpc.mcp.tool` Warm minReplicas≥2 (no MQT)
- Gate: check-mcp-invoke-dual.sh · PR#37
