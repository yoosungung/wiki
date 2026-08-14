---
id: inbox-ta-2026-08-14-k8s-daily-report
agent: ta
ticket_id: none
updated: 2026-08-14
status: inbox
sources:
  - schedule:ta-k8s-daily
  - wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md
  - wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md
  - wiki/Engineering/Infrastructure-and-DevOps/path-graph-Argo-ImagePullBackOff-runbook.md
---

# ta-k8s-daily 2026-08-14

- Node `didim-gpu` Ready; DiskPressure/MemoryPressure/PIDPressure=False; disk used ~43%; GPU 2/2 on `sglang-gemma4-12b` 2/2.
- CrashLoop/ImagePull/Pending PVC=0. All desired Deploy/STS Ready except allowlisted `runtime/pgbouncer-{ro,rw}` replicas=0 (empty endpoints).
- SGLang `/v1/models` 200 `max_model_len=40960` + tiny chat 200; TEI `/health` 200; nl2sql `:8080/health` 200; Leantime HTTP 302; postgres/mariadb TCP OK.
- postgres `postgresql-0` single Unhealthy readiness at 00:43Z then Ready 1/1 — probe flake, not incident.
- runtime Redis: Ready via `redis-cli ping` loopback; ClusterIP/pod IP connection refused from operator (known pitfall / runtime policy) — not ticketed.
- path-graph terminal Workflow CR ~100 (Error/Failed/Succeeded); filestash 1/1 — hygiene only.
- New since last drain: PVC `sw-factory/agent-runtime-backup` Bound 1Gi; CronJob `cursorbridge-agent-restart`.
- Leantime MCP discovery failed in runner; JSON-RPC Bearer worked. Open k8s/incident tickets: none (#590 Done; mcp 1/1).
- k8s-test worktree was `feature/426-sglang-gemma4-12b-context-40k` with local mods — did not `git pull` main.
