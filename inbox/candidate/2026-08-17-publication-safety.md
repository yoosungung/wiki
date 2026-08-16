---
id: inbox-candidate-2026-08-17-publication-safety
agent: candidate
ticket_id: 892
updated: 2026-08-17
status: inbox
sources:
  - ticket:892
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
---

# Publication-safety 03:00 KST 2026-08-17

- 미공개 Pass 스택은 preserve 브랜치로 백업한 뒤 origin/main rebase(충돌 0) → 콘텐츠 게이트 → ship. preserve는 백업일 뿐 ship 경로가 아니다.
- 게이트 PASS ≠ content-safe: `/people/unknown`, org-as-person, 이슈 slug를 인물로 쓴 stance, 약한 중립(발언 미확인), SSoT 없는 slug는 drop. 검색 URL 출처는 이번 미발행 diff에 없음.
- people slug remap은 collapse/접두(lee→i, park→bak, kim→gim, jung→jeong) + name_ko 매칭. 예: unknown 김기재 → gimgijae.
- yaml 추가 시 wiki stub도 seed (i-hyeok, i-tae-han). 약한 중립 줄을 버려도 orphan 0 유지.
- ship: origin/main `6e67c26`. SSoT yaml 961 / curated 930 / stub 31.
