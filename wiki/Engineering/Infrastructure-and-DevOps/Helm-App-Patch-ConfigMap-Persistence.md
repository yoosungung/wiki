---
id: helm-app-patch-configmap-persistence
title: "Helm App-Patch ConfigMap 영속화와 RBAC"
status: canonical
owner: km
updated: "2026-07-31"
last_updated: "2026-07-31"
review_after: "2026-10-31"
sources:
  - ticket:60
tags: ["Infrastructure", "DevOps", "Kubernetes", "Helm", "ConfigMap", "RBAC"]
type: "wiki"
---

# Helm App-Patch ConfigMap 영속화와 RBAC

컨테이너 안 핫픽스 파일은 **재시작 시 소실**한다. Helm이 관리하는 ConfigMap+volumeMount로 고정하고, 에이전트 SA의 CM write RBAC을 먼저 확인한다.

## 패턴

1. 패치 파일을 CM 키로 merge한다 (기존 키를 덮어쓰지 않도록 `kubectl create configmap --from-file` / strategic merge 주의).
2. Deployment에 `volumeMount` + `subPath`로 런타임 경로에 마운트한다.
3. 롤아웃 후 sha256으로 파일 일치 검증.

```yaml
# 개념 예시
volumeMounts:
  - name: app-patch
    mountPath: /var/www/html/app/.../Target.php
    subPath: Target.php
volumes:
  - name: app-patch
    configMap:
      name: leantime-app-patch
```

## RBAC 함정

| SA 권한 | 결과 |
| :--- | :--- |
| CM `get`만 | 키 존재 여부만 확인 가능; persist 불가 |
| CM `create`/`patch`/`update` 403 | 핫픽스만 남고 재시작 시 롤백 |
| Deploy patch는 가능 | volumeMount는 CM 키가 생긴 뒤에야 의미 있음 |

에이전트에 NS write를 줄 때는 **ConfigMap write**를 명시한다. Deploy-only 권한으로는 부족하다.

## 검증

- Pod 재시작 후에도 마운트 파일 mtime/sha256 유지
- 핫픽스 전용 경로가 CM에 없고 volumeMount만 있으면 restart = 원본 복귀

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Sessionless-MCP-Status-Label-Cache-Poison.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/K8s-Secret-vs-ConfigMap-Deploy-Hardening.md]]
