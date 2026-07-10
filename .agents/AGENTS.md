# 프로젝트 가이드: KM (Knowledge Management)

이 디렉토리는 범용적인 지식 관리를 위한 **Obsidian Vault**입니다. 이 파일은 이 저장소와 상호작용하는 Antigravity 에이전트(agy)를 위한 지침과 맥락을 제공합니다.

## 프로젝트 개요

- **목적**: 다양한 주제에 관한 기술 문서, 연구 자료, 아이디어 및 지식의 체계적 관리와 축적.
- **구조**: `raw/`(원본), `wiki/`(합성/요약), `assets/`(첨부파일) 3계층 구조를 기본으로 합니다.

## 개발 및 사용 원칙

1. **언어**: 모든 문서는 **한국어**로 작성하는 것을 원칙으로 합니다.
2. **내용의 성격**: 사실에 기반한 객관적인 지식 기록을 중시하며, 단순 메모를 넘어선 지식의 연결과 합성을 지향합니다.
3. **지식 연결**: Obsidian의 백링크(`[[ ]]`) 및 태그 기능을 활용하여 지식 간의 연결성을 극대화합니다.
4. **보안**: 자격 증명, API 키 또는 민감한 개인 정보는 이 저장소에 절대 포함하지 않습니다.

## 지식 관리 운영 원칙 (LLM Wiki 패턴)

이 저장소는 단순한 메모 보관함이 아닌, AI 에이전트와 협력하여 구축하는 **지능형 위키**를 지향합니다.

### 1. 3계층 아키텍처
- **원천 소스 (Raw Sources)**: 기사, 논문, 데이터 등 불변의 진실의 원천 (`raw/` 폴더).
- **위키 (The Wiki)**: 에이전트가 작성/수정하는 마크다운 파일군 (`wiki/` 폴더).
- **스키마 (The Schema)**: 위키 구조와 운영 규칙을 정의한 문서 (현재 이 파일 및 `GEMINI.md`).

### 2. 지속적 합성 (Continuous Synthesis)
- **정보 축적**: 새로운 소스 추가 시 단순 인덱싱이 아닌, 기존 위키 문서에 정보를 녹여내고 업데이트합니다.
- **상호 연결**: 문서 간의 링크(Internal Links)를 자동으로 생성하여 지식의 그래프를 형성합니다.
- **모순 관리**: 새로운 정보가 기존 내용과 충돌할 경우 이를 기록하고 합성을 시도합니다.

### 3. 인덱싱 및 로깅 (관리 자동화)
- **`index.md`**: 위키의 모든 항목을 카테고리별 분류한 콘텐츠 카탈로그.
- **`log.md`**: 수집(Ingest), 쿼리, 린트 작업의 연대순 기록.

### 4. 정기적 상태 점검 (Lint)
- 고립된 페이지(Orphaned pages) 연결 및 오래된 정보의 최신화.
- 언급되었으나 생성되지 않은 페이지 확인 및 보강.

---

## 🛠️ Antigravity Custom Skills (사용자 정의 스킬)

본 저장소에는 에이전트의 자율적 작업을 지원하기 위한 4가지 전용 스킬이 `.agents/skills/` 디렉토리에 정의되어 있습니다. 각 작업 수행 시 해당 스킬의 지침(`SKILL.md`)을 읽고 지침을 완수하십시오.

1. **[km-ingestor](file:///Users/suyoo/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/KM/.agents/skills/km-ingestor/SKILL.md)**
   - 외부 정보를 추출하여 `raw/` 폴더에 저장하고 메타데이터를 표준화합니다.
2. **[km-synthesizer](file:///Users/suyoo/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/KM/.agents/skills/km-synthesizer/SKILL.md)**
   - `raw/` 데이터를 분석하여 `wiki/` 5대 핵심 카테고리 구조에 지식을 합성하고 경로 기반 링크를 관리합니다.
3. **[km-researcher](file:///Users/suyoo/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/KM/.agents/skills/km-researcher/SKILL.md)**
   - 연구 주제 관리 문서를 분석하여 지식 탐색을 자동화하고 데일리 노트 및 `log.md`에 결과를 기록합니다.
4. **[km-linter](file:///Users/suyoo/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/KM/.agents/skills/km-linter/SKILL.md)**
   - 지식 베이스의 구조적 무결성을 점검하고 `index.md`, `log.md`를 Agent-Centric 포맷으로 최신화합니다.

---

## Obsidian CLI 사용 가이드

- **핵심 문법**: 인자는 `key=value` 형식을 사용하며, 공백이 포함된 경우 `key="value"`와 같이 큰따옴표로 감쌉니다.
- **기본 명령어**:
  - `obsidian help`: 전체 명령어 목록 확인.
  - `obsidian open path="경로"`: 특정 문서 열기.
  - `obsidian search query="검색어"`: 보관함 내 검색.
  - `obsidian create name="제목" content="내용"`: 새 노트 생성.
  - `obsidian daily`: 오늘의 데일리 노트 열기.
  - `obsidian daily:append content="내용"`: 데일리 노트 끝에 내용 추가.
  - `obsidian stats`: 보관함 통계(파일 개수 등) 확인.
  - `obsidian command id="명령어ID"`: 특정 Obsidian 커맨드 실행.
