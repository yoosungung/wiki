---
title: "Claude Code 개발자 Boris의 효율적인 AI 활용 팁"
related_raw: ["[[wiki/Engineering/AI-Native-Engineering/Claude Code 개발자 Boris의 효율적인 AI 활용 팁.md]]"]
tags: ['wiki', 'engineering_and_infra', 'ai_development']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Claude Code 개발자 Boris의 효율적인 AI 활용 팁

Claude Code의 개발자인 Boris가 공개한 AI 개발 환경 최적화 팁 12가지를 요약했습니다.

### 주요 내용

1.  **병렬 작업의 힘**: 터미널과 웹에서 여러 Claude 세션을 동시에 사용하여 병렬 작업을 수행하고, 시스템 알림으로 작업 시점을 파악합니다.
    *   [알림 설정 공식 문서](https://lnkd.in/gnRfbkV3)
2.  **'Opus 4.5' 모델 사용**: 속도보다 도구 사용 능력과 사람 개입 최소화가 중요하므로, 모든 작업에 'Opus 4.5 (with thinking)'를 사용합니다.
3.  **`CLAUDE.md`를 팀 지식 저장소로 활용**: Git으로 `CLAUDE.md` 파일을 팀 전체가 공유하고, Claude의 실수를 규칙으로 추가하여 AI가 팀의 코딩 스타일을 학습하고 실수를 반복하지 않도록 합니다.
4.  **PR 과정에서 문서 자동 업데이트**: Github Action을 활용하여 코드 리뷰(PR) 시 `CLAUDE.md` 파일을 자동으로 업데이트합니다.
    *   [Dan Shipper의 Compounding Engineering 플러그인](https://lnkd.in/gwfNYZxV)
5.  **코딩 전 '계획 모드(Plan Mode)' 필수**: '계획 모드'로 시작하여 AI와 계획을 완벽하게 수정한 후 코딩 모드로 전환합니다.
6.  **자주 쓰는 워크플로우는 '슬래시 커맨드'로**: 반복적인 작업은 슬래시 커맨드로 만들어 `.claude/commands/`에 저장하고, 인라인 Bash로 속도를 높입니다.
7.  **'서브 에이전트(Sub-agents)'로 작업 전문화**: `code-simplifier`나 `verify-app`과 같이 작업 목적에 맞는 서브 에이전트를 활용하여 특정 워크플로우를 자동화합니다.
8.  **포맷팅은 '훅(Hook)'으로 자동 마무리**: `PostToolUse` 훅을 사용하여 AI가 코드를 생성한 직후 자동으로 포맷팅 툴을 실행합니다.
9.  **보안 권한 스마트하게 관리**: 안전한 공통 Bash 명령어를 `.claude/settings.json`에 미리 등록하여 불필요한 승인 절차를 줄입니다.
10. **MCP로 모든 도구 연결**: `.mcp.json` 설정을 통해 Claude Code를 Slack, BigQuery 등 다양한 도구와 연결합니다.
11. **긴 작업은 백그라운드에서 처리**: 백그라운드 에이전트나 `ralph-wiggum` 플러그인을 활용하고, 샌드박스 환경에서는 `--permission-mode=dontAsk` 설정을 사용합니다.
    *   [ralph-wiggum 플러그인 깃헙](https://lnkd.in/g_rFKyDv)
12. **AI에게 '검증 수단' 제공**: Claude가 코드를 작성한 후 스스로 검증할 수 있는 루프를 만들어 품질을 높입니다.
    *   [Claude Chrome 확장 프로그램](https.lnkd.in/gkq6N88d)

### 추가 팁

*   **개인적인 모델 선택 워크플로우**: Opus 4.5를 주력으로 사용하고, 막히면 GPT 5.2, 디자인은 Gemini 3 Pro, 자잘한 수정은 Sonnet 4.5를 사용하는 등 상황에 맞춰 모델을 교체합니다.
*   **Boris의 원본 글**: [https://x.com/bcherny/status/2007179832300581177](https://x.com/bcherny/status/2007179832300581177)
*   **PRD(Product Requirements Document) 작성의 중요성**: 코딩 시작 전 PRD 작성을 통해 계획을 명확히 합니다.

### 관련 노트

*   AI 개발 워크플로우
*   Claude Code 활용법
*   LLM 모델 선택 전략
*   개발 생산성 향상 팁
*   Git과 코드 리뷰 자동화
*   AI 에이전트 활용
*   보안 권한 관리
*   PRD 작성 가이드
