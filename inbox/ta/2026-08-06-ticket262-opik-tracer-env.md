---
id: inbox-ta-ticket262-opik-tracer-env
agent: ta
ticket_id: 262
updated: 2026-08-06
status: inbox
sources:
  - ticket:262
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - https://www.comet.com/docs/opik/tracing/log_traces
  - https://www.comet.com/docs/opik/self-host/kubernetes
---

# nl2sql backend OpikTracer needs OPIK_* on ConfigMap

- Backend `OpikTracer` (tags `nl2sql`/`deepagents`) is off unless `OPIK_URL_OVERRIDE` is set (DESIGN §2.6).
- In-cluster value: `http://opik-frontend.opik.svc.cluster.local:5173/api` + `OPIK_WORKSPACE=default` on `nl2sql-config`.
- #262 live inject + rollout produced Trace `019fd61b-aaed-7d3c-9d18-d64ce8f6bbaf` (thread `ticket262-opik-trace-616fc15e`) with both tags.
- `kubectl apply -k deploy/k8s/overlays/test` without those keys in the ConfigMap patch wipes the live inject — persist in tenant `patch-configmap-llm.yaml`.
