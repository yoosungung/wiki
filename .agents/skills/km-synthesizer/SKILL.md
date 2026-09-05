---
name: km-synthesizer
description: `raw/` 데이터를 분석하여 `wiki/` 5대 핵심 카테고리 구조에 지식을 합성하고 경로 기반 링크를 관리합니다.
---

# KM_SYNTHESIZER_AGENT_v1

## 🎯 OBJECTIVE
파편화된 원천 데이터를 구조화된 지식으로 변환하여 정해진 계층 구조(Hierarchy)에 통합함.

## 📂 TARGET_STRUCTURE (wiki/)
모든 신규/수정 문서는 다음 5대 카테고리 및 하위 서브폴더에 배치되어야 함:
1. **Agents**: [Frameworks, Text-to-SQL, Memory, Multi-Agent, Robotics, Coding, etc.]
2. **Engineering**: [AI-Native, Prompt, Infrastructure, DevOps, Dev-Env, Security]
3. **Models**: [Architectures, Optimization, Reasoning, RL, SFT, Small-Models]
4. **RAG**: [GraphRAG, Semantic-Chunking, Databases, etc.]
5. **Business**: [Trends, Startup, Legal, Marketing, Recommendation]

## 📋 WORKFLOW

### 1. SOURCE_ANALYSIS
- `raw/` 문서를 읽고 핵심 엔티티, 데이터, 인사이트를 추출함.

### 2. KNOWLEDGE_MAPPING
- `index.md`를 참조하고, 필요 시 `wiki/` 전역 검색으로 관련 노트를 **전부** 식별함. 한 `raw/`는 단일 노트가 아니라 관련 entity/concept/요약 페이지 여러 개를 갱신할 수 있음.
- project·연구 과제의 지정 노트는 우선 타깃일 뿐 유일 타깃이 아님. 적합한 기존 노트가 없으면 `TARGET_STRUCTURE`에 맞춰 **신규 생성**함.
- 기존 노트를 검색하여 업데이트(`replace`) 또는 신규 생성(`write_file`) 여부를 결정함. 이미 동일 claim이 반영된 경우만 스킵하고 `log.md`에 `ALREADY_COVERED`로 기록함(내용 폐기 아님).

### 3. AGENT_EDITING
- **FRONTMATTER**: `related_raw: ["[[파일명.md]]"]` 및 `tags` 업데이트.
  - Quartz 빌드 시 올바른 수정 날짜 반영을 위해, frontmatter에 `last_updated: "YYYY-MM-DD"`와 `updated: "YYYY-MM-DD"` 필드를 반드시 동일하게 생성/업데이트함.
  - YAML 매핑 키는 문서당 **1회만**. `related_raw`를 기존 블록 아래에 한 줄 더 붙이지 말고 배열을 합친다. 중복 키는 Quartz `duplicated mapping key`로 GitHub Pages 빌드가 **fatal** 종료한다.
- **QUARTZ_KATEX** (본문 `$`): Quartz는 `$...$` / `$$...$$`를 KaTeX 수식으로 파싱한다. 통화 기호 `$`도 수식 시작이다.
  - `입력 $0.08 / 출력 $0.30`처럼 한글이 짝 `$` 사이에 들어가면 `unicodeTextInMathMode`(예: 문자 `력`) 경고가 난다. `strict: warn`이면 배포는 되고, 해당 구간만 수식으로 깨진다.
  - 가격·금액은 `` `$0.08` `` 또는 `USD 0.08`로 쓰고, 진짜 수식 안 한글·라벨은 `\text{출력}`으로 감싼다. 홀수 개의 `$`(예: `$0.08/1M 토큰`)도 금지.
- **LINKING**: 관련된 다른 `wiki/` 문서에 대해 **현재의 전체 상대 경로**(`[[wiki/Category/Sub/File.md]]`)를 사용하여 링크를 생성함.

### 4. VALIDATION
- 생성된 링크가 유효한지 `km-linter` 로직으로 자가 점검함.
- `log.md`에 `SYNTHESIZE` 액션을 기록함.

### 5. CLEANUP
- 해당 `raw/`의 핵심 claim이 관련 `wiki/` 노트(기존·신규)에 모두 매핑·반영되고 `log.md`에 `SYNTHESIZE`(또는 `ALREADY_COVERED`)가 기록된 뒤에만 원본 `raw/` 파일을 삭제함. 미매핑 claim이 남으면 삭제하지 않음.

## ⚠️ CONSTRAINTS
- **한국어 작성 원칙**: 영문으로 된 `raw` 원천 소스를 위키에 합성할 때는 반드시 가독성 높은 한국어로 번역 및 핵심 요지를 요약하여 작성함.
- **노이즈 정제 (Sanitization)**: 외부 플랫폼 스크랩 시 묻어 나온 로그인 화면, 소셜 미디어 푸터, 다국어 선택 목록 등 실제 지식과 관련 없는 노이즈 텍스트는 위키 합성 시 완전히 제외하고 정제함.
- **일반화된 파일명 준수**: 파일명은 `Concept-or-Pattern-Name.md` 스타일을 따르고, 소셜 공유 제목(예: `~님이 토픽에 대해 올림.md`)을 그대로 파일명이나 제목으로 쓰지 않음.
- 단순 요약이 아닌 **지식의 상호 연결**에 집중함.
- 파일명에 공백이나 특수문자가 포함된 경우 정확히 매칭함 (NFC 정규화 준수).
- **부분 합성 금지**: 지정 노트 한곳에만 넣고 나머지 사실을 버리는 흐름을 금지함. ingest된 `raw/`는 관련 노트 전체에 소진함.

## ♻️ REUSABLE_KNOWLEDGE (재사용 지식 우선)
- inbox/`raw`의 사실은 **이후 유사 상황에서 바로 참고할 패턴·절차·함정·명령**으로 재서술함.
- 일회성 이벤트 로그(“오늘 머지됨”, “CI red”, “담당 라우팅”)는 본문에 올리지 않음. 재사용 claim만 atomic 페이지에 남김.
- 제품명·티켓 맥락은 **예시 한 줄**로만 두고, 제목·요지는 패턴 단위로 분리함.
- 정본 정책: [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]

## 🧭 GENERALIZED_PATH (폴더·제목 = 검색 키)
- 경로·파일명·`title`은 **검색·백링크 키**다. 제품코드·날짜·PR/티켓 번호를 제목/슬러그에 넣지 않음.
- 권장: `Concept-or-Pattern-Name.md` (Pascal/kebab, 공백·특수문자 최소화). 예: `Playwright-Frontend-UI-Smoke-Pattern.md` (X: `nl2sql-Playwright-E2E-Smoke.md`).
- 5대 카테고리 + 기존 서브폴더에 맞추고, 일회성 이벤트용 폴더를 만들지 않음.

## 🚫 EXCLUDE_PROGRESS (진행 정보 비합성)
- **제외**: 내부 `PR#N`, `티켓#N`/`ticket:N` 진행·머지/리뷰 상태, CI red/green 스냅샷, assignee·Waiting for Approval 라우팅, “pm-owned” 등 워크플로 메타.
- **허용**: 업스트림 OSS의 **기능 근거**로서의 PR/이슈 URL(예: LiteRT `pull/2688`) — 단, 머지 의식·담당자 서사 없이 스펙/API 변화만 요약.
- frontmatter `sources`에 `ticket:N`을 lineage로 남기는 것은 가능하나, **본문 서술에 티켓/PR 진행을 복제하지 않음**.

## 🛠️ TECHNICAL_CONCRETENESS (기술적 구체성 원칙)
- 위키 작성 시 단순 뉴스나 현황 나열을 지양하고, **"향후 실제 개발 및 구현에 즉시 참고할 수 있는 구체적인 설계 아이디어, 시스템 구조/방법론, API 스펙 및 CLI 예시"**를 반드시 포함함.
- 오픈소스 프로젝트, 표준 규격의 경우 **공식 GitHub 리포지토리, 공식 문서(docs), 원천 연구 논문(arXiv 등)의 실 작동 참고 링크(Reference Links)**를 위키 본문에 명시함.
- 환경 설정(Configuration), 설치(Installation) 및 프롬프트 인젝션 명령어 등 **실천적인 코드/커맨드 블록**을 적극 수록함.
