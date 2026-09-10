---
title: "How-to-run-llms-with-docker"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/How-to-run-llms-with-docker.md]]"]
tags: ['wiki', 'engineering_and_infra', 'dev_environment', 'dev_setup_guides']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---


Unsloth와 Docker를 활용하여 Mac 또는 Windows 환경에서 LLM을 로컬로 실행하는 방법에 대한 요약입니다.

## 기술적 세부 사항

*   **Docker Model Runner (DMR):** AI 모델을 컨테이너처럼 쉽게 실행할 수 있는 오픈 소스 도구입니다. Unsloth 모델과 llama.cpp를 백엔드로 사용하여 빠른 추론을 제공합니다.
*   **하드웨어 요구 사항:** VRAM과 RAM의 합이 양자화된 모델의 크기보다 커야 합니다.
*   **양자화 권장 사항:**
    *   30B 미만 모델: 최소 4비트(Q4) 양자화 권장
    *   70B 이상 모델: 최소 2비트 양자화(UD_Q2_K_XL) 권장
*   **모델 실행 방법:**
    *   **Docker 터미널:** `docker model run` 명령어를 사용하여 모델을 실행합니다.
    *   **Docker Desktop:** 'Models' 탭에서 모델을 검색하고 실행할 수 있습니다.

## 관련 링크

*   **Unsloth 문서:** [https://docs.unsloth.ai/models/how-to-run-llms-with-docker](https://docs.unsloth.ai/models/how-to-run-llms-with-docker)
*   **Docker Model Runner GitHub:** [https://github.com/docker/model-runner](https://github.com/docker/model-runner)

## 관련 노트

*   [[wiki/Engineering/Infrastructure-and-DevOps/KuberbetesPodOperator]]
*   [[wiki/Engineering/Infrastructure-and-DevOps/DGX Spark]]
*   [[wiki/Engineering/Infrastructure-and-DevOps/DGX Spark에서의 VLM 파인튜닝]]
*   [[wiki/Agents/Memory-and-Cognition/OpenMemory]]

