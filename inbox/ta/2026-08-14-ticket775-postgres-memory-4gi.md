---
id: inbox-ta-2026-08-14-ticket775-postgres-memory-4gi
agent: ta
ticket_id: 775
updated: 2026-08-14
status: inbox
sources:
  - ticket:775
  - ticket:751
  - ticket:767
---

# Shared postgres memory 512Mi → 4Gi (#775)

- `postgresql-0` (ns `postgres`, Hermes+spider2db 공유) cgroup **limit 512Mi**에서 Full EX 백엔드가 SIGKILL → `server closed the connection unexpectedly`. 컨테이너 Restart는 0.
- 클러스터 전역 `statement_timeout`은 Hermes 정상 쿼리까지 자를 수 있어 쓰지 않음.
- SoR: k8s-test `helm/values/postgresql.yaml` `primary.resources` **limit 4Gi / request 2Gi**. 게이트 `scripts/test-postgresql-resources.sh`.
- `didim-gpu` 여유(~9%→11% requests, ~31%→34% limits of ~125Gi)로 4Gi 스케줄 OK. helm CLI 없는 runner는 STS patch로 즉시 적용.
- 함정: Helm values만 바꾸고 live STS를 안 맞추면 다음 `deploy.sh` 전까지 512Mi가 남는다.