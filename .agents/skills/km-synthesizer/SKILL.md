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
- **LINKING**: 관련된 다른 `wiki/` 문서에 대해 **현재의 전체 상대 경로**(`[[wiki/Category/Sub/File.md]]`)를 사용하여 링크를 생성함.

### 4. VALIDATION
- 생성된 링크가 유효한지 `km-linter` 로직으로 자가 점검함.
- `log.md`에 `SYNTHESIZE` 액션을 기록함.

### 5. CLEANUP
- 해당 `raw/`의 핵심 claim이 관련 `wiki/` 노트(기존·신규)에 모두 매핑·반영되고 `log.md`에 `SYNTHESIZE`(또는 `ALREADY_COVERED`)가 기록된 뒤에만 원본 `raw/` 파일을 삭제함. 미매핑 claim이 남으면 삭제하지 않음.

## ⚠️ CONSTRAINTS
- 단순 요약이 아닌 **지식의 상호 연결**에 집중함.
- 파일명에 공백이나 특수문자가 포함된 경우 정확히 매칭함 (NFC 정규화 준수).
- **부분 합성 금지**: 지정 노트 한곳에만 넣고 나머지 사실을 버리는 흐름을 금지함. ingest된 `raw/`는 관련 노트 전체에 소진함.

## 🛠️ TECHNICAL_CONCRETENESS (기술적 구체성 원칙)
- 위키 작성 시 단순 뉴스나 현황 나열을 지양하고, **"향후 실제 개발 및 구현에 즉시 참고할 수 있는 구체적인 설계 아이디어, 시스템 구조/방법론, API 스펙 및 CLI 예시"**를 반드시 포함함.
- 오픈소스 프로젝트, 표준 규격의 경우 **공식 GitHub 리포지토리, 공식 문서(docs), 원천 연구 논문(arXiv 등)의 실 작동 참고 링크(Reference Links)**를 위키 본문에 명시함.
- 환경 설정(Configuration), 설치(Installation) 및 프롬프트 인젝션 명령어 등 **실천적인 코드/커맨드 블록**을 적극 수록함.
