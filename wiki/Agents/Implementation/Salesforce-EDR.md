---
title: "Salesforce-EDR"
related_raw: ["[[wiki/Agents/Implementation/Salesforce-EDR.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'implementations', 'llm_agent_builders_research']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Salesforce Enterprise Deep Research (EDR)

**Enterprise Deep Research (EDR)**는 SalesforceAIResearch에서 개발한 다중 에이전트 시스템으로, 기업 심층 데이터 분석을 자동화합니다.

![EDR Logo](https://github.com/SalesforceAIResearch/enterprise-deep-research/raw/main/assets/edr-logo.png)

## 주요 기능 및 구성 요소

*   **마스터 플래닝 에이전트**: 적응형 쿼리 분해를 담당합니다.
*   **전문 검색 에이전트**: 일반, 학술, GitHub, LinkedIn의 네 가지 유형이 있습니다.
*   **확장 가능한 도구 생태계**: NL2SQL, 파일 분석, 기업 워크플로우를 지원합니다.
*   **시각화 에이전트**: 데이터 기반 통찰력을 제공합니다.
*   **반영 메커니즘**: 지식 격차를 감지하고 연구 방향을 업데이트하며, 필요에 따라 인간의 개입을 허용합니다.
*   **실시간 조종 명령**: 지속적인 연구 개선을 가능하게 합니다.

이러한 구성 요소들은 자동 보고서 생성, 실시간 스트리밍, 원활한 기업 배포를 가능하게 합니다.

## 아키텍처

![Architecture Overview](https://github.com/SalesforceAIResearch/enterprise-deep-research/raw/main/assets/edr_ppl.png)

## 벤치마킹

![Benchmark Results](https://github.com/SalesforceAIResearch/enterprise-deep-research/raw/main/assets/leaderboard.png)

## 리소스

*   **GitHub Repository**: [https://github.com/SalesforceAIResearch/enterprise-deep-research](https://github.com/SalesforceAIResearch/enterprise-deep-research)
*   **arXiv Paper**: [https://arxiv.org/abs/2510.17797](https://arxiv.org/abs/2510.17797)
*   **Hugging Face EDR-200 Dataset**: [https://huggingface.co/datasets/Salesforce/EDR-200](https://huggingface.co/datasets/Salesforce/EDR-200)

## 출처

*   [GitHub README](https://github.com/SalesforceAIResearch/enterprise-deep-research/blob/main/README.md)
