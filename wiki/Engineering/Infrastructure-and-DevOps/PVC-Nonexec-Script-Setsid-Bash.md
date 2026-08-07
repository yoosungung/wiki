---
id: pvc-nonexec-script-setsid-bash
title: "PVC 시드 스크립트(0644) — setsid + bash 기동"
status: canonical
owner: km
updated: "2026-08-07"
last_updated: "2026-08-07"
review_after: "2026-11-07"
sources:
  - ticket:176
  - ticket:308
tags: ["Infrastructure", "DevOps", "Kubernetes", "CronJob", "Launcher"]
type: "wiki"
---

# PVC 시드 스크립트(0644) — setsid + bash 기동

CronJob/`kubectl exec` 런처가 PVC에 시드된 워커를 **`exec "$WORKER"`**로 직접 실행하면, 모드 **0644(비실행)**일 때 Permission denied(126) → completion status 미기록 → 모니터 **exit 99**(process disappeared). empty `worker.log` + Permission denied before first line이면 이 축을 먼저 본다.

## 수정

```bash
# 잘못된 예
exec "$WORKER"

# 권장 (repo SSoT)
setsid bash "$WORKER" "$@"   # 또는 exec bash|python3 …/agent/cron/…
# skill 경로 = thin shim only
#   install_skill_shims.sh <skill-scripts-dir>
# 로그는 durable 경로(예: state/agent.log); /tmp만 쓰면 Pod 재시작 시 유실
```

- `nohup ... &`만으로는 exec 세션 종료와 함께 죽을 수 있음 → **`setsid`**로 세션 분리.
- 회귀: launcher detach 단위 테스트(시드 0644 재현) + persona ConfigMap 키가 **~100B shim**인지(다KB `nohup` 풀카피 금지).

## 운영 함정

1. PVC hotfix는 다음 ConfigMap/agents.yaml **reseed에 덮어씌워질 수 있음**. Pod SA가 CM patch Forbidden이면 플랫폼/어드민 reseed가 필요. **내구성**: repo `agent/cron/`을 SSoT로 두고 skill·persona 경로는 thin `exec` shim — reseed/seed-persona가 bare `nohup`/`exec "$@"` 풀카피를 복원하면 exit 99가 재발한다. 렌더 호스트의 gitignored persona 트리도 `install_skill_shims.sh`로 재생성한 뒤 apply.
2. exit 99 다음이 exit 1이면 **런처는 통과**한 것 — 오케스트레이터가 요구하는 API 키·모델 호스트(NXDOMAIN)를 별축으로 본다.
3. **LLM Serving Ready ≠ exit 99 원인 배제 완료**. 서빙 Pod가 `/v1/models` 200·장문 decode 중이어도 호스트 watchdog(~600s)이 완료 status 전에 프로세스를 죽이면 모니터는 exit 99다 — 실패 창의 **해당 run_id 로그**를 보고, 이전 Pass 로그를 오인하지 않는다.
4. `tenant_cd` 레지스트리가 비면 Deploying Test/CD는 N/A — [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]].
5. 모니터가 zombie PID를 alive로 보면 exit 99가 재발 — [[wiki/Engineering/Infrastructure-and-DevOps/Cron-Monitor-Zombie-PID-Check.md]].

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/Cron-Monitor-Zombie-PID-Check.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
- [[wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
