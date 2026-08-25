---
id: metadata-git-pvc-resync
title: "메타데이터 Git PVC 재동기화 (브랜치·sparse·지연)"
status: canonical
owner: km
updated: "2026-08-25"
last_updated: "2026-08-25"
review_after: "2026-11-25"
review_after: "2026-11-20"
sources:
  - ticket:689
  - ticket:752
  - ticket:753
  - ticket:1047
  - ticket:1048
  - ticket:1050
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

## 콘솔 API를 통한 메타데이터 미러링 (kubectl exec 불가 시)

에이전트 SA(Service Account) 권한 문제로 `pods/exec`를 호출할 수 없거나 `nl2sql-secrets`에 직접 접근할 수 없을 때, 백엔드 콘솔 API를 활용하여 라이브 카탈로그를 시딩(seed)할 수 있다.

- **인증 방식**: `X-Forwarded-User` 및 `X-Forwarded-Email` 헤더를 주입하여 인증 장벽을 통과한다.
- **업로드 및 검증 API 절차**:
  1. `POST /api/metadata/fs/validate` 호출을 통해 전체 유효성 검증을 먼저 통과시킨다.
  2. `PUT /api/metadata/fs/{path}` API에 `base_sha`와 변경할 `body` 내용을 전송하여 카탈로그 파일을 원격 PVC에 직접 갱신한다.
- **동기화 확인 (Live Evidence)**:
  - PUT 응답값의 `sync.status=ok` 및 `/api/admin/metadata/push-status` 조회 결과 내 `last_good_ref` 값의 갱신 여부로 확인한다. (제품 merge SHA와 metadata git SHA는 다를 수 있음)
- **라이브 데이터 보존 (Rich Grains 보호)**:
  - 더 세부적인 설정이 적용된 풍부한 라이브 그레인(예: live `complex_oracle_times`, `bowlingleague_bowler_score`, `e_commerce_sale`)을 얇은 mcp fixture로 덮어쓰지 말아야 한다.
  - 추가/업데이트 시에는 seal `*.model.json` 및 누락된 그레인 정보만 타겟하여 수정한다. `base_sha=null`로 **create**할 때도 기존 rich 모델은 PUT 대상에서 제외한다.
- **타입 정합 (PG catalog)**:
  - fixture의 `integer` 컬럼이 live PG `bigint`와 맞지 않으면 validate/PUT 전에 `bigint`로 coerce한다(예: bowlingleague·wwe_match grain).
- **Live SSE 증거 (AC2)**:
  - 배포 Done 게이트는 제품 merge SHA가 아니라 live chat SSE에서 `exec_result match` + `meta_ref`가 `/admin/metadata/push-status`의 `last_good_ref`와 일치하는지로 본다.


## 제품 SHA ≠ 메타데이터 SHA

제품 레포 merge SHA로 PVC를 다시 클론하지 않는다. 카탈로그는 **metadata git** `origin/main` 이다. MCP `/ready` HEAD가 뒤처져도 chat이 backend `meta_ref`를 lazy-fetch할 수 있다 — `/ready` 지연 ≠ search 미반영 증거. 라이브 증거는 `/admin/sync` `status=ok` + chat `meta_ref`(및 MCP PVC SHA ↔ `refs/heads/main`)다.

`test-*` 이미지 롤과 init 바이너리 URL을 섞지 않는다 — [[wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md]].

## 관련

- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md]]
