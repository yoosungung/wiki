---
id: org-wiki-pages-deploy-sync-timeout
title: "org-wiki Quartz→GitHub Pages deploy sync timeout"
status: canonical
owner: km
updated: "2026-11-10"
review_after: "2027-02-10"
sources:
  - ticket:2567ad37-b7e3-45db-9c8b-7f971aa00182
  - https://github.com/yoosungung/wiki/actions/runs/42739993452
  - https://github.com/yoosungung/wiki/actions/runs/42717241880
  - https://github.com/actions/deploy-pages/issues/165
tags: ["Engineering", "Infrastructure", "GitHub-Pages", "Quartz", "org-wiki"]
type: "wiki"
---

# org-wiki Quartz→GitHub Pages deploy sync timeout

`yoosungung/wiki` Deploy workflow가 **build success** 뒤 `actions/deploy-pages@v4`에서만 실패하면, 제품/콘텐츠 회귀보다 **GitHub Pages sync 지연 + 10분 하드캡**을 먼저 의심한다.

## 판별

| 신호 | 해석 |
| :--- | :--- |
| build job green, deploy step `Timeout reached, aborting!` | Pages sync wall clock > action/backend 10m |
| 로그가 `deployment_queued` → 장시간 `syncing_files` | 백엔드 동기화 지연 (artifact ~40MB 전후에서도 간헐) |
| tip 다음 push의 Deploy는 ~1–2분에 succeed | 일시 flake; 동일 SHA re-run은 deployment id=SHA라 cancel 후 즉시 실패하기 쉬움 |
| annotation budget/minutes · job 수초 empty | 다른 축 — [[wiki/Engineering/AI-Native-Engineering/Actions-Budget-Blocks-CI-Rerun.md]] |

## 운영 규칙

1. **timeout 입력 상향은 무효** — `deploy-pages`는 `Math.min(timeout, 600000)`이고 Pages 백엔드도 ~10m을 강제한다 ([deploy-pages#165](https://github.com/actions/deploy-pages/issues/165)).
2. 실패 run을 **Re-run**하지 말고 **새 tip commit**(정상 inbox/wiki push)으로 재배포한다. cancel된 deployment id는 commit SHA다.
3. 동시 push가 많으면 concurrency `cancel-in-progress: true`로 tip만 배포한다 (느린 구 SHA에 10분을 쓰지 않음).
4. `wiki.askwho.net` HTTP 200만으로 새 tip 반영을 단정하지 않는다 — 이전 artifact가 계속 서빙될 수 있다. Actions tip conclusion을 본다.

## 증거 (2026-11-10)

- fail `42739993452` (c6afa78): deploy ~10m `syncing_files` → Timeout
- success `42740527660` (3550498): deploy ~90s; site `https://wiki.askwho.net` 200
