---
title: "LLM의 복잡한 문제 해결 전략: 멀티홉 및 다단계 추론"
related_raw:
  - "[[LLM은 어려운 문제를 어떤 식으로 풀까.md]]"
tags: ["Models", "Reasoning", "Multi-hop", "Cognition", "Chain-of-Thought"]
type: "wiki"
status: "published"
last_updated: "2026-05-01"
---

# LLM의 복잡한 문제 해결 전략: 멀티홉 및 다단계 추론

## 1. 개요
LLM이 직면하는 '어려운 문제'란 단일 문서나 단일 정보만으로는 해결할 수 없고, 여러 단계의 추론이나 다양한 정보원으로부터의 조각들을 결합해야만 답을 낼 수 있는 문제(Multi-hop, Multi-turn)를 의미합니다.

## 2. 멀티홉(Multi-hop) 추론 프로세스
단순한 예시: "A 영화의 감독이 졸업한 대학은 어디인가?"
1. **1단계 (First Hop)**: "A 영화의 감독이 누구인가?"를 먼저 검색하거나 추론하여 결과를 얻음 (예: 감독 B).
2. **2단계 (Second Hop)**: 얻어낸 결과(감독 B)를 바탕으로 "감독 B의 학력"을 다시 검색하거나 추론함.

## 3. 주요 문제 해결 전략
- **작업 분해 (Task Decomposition)**: 복잡한 질문을 여러 개의 작고 해결 가능한 하위 질문으로 나눕니다.
- **연쇄 추론 (Chain-of-Thought)**: 중간 단계의 사고 과정을 명시적으로 생성하여 최종 답안의 논리적 정확도를 높입니다.
- **반복적 검색 (Iterative Retrieval)**: 1단계에서 얻은 정보를 바탕으로 다음 단계에 필요한 새로운 검색 쿼리를 생성하여 지식을 확장합니다.

## 4. 해결해야 할 과제
- **오류 전파 (Error Propagation)**: 초기 단계에서 잘못된 정보를 얻을 경우, 이후 모든 단계에서 오류가 누적될 위험이 있습니다.
- **컨텍스트 관리**: 추론 단계가 길어질수록 컨텍스트 윈도우 내에서 중요한 정보를 유지하기가 어려워집니다.
- **계산 비용**: 단계별 추론은 단일 추론보다 더 많은 토큰 소비와 지연 시간(Latency)을 발생시킵니다.

## 관련 문서
- [[wiki/Models/Reasoning-and-Cognition/000_Reasoning-and-Cognition-MOC.md|추론 및 인지 MOC]]
- [[wiki/Models/Reasoning-and-Cognition/LLM 추론의 함정 - 생각을 멈춰야 정확해진다.md|추론 시의 생각 멈추기 전략]]
- [[wiki/RAG/DEO-RAG-BigQuery-Gemini.md|DEO-RAG: 고도화된 RAG 시스템]]
