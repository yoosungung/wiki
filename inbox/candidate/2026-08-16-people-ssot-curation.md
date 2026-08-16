---
id: inbox-candidate-2026-08-16-people-ssot-curation
agent: candidate
ticket_id: 882
updated: 2026-08-16
status: inbox
sources:
  - ticket:882
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
---

# People SSoT curation 18:00 KST 2026-08-16

- 미공개 Pass 스택은 curation에 ff-merge하지 않는다. `origin/main` detach → 작업 → `push HEAD:main` → 로컬 스택 checkout. preserve 브랜치는 백업일 뿐 ship 경로가 아니다.
- 인물 승격은 allowlist 공식/프로필 URL(≥1)이 같은 사람일 때만. 기자·동명이인·역할 불일치·비인물(학교/부처)·직원명단 미기재 페이지는 hold.
- 동명이인 함정: 허용 호스트라도 다른 직의 동명이인 URL은 붙이지 않는다 (예: 교육청 인사 기사의 김홍국 ≠ 특임교수 김홍국).
- 2026-08-16: 조희대(scourt.go.kr 약력), 노무현(pa.go.kr 제16대 약력) 승격. origin/main `f747bb8`.
- 잔여 stub 27건 전수 검토 후 추가 승격 0 (shortage). hold 축: 비인물(정부·노동부·배재고), 역할불일치(박재철≠서울청장, 고희진≠국회의원, 홍인표≠가스공사 사장), 동명이인(강두식 전 의장, 김홍국 지스트/교육청, 황성택 트러스톤), 기자 11, 신원약함(시민·role null·연구원·전문가·의혹 당사자).
- 직원명단 페이지에 성명이 없으면 go.kr이어도 승격 근거로 쓰지 않는다.
