---
id: inbox-pm-candidate-correction-github-contract
agent: pm
ticket_id: dab8e0cf-335e-4ef3-baab-8a44fb9c3ef0
updated: 2026-11-09
status: inbox
sources:
  - ticket:dab8e0cf-335e-4ef3-baab-8a44fb9c3ef0
  - candidate.win:AGENTS.md
  - candidate.win:ROADMAP.md
  - candidate.win:wiki/static/js/report-issue-url.js
---

# candidate.win 정정·삭제 UX vs GitHub-비노출 계약

- Repository Contract (`AGENTS.md`): web 사용자는 GitHub를 모르게 처리.
- 현행 모달 `submitReport`는 `github.com/.../issues/new`를 `window.open`하고 GitHub 문구를 노출 → **계약 위반**.
- `ROADMAP`/`README`는 GitHub Issues 단일 채널을 운영 정책으로 채택 → 문서 간 충돌.
- `CANDYDATE_ISSUES_TOKEN`은 서버측 자동 생성을 암시하나 미구현(클라이언트 리다이렉트만).
- 결정 옵션: A 계약유지+서버생성 / B 계약개정 / C 비공개 채널. Eric Approval 대기.


## Decision (2026-11-09)
- Eric approved **Option A** (계약 유지 + 서버측 Issues 생성).
- Parent dab8e0cf done (policy). Implementation child: f35f32d7-3eeb-4ed6-983a-353d6db5c0ee (@candidate).
