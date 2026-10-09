---
id: crewrp-tasks-tab-compact-kanban
title: "CrewRP 할 일 탭: compact 칸반·상세 납기"
status: canonical
owner: km
updated: "2026-10-10"
review_after: "2027-01-09"
sources:
  - inbox/crewrp/2026-10-06-tasks-tab-compact-kanban.md
  - inbox/pm/2026-10-06-crewrp-tasks-tab-ux.md
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - repo:yoosungung/crewrp@84d8b4b
tags: ["Engineering", "DevEnv", "CrewRP", "UX"]
type: "wiki"
---

# CrewRP 할 일 탭: compact 칸반·상세 납기

## 레이아웃

- **compact(폰):** 가로 260pt 3열이 아니라 레인별 **세로 섹션**(전체 너비). 와이드만 다열 유지.
- 분기 정본: `kanbanUsesStackedLanes(compact)` — iOS size class, Android width < 600dp.
- 예전 iOS `ScrollView(.horizontal)` + 260pt / Android `LazyRow` 260.dp는 폰에서 한 레인이 화면을 거의 차지함 → 갭은 보드 레이아웃·상세 편집.

## 상세 편집

- 상태는 자유 텍스트가 아니라 **접수 / 진행 중 / 완료** 세그먼트.
- 납기: `YYYY-MM-DD` → Projects v2 Due (`dueFieldId` + `dueOn`).
- iOS `updateTask`는 Due를 **반드시** 보낸다. nil이면 납기 저장이 빠진다.
- 카드 행(`TaskRow`)에는 레인·납기가 이미 있음 — 갭은 편집 시트·compact 보드.

## 범위

- 계약 유지: 칸반 ↔ 마감일 리스트, Projects v2 Status/Due.
- Phase 4 enqueue 아님(maintenance UX). Due 필드 ensure: [[wiki/Engineering/Development-Environment/CrewRP-Projects-Due-Date-Field.md]].
- iOS 납기 silent no-op: [[wiki/Engineering/Development-Environment/CrewRP-iOS-Due-Edit-Silent-Noop.md]]. 자료실 목록→상세: [[wiki/Engineering/Development-Environment/CrewRP-Docs-Tab-List-Detail.md]].
