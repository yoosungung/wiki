---
id: ghcr-actions-package-write-acl
title: "GHCR: Actions packages:write ≠ 패키지 Manage ACL"
status: canonical
owner: km
updated: "2026-08-04"
last_updated: "2026-08-04"
review_after: "2026-11-04"
sources:
  - ticket:60
  - https://stackoverflow.com/questions/70646920/github-token-permission-denied-write-package-when-build-and-push-docker-in-github-workflows
tags: ["Infrastructure", "DevOps", "GHCR", "GitHub-Actions", "ACL"]
type: "wiki"
---

# GHCR: Actions packages:write ≠ 패키지 Manage ACL

워크플로에 `permissions: packages: write`가 있고 `docker login`·빌드가 성공해도, **기존 패키지 ACL**에 리포가 Write로 없으면 blob `HEAD`/`PUT`이 **403**이다.

## 증상

```text
# login OK, build OK
HEAD …/blobs/sha256:… 403 Forbidden
# → ghcr.io/<owner>/<image>:tag push 실패
```

전형 원인: 패키지를 예전에 **PAT로 생성** → Actions 리포가 package **Manage Actions access**에 없음.

## 수정 (인간)

1. GitHub Packages → 해당 패키지 → **Manage Actions access**에 워크플로 리포를 **Write**로 추가, 또는
2. 패키지 삭제 후 Actions가 재생성하도록 재실행

이후: 워크플로 재실행 → 런타임 STS/Deploy rollout → 앱/MCP 스모크.

## 축 분리

- Test overlay apply ≠ GHCR publish — [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
- git Contents Write ≠ packages Write — [[wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md]]

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md]]
