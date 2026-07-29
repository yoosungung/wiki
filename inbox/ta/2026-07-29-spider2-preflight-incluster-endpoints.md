---
id: inbox-ta-spider2-preflight-incluster-endpoints
agent: ta
ticket_id: 32
updated: 2026-07-29
status: inbox
sources:
  - ticket:32
  - repo:k8s-test/README.md
---

# Spider2 #37 preflight: in-cluster endpoints from sw-factory

- Agent runners in `sw-factory` cannot resolve short/LAN hosts `k8s-test` / `opik.k8s-test` (DNS search is `*.svc.cluster.local`).
- From `cursor-agent-ta-0` (ns=sw-factory): TCP OK to `postgresql.postgres.svc.cluster.local:5432`; HTTP 200 to `http://opik-frontend.opik.svc.cluster.local:5173` and `/api`.
- For in-cluster `.env` / #37 smoke: use ClusterIP FQDNs — PG host `postgresql.postgres.svc.cluster.local:5432`; Opik `OPIK_URL_OVERRIDE=http://opik-frontend.opik.svc.cluster.local:5173/api` (see k8s-test README Opik section). Do not rely on NodePort/`*.k8s-test` without hosts injection.
