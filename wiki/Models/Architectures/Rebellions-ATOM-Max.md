---
title: "리벨리온 ATOM™-Max: 대규모 추론을 위한 차세대 NPU 아키텍처"
related_raw: ["[[2026-05-12-SqueezeBits_Introducing_ATOM_Max.md]]", "[[2026-05-12-Rebellions_ATOM_Max_POD_Overview.md]]"]
tags: ["Models/Architectures", "NPU", "Rebellions", "ATOM-Max", "Hardware"]
date: "2026-05-12"
---

# 리벨리온 ATOM™-Max 아키텍처 분석

## 1. 하드웨어 구성 및 사양
ATOM™-Max는 대규모 AI 모델 추론을 위해 설계된 리벨리온의 차세대 AI 가속기입니다.
- **멀티 칩 모듈(MCM) 구조**: 하나의 카드에 4개의 ATOM NPU 다이와 1개의 중앙 PCIe 컨트롤러를 통합.
- **주요 제원**:
    - **연산 성능**: 512 TOPS (INT8), 128 TFLOPS (FP16)
    - **대역폭**: 1 TB/s (PCIe Gen5 x16 인터페이스 기반)
    - **전력 소모**: 350W TDP
- **고밀도 구성**: 표준 8슬롯 서버 노드에 최대 32개의 NPU를 탑재할 수 있어 매우 높은 연산 밀도를 제공합니다.

## 2. 메모리 및 데이터 흐름 최적화
- **온칩 SRAM 활용**: NPU당 64MB의 대용량 SRAM을 탑재하여 외부 DRAM 접근을 최소화하고 중간 연산 결과를 효율적으로 처리합니다.
- **연산자 융합(Layer Fusion)**: Linear 레이어와 Activation(예: ReLU) 기능을 하나의 연산으로 결합하여 메모리 트래픽을 절감합니다.

## 3. 확장 인프라: ATOM™-Max POD
- **Rack-Scale 인프라**: 8대의 서버(64 NPUs)로 구성된 미니 POD부터 대규모 클러스터까지 선형적으로 확장 가능한 턴키 솔루션입니다.
- **RDMA 네트워킹**: 노드 간 400 GB/s의 고속 RDMA 패브릭을 통해 초저지연 분산 처리를 지원합니다.
- **RSD (Rebellions Scalable Design)**: 모듈형 설계를 통해 분산된 자원을 효율적으로 관리합니다.

## 4. 소프트웨어 생태계와의 정합성
- **vLLM-RBLN**: ATOM-Max의 성능을 활용하여 연속 배칭(Continuous Batching) 및 PagedAttention을 지원하는 서빙 플러그인.
- **PyTorch Native UX**: `torch.compile` 및 Eager Mode(torch-rbln) 지원을 통해 개발자 친숙도를 높이고 있습니다.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Rebellions-Software-Stack.md]]
- [[wiki/Engineering/Development-Environment/torch-rbln.md]]
