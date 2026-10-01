---
id: unitutor-learner-storage-and-stage3-locks
title: "UniTutor Local-first learner · Stage3 product locks"
status: canonical
owner: km
updated: "2026-10-02"
review_after: "2027-01-02"
sources:
  - inbox/uni-tutor/2026-10-01-unitutor-local-first-learner-storage.md
  - inbox/uni-tutor/2026-10-01-unitutor-fsrs-reviewcard-session-close.md
  - inbox/uni-tutor/2026-10-01-unitutor-mathjs-formula-verdict.md
  - inbox/uni-tutor/2026-10-02-cardfaded-web-push.md
  - inbox/uni-tutor/2026-10-02-unitutor-cardfaded-web-push.md
  - inbox/uni-tutor/2026-10-02-unitutor-free-tutor-quota.md
  - inbox/uni-tutor/2026-10-02-unitutor-free-quota-paid-unlock.md
  - inbox/uni-tutor/2026-10-02-unitutor-ad-reward-turns.md
  - inbox/pm/2026-09-30-unitutor-stage1-breakdown.md
  - inbox/pm/2026-10-01-unitutor-stage3-breakdown.md
  - inbox/pm/2026-10-02-unitutor-stage3-product-lock.md
tags: ["Engineering", "AI-Native", "UniTutor", "Product"]
type: "wiki"
---

# UniTutor Local-first learner · Stage3 product locks

테넌트 L0(`ARCHITECTURE`/`PRODUCT`/`ROADMAP`)이 정본. 여기는 에이전트 inbox에서 뽑은 **운영·구현 함정**만.

## Local-first learner

- Key: `unitutor:learner:{CourseRef.id}` (`localStorage`, IndexedDB 아님)
- v1 payload: `path`, `knownSpanIds`, `returnQuestionSpanId`, `wrongAnswers[]`, 이후 `reviewCards[]` append (version bump 없음·누락 시 `[]`)
- Quota/private-mode throw → save false / load null
- FSRS: `ts-fsrs` `createEmptyCard` + `next(..., Rating.Good)` → `card.due` = `ReviewCard.fadesAt` (`enable_fuzz=false`면 결정적)

## formulaVerdict

- **Math.js** (Pyodide 제외 — 초기 WASM 비용). `checkFormula` → `applyFormulaVerdict`가 유도 질문만 교체. incorrect여도 정답/풀이를 `TutorTurn`에 넣지 않음.

## Stage3 product locks (ROADMAP HTML 마커)

| 항목 | 값 |
|------|-----|
| 다시 보기 알림 | **3**/일 (`notify-daily-limit:3`) — SW local `CardFaded`, 서버 Push subscription 없음 |
| 무료 TutorTurn | **5**/일 (`free-tutor-turns:5`) — ledger `unitutor:tutor-quota` |
| 광고 보상 | 1회 → 문답 **3** (`ad-reward-tutor-turns:3`); BYOK는 후속 |
| 유료 | `unitutor:entitlement` plan=paid **스텁** (결제 벤더 없음) |

CardFaded 문구: `{concept}, 2분이면 확인할 수 있어요.` 일일 카운트는 알림 await 전에 예약해 동시 호출이 상한을 넘지 않게 함.

## 마일스톤 메모

- 1단계: 강의 보면서 질문받기 (VTT/캔버스/TutorTurn). 첫 과목은 human 게이트.
- 3단계: 복습·비즈니스 분기. 수식 판정부터 착수; 한도/수익 자식은 product lock 전 kickoff 금지.
- factory roadmap checklist sync는 테넌트 ROADMAP이 `##`+`- [ ]`일 때 유리 (`###`+plain bullet이면 no-op).
