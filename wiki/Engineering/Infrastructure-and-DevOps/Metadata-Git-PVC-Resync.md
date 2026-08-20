---
id: metadata-git-pvc-resync
title: "메타데이터 Git PVC 재동기화 (브랜치·sparse·지연)"
status: canonical
owner: km
updated: "2026-08-20"
last_updated: "2026-08-20"
review_after: "2026-11-20"
sources:
  - ticket:689
  - ticket:752
  - ticket:753
  - ticket:1047
  - ticket:1048
tags: ["Infrastructure", "DevOps", "Git", "Kubernetes", "PVC", "MCP"]
type: "wiki"
---

# 메타데이터 Git PVC 재동기화 (브랜치·sparse·지연)

앱이 메타데이터를 **in-cluster git-http + PVC worktree**에 두면, push 성공 ≠ 검색/카탈로그 반영이다. 에이전트 EX·search는 **MCP(또는 catalog sidecar) tip SHA**를 본다. **제품 git 픽스처 ≠ live catalog** — tip EX는 metadata git seed + `/admin/sync` `status=ok`가 필요하다.

## 증상 → 원인

| 증상 | 원인 |
| :--- | :--- |
| `push_failed` `src refspec 'refs/heads/main' does not match any existing object` | PVC HEAD가 `master`이고 `refs/heads/main`이 없음. 앱은 `METADATA_GIT_BRANCH=main` |
| 백엔드 PVC는 새 SHA, MCP PVC는 이전 SHA | fetch만 되고 checkout/reset 안 됨. search는 MCP 쪽 |
| working tree가 스키마 일부만 | sparse/부분 clone. bare는 풀 카탈로그인데 worktree만 빈약 |
| 소스 zip은 에이전트 PVC, 배포 checkout은 얕음 | 대용량 `localdb`는 앱 Pod PVC에 있음. ephemeral tenant clone과 혼동 금지 |

## 재동기화

```bash
# 개념: 양쪽 PVC를 origin/main으로 재클론한 뒤 기동
kubectl scale deploy/<backend> <mcp> --replicas=0
# PVC 안에서: git clone origin/main (브랜치 main 고정)
kubectl scale deploy/<backend> <mcp> --replicas=1
# 스모크: mcp SHA == remotes/origin/main 후에 search / EX
```

인증 401과 혼동하지 않는다 — [[wiki/Engineering/Infrastructure-and-DevOps/Git-HTTP-Basic-Auth-Username-Env.md]]. RWO면 scale 0이 Recreate보다 안전하다 — [[wiki/Engineering/Infrastructure-and-DevOps/RWO-PVC-Recreate-Deploy-Strategy.md]].

## 제품 SHA ≠ 메타데이터 SHA

제품 레포 merge SHA로 PVC를 다시 클론하지 않는다. 카탈로그는 **metadata git** `origin/main` 이다. MCP `/ready` HEAD가 뒤처져도 chat이 backend `meta_ref`를 lazy-fetch할 수 있다 — `/ready` 지연 ≠ search 미반영 증거. 라이브 증거는 `/admin/sync` `status=ok` + chat `meta_ref`(및 MCP PVC SHA ↔ `refs/heads/main`)다.

`test-*` 이미지 롤과 init 바이너리 URL을 섞지 않는다 — [[wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md]].

## 관련

- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md]]
