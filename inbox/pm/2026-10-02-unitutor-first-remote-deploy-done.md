---
id: inbox-pm-unitutor-first-remote-deploy-done
agent: pm
ticket_id: 25217dd4-521b-452e-ba9f-e4766b3898af
updated: 2026-10-02
status: inbox
sources:
  - ticket:25217dd4-521b-452e-ba9f-e4766b3898af
  - https://github.com/yoosungung/UniTutorAI/pull/22
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37014651191
---

# UniTutor 첫 원격 Deploy closeout

- Pages smoke host는 `unitutor.askwho.net` (Dashboard DNS). `tutor.askwho.net`은 NXDOMAIN — #21로 정렬.
- API는 `api.tutor.askwho.net/health` 유지.
- Zone DNS list **403**(token에 Zone DNS Read 없음)이면 Ensure는 soft-skip하고 Smoke로 진행해야 함. Dashboard가 이미 CNAME을 소유한 경우 hard-fail 금지.
- 첫 green Deploy: run 37014651191 (merge `bd40a573` / PR #22).
