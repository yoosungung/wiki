---
title: "Superpowers - 에이전트 기반 소프트웨어 개발 프레임워크"
related_raw: ["[[wiki/Agents/Frameworks/Superpowers/Superpowers - 에이전트 기반 소프트웨어 개발 프레임워크.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'llm_systems_projects']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Superpowers: 에이전트 기반 소프트웨어 개발 프레임워크

## 개요
GitHub 저장소 "obra/superpowers"는 코딩 에이전트를 위한 에이전트 기반 기술 프레임워크이자 소프트웨어 개발 방법론을 제공합니다. 이 프레임워크는 코딩 에이전트가 작업을 바로 코딩하는 대신, 사용자와의 대화를 통해 사양을 도출하고 구현 계획을 수립하도록 지원하여 개발 프로세스의 효율성과 정확성을 높입니다.

## 주요 특징 및 방법론

1.  **대화형 사양 도출:** 코딩 에이전트가 사용자와의 상호작용을 통해 요구 사항을 명확히 이해하고 상세한 사양을 도출합니다.
2.  **구현 계획 수립:** 사양을 기반으로 에이전트가 구현 계획을 수립하며, 이 과정에서 TDD(Test-Driven Development) 원칙을 적용합니다.
3.  **TDD (Test-Driven Development) 강조:** 테스트 코드를 먼저 작성하고, 이를 통과하는 코드를 개발하는 TDD 방식을 적극적으로 활용하여 코드의 품질과 신뢰성을 확보합니다.
4.  **서브 에이전트 기반 개발:** 복잡한 개발 작업을 여러 서브 에이전트에게 분배하여 병렬적으로 처리하고, 각 서브 에이전트의 결과를 통합하는 방식을 사용합니다.
5.  **자동화된 코드 리뷰 및 브랜치 관리:** 개발된 코드에 대한 자동화된 리뷰 프로세스를 포함하며, Git 브랜치 관리 기능을 활용하여 효율적인 협업 환경을 제공합니다.
6.  **다양한 플랫폼 지원:** Claude Code, Codex, OpenCode와 같은 주요 AI 코딩 플랫폼에 설치하여 사용할 수 있습니다.

## 기술 스택 및 라이선스
*   **지원 플랫폼**: Claude Code, Codex, OpenCode
*   **라이선스**: MIT 라이선스

## 시사점
Superpowers는 AI 기반 코딩 에이전트의 역할을 단순한 코드 생성자를 넘어선, 개발 프로세스 전반을 주도하고 관리하는 주체로 확장합니다. 특히 TDD와 서브 에이전트 기반 접근 방식은 복잡한 소프트웨어 프로젝트에서 AI의 활용도를 높이고, 개발 효율성을 극대화하는 데 기여할 것으로 기대됩니다.

---
**원본 URL**: [GitHub Repository](https://github.com/obra/superpowers)

**관련 URL:**
*   `https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md`
*   `https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md`
*   `https://github.com/obra/superpowers/issues`
*   `https://github.com/obra/superpowers-marketplace`

**관련 노트**:
*   [[wiki/Agents/Frameworks/Langchain Open Deep Research 아키텍처 가이드]]
*   [[wiki/Agents/Coding-and-Engineering/Claude Code의 Task 변화와 AI-native 엔지니어의 조건]]
*   [[wiki/Engineering/AI-Native-Engineering/AI 기반 코딩의 실제 사례 - Cursor와 OpenAI]]
*   [[wiki/Engineering/AI-Native-Engineering/Claude Code 개발자 Boris의 효율적인 AI 활용 팁]]
