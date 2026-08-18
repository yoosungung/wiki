---
id: path-graph-argo-imagepullbackoff-runbook
title: "path-graph stale Argo Workflow ImagePullBackOff 런북"
status: canonical
owner: km
updated: "2026-08-18"
last_updated: "2026-08-18"
review_after: "2026-11-18"
sources:
  - ticket:41
  - https://github.com/yoosungung/k8s-test/pull/1
  - schedule:ta-k8s-daily
tags: ["Infrastructure", "DevOps", "Argo", "Kubernetes", "path-graph"]
type: "wiki"
---

# path-graph stale Argo Workflow ImagePullBackOff 런북

티켓 #41 — `path-graph` 네임스페이스에서 수주간 잔존한 Argo probe/test Workflow가 `ImagePullBackOff`를 재생산하던 사건과 수정 절차.

## 증상

- ns=`path-graph`의 `*-resolve-manifest-*` Pod가 `path-graph/pipeline:0.0.0`에 대해 `ImagePullBackOff`.
- `filestash` Deployment는 Ready(1/1) 유지.
- ta-k8s-daily(2026-07-30): 9개 stale Pod, DiskPressure 없음.

## 원인

- leftover Argo probe/test Workflow가 여전히 `Running`.
- Pod는 `Workflow/<name>`이 owner이므로 **Pod만 삭제하면 재생성**.

## 수정 (Eric 승인)

```bash
# Workflow 단위 삭제(cascade로 Pod 제거). filestash Deployment Pod는 건드리지 않음.
kubectl get workflow -n path-graph
kubectl delete workflow -n path-graph <stuck-wf-names>
kubectl get pods -n path-graph   # ImagePullBackOff=0, filestash 1/1
```

## Closeout (2026-07-30)

- ta remediations 검증 후 pm이 [k8s-test PR#1](https://github.com/yoosungung/k8s-test/pull/1) 런북을 README/AGENTS에 머지(`eb26446719358e382734e3c6e9100aa351bf27c3`).
- Post-merge: ImagePullBackOff=0; filestash 1/1; 티켓 #41 → Done.
- Pitfall: Leantime MCP discovery/auth가 agent runner에서 자주 실패 — JSON-RPC Bearer로 get/update 가능; `Comments.addComment`는 insert 성공 후 notification 경로에서 `-32000`을 반환할 수 있음.

## 위생 (terminal leftover Workflow)

ImagePullBackOff가 0이어도 **Failed/Error/Succeeded terminal Workflow CR**이 수십 건 남을 수 있다(사용자 영향 없음). 정리 시에도 **Pod가 아니라 Workflow 단위 delete**. Running만 남기거나 일괄 `kubectl delete workflow -n path-graph --field-selector=status.phase!=Running` 계열로 정리.

**재확인 (일일 점검 패턴)**: filestash Ready·ImagePullBackOff=0인 상태에서도 terminal Workflow CR이 다수 남는 것은 정상 잔여로 본다. 일일 리포트에서 “abnormal pods”와 분리하고, 정리는 여전히 Workflow-delete. 의도적 scale-0 empty endpoints와 함께 판별: [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md]].

**재확인 (2026-08-03)**: filestash 1/1·ImagePullBackOff=0·Warning events 없음; terminal Error/Failed/Succeeded Workflow CR만 잔존 → 위생 대상일 뿐 incident 아님. 점검은 read-only kubectl 유지.

**재확인 (2026-08-16)**: filestash 1/1·terminal Workflow CR만 잔존 패턴 동일 → incident 아님. scale-0 empty endpoints와 함께 판별: [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md]].

**재확인 (2026-08-18)**: filestash 1/1·ImagePullBackOff=0·terminal Error/Failed/Succeeded Workflow CR만 잔존 → 위생, incident 아님. graph storage STS가 Helm 기본(예: 1Gi)보다 낮은 limit(예: 512Mi)이어도 Ready·최근 OOM 없으면 일일 티켓 없음 — live SoR.

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/000_Infrastructure-and-DevOps-MOC.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Intentional-Scale-Zero-Empty-Endpoints.md]]
- [[wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md]]
