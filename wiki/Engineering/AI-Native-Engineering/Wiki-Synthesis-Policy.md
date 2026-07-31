---
id: wiki-synthesis-policy
title: "Wiki 합성 정책 (재사용·일반화·진행정보 제외)"
status: canonical
owner: km
updated: "2026-07-31"
last_updated: "2026-07-31"
review_after: "2026-10-31"
sources:
  - ticket:51
tags: ["Engineering", "AI-Native", "KM", "Synthesis", "Policy"]
type: "wiki"
---

# Wiki 합성 정책 (재사용·일반화·진행정보 제외)

inbox/`raw` → `wiki/` promote·합성 시 적용하는 품질 규칙. 스킬 정본은 `.agents/skills/km-synthesizer/SKILL.md`.

## REUSABLE_KNOWLEDGE

| 넣을 것 | 넣지 말 것 |
| :--- | :--- |
| 재현 가능한 절차·명령·설정 키 | “오늘 머지됨 / CI red” 스냅샷 |
| 함정·대안·축 분리(예: UI 스모크 vs SQL EX) | 담당자·승인 대기·라우팅 서사 |
| 다음 유사 작업에 바로 쓸 패턴 | 일회성 이벤트 일기 |

제품·레포 이름은 **예시**로만 본문에 두고, 노트 요지는 패턴 단위로 쓴다.

## GENERALIZED_PATH

- 폴더·파일명·`title` = **검색·백링크 키**.
- 권장: `Concept-or-Pattern-Name.md` (공백·특수문자·날짜 prefix·제품코드 최소화).
- 나쁜 예: `nl2sql-Playwright-E2E-Smoke.md` → 좋은 예: `Playwright-Frontend-UI-Smoke-Pattern.md`.
- 5대 카테고리(`Agents`/`Engineering`/`Models`/`RAG`/`Business`)와 기존 서브폴더에만 배치.

## EXCLUDE_PROGRESS

**제외(내부 진행 메타)**

- `PR#N`, `티켓#N` / `ticket #N`의 머지·리뷰·CI 상태
- assignee, Waiting for Approval, “pm-owned” 등 워크플로 문구

**허용**

- 업스트림 OSS **기능 변화**를 가리키는 PR/이슈 URL (스펙·API만; 머지 의식 금지)
- frontmatter `sources:`에 `ticket:N` lineage (본문 복제 금지)

## 적용 체크리스트 (promote 직전)

1. 이 노트를 6개월 뒤 다른 제품에서도 검색해 쓸 수 있는가?
2. 제목만 보고 패턴이 보이는가? (제품/티켓/PR이 제목에 없는가?)
3. 본문에 내부 PR#·티켓# 진행 로그가 없는가?

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Playwright-Frontend-UI-Smoke-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
