# 프로젝트 가이드: KM (Knowledge Management)

이 저장소는 범용적인 지식 관리를 위한 **Obsidian Vault**입니다. 이 파일은 **Cursor Agent** 및 기타 AI 코딩 에이전트를 위한 지침과 맥락을 제공합니다.

## 프로젝트 개요

- **목적**: 다양한 주제에 관한 기술 문서, 연구 자료, 아이디어 및 지식의 체계적 관리와 축적.
- **구조**: `wiki/`(canonical 본문), `INDEX.md`(카탈로그), `inbox/{agent}/`(기여 원료), `raw/`(선택 원천), `assets/`(첨부). Quartz는 `wiki/` 본문을 게시하며 `inbox/`·`raw/`는 제외한다.

## 개발 및 사용 원칙

1. **언어**: 모든 문서는 **한국어**로 작성하는 것을 원칙으로 합니다.
2. **내용의 성격**: 사실에 기반한 객관적인 지식 기록을 중시하며, 단순 메모를 넘어선 지식의 연결과 합성을 지향합니다.
3. **지식 연결**: Obsidian의 백링크(`[[ ]]`) 및 태그 기능을 활용하여 지식 간의 연결성을 극대화합니다.
4. **보안**: 자격 증명, API 키 또는 민감한 개인 정보는 이 저장소에 절대 포함하지 않습니다.

## 지식 관리 운영 원칙 (LLM Wiki 패턴)

이 저장소는 단순한 메모 보관함이 아닌, AI 에이전트와 협력하여 구축하는 **지능형 위키**를 지향합니다.

### 1. 3계층 아키텍처
- **원천 소스 (Raw Sources)**: 기사, 논문, 데이터 등 불변의 진실의 원천 (`raw/` 폴더). 에이전트 기여 원료는 `inbox/{agent}/` (promote 후 `git rm`, `inbox/_archived/` 없음).
- **위키 (The Wiki)**: 에이전트가 작성/수정하는 마크다운 파일군 (`wiki/` 폴더).
- **스키마 (The Schema)**: 위키 구조와 운영 규칙을 정의한 문서 (현재 이 파일).

### 2. 지속적 합성 (Continuous Synthesis)
- **정보 축적**: 새로운 소스 추가 시 단순 인덱싱이 아닌, 기존 위키 문서에 정보를 녹여내고 업데이트합니다.
- **전 위키 확산**: `projects/`·연구 과제의 지정 노트는 우선 타깃일 뿐 유일 타깃이 아님. 한 `raw/`의 사실은 관련 노트를 **전부** 갱신하고, 없으면 신규 생성합니다. “중복/툴링” 이유로 합성을 생략하지 않으며, 이미 반영된 claim만 `ALREADY_COVERED`로 기록합니다.
- **재사용·일반화**: inbox/`raw`는 유사 상황에 쓸 **패턴·절차·함정**으로 합성한다. 폴더·제목은 검색 키이므로 제품/일회성 이벤트·PR·티켓 번호를 슬러그에 넣지 않는다. 내부 PR#·티켓# 등 **진행 정보는 합성하지 않는다** (정본: [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]).
- **상호 연결**: 문서 간의 링크(Internal Links)를 자동으로 생성하여 지식의 그래프를 형성합니다.
- **모순 관리**: 새로운 정보가 기존 내용과 충돌할 경우 이를 기록하고 합성을 시도합니다.

### 3. 인덱싱 및 로깅 (관리 자동화)
- **`INDEX.md`**: 위키의 모든 항목을 카테고리별 분류한 콘텐츠 카탈로그 (org-wiki 정본).
- **`log.md`**: 수집(Ingest), 쿼리, 린트 작업의 연대순 기록.

### 4. 정기적 상태 점검 (Lint)
- 고립된 페이지(Orphaned pages) 연결 및 오래된 정보의 최신화.
- 언급되었으나 생성되지 않은 페이지 확인 및 보강.

### 5. 지식 자산 유지기간
공개 페이지([`/log`](https://wiki.askwho.net/log) = 루트 `log.md`)가 길어 보이는 이유는 **기간 기반 자동 삭제가 없기 때문**입니다.

| 자산 | 유지기간 | 삭제 시점 |
|------|----------|-----------|
| **`log.md`** | 무기한 누적 (append-only) | **자동 삭제 없음**. 에이전트는 행만 추가하며, 기간으로 prune하지 않음. |
| **데일리 노트** (`YYYY-MM-DD.md`) | D-0(오늘)·D-1(어제)만 유지 | D-2 이전 파일은 린트/리서치 CLEANUP 시 삭제 |
| **`raw/`** | 합성 완료까지 | 관련 wiki 노트에 claim 전부 매핑·로그 기록 후 원본 삭제 (미매핑 시 유지) |
| **`inbox/{agent}/`** | promote까지 | canonical `wiki/` 반영 후 **`git rm`** (아카이브 폴더 없음) |
| **`wiki/`** | 영구 (지식 본체) | 일상적 자동 삭제 없음 |

※ Git 히스토리에는 과거 버전이 남을 수 있으나, 공개 Quartz 사이트는 현재 워킹트리의 `log.md` 전체를 그대로 게시합니다.

---

## Cursor Agent Skills

에이전트 자율 작업을 위한 4가지 스킬이 `.agents/skills/`에 정의되어 있습니다. Cursor는 해당 디렉터리를 자동 탐색하며, 관련 작업 시 `SKILL.md`를 읽고 지침을 따릅니다.

| 스킬 | 경로 | 용도 |
|------|------|------|
| km-ingestor | `.agents/skills/km-ingestor/SKILL.md` | 외부 정보를 `raw/`에 저장·메타데이터 표준화 |
| km-synthesizer | `.agents/skills/km-synthesizer/SKILL.md` | `raw/` → `wiki/` 지식 합성 |
| km-researcher | `.agents/skills/km-researcher/SKILL.md` | `연구_주제_관리.md` 기반 자동 탐색 |
| km-linter | `.agents/skills/km-linter/SKILL.md` | 구조 무결성 점검, `INDEX.md`/`log.md` 갱신 |

### Cursor 도구 매핑
- 웹 검색: `WebSearch`
- URL/파일 읽기: `Read`, `Shell`(curl)
- 파일 쓰기: `Write`, `StrReplace`
- Python 실행: `.venv` 가상환경 사용

---

## Obsidian CLI 사용 가이드

로컬 Obsidian 환경에서만 사용합니다. Cursor 클라우드 에이전트는 `Read`/`Write`/`Grep` 도구로 대체합니다.

- **핵심 문법**: 인자는 `key=value` 형식을 사용하며, 공백이 포함된 경우 `key="value"`와 같이 큰따옴표로 감쌉니다.
- **기본 명령어**:
  - `obsidian help`: 전체 명령어 목록 확인.
  - `obsidian open path="경로"`: 특정 문서 열기.
  - `obsidian search query="검색어"`: 보관함 내 검색.
  - `obsidian create name="제목" content="내용"`: 새 노트 생성.
  - `obsidian daily`: 오늘의 데일리 노트 열기.
  - `obsidian daily:append content="내용"`: 데일리 노트 끝에 내용 추가.
  - `obsidian stats`: 보관함 통계(파일 개수 등) 확인.
