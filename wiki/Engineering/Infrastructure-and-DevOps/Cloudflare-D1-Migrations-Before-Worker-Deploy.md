---
id: cloudflare-d1-migrations-before-worker-deploy
title: "D1 마이그레이션은 Worker deploy보다 먼저"
status: canonical
owner: km
updated: "2026-09-19"
last_updated: "2026-09-19"
review_after: "2026-12-18"
sources:
  - inbox/ta/2026-09-18-d1-migrations-on-deploy.md
  - ticket:22f76e62-a1de-43b6-8032-086d35d127db
  - https://developers.cloudflare.com/d1/wrangler-commands/
tags: ["Engineering", "DevOps", "Cloudflare", "D1", "Workers"]
type: "wiki"
---

# D1 마이그레이션은 Worker deploy보다 먼저

`wrangler deploy`는 Worker 스크립트만 배포한다. D1 스키마는 [`d1 migrations apply`](https://developers.cloudflare.com/d1/wrangler-commands/)로 따로 적용한다. 마이그레이션이 추가한 컬럼을 읽는 SQL이 먼저 나가면 SELECT/INSERT가 HTTP 500이 된다.

## 순서

바인딩 이름은 Wrangler 설정의 D1 binding이다. 원격(배포된 Worker가 보는 DB)은 `--remote`.

```bash
npx wrangler d1 migrations apply <BINDING> --remote
npx wrangler deploy
```

로컬 `wrangler dev`는 `--local`. 프리뷰 DB는 `--preview`. 환경이 나뉘면 `--env`를 apply와 deploy 양쪽에 맞춘다.

`npm run deploy`(또는 동등 스크립트)가 **apply 성공 후에만** deploy를 호출하게 두면, Actions와 수동 배포가 같은 순서를 탄다. 스키마를 먼저, 코드를 나중에.

## 함정

- **확인 프롬프트**: 대화형 CLI는 apply 전 확인을 묻는다. CI 등 비대화형은 확인을 건너뛰지만 **백업은 캡처**한다. 한 마이그레이션이 실패하면 그 건만 롤백되고, 이전 성공분은 유지된다.
- **재실행 안전**: 이미 적용 기록에 있는 파일은 no-op이다. 같은 명령을 배포 잡마다 돌려도 된다.
- **토큰 분리**: Workers 편집 권한만으로는 D1 apply가 거절될 수 있다. Cloudflare 토큰에 D1 편집이 필요하다. GitHub Actions에서 워크플로 YAML 자체를 고치려면 토큰에 `workflow` 스코프가 필요하다(Workers 배포 토큰과 별개).
- **증상 축**: 코드는 새 컬럼을 가정하는데 원격 DB에 그 컬럼이 없으면 500. 앱 로직 버그로 보기 전에 원격 `migrations list`와 apply 여부를 먼저 본다.

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
