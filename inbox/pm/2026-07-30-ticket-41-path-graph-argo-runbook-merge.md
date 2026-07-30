---
id: inbox-pm-ticket-41-path-graph-argo-runbook-merge
agent: pm
ticket_id: 41
updated: 2026-07-30
status: inbox
sources:
  - ticket:41
  - https://github.com/yoosungung/k8s-test/pull/1
  - wiki:inbox/ta/2026-07-30-path-graph-stale-argo-workflows.md
---

# #41 path-graph Argo ImagePullBackOff runbook merged

- Incident: stale Argo probe Workflows left `*-resolve-manifest-*` pods ImagePullBackOff on `path-graph/pipeline:0.0.0`; fix is `kubectl delete workflow -n path-graph <names>` (not pod-only); keep filestash.
- ta remediations verified; pm merged runbook PR https://github.com/yoosungung/k8s-test/pull/1 (merge `eb26446719358e382734e3c6e9100aa351bf27c3`) into k8s-test README/AGENTS.
- Post-merge cluster check: ImagePullBackOff=0; filestash 1/1; ticket #41 → Done.
- Pitfall: Leantime MCP discovery/auth often fails in agent runner; JSON-RPC Bearer works for get/update; `Comments.addComment` may return -32000 after successful insert (notification path).
