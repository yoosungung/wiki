---
title: "Azure-AI-Foundry-Local-Setup"
related_raw: ["[[wiki/Engineering/Development-Environment/Azure-AI-Foundry-Local-Setup.md]]"]
tags: ['wiki', 'engineering_and_infra', 'dev_environment', 'dev_setup_guides']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Azure AI Foundry 로컬 개발 시작하기

**출처**: [원본 링크](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?view=foundry-classic)

Foundry Local은 장치에서 AI 모델을 로컬로 실행하기 위한 Microsoft의 미리 보기 도구입니다.

## 주요 내용

*   **전제 조건:** Windows, macOS, Windows Server 2025를 지원하며, 최소 8GB RAM과 3GB의 여유 디스크 공간이 필요합니다.
*   **빠른 시작 (CLI 설정):**
    *   **설치:** Windows에서는 `winget`, macOS에서는 `brew`를 사용하여 설치합니다.
    *   **모델 실행:** `foundry model run <model_name>` 명령으로 모델을 다운로드하고 실행할 수 있습니다.
*   **시작 프로젝트:** 채팅, 요약, 함수 호출 등 실제 시나리오를 보여주는 프로젝트를 제공합니다.
*   **OpenAI 오픈 소스 모델 실행:** `foundry model run gpt-oss-20b` 명령으로 GPT-OSS-20B 모델을 실행할 수 있습니다.

## 관련 링크

*   **Foundry Local GitHub:** [https://github.com/microsoft/foundry-local](https://github.com/microsoft/foundry-local)
*   **Foundry Local 문서:** [https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)

---
## 관련 노트
- [[wiki/Engineering/Infrastructure-and-DevOps/How-to-run-llms-with-docker]]
- [[wiki/Agents/Frameworks/Microsoft-Frameworks/Microsoft-spec-to-agents]]
