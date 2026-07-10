---
title: "MiroFish: 군집 지능 기반 미래 시뮬레이션 엔진"
related_raw: ["[[MiroFish is a multi-agent swarm intelligence engine that builds a high-fidelity digital world from seed materials you provide, then runs… | AI Engineering.md]]"]
tags: ["Agents", "Multi-Agent", "Swarm_Intelligence", "Simulation", "MiroFish", "CAMEL-AI"]
type: "wiki"
status: "published"
last_updated: "2026-05-15"
---

# MiroFish: 수만 명의 AI 에이전트가 그리는 미래의 시나리오

## 1. 개요
MiroFish는 CAMEL-AI의 OASIS 엔진을 기반으로 구축된 **멀티 에이전트 군집 지능(Swarm Intelligence) 시뮬레이션 엔진**입니다. 현실 세계의 데이터(뉴스, 정책 초안, 금융 데이터 등)를 기반으로 고정밀 디지털 환경을 구축하고, 수천 명의 자율형 AI 에이전트를 투입하여 특정 사건이나 결정이 미래에 어떤 결과를 초래할지 예측합니다.

## 2. 핵심 메커니즘

### 1) 시드 추출 및 지식 그래프 구축
- 뉴스 기사나 데이터 리포트에서 핵심 신호를 추출하여 시뮬레이션 환경의 기초가 되는 지식 그래프를 형성합니다.

### 2) 독립적 개성을 가진 에이전트 군집
- 투입되는 각 에이전트는 독립적인 성격, 장기 기억, 행동 로직을 가집니다.
- 에이전트들은 환경 내에서 사회적으로 상호작용하며 매 라운드 기억을 업데이트합니다.

### 3) 실시간 변수 주입 (Bird's Eye View)
- 시뮬레이션 도중 사용자가 특정 변수(예: 정책 변경, 돌발 사건 발생)를 주입하고, 그에 따른 시스템의 궤적 변화를 실시간으로 관찰할 수 있습니다.

### 4) 심층 분석 보고 (ReportAgent)
- 시뮬레이션 종료 후, `ReportAgent`가 방대한 상호작용 데이터를 분석하여 요약 리포트를 제공하며, 사용자는 개별 에이전트와 직접 대화하여 그들의 의사결정 근거를 물을 수 있습니다.

## 3. 주요 활용 사례
- **여론 모델링**: 새로운 정책이나 제품 출시 시 사회적 반응 예측.
- **거시 경제 시뮬레이션**: 특정 경제 변수 변화에 따른 시장의 연쇄 반응 분석.
- **내러티브 예측**: 소설이나 시나리오의 초기 설정에서 발생 가능한 다양한 결말 탐색.

## 4. 기술적 기반
- **엔진**: CAMEL-AI OASIS
- **투자/지원**: Shanda Group
- **오픈소스**: [666ghj/MiroFish](https://github.com/666ghj/MiroFish)

## 관련 문서
- [[wiki/Agents/Multi-Agent-and-Orchestration/000_Multi-Agent-and-Orchestration-MOC.md|멀티 에이전트 및 오케스트레이션 MOC]]
- [[wiki/Agents/Memory-and-Cognition/000_Memory-and-Cognition-MOC.md|에이전트 메모리 및 인지 MOC]]
- [[wiki/Models/Architectures/World-Models-Analysis.md|월드 모델 분석]]
