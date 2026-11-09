---
id: inbox-candidate-report-worker-vs-leantime-pr21
agent: candidate
ticket_id: f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
updated: 2026-11-09
status: inbox
sources:
  - ticket:f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
  - ticket:85b94ff9-1aa1-4616-8df6-3c87eef2c01a
  - ticket:dab8e0cf-335e-4ef3-baab-8a44fb9c3ef0
---

# candidate.win 정정 폼: Leantime PR#21 vs Option A Worker

- Leantime Done(`85b94ff9`/PR #21)은 `window.open` GitHub Issues 사전채움. Non-goal = 백엔드 신설 없음.
- Option A(Eric 승인)는 AGENTS Repository Contract(GitHub 비노출) → 신규 `edge/report` Worker. 레포 히스토리에 선행 Worker 없음.
- README `CANDYDATE_ISSUES_TOKEN` “빌드 주입”은 aspirational; 템플릿/JS 실사용 코드 없음.
- prod `POST /api/report`는 라우트 미연결 시 405.
