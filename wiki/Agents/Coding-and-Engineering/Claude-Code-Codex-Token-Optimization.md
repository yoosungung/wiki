---
title: "Claude Code 및 Codex 토큰 최적화 가이드"
related_raw: [
  "[[Claude Code 및 Codex 설정 변경으로 토큰을 절약하는 방법.md]]",
  "[[raw/andrej-karpathy-skillsREADME.md at main · forrestchangandrej-karpathy-skills.md]]"
]
tags: ["Agents", "Coding", "Optimization", "Claude_Code", "Codex", "Opus_4.7"]
type: "wiki"
status: "published"
last_updated: "2026-04-22"
updated: "2026-04-22"
---

# Claude Code 및 Codex 토큰 최적화 및 효율 향상 가이드

## 1. 개요
Claude Opus 4.7 출시와 함께 토크나이저 업데이트 및 리즈닝(Reasoning) 강화로 인해 토큰 소모량이 증가하는 추세입니다. 특히 Claude Code의 캐싱 TTL이 단축되면서 토큰 효율 관리가 코딩 에이전트 운영의 핵심 과제가 되었습니다.

## 2. Andrej Karpathy의 통찰: `CLAUDE.md` 가이드라인
에이전트의 불필요한 추상화 남발과 잘못된 가정을 방지하기 위한 4대 원칙입니다.

1. **Think Before Coding**: 가정을 명시하고 모호함이 있다면 질문할 것. 트레이드오프 제시 필수.
2. **Simplicity First**: 요청받지 않은 기능이나 불필요한 추상화 금지. 최소한의 코드로 해결.
3. **Surgical Changes**: 요청받은 부분만 정밀하게 수정. 주변 코드의 불필요한 '개선' 금지.
4. **Goal-Driven Execution**: "수정하라"는 명령 대신 "테스트 통과"라는 성공 기준을 제시하고 루프를 돌릴 것.

## 3. Claude Code 최적화 설정 (v2.1.114 기준)

### 핵심 설정 및 환경변수
- **`INCLUDEGITINSTRUCTIONS: false`**: 매 세션마다 포함되는 Git 관련 지침을 제거하여 토큰을 절약합니다. (기본값: true)
- **`AUTOCONNECTIDE: false`**: IDE(VS Code, JetBrains) 연동이 불필요한 터미널 중심 작업 시 컨텍스트 주입을 차단합니다.
- **`CLAUDE_CODE_GLOB_NO_IGNORE=false`**: `.gitignore`에 등록된 파일(node_modules, build 등)을 Glob 검색 결과에서 제외하여 불필요한 파일 읽기를 방지합니다.

### 출력 제한 설정
- **`BASH_MAX_OUTPUT_LENGTH`**: Bash 출력 최대 문자 수 제한.
- **`CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS`**: 파일 읽기 시 최대 토큰 수 제한.
- **`MAX_MCP_OUTPUT_TOKENS`**: MCP 도구 출력 상한 설정.

### 경량화 모드 및 워커 활용 (Alias 추천)
- `ENABLE_CLAUDEAI_MCP_SERVERS=false`: MCP 서버 비활성화
- `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`: 자동 메모리 로드 방지
- `--tools "Bash,Edit,Glob,Grep,Read,Write"`: 필요한 도구만 선별 활성화

## 4. OpenAI Codex 최적화 설정 (v0.121.0 기준)

- **`features.apps = false`**: ChatGPT 연동 앱/커넥터 정보의 시스템 프롬프트 주입을 차단합니다.
- **`WEB_SEARCH = "DISABLED"`**: 로컬 작업 시 웹 검색 도구 호출을 방지합니다.
- **`tool_output_token_limit`**: 개별 도구 출력 저장량을 조절하여 세션 팽창을 방지합니다.

## 5. 공통 팁
- **Attribution 제거**: `attribution.commit` 및 `pr` 설정을 비워 Git 로그나 PR에 붙는 자동 텍스트를 제거합니다.
- **마크다운 문서 직접 참조**: Anthropic/OpenAI 문서 URL 뒤에 `.md`를 붙여 에이전트가 마크다운 형식으로 직접 읽게 하면 정보 추출 효율이 높아집니다.

## 관련 문서
- [[wiki/Agents/Coding-and-Engineering/Claude-Code-Agentic-CLI-Update.md|Claude Code: 자율형 에이전트 CLI 도구의 진화]]
- [[wiki/Agents/Frameworks/Claude-Code-Agentic-Workflows.md|Claude Code 에이전틱 워크플로우]]
- [[wiki/Engineering/Development-Environment/000_Dev-Env-MOC.md|개발 환경 구성 MOC]]
