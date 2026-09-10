---
title: "Microsoft-spec-to-agents"
related_raw: ["[[wiki/Agents/Frameworks/Microsoft-Frameworks/Microsoft-spec-to-agents.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'implementations', 'big_tech_llm_agents']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Microsoft Spec-to-Agents

**출처**: [원본 링크](https://github.com/microsoft/spec-to-agents/blob/main/README.md)

이 문서는 Microsoft의 `spec-to-agents` 프로젝트에 대한 README 파일로, 이벤트 계획을 위한 다중 에이전트 시스템에 대해 설명합니다. 이 시스템은 [[wiki/Agents/Frameworks/Microsoft-Frameworks/Microsoft Agent Framework|Microsoft Agent Framework]]를 기반으로 하며, Semantic Kernel의 엔터프라이즈 오케스트레이션과 AutoGen의 다중 에이전트 패턴을 결합합니다.

**주요 내용:**

*   **시연 내용**: 이 프로젝트는 다음을 포함하는 프로덕션 준비가 된 다중 에이전트 시스템을 구축하는 방법을 보여줍니다.
    *   **다중 에이전트 오케스트레이션**: 5개의 전문 에이전트가 이벤트 계획을 조율합니다.
    *   **Human-in-the-Loop**: 워크플로 실행 중 대화형 승인 및 피드백을 제공합니다.
    *   **도구 통합**: 웹 검색, 날씨 API, 캘린더 관리 및 코드 인터프리터를 포함합니다.
    *   **Azure 배포**: Azure Developer CLI (azd)를 사용한 원클릭 배포를 지원합니다.

*   **아키텍처**:
    *   **다중 에이전트 워크플로 설계**: 이벤트 코디네이터가 전문 에이전트에게 작업을 라우팅하고 출력을 종합적인 이벤트 계획으로 통합하는 '코디네이터 중심의 스타 토폴로지'를 사용합니다.
    *   **에이전트 도구 및 기능**: 각 전문 에이전트는 전문 분야에 특화된 도구에 접근할 수 있습니다.
        *   **장소 전문가 (Venue Specialist)**: 웹 검색 (Bing Grounding)
        *   **예산 분석가 (Budget Analyst)**: 코드 인터프리터 (Python REPL)
        *   **케이터링 코디네이터 (Catering Coordinator)**: 웹 검색 (Bing Grounding)
        *   **물류 관리자 (Logistics Manager)**: 날씨 API (Open-Meteo) + 캘린더 도구 (iCalendar)
        *   **모든 에이전트**: [[wiki/Agents/Frameworks/MCP/MCP|MCP]] 순차적 사고 (복잡한 추론을 위한 모델 컨텍스트 프로토콜)

*   **빠른 시작**:
    *   **전제 조건**: Python 3.11+, `uv` (Python 패키지 관리자), Azure CLI (az), Azure Developer CLI (azd), Azure 구독이 필요합니다.
    *   **Azure에 배포**: `git clone`, `az login`, `azd auth login`, `azd up` 명령어를 통해 Microsoft Foundry + OpenAI 모델 프로비저닝, `.env` 파일 생성, Python 종속성 설치 (uv sync)가 자동으로 이루어집니다.
    *   **로컬 실행**: `uv run console` (대화형 콘솔) 또는 `uv run app` (DevUI) 명령어를 통해 실행할 수 있습니다.
    *   **예시 입력**: "Plan a corporate holiday party for 50 people on December 6th, 2025 in Seattle with a budget of $5,000. Include venue options, catering for dietary restrictions, and check the weather forecast."와 같은 이벤트 계획 요청을 처리할 수 있습니다.

*   **프로젝트 구조**:
    *   `src/spec_to_agents/`: `main.py` (DevUI), `console.py` (CLI), `agents/` (에이전트 정의), `prompts/` (시스템 프롬프트), `tools/` (도구 구현), `workflow/` (워크플로 오케스트레이션 로직), `utils/` (유틸리티)를 포함합니다.
    *   `tests/`: 단위 및 통합 테스트.
    *   `infra/`: Azure 인프라 (Bicep 템플릿).
    *   `scripts/`: 프로비저닝 후 후크.

*   **주요 기능**:
    *   **서비스 관리 스레드**: 모든 에이전트는 `store=True`를 사용하여 Azure AI 서비스를 통한 자동 대화 기록 관리를 지원합니다.
    *   **Human-in-the-Loop**: `ctx.request_info()`를 통해 사용자 입력 시 워크플로를 일시 중지하고 상태를 자동으로 보존합니다.
    *   **구조화된 출력 라우팅**: 에이전트는 명시적인 라우팅 결정 (`next_agent` 필드)을 포함하는 Pydantic 모델을 반환하여 동적 워크플로 오케스트레이션을 가능하게 합니다.

*   **Azure 리소스**: `azd up`에 의해 자동으로 프로비저닝됩니다.
    *   **Microsoft Foundry**: 서비스 관리 에이전트를 위한 AIServices 리소스 및 프로젝트.
    *   **Azure OpenAI**: gpt-5-mini (기본) 및 gpt-4.1-mini (웹 검색).
    *   **Bing Search**: 웹 검색을 위한 Grounding API.
    *   **Container Registry & App**: 배포용 (선택 사항).
    *   **Application Insights**: 원격 측정 및 모니터링.

**관련 링크:**

*   [[wiki/Agents/Frameworks/Microsoft-Frameworks/Microsoft Agent Framework]]
*   Ignite 2025 Lab: LAB513 - Build A2A and MCP Systems Using SWE Agents and Agent Framework: https://github.com/microsoft/ignite25-LAB513-build-a2a-and-mcp-systems-using-swe-agents-and-agent-framework/blob/main/lab/instructions/instructions.md
*   uv (Python 패키지 관리자): https://docs.astral.sh/uv/
*   Azure CLI (az) 설치: https://learn.microsoft.com/cli/azure/install-azure-cli
*   Azure Developer CLI (azd) 설치: https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd
*   개발 설정 (DEV_SETUP.md): /microsoft/spec-to-agents/blob/main/DEV_SETUP.md
*   라이선스 (LICENSE): /microsoft/spec-to-agents/blob/main/LICENSE
*   GitHub Codespaces에서 열기: https://codespaces.new/microsoft/spec-to-agents

**이미지:**

*   Spec-to-Agents 로고: https://github.com/microsoft/spec-to-agents/raw/main/assets/spec_logo.png
*   이벤트 계획 에이전트 디자인: https://github.com/microsoft/spec-to-agents/raw/main/assets/Event%20Planning%20Agent%20Design.png
*   에이전트 도구: https://github.com/microsoft/spec-to-agents/raw/main/assets/Agent%20Tools.png

---
## 관련 노트
- [[wiki/Agents/Multi-Agent-and-Orchestration/멀티-에이전트-패턴]]
- [[wiki/Agents/Frameworks/MCP/MCP]]
