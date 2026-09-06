---
id: inbox-ta-2026-09-06-k8s-daily-report
agent: ta
ticket_id: 1716
updated: 2026-09-06
status: inbox
sources:
  - schedule:ta-k8s-daily
  - ticket:1716
---

# k8s daily 2026-09-06

- Cluster `didim-gpu` Ready; Disk/Memory/PID Pressure false; node mem ~40%, rootfs ~58%.
- No CrashLoop/ImagePull/Pending/Failed; Warning events 0; all 49 PVCs Bound.
- Intentional scale-0 empty endpoints: `llm-serving/sglang-gemma4-12b`, `runtime/pgbouncer-ro|rw`.
- `postgres/postgresql-0` limits 4Gi / requests 2Gi, restart 0.
- `nebula/nebula-storaged-0` restart 4: OOMKilled ~2026-09-05T22:13Z (limit 512Mi), now Ready ~77Mi — watch only; Nebula not managed by k8s-test repo.
- Outcome: 정상; Incident tickets none.
