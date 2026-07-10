---
title: "HaluMem: 에이전트 메모리 시스템의 수집·업데이트·질의(Extraction-Update-QA) 환각 검증 벤치마크"
tags: ["HaluMem", "Agent-Memory", "Hallucination-Benchmark", "Memory-Evaluation"]
last_updated: "2026-07-06"
related_raw: ["[[2026-07-06-kalyan_ks_halumem_benchmark.md]]"]
---

# 📊 HaluMem: 에이전트 메모리 시스템의 수집·업데이트·질의(Extraction-Update-QA) 환각 검증 벤치마크

**HaluMem** (Hallucination in Memory Benchmark)은 에이전트의 장기 메모리 아키텍처가 정보를 처리하는 과정에서 발생하는 환각 현상을 단계적으로 측정하기 위해 설계된 오퍼레이션 레벨 벤치마크입니다.

## 1. 3단계 메모리 오퍼레이션 평가 구조
1. **메모리 수집 (Memory Extraction)**: 원천 텍스트에서 불변의 단일 사실(Fact)을 올바르게 누락 없이 추출하는 능력을 검증.
2. **메모리 업데이트 (Memory Updating)**: 기존 메모리에 저장된 내용과 대조하여 충돌하는 새로운 사실을 갱신하거나 무효화(invalidate)하는 능력 검증.
3. **메모리 질의 응답 (Memory QA)**: 다단계로 중첩되고 파편화되어 분산 저장된 메모리들로부터 근거를 조합하여 답을 추론하는 최종 QA 능력 검증.

## 2. HaluMem 데이터셋 사양
- **HaluMem-Medium** & **HaluMem-Long**: 인간-AI의 다회차 대화 세션을 기반으로 구축된 데이터셋.
- **데이터량**: 15,000개 이상의 메모리 인스턴스, 3,500개의 검증용 질문 포함.
- **특징**: 컨텍스트 크기가 **1M 토큰 이상**이고, 최대 1,500~2,600 turn 이상의 초장기 대화 이력을 포함하여 장기 보존(long-horizon stability)을 극한까지 스트레스 테스트함.

---
**관련 문서**:
- [[wiki/Agents/Memory-and-Cognition/에이전트-네이티브-메모리-시스템-평가-연구-2026.md]]
- [[wiki/Agents/Frameworks/Evaluations/000_Evaluations-MOC]]

