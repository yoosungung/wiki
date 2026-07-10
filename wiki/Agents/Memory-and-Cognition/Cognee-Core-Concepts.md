---
title: "Cognee 핵심 개념 및 주요 작업"
related_raw: ["[[wiki/Agents/Memory-and-Cognition/Cognee 핵심 개념.md]]", "[[wiki/Agents/Memory-and-Cognition/Cognee 빠른 시작.md]]"]
tags: ['wiki', 'agents', 'memory', 'concepts']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
---

# Cognee 핵심 개념

Cognee는 원시 데이터를 지능적인 지식 구조로 변환하기 위해 모듈식 설계와 명확한 데이터 단위를 사용합니다.

## 1. 주요 구성 요소
- **데이터포인트 (DataPoints)**: 그래프의 노드가 되는 최소 구조화 데이터 단위입니다.
- **작업 (Tasks)**: 데이터를 변환하거나 처리하는 개별 실행 단위입니다.
- **파이프라인 (Pipelines)**: 여러 작업을 오케스트레이션하여 워크플로우를 생성합니다.

## 2. 4대 핵심 작업 (Core Operations)
AI 메모리 구축 및 활용을 위한 네 가지 API 메서드가 제공됩니다:
- **`.add()`**: 데이터를 시스템에 수집하고 준비합니다.
- **`.cognify()`**: 수집된 데이터에서 엔티티와 관계를 추출하여 지식 그래프를 생성하는 핵심 단계입니다.
- **`.memify()`**: 그래프의 의미론적 강화를 수행하는 단계입니다(예정).
- **`.search()`**: 벡터 유사성, 그래프 탐색 또는 하이브리드 방식을 사용하여 정보를 검색합니다.

## 3. 고급 개념
- **노드 세트 (Node Sets)**: 지식 기반 콘텐츠를 분류하고 필터링하기 위한 태그 및 조직 시스템입니다.
- **온톨로지 (Ontology)**: RDF/XML 등을 통해 외부 지식 체계와 연결할 수 있는 구조를 제공합니다.

## 관련 문서
- [[wiki/Agents/Memory-and-Cognition/Cognee-Architecture.md|Cognee 아키텍처]]
- [[wiki/Agents/Memory-and-Cognition/Cognee-Setup-Guide.md|Cognee 설정 가이드]]
- [[wiki/Agents/Memory-and-Cognition/Cognee-MOC.md|Cognee-MOC]]
