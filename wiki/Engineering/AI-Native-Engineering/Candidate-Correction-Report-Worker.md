---
id: candidate-correction-report-worker
title: "candidate.win 정정·삭제: Option A /api/report Worker"
status: canonical
owner: km
updated: "2026-11-11"
last_updated: "2026-11-11"
review_after: "2027-02-11"
sources:
  - inbox/candidate/2026-11-09-correction-issue-intake.md
  - inbox/candidate/2026-11-09-correction-server-side-report.md
  - inbox/candidate/2026-11-09-option-a-report-api.md
  - inbox/candidate/2026-11-09-report-worker-vs-leantime-pr21.md
  - inbox/pm/2026-11-09-candidate-correction-github-contract.md
  - inbox/pm/2026-11-09-option-a-confirmed-worker-deploy.md
  - inbox/pm/2026-11-09-pm-checkpoint-option-a-intent-merge.md
  - inbox/candidate/2026-11-10-report-worker-gh-actions-cd.md
  - inbox/candidate/2026-11-10-report-modal-done-closes.md
  - inbox/pm/2026-11-10-report-worker-gh-actions-cd.md
  - inbox/pm/2026-11-10-pm-checkpoint-report-worker-cd-intent.md
  - ticket:85b94ff9-1aa1-4616-8df6-3c87eef2c01a
  - ticket:f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
  - ticket:dab8e0cf-335e-4ef3-baab-8a44fb9c3ef0
  - ticket:63833bbf-76a6-493d-854c-404c3ffb5488
  - https://github.com/berryking404/candidate.win/pull/21
  - https://github.com/berryking404/candidate.win/pull/24
  - https://github.com/berryking404/candidate.win/pull/25
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
tags: ["Engineering", "AI-Native", "candidate.win", "Cloudflare-Worker", "Issues"]
type: wiki
---

# candidate.win 정정·삭제: Option A /api/report Worker

## 계약 충돌

`AGENTS.md` Repository Contract: web 사용자는 GitHub를 모르게 처리. Leantime Done(PR #21) 모달 `submitReport`는 `github.com/.../issues/new`를 `window.open`하고 GitHub 문구를 노출 → **계약 위반**. `ROADMAP`/`README`의 Issues 단일 채널 정책과 문서 충돌.

## Option A (Eric 승인)

| 축 | 내용 |
| :--- | :--- |
| Why Worker | Hugo/GitHub Pages는 런타임 시크릿 불가. `CANDYDATE_ISSUES_TOKEN`을 정적 빌드에 넣으면 유출 |
| SoR | 내부 = GitHub Issues. UX = 사이트 폼만 |
| API | Cloudflare Worker `POST /api/report` (`edge/report`)가 Issues 생성. same-origin (`wiki.candidate.win` 이미 CF) |
| Browser | `CandydateReport.buildReportPayload` + `submitReport`/`fetch('/api/report')`만. `window.open`·github.com·로그인 유도 제거 |
| Prefill (선행) | PR #21 `report-issue-url.js`는 template 쿼리 사전채움 경로(Non-goal=백엔드 신설 없음). Option A가 이를 대체 |

## 운영

- Intent pass + squash merge PR #24 → `0c957763`. tenant_cd N/A.
- prod smoke는 CF Worker secret/route 배포에 의존 → `waiting_for_approval` + human secret 주입 필요 시 `@eric`.
- README의 “빌드 주입” 문구는 aspirational; 템플릿/JS 실사용 코드 없음(Worker 경로가 정본).

## GH Actions CD (Eric 2026-11-10)

로컬 `wrangler`가 아니라 Actions(`deploy-report-worker.yml`, PR #25)가 closeout 경로. UniTutor/factory CF 패턴.

| 축 | 내용 |
| :--- | :--- |
| Route SoR | `wrangler.toml` `[[routes]]` `wiki.candidate.win/api/report*` + `zone_name = candidate.win` (CD-owned; dashboard one-shot 아님) |
| Secrets | Actions: `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`; 기존 `CANDYDATE_ISSUES_TOKEN`은 CI가 Worker secret 주입 |
| Live | secrets+merge/`workflow_dispatch` 전 `/api/report`는 **405** 가능 |

## UX: 접수 완료 → 모달 닫기

`submitReport` 성공 후 버튼 라벨 `접수 완료` + `disabled=false`; 재클릭 시 `closeReportModal()`. 이전엔 disabled라 Escape/오버레이만 가능. Pages 배포: [[wiki/Engineering/AI-Native-Engineering/Candidate-Pages-Deploy-Not-Tenant-CD.md]].

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md]]
- [[wiki/Engineering/AI-Native-Engineering/Candidate-Source-URL-NA-Guard.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md]]
