---
id: crewrp-pr-local-test-evidence
title: "CrewRP PR Intent: Actions 없음 → 로컬 테스트 증거"
status: canonical
owner: km
updated: "2026-10-07"
review_after: "2027-01-06"
sources:
  - inbox/pm/2026-10-06-crewrp-pr-no-gha.md
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - https://github.com/yoosungung/CrewRP/pull/2
tags: ["Engineering", "DevEnv", "CrewRP", "CI"]
type: "wiki"
---

# CrewRP PR Intent: Actions 없음 → 로컬 테스트 증거

`yoosungung/CrewRP`는 GitHub Actions workflow가 **0개**다. PR checks가 비어 있어도 **CI pending이 아니다**.

## Intent 게이트

- 로컬 증거: `swift test` / `:crewrp-core:test` (및 해당 티켓 AC).
- 로그인된 시뮬/실기기 칸반·상세 스모크는 유닛테스트와 **별개 AC**.
- **머지 ≠ Done** — UI/기기 스모크가 남으면 Done으로 올리지 않는다.

## 관련

- [[wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md]]
- [[wiki/Engineering/AI-Native-Engineering/Intent-Pass-Diff-First-Merge.md]]
