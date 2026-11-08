---
id: gha-macos-14-runner-retirement-hotfix
title: "GHA macOS-14 runner 폐기 → macos-15 + tag re-dispatch"
status: canonical
owner: km
updated: "2026-11-09"
last_updated: "2026-11-09"
review_after: "2027-02-01"
sources:
  - inbox/ta/2026-11-09-rhwp-batch-macos14-retire-release-hotfix.md
  - inbox/pm/2026-11-09-pm-checkpoint-rhwp-v090-macos14-unsupported.md
  - inbox/pm/2026-11-09-pm-checkpoint-rhwp-v090-release-cancelled.md
  - inbox/pm/2026-11-09-pm-checkpoint-rhwp-v090-release-success-await-seal.md
  - ticket:0f34dece-193b-4a93-bca5-6c8d408fb620
  - https://github.blog/changelog/2026-10-01-github-actions-macos-14-runner-image-retirement/
  - https://github.com/actions/runner-images/issues/13518
  - https://github.com/yoosungung/rhwp_batch/pull/7
  - https://github.com/yoosungung/rhwp_batch/actions/runs/42529172553
tags: ["Engineering", "AI-Native", "GitHub-Actions", "macOS", "CI"]
type: "wiki"
---

# GHA macOS-14 runner 폐기 → macos-15 + tag re-dispatch

GitHub Actions는 **2026-11-02**에 `macos-14` / `macos-14-large` / `macos-14-xlarge` 이미지를 폐기했다. 이후 해당 `runs-on` 잡은 annotation `macos-14-arm64-us-default is not supported`와 함께 ~1s·빈 steps·`runner_id=0`으로 즉시 실패한다. 이는 [[wiki/Engineering/AI-Native-Engineering/Actions-Budget-Blocks-CI-Rerun.md]]의 **분 예산 고갈**과 신호가 비슷하지만 원인·복구가 다르다.

## 판별

| 신호 | 해석 |
| :--- | :--- |
| annotation: `…macos-14… is not supported` | 러너 이미지 폐기 — 워크플로 라벨 핫픽스 |
| mac job ~1s, steps empty, `runner_id=0`; linux green | 플랫폼/라벨 차단 — 제품 회귀 아님 |
| annotation: Actions budget/minutes | 예산 축 — budget 페이지 |

## 핫픽스 패턴 (rhwp_batch v0.9.0 증거)

1. mac matrix를 **`macos-15`**(또는 정책상 `macos-26`/`macos-latest`)로 핀.
2. 이미 push된 annotated tag를 다시 태울 수 있게 `workflow_dispatch` + `tag` input 추가 — **force-retag 금지**.
3. Evidence: PR #7 merge `9e10cc9` → dispatch run 42529172553 success (linux+mac+publish+docker) → GH Release `v0.9.0` assets.

## 운영 규칙

1. unsupported-runner 실패에 빈 커밋·동일 SHA re-run을 반복하지 않는다(분 낭비; 라벨이 그대로면 동일 실패).
2. IC는 워크플로 `runs-on` 핫픽스(option1)를 우선; platform restore(option2)는 이미지 복구가 있을 때만.
3. Xcode 15 하드코딩 경로·iOS 17 simulator는 macos-15 이미지에 없을 수 있다 — Apple 빌드 잡은 이미지 README를 확인.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Actions-Budget-Blocks-CI-Rerun.md]]
- [[wiki/Engineering/Development-Environment/Cargo-Nested-Workspace-Vendor-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md]]
