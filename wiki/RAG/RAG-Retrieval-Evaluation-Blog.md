# 오픈 가중치 모델 파인튜닝 가이드

## 핵심 주장 (Claims)
오픈 가중치(Open-weights) 모델의 발전으로 기업들은 타사 API에 의존하지 않고도 자신의 데이터와 인프라에서 작동하는 비용 효율적이고 고성능의 맞춤형 LLM을 구축할 수 있게 되었습니다. 파인튜닝(Fine-tuning)을 통해 더 작은 모델로도 거대 범용 모델의 성능을 따라잡을 수 있으며, 지연 시간(latency)과 비용을 절감할 수 있습니다.

## 시스템 구조 및 파인튜닝 전략 (Strategies & Architecture)
**파인튜닝 vs RAG vs 프롬프트 엔지니어링**:
- **프롬프트 엔지니어링**: 지침과 예시만으로 원하는 동작을 얻을 수 있을 때 사용 (가장 빠르고 저렴).
- **RAG (검색 증강 생성)**: 모델의 훈련 데이터에 없는 최신 지식이나 외부 지식을 인용 기반으로 답변해야 할 때 사용.
- **파인튜닝**: 특정 스타일이나 형식을 일관되게 유지해야 하거나, 작은 모델의 품질을 높여 비용/지연시간을 줄이려 할 때 사용.

**주요 오픈 가중치 베이스 모델**:
- **Gemma (Google DeepMind)**: 파라미터 대비 지능 밀도가 높으며, 온디바이스 챗 및 요약 작업에 적합.
- **Nemotron (NVIDIA)**: 멀티 에이전트 시스템 및 도구 사용(tool-use)을 위해 설계된 높은 처리량의 모델.
- **GLiNER (Fastino Labs)**: 텍스트 분류 및 추출에 특화된 매우 작고 특수화된 인코더 기반 모델.

**학습 기법 (Training Methods)**:
- **PEFT (Parameter-Efficient Fine-Tuning)**: 모델 전체가 아닌 일부 파라미터(약 1%)만 학습하여 메모리를 절약. 대표적으로 LoRA와 4-bit 양자화를 더한 QLoRA가 있음.
- **SFT (Supervised Fine-Tuning)**: 정답(input-output 쌍)을 주고 이를 모방하도록 지도 학습.
- **RL (Reinforcement Learning)**: 인간의 선호도(RLHF)나 직접적인 선호도 최적화(DPO, GRPO)를 통해 모델의 행동을 보상 기반으로 조정.

## 평가(Evaluation) 설계
- 오프더셸프(off-the-shelf) 지표보다는 실제 시스템 실패 사례(error analysis)를 기반으로 작업 특화형(task-specific) 검사를 작성하십시오.
- 점수제(1-5점)보다는 명확한 이진(Pass/Fail) 판단을 우선시하십시오.
