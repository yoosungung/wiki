---
id: pvc-nonexec-script-setsid-bash
title: "PVC 시드 스크립트(0644) — setsid + bash 기동"
status: canonical
owner: km
updated: "2026-08-05"
last_updated: "2026-08-05"
review_after: "2026-11-05"
sources:
  - ticket:176
tags: ["Infrastructure", "DevOps", "Kubernetes", "CronJob", "Launcher"]
type: "wiki"
---

# PVC 시드 스크립트(0644) — setsid + bash 기동

CronJob/`kubectl exec` 런처가 PVC에 시드된 워커를 **`exec "$WORKER"`**로 직접 실행하면, 모드 **0644(비실행)**일 때 Permission denied(126) → completion status 미기록 → 모니터 **exit 99**(process disappeared).

## 수정

```bash
# 잘못된 예
exec "$WORKER"

# 권장
setsid bash "$WORKER" "$@"   # 또는 exec bash "$@"
# 로그는 durable 경로(예: state/agent.log); /tmp만 쓰면 Pod 재시작 시 유실
```

- `nohup ... &`만으로는 exec 세션 종료와 함께 죽을 수 있음 → **`setsid`**로 세션 분리.
- 회귀: launcher detach 단위 테스트(시드 0644 재현).

## 운영 함정

1. PVC hotfix는 다음 ConfigMap/agents.yaml **reseed에 덮어씌워질 수 있음**. Pod SA가 CM patch Forbidden이면 플랫폼/어드민 reseed가 필요.
2. exit 99 다음이 exit 1이면 **런처는 통과**한 것 — 오케스트레이터가 요구하는 API 키·모델 호스트(NXDOMAIN)를 별축으로 본다.
3. `tenant_cd` 레지스트리가 비면 Deploying Test/CD는 N/A — [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]].

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
