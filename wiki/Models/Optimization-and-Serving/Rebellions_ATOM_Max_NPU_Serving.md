---
title: "리벨리온 ATOM™-Max NPU와 LLM 최적화 서빙"
date: "2026-05-08"
tags: ["Rebellions", "NPU", "ATOM-Max", "vLLM", "Optimization"]
related_raw: ["[[raw/2026-05-08-rebellions-llm-serving-with-npu.md]]", "[[raw/2026-05-08-rebellions-software-stack.md]]", "[[raw/2026-05-08-squeezebits-introducing-atom-max-npu.md]]", "[[raw/2026-05-08-rebellions-atom-max-pod.md]]", "[[raw/2026-05-08-rebellions-vllm-hands-on-workshop.md]]"]
---

# 리벨리온 ATOM™-Max NPU와 LLM 최적화 서빙

리벨리온(Rebellions)은 대규모 AI 추론을 위해 설계된 차세대 NPU인 **ATOM™-Max**와 이를 지원하는 포괄적인 소프트웨어 생태계를 통해 고성능 LLM 서빙을 제공합니다.

## ATOM™-Max 아키텍처 및 인프라
- **ATOM™-Max NPU**: 삼성 5nm 공정에서 제조된 AI 가속기로, 카드당 128 TFLOPS(FP16) 및 512 TOPS(INT8)의 성능을 제공합니다. 다이(Die) 4개와 PCIe 컨트롤러를 결합한 형태로, 표준 서버 노드에서 최대 32개의 NPU를 구성할 수 있습니다.
- **ATOM™-Max POD**: 대규모 분산 처리를 위한 랙 스케일(Rack-Scale) 인프라입니다. 400GB/s RDMA 네트워크로 연결되며, 8대 서버로 구성된 미니 POD에서 시작해 선형적으로 확장 가능한 RSD(Rebellions Scalable Design)를 지원합니다.

## RBLN 소프트웨어 스택과 런타임
리벨리온의 소프트웨어 스택은 [[wiki/Engineering/Infrastructure-and-DevOps/AI_Inference_Infrastructure.md]]를 구축하는 데 핵심적인 역할을 합니다.
- **계층 구조**: Frontend/Backend 컴파일러, 고도로 최적화된 Compute Library, 실행을 관리하는 Runtime Module, Driver, Firmware로 구성됩니다.
- **PyTorch Native UX 지원**: SqueezeBits와의 협력을 통해 개발자 경험을 개선하고 있습니다. `torch.compile` 통합(TorchDynamo)을 통해 외부 변환 과정 없이 PyTorch 코드를 직접 NPU에서 실행할 수 있으며, `torch-rbln`을 통한 Eager Mode 실행도 지원하여 디버깅과 프로토타이핑을 용이하게 합니다.

## vLLM을 활용한 LLM 서빙 최적화
리벨리온은 vLLM 프레임워크와 NPU를 매끄럽게 통합하는 **vLLM-RBLN 플러그인**을 제공합니다.
- **Attention 메커니즘 최적화**: FlashAttention(SRAM에 최적화된 타일 기반 커널), PagedAttention(KV 블록 기반의 커널 레벨 동적 DMA 메모리 관리), Sliding Window Attention 등을 NPU 아키텍처에 맞게 재설계했습니다.
- **분산 추론(RSD)**: Context-building과 Decoding을 분리하는 Disaggregated Prefill, 멀티 노드 실행, 그리고 MoE(Mixture of Experts) 라우팅 분산 처리를 지원합니다.
- 실제 2025년 10월 SqueezeBits와 공동 개최한 워크숍에서는 Eager Mode에서 Graph Mode로의 전환과 vLLM 백엔드 플러그인을 활용한 Qwen1.5-MoE 분산 추론 데모가 성공적으로 진행되었습니다.

관련 문서:
- [[wiki/Models/Optimization-and-Serving/vLLM_Serving_Techniques.md]]
- [[wiki/Models/Optimization-and-Serving/K-EXAONE_Optimization.md]]
