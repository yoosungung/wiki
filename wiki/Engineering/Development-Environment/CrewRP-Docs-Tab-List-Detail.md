---
id: crewrp-docs-tab-list-detail
title: "CrewRP 자료실 탭: 목록→상세·lazy 드릴다운"
status: canonical
owner: km
updated: "2026-10-10"
review_after: "2027-01-09"
sources:
  - inbox/pm/2026-10-09-crewrp-docs-tab-ux.md
  - inbox/crewrp/2026-10-09-crewrp-docs-tab-list-detail.md
  - inbox/crewrp/2026-10-09-crewrp-docs-tab-emu-smoke.md
  - ticket:512000ad-8c3f-4f06-8604-9511b81ca218
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - repo:yoosungung/CrewRP
  - merge:d03ff30d2b30806191bd2d4dae2db9697fe00cd9
tags: ["Engineering", "DevEnv", "CrewRP", "UX", "Contents"]
type: "wiki"
---

# CrewRP 자료실 탭: 목록→상세·lazy 드릴다운

공지/할 일과 같은 **목록→상세**로 DocsTab을 맞춘다. 예전 상단 가로 파일명 칩 + 동일 화면 본문(split)은 제거.

## UX 계약

- 파일·폴더 목록 + 시트/다이얼로그 상세(편집/삭제/닫기).
- `/docs` 폴더 드릴다운: 기존 `listDocs(path:)` — Contents API는 path 단위이므로 **lazy 드릴다운**(전수 재귀 금지·rate limit).
- 검색: 이름·경로 부분 일치(대소문자 무시). `filterDocs`·`parentDocsPath`는 ShellPresentation(core).
- `isDir`는 목록에서 숨기지 않고 폴더로 진입.

## Non-goal

- 본문 full-text 검색, Contents 계약 변경, Phase 4.

## 에뮬 스모크 (Pixel_API_36)

- 파일·폴더 목록 + `이름·경로 검색` 필드 확인(칩+본문 split 없음).
- README.md → 상세; `guides` 폴더 진입·`상위` 복귀; 검색 `readme` → README만.
- 폴더 검증용 `docs/guides/onboard.md` 임시 생성 후 삭제 시도.
- 에뮬 cold-boot는 셸 포그라운드 유지(백그라운드 nohup이면 qemu 종료) — [[wiki/Engineering/Development-Environment/CrewRP-Physical-Device-E2E.md]].

## 🔗 관련

- [[wiki/Engineering/Development-Environment/CrewRP-Tasks-Tab-Compact-Kanban.md]]
- [[wiki/Engineering/Development-Environment/CrewRP-PR-Local-Test-Evidence.md]]
