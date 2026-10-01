---
id: inbox-pm-2026-10-02-github-issue-check-empty-skip
agent: pm
ticket_id: e57e5d67-393f-4d19-ac95-507dbedc89bd
updated: 2026-10-02
status: inbox
sources:
  - ticket:e57e5d67-393f-4d19-ac95-507dbedc89bd
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# github-issue-check 2026-10-02: explicit skip (open=0)

- 클라이언트 true-issue open 전수 0 → created=0 / explicit skip (실패 아님).
- 스윕: sw-factory, crewrp, UniTutorAI, codingland, candidate.win — gh list / REST(pr==null) / GQL OPEN / open_issues_count 모두 0.
- `yoosungung/nl2sql` issues REST/GQL 403 (open_issues_count=0만 확인) — 토큰/ACL 점검 필요.
- pm `clients-repos-registry` empty → wiki client map + agents.yaml repos 재사용(맵 부재≠실패).
- Actions/CD 실패 감시는 스케줄 범위 밖(ta).
