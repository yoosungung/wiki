---
title: "KTransformers"
related_raw: ["[[wiki/Models/Optimization-and-Serving/KTransformers.md]]"]
tags: ['wiki', 'ai_core', 'models_and_libraries', 'llm_optimization_and_serving']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# KTransformers: CPU/GPU 하이브리드 추론을 위한 프레임워크

**출처**: [원본 링크](https://github.com/kvcache-ai/ktransformers)

KTransformers는 CPU-GPU 이종 컴퓨팅을 통해 대규모 언어 모델(LLM)의 효율적인 추론 및 미세 조정을 위한 유연한 프레임워크입니다. 이 프로젝트는 `kt-kernel`과 `kt-sft`라는 두 가지 핵심 모듈로 구성되어 있습니다.

**🎯 개요**
KTransformers는 LLM 추론 및 미세 조정 최적화를 경험하기 위한 유연한 프레임워크로, CPU-GPU 이종 컴퓨팅을 활용하여 효율성을 극대화합니다.

**📦 핵심 모듈**

*   **🚀 kt-kernel - 고성능 추론 커널**
    *   **목적:** 이종 LLM 추론을 위한 CPU 최적화 커널 연산.
    *   **주요 기능:**
        *   **AMX/AVX 가속:** INT4/INT8 양자화 추론을 위한 Intel AMX 및 AVX512/AVX2 최적화 커널을 제공합니다.
        *   **MoE 최적화:** NUMA-aware 메모리 관리를 통해 효율적인 Mixture-of-Experts(MoE) 추론을 지원합니다.
        *   **양자화 지원:** CPU 측 INT4/INT8 양자화 가중치와 GPU 측 GPTQ를 지원합니다.
        *   **쉬운 통합:** SGLang 및 기타 프레임워크를 위한 깔끔한 Python API를 제공합니다.
    *   **사용 사례:** 대규모 MoE 모델을 위한 CPU-GPU 하이브리드 추론, 프로덕션 서빙을 위한 SGLang과의 통합, 이종 전문가 배치(핫 전문가 GPU, 콜드 전문가 CPU).
    *   **성능 예시:** DeepSeek-R1-0528 (FP8) 모델을 8×L20 GPU + Xeon Gold 6454S 구성에서 실행 시, 총 처리량 227.85 토큰/초, 출력 처리량 87.58 토큰/초 (8방향 동시성)를 달성합니다.
    *   **문서:** 전체 문서는 [여기](https://kvcache-ai.github.io/ktransformers/kt-kernel/)에서 확인할 수 있습니다.

*   **🎓 kt-sft - 미세 조정 프레임워크**
    *   **목적:** 초거대 MoE 모델 미세 조정을 위한 KTransformers와 LLaMA-Factory 통합.
    *   **주요 기능:**
        *   **자원 효율성:** 671B DeepSeek-V3 모델을 단 70GB GPU 메모리 + 1.3TB RAM으로 미세 조정할 수 있습니다.
        *   **LoRA 지원:** 이종 가속을 통한 전체 LoRA 미세 조정을 지원합니다.
        *   **LLaMA-Factory 통합:** 인기 있는 미세 조정 프레임워크와의 원활한 통합을 제공합니다.
        *   **프로덕션 준비:** 채팅, 배치 추론 및 메트릭 평가 기능을 포함합니다.
    *   **성능 예시:**
        *   DeepSeek-V3 (671B) LoRA + AMX: 70GB GPU 메모리(멀티 GPU)로 약 40 토큰/초.
        *   DeepSeek-V2-Lite (14B) LoRA + AMX: 6GB GPU 메모리로 약 530 토큰/초.
    *   **문서:** 전체 문서는 [여기](https://kvcache-ai.github.io/ktransformers/kt-sft/)에서 확인할 수 있습니다.

**🔥 주요 업데이트 (최근 예시)**
*   2025년 11월 6일: Kimi-K2-Thinking 추론 및 미세 조정 지원.
*   2025년 11월 4일: KTransformers 미세 조정 × LLaMA-Factory 통합.
*   2025년 10월 27일: Ascend NPU 지원.
*   2025년 10월 10일: SGLang 통합.
*   2025년 9월 11일: Qwen3-Next 지원.

**🔥 인용**
KTransformers를 연구에 사용하는 경우 다음 논문을 인용해 주십시오:
`@inproceedings{10.1145/3731569.3764843,
title = {KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models},
author = {Chen, Hongtao and Xie, Weiyu and Zhang, Boxin and Tang, Jingqi and Wang, Jiahao and Dong, Jianwei and Chen, Jiahao and Yuan, Ziwei and Lin, Chen and Qiu, Chengyu and Zhu, Yuening and Ou, Qingliang and Liao, Jiaqi and Chen, Xianglin and Ai, Zhiyuan and Wu, Yongwei and Zhang, Mingxing},
booktitle = {Proceedings of the ACM SIGOPS 31st Symposium on Operating Systems Principles},
year = {2025}
}`

**💬 커뮤니티 및 지원**
*   GitHub Issues: https://github.com/kvcache-ai/ktransformers/issues
*   WeChat 그룹: `archive/WeChatGroup.png` 이미지 참조.

**관련 링크:**
*   프로젝트 웹사이트: https://kvcache-ai.github.io/ktransformers/
*   Kimi-K2-Thinking 추론 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-kernel/kimi_k2_thinking_inference/
*   Kimi-K2-Thinking 미세 조정 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-sft/kimi_k2_thinking_finetune/
*   LLaMA-Factory 통합 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-sft/llama_factory_integration/
*   Ascend NPU 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-kernel/ascend_npu/
*   SGLang 블로그: https://kvcache-ai.github.io/ktransformers/blog/sglang_integration/
*   Qwen3-Next 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-kernel/qwen3_next/
*   Kimi-K2-0905 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-kernel/kimi_k2_0905/
*   SmallThinker 및 GLM4-MoE 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-kernel/small_thinker_glm4_moe/
*   Kimi-K2 튜토리얼: https://kvcache-ai..github.io/ktransformers/kt-kernel/kimi_k2/
*   Intel Arc GPU 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-kernel/intel_arc_gpu/
*   AMX-Int8, AMX-BF16 및 Qwen3MoE 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-kernel/amx_int8_bf16_qwen3moe/
*   LLaMA 4 모델 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-kernel/llama4/
*   AMD GPU의 ROCm 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-kernel/rocm_amd_gpu/
*   Deepseek-R1 및 V3 쇼케이스 및 재현 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-kernel/deepseek_r1_v3/
*   인젝션 및 멀티 GPU 상세 튜토리얼: https://kvcache-ai.github.io/ktransformers/kt-kernel/injection_multi_gpu/
