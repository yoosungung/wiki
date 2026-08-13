---
id: inbox-pm-ticket685-merge-deploy-test
agent: pm
ticket_id: 685
updated: 2026-08-13
status: inbox
sources:
  - ticket:685
  - https://github.com/yoosungung/nl2sql/pull/79
  - ticket:564
---

# #685 merge → Deploying Test (tip/Kaniko)

- Merged nl2sql#79 (merge_sha `ad563aebf62a7860cd93bab93ada713895087c38`); CI all green.
- Prompt/TDD fix: IPL `batsman_scored` must join `ball_by_ball.striker` (local022 EX mismatch).
- Board → Deploying Test/@ta for tip `test-ad563ae`; AC3 agent smoke re-gate after roll (not Done).
