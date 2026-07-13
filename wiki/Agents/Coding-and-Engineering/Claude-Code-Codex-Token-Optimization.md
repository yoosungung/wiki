---
title: "Claude Code 및 Codex 토큰 최적화 가이드"
related_raw: [
  "[[Claude Code 및 Codex 설정 변경으로 토큰을 절약하는 방🇧ᅥᆸ.md]]",
  "[[raw/andrej-karpathy-skillsREADME.md at main · forrestchangandrej-karpathy-skills.md]]",
  "[[raw/2026-07-13-jyoung105-codex-future-slide-skill.md]]",
  "[[raw/2026-07-13-eordax-vibe-coding-claude-code.md]]"
]
tags: ["Agents", "Coding", "Optimization", "Claude_Code", "Codex", "Opus_4.7", "Vibe_Coding"]
type: "wiki"
status: "published"
last_updated: "2026-07-13"
updated: "2026-07-13"
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

### Codex 스킬 최적화 및 커스텀 스킬 추가 (`~/.codex/skills`)
빌더들은 Codex 및 에이전트 환경의 설정을 변경하여 성능을 극대화하고 토큰 소모량을 제한하는 전략을 취하고 있습니다.
- **npx skills add**: `npx skills add <github-url>`을 사용하여 외부에서 정교하게 작성된 커스텀 스킬을 추가할 수 있습니다. 예를 들어, Lee Jae-young이 개발한 `future-slide-skill`은 슬라이드 생성 단계를 세부적으로 쪼개어 기획-프롬프트-이미지-디자인을 나누어 처리함으로써 한 번에 긴 프롬프트를 처리할 때의 환각과 토큰 낭비를 원천 방어합니다. 스킬 추가 후 에이전트를 재시작하여 적용합니다.

## 5. 바이브 코딩(Vibe Coding)과 자율 에이전트의 통제
AWS의 Eduardo Ordax가 주장한 바와 같이, 개발 패러다임이 단순 코드 제안(Copilot)에서 자율 코딩 에이전트(Claude Code 등)로 전환되면서 '바이브 코딩'이 대두되고 있습니다.
- **시스템 설계와 오케스트레이션**: 개발자는 이제 세부 코드를 일일이 타이핑하는 대신, 에이전트가 Git 작업 공간에서 격리된 브랜치나 컨테이너(MXC 등) 내에 자율 진입하여 빌드와 테스트를 실행하고 코드를 정밀 수정할 수 있도록 외곽 제어 루프(Harness)를 디자인하는 능력이 중요해집니다.
- **바이브 코딩의 생산성**: 단순 프롬프팅을 탈피하여, 에이전트가 POSIX 도구를 활용해 프로젝트 전반을 자율 탐색(Navigation over Retrieval)하게 하고 이를 통제 및 가드하는 프레임워크 설계가 병행되어야 합니다.

## 6. 공통 팁
- **Attribution 제거**: `attribution.commit` 및 `pr` 설정을 비워 Git 로그나 PR에 붙는 자동 텍스트를 제거합니다.
- **마크다운 문서 직접 참조**: Anthropic/OpenAI 문서 URL 뒤에 `.md`를 붙여 에이전트가 마크다운 형식으로 직접 읽게 하면 정보 추출 효율이 높아집니다.

## 7. 관련 문서
- [[wiki/Agents/Coding-and-Engineering/Claude-Code-Agentic-CLI-Update.md|Claude Code: 자율형 에이전트 CLI 도구의 진화]]
- [[wiki/Agents/Frameworks/Claude-Code-Agentic-Workflows.md|Claude Code 에이전틱 워크플로우]]
- [[wiki/Engineering/Development-Environment/000_Dev-Env-MOC.md|개발 환경 구성 MOC]]
