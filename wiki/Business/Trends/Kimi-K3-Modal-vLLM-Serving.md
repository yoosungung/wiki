---
title: "Kimi K3: vLLM 및 Modal 기반 서빙 인프라 아키텍처"
related_raw: ["[[raw/Kimi K3 runs on Modal since Day 0 - powered by vLLM! vLLM provides the serving engine; Modal exposes it as a production endpoint that scales on demand. One deploy gets you the full model, and it….md]]"]
tags: ['#inbox', '#Kimi-K3', '#vLLM', '#Modal', '#AI-Serving', '#LLMOps']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# Kimi K3: vLLM 및 Modal 기반 서빙 인프라 아키텍처

## 1. 개요
* **배경**: Moonshot AI의 최신 거대 언어 모델인 **Kimi K3**는 초기 서비스 기획 시점부터 클라우드 GPU 런타임인 **Modal**과 고성능 추론 엔진 **vLLM**을 기반으로 인프라를 구축하여 구동되고 있습니다.
* **아키텍처 구성**:
  - **추론 엔진 (Serving Engine)**: vLLM이 추론 연산을 최적화하여 연산 효율을 극대화합니다.
  - **인프라 플랫폼 (Endpoint Platform)**: Modal이 외부 엔드포인트를 제공하며, 실시간 유입 트래픽 변화에 맞춰 자동으로 GPU 컨테이너 노드를 확장/축소(Scales on demand)합니다.

## 2. 기술적 장점 및 시사점
* **배포 관리 제로화 (No Ops)**: 엔지니어가 실시간으로 GPU 인스턴스 클러스터를 모니터링하고 프로비저닝할 필요 없이, 단일 배포 명령어를 통해 3T급 전체 모델 서빙 파이프라인을 로드하고 온디맨드 스케일아웃 환경을 구성할 수 있습니다.
* **비용 효율성**: 트래픽이 몰리지 않는 시간대에는 인프라 사용량이 최소화되어 유휴 GPU 장치 고정 유지비가 절감됩니다.
