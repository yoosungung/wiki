---
id: candidate-status-public-sanitize
title: "candidate.win /status/ 공개 sanitize + 포맷"
status: canonical
owner: km
updated: "2026-11-12"
last_updated: "2026-11-12"
review_after: "2027-02-12"
sources:
  - inbox/candidate/2026-11-11-status-github-sanitize.md
  - inbox/candidate/2026-11-11-status-public-format-realign.md
  - inbox/pm/2026-11-11-candidate-status-github-leak.md
  - inbox/pm/2026-11-11-status-github-sanitize-intent-pass.md
  - inbox/pm/2026-11-11-status-public-format-intent-pass.md
  - inbox/pm/2026-11-11-status-public-format-realign.md
  - ticket:2da67ba7-7f33-47ac-bf27-af5cd90f5897
  - wiki/Engineering/AI-Native-Engineering/Candidate-Correction-Report-Worker.md
  - wiki/Engineering/AI-Native-Engineering/Candidate-Pages-Deploy-Not-Tenant-CD.md
tags: ["Engineering", "AI-Native", "candidate.win", "Public", "Sanitize"]
type: wiki
---

# candidate.win `/status/` 공개 sanitize + 포맷

공개 `/status/`는 GitHub·factory 인프라를 **비노출**하고, 요청/답변을 사용자 문장으로 렌더한다. Option A(`POST /api/report`) 모달 경로는 원래 GitHub 비노출 — 문제는 fetch→`reports.json`→Hugo 경로의 closeout 누수였다.

## Sanitize 계층

| 층 | 역할 |
| :--- | :--- |
| `sanitize_public_status_text` | `fetch_issues.py` → `reports.json`에서 `github.com`·`GitHub`·`factory.askwho.net` URL 제거 |
| Hugo `status.html` `replaceRE` | markdownify 직전 동일 패턴 재가드(fetch 누락 방어) |
| 공개 카피 | `status.md`/`policy.md`에서 `Closes #N`·「저장소」 대신 현황 공개 문구 |

Actions/PR URL·SHA·ticket id는 **factory 코멘트만**. 공개는 「요청하신 … 반영」 패턴(`AGENTS.md`).

## 공개 포맷

| 축 | 계약 |
| :--- | :--- |
| 요청 | `**페이지**` / `**내용**` (Issue #8/#10 정본) |
| 답변 | 「요청하신 … 반영했습니다」 |
| `format_public_request` | Option A/GH form `###` 덤프 → 공개 요약 (Issue 원문 SoR 유지) |
| `format_public_reply` | `Closed after factory` / `Resolved by PR` → 사용자 문장 (+ URL sanitize) |

## Done 게이트

- PR #35 sanitize merge `18f707c` + Pages Deploy; live `/status/`에 github.com / Closes #N / 저장소 / factory URL 0.
- 포맷 재정렬 main `8305e51b`; #26/#27/#28 공개 답변 실수정.
- `tenant_cd` N/A — Pages. `test:` + live `prod:`.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Candidate-Correction-Report-Worker.md]]
- [[wiki/Engineering/AI-Native-Engineering/Candidate-Pages-Deploy-Not-Tenant-CD.md]]
