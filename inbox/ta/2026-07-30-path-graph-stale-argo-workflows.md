---
id: inbox-ta-path-graph-stale-argo-workflows
agent: ta
ticket_id: 41
updated: 2026-07-30
status: inbox
sources:
  - ticket:41
---

# path-graph stale Argo Workflow ImagePullBackOff

- Symptom: `path-graph` ns `*-resolve-manifest-*` pods stuck `ImagePullBackOff` on `path-graph/pipeline:0.0.0` for weeks; filestash Ready.
- Cause: leftover Argo probe/test Workflows still `Running`; pods owned by `Workflow/<name>` so deleting pods alone recreates them.
- Fix (Eric-approved): `kubectl delete workflow -n path-graph <stuck-wf-names>` (cascade removes pods). Do not delete filestash Deployment pods.
- Verify: `kubectl get pods -n path-graph` shows no ImagePullBackOff; filestash 1/1.
