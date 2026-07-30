---
id: inbox-ta-2026-07-30-k8s-daily-report
agent: ta
ticket_id: 42
updated: 2026-07-30
status: inbox
sources:
  - ticket:42
  - ticket:41
  - kubectl:read-only ta-k8s-daily
---

# k8s daily 2026-07-30 (ta-k8s-daily)

- Node `didim-gpu` Ready; DiskPressure=False; allocatable nvidia.com/gpu=2.
- `sglang-gemma4-12b` x2 Running (1 GPU each) blocks `sglang-gemma4-31b` (needs 2) → Pending 23d; Leantime #42 Waiting for Approval.
- `path-graph` 9 stale Argo `*-resolve-manifest-*` pods ImagePullBackOff on `path-graph/pipeline:0.0.0` (26d); filestash Ready; Leantime #41 New.
- All PVCs Bound; `sw-factory` (leantime + agents) Ready; no DiskPressure.
- Leantime MCP discovery/auth failed in agent runner; JSON-RPC Bearer worked as fallback.
