---
id: inbox-candidate-2026-08-30-people-ssot-curation
agent: candidate
ticket_id: 1474
updated: 2026-08-30
status: inbox
sources:
  - schedule:people-ssot-curation-18h-kst
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
---

# People SSoT curation 2026-08-30 (18:00 KST)

- Pass stack 10 commits를 `agent/pass-stack-preserve-20260830-18h`에 보존한 뒤 `origin/main` detach에서 큐레이션(스택 ff merge 금지).
- origin/main SSoT: people yaml 1046 (curated 1016 / stub 30) / wiki orphan 0; parse_err 0.
- stub→curated 승격 0: allowlist URL·동일인·동일직 조건 충족 stub 없음. 목표 미달 ≠ 강제 승격.
- hold 축: 비인물(학교·부처·정부), 역할 불일치, 기자/통신원, go.kr 직원명단 미기재, 동명이인(장석영), allowlist URL 부재.
- pytest `test_people_curation_sources.py` 3 passed; content diff 없음 → commit/push 없음.
