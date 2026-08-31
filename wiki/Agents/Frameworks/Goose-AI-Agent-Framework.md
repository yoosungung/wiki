---
title: Goose AI 에이전트 프레임워크
status: published
tags: [Agents, Frameworks, GooseAI, OpenSource, MCP]
related_raw: ["[[raw/2026-08-31-goose-agent-framework-engineering-ai-maturity-model.md]]", "[[raw/2026-08-30-goose-framework-aaif-agentic-engineering.md]]", "[[2026-05-08-goose-ai-future-of-work.md]]"]
last_updated: "2026-08-31"
updated: "2026-08-31"
---

# Goose AI (구스): 블록(Block)의 오픈소스 에이전트 프레임워크

**Goose (구스)**는 잭 도시가 이끄는 블록(Block)에서 공개한 오픈소스 AI 에이전트 프레임워크입니다. 내부적으로 5,000명의 인력 감축 이후 그 공백을 메우기 위해 개발된 "디지털 노동 인프라"로서의 성격을 띱니다.

## 🌟 핵심 특징

### 1. 모델 불가지론 (Model Agnostic) 및 Rust 기반 구현
- 특정 모델에 종속되지 않고 Claude, GPT-5, Gemini 등 15개 이상의 LLM 백엔드를 유연하게 지원합니다.
- Rust로 작성되어 높은 성능과 시스템 자원 활용률을 보장합니다.

### 2. 자율적 작업 수행 (올인원 에이전트)
- 단순 코딩 추천(Copilot)을 넘어, 패키지 설치, 독자 셸 실행, 코드 파일 생성/수정, 자체 테스트 스위트(Test suite) 실행 및 검증까지 전 과정을 자율 제어합니다.
- 문제를 스스로 디버깅하여 수정하는 자가 수정(Self-correction) 능력을 지녔습니다.

### 3. 로컬 실행 및 지속적 기억
- 개발자 기기 내부(Local)에서 직접 실행할 수 있으며 지속적인 메모리를 진화시켜 나갑니다. 보안이 필수적인 오프라인/엔터프라이즈 환경에 적합합니다.

### 4. MCP(Model Context Protocol) 통합
- [[wiki/Agents/Frameworks/MCP/000_MCP-MOC.md|MCP]]의 **공식 래퍼런스 구현체** 역할을 수행하며, 로컬 파일 시스템, 외부 API 도구 등을 손쉽게 융합해 쓸 수 있습니다.
- 조직의 에이전틱 엔지니어링 성숙도 모델(Level 3~8)에서 자율 Task 수행을 위한 실천적인 인프라 툴로 채택됩니다. (상세는 [[wiki/Agents/Coding-and-Engineering/에이전트-기반-엔지니어링-조직-전환-및-성숙도-모델.md|에이전트 엔지니어링 성숙도 모델]] 참조)

## 📉 사회적 및 경제적 함의 (구스쇼크)
- **노동의 재정의**: 인간의 역할이 '실행자'에서 문제를 정의하고 행동을 규정하는 '설계자'로 강제 이주되고 있음을 보여줍니다.
- **기술의 민주화 vs 권력 집중**: 강력한 생산 수단을 대중에게 개방하는 동시에, 인간 노동의 가치를 비용 효율성 측면에서 해체하는 양가적 성격을 가집니다.

## 🏛️ AAIF (Agentic AI Foundation) 기증 (2026년 업데이트)
- **표준화 기구 이관**: 블록(Block)은 2026년 자체적으로 관리하던 `goose` 프레임워크를 리눅스 재단 산하의 **Agentic AI Foundation (AAIF)**에 공식 기증하였습니다.
- **상호운용성 표준 수립**: AAIF는 Anthropic의 MCP(Model Context Protocol), OpenAI의 `AGENTS.md` 규격과 함께 `goose` 에이전트 실행 엔진을 3대 핵심 기둥으로 삼아 벤더 종속이 없는 오픈 에이전트 인프라 표준을 정의합니다.
- **에이전틱 엔지니어링(Agentic Engineering)**: 기존의 수동 코딩 패러다임에서 탈피해, 확률론적으로 동작하는 자율 에이전트 군(Swarms)의 오케스트레이션 설계, 컨텍스트 엔지니어링, 거버넌스를 설계하는 전문 규율로서의 '에이전틱 엔지니어링'이 새로운 핵심 기술 분과로 부상했습니다.

## 🔗 관련 문서
- [[wiki/Agents/Frameworks/000_Frameworks-MOC.md]]
- [[wiki/Agents/Frameworks/MCP/000_MCP-MOC.md]]
- [[wiki/Business/Trends/AI-Agent-Economy.md]]
- [[wiki/Agents/Multi-Agent-and-Orchestration/자율수행-멀티-에이전트-시스템-오케스트레이션-및-보안-격리-2026.md]]

