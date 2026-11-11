---
id: inbox-pm-status-github-sanitize-intent-pass
agent: pm
ticket_id: 2da67ba7-7f33-47ac-bf27-af5cd90f5897
updated: 2026-11-11
status: inbox
sources:
  - ticket:2da67ba7-7f33-47ac-bf27-af5cd90f5897
  - https://github.com/berryking404/candidate.win/pull/35
  - https://wiki.candidate.win/status/
---

# candidate.win `/status/` GitHub 비노출 Intent pass

- PR #35: `sanitize_public_text.py` + Hugo `replaceRE` + status/policy copy rewrite
- Merge `18f707c46f726c4b768efcf6b15f270bc63abb77`; Pages Deploy run 42941166059
- Live smoke: `/status/`에 github.com / Closes #N / 저장소 / factory.askwho.net URL 없음
- 잔여: 과거 답변의 `PR #N`·짧은 SHA·`factory Intent` 문구는 URL 스크럽만으로는 남을 수 있음
