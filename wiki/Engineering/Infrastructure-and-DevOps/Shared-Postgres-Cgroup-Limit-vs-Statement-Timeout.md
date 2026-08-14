---
id: shared-postgres-cgroup-limit-vs-statement-timeout
title: "공유 Postgres: cgroup limit vs statement_timeout"
status: canonical
owner: km
updated: "2026-08-14"
last_updated: "2026-08-14"
review_after: "2026-11-14"
sources:
  - ticket:775
tags: ["Infrastructure", "DevOps", "PostgreSQL", "Kubernetes", "Helm", "OOM"]
type: "wiki"
---

# 공유 Postgres: cgroup limit vs statement_timeout

벤치/Full EX가 공유 Postgres를 때릴 때 **클라이언트 `server closed the connection unexpectedly`** 는 쿼리 타임아웃이 아니라 **cgroup OOM(SIGKILL)** 일 수 있다. 컨테이너 Restart=0이어도 프로세스가 죽었을 수 있다.

## 축 분리

| 증상 | 원인 | 조치 |
| :--- | :--- | :--- |
| 연결이 갑자기 끊김, Pod OOMKilled/시그널 | STS `resources.limits.memory` 부족 | Helm values의 **limit/request를 올리고 live STS와 일치** |
| 정상 OLTP까지 잘림 | 클러스터 전역 `statement_timeout` | 전역 타임아웃으로 벤치를 막지 말 것 |

전역 `statement_timeout`은 공유 DB의 짧은 정상 쿼리까지 자른다. 메모리 한도를 먼저 맞춘다.

## Helm values ≠ live STS

values만 바꾸고 live StatefulSet을 안 맞추면 다음 `deploy.sh` 전까지 옛 limit가 남는다.

```yaml
# 개념: helm/values/postgresql.yaml
primary:
  resources:
    requests:
      memory: 2Gi
    limits:
      memory: 4Gi
```

- deploy 스크립트가 `-f values.yaml` 이고 `--reuse-values`가 없으면 다음 upgrade가 옛 limit로 회귀하지 않는다.
- 러너에 helm CLI/`secrets` get이 없으면 `helm get values`는 못 읽는다. **live STS `resources`를 직접 확인**한다.
- helm이 없을 때는 STS patch로 즉시 적용하되, SoR은 git values + 게이트 스크립트다.

## 함정

- 공유 인스턴스의 빈 부가 DB(사용자 테이블 0)를 같은 티켓에서 DROP하지 않는다. 삭제는 별 승인.
- 노드 여유(requests/limits vs allocatable)를 보고 스케줄 가능한 limit만 올린다.

## 관련

- [[wiki/Engineering/Infrastructure-and-DevOps/Helm-App-Patch-ConfigMap-Persistence.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/RWO-PVC-Recreate-Deploy-Strategy.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
