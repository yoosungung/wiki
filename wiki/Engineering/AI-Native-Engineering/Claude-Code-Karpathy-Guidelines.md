---
title: "안드레 카파시 영감: Claude Code 및 CLAUDE.md 지침"
related_raw: ["[[andrej-karpathy-skillsREADME.md at main · forrestchangandrej-karpathy-skills.md]]", "[[AI 코딩 에이전트를 통제하는 65줄의 원칙.md]]"]
tags: ["Engineering", "AI-Native", "Claude_Code", "CLAUDE_md", "Karpathy", "Prompt_Engineering"]
type: "wiki"
status: "published"
last_updated: "2026-05-15"
---

# Karpathy-Inspired Claude Code & CLAUDE.md 지침

## 1. 개요
안드레 카파시(Andrej Karpathy)가 지적한 LLM 코딩의 고질적인 문제점(잘못된 가정, 복잡한 추상화 남발, 불필요한 코드 수정 등)을 해결하기 위한 Claude Code용 가이드라인입니다. 최근 주목받는 **단 65줄의 `CLAUDE.md`** 파일은 에이전트에게 "작업 헌장" 역할을 하며, 단순한 명령을 넘어 명확한 작업 환경을 구축하는 데 집중합니다.

## 2. 4대 핵심 원칙 및 구체적 사례

### 1) 코딩 전 사고 (Think Before Coding)
- **가정 방지**: 추측으로 구현하지 말고, 선택지와 트레이드오프(Trade-off)를 먼저 제시하게 합니다.
- **예시**: "로그인 기능을 추가해줘" 요청 시, 곧바로 코드를 짜지 않고 세션, OAuth, JWT 방식의 장단점을 비교하여 사용자에게 확인을 요청합니다.

### 2) 단순성 우선 (Simplicity First)
- **최소 코드 원칙**: 미래의 유연성을 설계하지 말고, 현재의 문제를 가장 단순한 방식으로 해결합니다.
- **예시**: 거창한 객체지향 설계보다는 직관적인 함수형 구현을 우선시하며, 만들지 않아도 되는 코드를 만들지 않는 것이 생산성의 핵심입니다.

### 3) 외과적 수정 (Surgical Changes)
- **정밀 타격**: 요청된 변경 사항과 직접 관련된 코드만 수정합니다.
- **스타일 유지**: 본인이 작성하지 않은 기존 코드의 서식이나 주석을 마음대로 고치지 않도록 제한합니다.
- **예시**: 특정 함수의 예외 처리를 고치는 작업 시, 해당 함수와 관련 테스트 범위 내에서만 움직이게 합니다.

### 4) 목표 기반 실행 (Goal-Driven Execution)
- **성공 기준 중심**: "이 에러를 없애줘" 대신 "실패하는 테스트 케이스를 먼저 만들고, 이를 통과시킨 뒤 전체 테스트를 확인해줘"라고 지시합니다.
- **검증 루프**: 스스로 검증할 수 있는 좁고 명확한 목표를 부여하여 에이전트가 작업 완료 여부를 스스로 판단하게 합니다.

## 3. 65줄의 마법: 왜 효과적인가?
AI는 코딩 능력이 부족한 것이 아니라, **브레이크 없이 너무 빠르게 달리는 것**이 문제입니다. `CLAUDE.md`는 AI가 과하게 추측하고 고치는 습관을 제어하는 '브레이크' 역할을 합니다. 에이전트에게 더 많은 자유를 주는 것이 아니라, 더 좁고 명확한 경계를 세워주는 것이 품질을 높이는 비결입니다.


## 관련 문서
- [[wiki/Engineering/AI-Native-Engineering/Claude-Code-Next-Gen-Coding-Agent.md|Claude Code: 차세대 코딩 에이전트 분석]]
- [[wiki/Engineering/AI-Native-Engineering/Claude-Code-Karpathy-Optimization.md|Claude Code 최적화 기법]]
- [[wiki/Engineering/Prompt-Engineering/000_Prompt-Engineering-MOC.md|프롬프트 엔지니어링 MOC]]
