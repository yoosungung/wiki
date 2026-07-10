---
title: "Video-RLM-2026"
related_raw: ["[[wiki/Models/RL/Video-RLM-2026.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'recursive_language_models_rlm']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Video-RLM: Recursive Language Models for Long Videos

## 📑 개요 (Overview)
- **URL**: [arXiv:2603.19001](https://arxiv.org/abs/2603.19001)
- **핵심 키워드**: #Recursive-Language-Models #RLM #Video-Understanding #Long-Context

## 📽️ 핵심 기술 아키텍처 (Key Architecture)
MIT CSAIL 연구진이 제안한 RLM(Recursive Language Models) 프레임워크를 비디오 도메인으로 확장한 연구입니다.

### 1. Master-Worker 아키텍처
- **Master 모델**: 비디오 전체의 맥락을 파악하고 탐색 전략을 수립합니다.
- **Worker 모델**: Master로부터 할당받은 특정 비디오 구간에서 손실 없는 시각적 증거를 수집합니다.
- Master와 Worker가 병렬로 작동하며 정보를 재귀적으로 처리합니다.

### 2. 로그 단위 계산 최적화
- 비디오 길이가 길어짐에 따라 계산량이 선형이 아닌 **로그(logarithmic) 단위**로 증가하도록 설계되었습니다.
- 이를 통해 수 시간 분량의 매우 긴 영상에서도 효율적인 추론이 가능합니다.

## 📈 주요 기여 및 성과 (Contributions & Results)
- **효율성**: 초장기 문맥 처리 시 발생하는 '컨텍스트 망각(Context Rot)' 문제를 시스템 아키텍처적으로 해결했습니다.
- **에이전트 통합**: `recursive-decomposition-skill`과 연동하여 복잡한 시각적 데이터를 분석하는 에이전트의 핵심 엔진으로 활용 가능합니다.

## 🔗 관련 링크 (Related Links)
- **기존 노트 연결**: [[wiki/Models/RL/재귀적 언어 모델(RLM)]], [[wiki/Agents/Frameworks/구글의-Embodied-Agent-SIMA]]

---
*Created on: 2026-03-20*
