---
id: git-http-basic-auth-username-env
title: "Git HTTP basic-auth username을 env로 분리"
status: canonical
owner: km
updated: "2026-08-12"
last_updated: "2026-08-12"
review_after: "2026-11-12"
sources:
  - ticket:564
tags: ["Infrastructure", "DevOps", "Git", "Kubernetes", "Config"]
type: "wiki"
---

# Git HTTP basic-auth username을 env로 분리

앱/MCP가 GitLab deploy-token용 basic-auth user `oauth2`를 하드코딩하면, in-cluster `git-http` htpasswd가 `git`만 있을 때 `oauth2:token` → **HTTP 401**이 난다.

## 패턴

```text
METADATA_GIT_HTTP_USER / MCP_GIT_HTTP_USER   # 또는 *_USERNAME
default: oauth2   # 외부 GitLab 호환
test overlay: git + http://git-http-server.<ns>.svc:80/git/<repo>.git
```

## 롤아웃 함정

새 이미지(코드가 username env를 읽음) **이전**에 Pod를 재시작하면:

1. `ensure_origin`이 PVC remote URL-creds를 덮어쓰고
2. 구 바이너리가 여전히 `oauth2`로 fetch → CrashLoop

**순서**: 이미지/ConfigMap(username=`git`) 라이브 확인 → 그다음 restart.

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Helm-App-Patch-ConfigMap-Persistence.md]]
