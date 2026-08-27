# OpenWiki: 코드베이스 문서화 에이전트 CLI

## 핵심 주장 (Claims)
OpenWiki는 코드베이스나 개인 지식을 위한 위키를 작성하고 유지 관리하는 CLI 도구입니다. 에이전트가 소스 코드를 읽고 서로 연결된 Markdown 위키를 합성하며, 코드가 변경될 때마다 이를 최신 상태로 자동 업데이트합니다.

## 기능 및 모드 (Features & Modes)
OpenWiki는 두 가지 모드로 동작합니다.
1. **Code 모드 (기본)**: 현재 리포지토리를 스캔하여 `openwiki/` 폴더에 문서를 생성합니다.
2. **Personal 모드**: Notion, Slack, Gmail, X(Twitter), Web Search, Hacker News 등의 연결된 소스에서 데이터를 수집하여 `~/.openwiki/wiki/`에 개인 브레인 위키를 생성합니다.

**주요 특징**:
- 12개 이상의 LLM 프로바이더 지원 (OpenAI, Anthropic, Gemini, GitHub Copilot, AWS Bedrock 등).
- LangSmith 통합: 런타임 추적 데이터(도구 호출, 지연시간 등)를 가져와 실제 코드 동작 방식을 문서에 반영.
- 다이아그램 자동 생성: Mermaid를 사용하여 시퀀스, ER, 상태 다이아그램 등을 생성하고 유효성을 검증(실패 시 복구).
- Google Open Knowledge Format (OKF v0.1) 호환 출력.

## 시스템 구조 및 프라이버시 (Architecture & Privacy)
- 에이전트는 작성된 위키를 메모리로 활용(`AGENTS.md`, `CLAUDE.md` 업데이트).
- `.openwikiignore` 파일을 통해 스캔 및 문서화에서 제외할 민감한 경로나 생성된 파일을 지정 가능.
- 사용자가 `openwiki/INSTRUCTIONS.md`에 지침을 작성하여 문서화 범위와 우선순위를 제어.

## CLI 커맨드
**설치**:
```bash
npm install -g openwiki
```

**코드 모드 초기화 및 업데이트**:
```bash
openwiki --init
openwiki --update
```

**개인 모드 초기화 및 커넥터 연동**:
```bash
openwiki personal --init
openwiki auth notion        # 브라우저 OAuth 인증
openwiki ingest web-search  # 특정 소스 데이터 수집
```

**위키 시각화 (Interactive Node Graph)**:
```bash
openwiki visualize
```
