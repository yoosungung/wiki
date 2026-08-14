---
id: inbox-ta-2026-08-14-ticket775-helm-live-4gi
agent: ta
ticket_id: 775
updated: 2026-08-14
status: inbox
sources:
  - ticket:775
  - https://github.com/yoosungung/k8s-test/pull/4
---

# Helm values vs live STS 4Gi (#775)

- `origin/main` `helm/values/postgresql.yaml` 과 live `postgresql-0`/`sts/postgresql` 모두 **limit 4Gi / request 2Gi**. PR #4 merge `bdc4556`.
- `deploy.sh`는 `-f helm/values/postgresql.yaml` 이고 `--reuse-values` 없음 → 다음 Helm upgrade가 512Mi로 회귀하지 않음.
- ta runner에 helm CLI 없음 + `secrets` get 불가 → `helm get values`는 못 읽음. live STS는 이미 4Gi.
- `hermesdb`: 사용자 테이블 0, size ~8MB, 현재 세션 없음. Bitnami `auth.database` + `deploy.sh` pgvector 대상이라 **이 티켓에서 DROP 금지**. 삭제는 별 티켓+Eric 승인.
