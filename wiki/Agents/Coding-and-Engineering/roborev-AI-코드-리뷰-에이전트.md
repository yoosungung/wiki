---
related_raw: ["[[2026-06-29-automate-code-review-with-roborev.md]]"]
tags: ["#wiki", "Agents/Coding", "Agents/Evaluations", "Code-Review", "TUI"]
---

# roborev: AI 에이전트 커밋 자동 코드 리뷰 시스템

**roborev**는 개발자 및 AI 코딩 에이전트(Codex, Claude Code, Gemini, Copilot 등)가 생성한 모든 커밋을 감지하고, 실제 사용자에게 검토를 맡기기 전에 자동으로 즉각적인 피드백 루프를 제공하는 로컬 구동형 코드 리뷰 시스템입니다.

## 1. 도입 배경 및 특징
AI 코딩 에이전트의 개발 속도는 인간 리뷰어의 처리 능력을 훨씬 능가합니다. PR(Pull Request)을 열어 리뷰하는 시점에는 이미 수십 개의 커밋이 누적되어 구조적 오류가 심화된 상태일 수 있습니다. roborev는 **커밋 즉시(Background post-commit review)** 분석을 진행하여 이러한 피드백 갭을 해소합니다.

## 2. 핵심 아키텍처 및 작동 루프
- **자동 훅 설치**: `roborev init` 명령을 통해 git post-commit 훅을 구성하며, 이후 추가적인 명령 없이 백그라운드에서 동작합니다.
- **TUI & 피드백**: 코드 분석 결과는 Vim 스타일 단축키로 제어 가능한 대화형 TUI 창에 출력되거나, API/이벤트를 통해 코딩 에이전트에게 직접 피드백 데이터로 전달됩니다.
- **자가 정제 루프 (Self-refining)**:
  - `roborev fix`: 발견된 결함을 코딩 에이전트에게 즉시 전달하여 코드 수정 후 재커밋을 유도합니다.
  - `roborev refine`: 격리된 가상 작업 공간(isolated worktree)에서 `수정 -> 검증 -> 재수정` 과정을 한계치 도달 혹은 패스할 때까지 **무인 자율 구동(Unattended loop)**합니다.
- **다양한 분석 레이어**: 중복 코드 탐색, 코드 복잡도 분석, 리팩토링 제안, 테스트 픽스처 유효성 검증, 미사용 코드 제거, 보안 취약점 점검, API 디자인 및 아키텍처 검증을 포함하며 `--fix` 옵션을 통해 자동 패치 기능을 활성화할 수 있습니다.
- **로컬 실행성**: 외부 호스팅 서비스 없이 전적으로 로컬에서 동작하여 소스 코드 보안이 보장됩니다.

## 🔗 연결된 문서
- [[wiki/Agents/Coding-and-Engineering/000_Coding-and-Engineering-MOC.md]]
- [[wiki/Agents/Coding-and-Engineering/루프-엔지니어링-패러다임-및-시스템-안전.md]]
- [[index.md]]
