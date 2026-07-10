# Native Attention

리벨리온(Rebellions) NPU 아키텍처에서 구현된 **네이티브 어텐션(Native Attention)** 기술은 LLM의 핵심 연산인 어텐션 메커니즘을 하드웨어 수준에서 직접 실행하도록 최적화한 구현체입니다.

## 1. 개요
기존 GPU 환경에서 CUDA 커널을 통해 어텐션을 처리하던 방식과 달리, 리벨리온 NPU는 어텐션 연산 경로를 런타임 및 하드웨어 설계에 내재화(Native)하여 오버헤드를 극적으로 줄입니다.

- **목적**: 메모리 대역폭 병목 해소 및 긴 컨텍스트(Long Context) 처리 성능 극대화.
- **핵심 전략**: 알고리즘과 하드웨어의 공동 설계(Co-design).

## 2. 핵심 기술 구성

### FlashAttention 가속
- **Tile-based Processing**: NPU 내부의 로컬 SRAM 크기에 맞춰 연산 단위를 타일(Tile)화하여 처리합니다.
- **DRAM I/O 최소화**: 중간 결과물인 Attention Score 행렬을 DRAM에 쓰지 않고 SRAM 내에서 완결하여 메모리 벽(Memory Wall) 문제를 해결합니다.

### 커널 퓨전 (Kernel Fusion)
- **Fused Operators**: QK^T(Score 계산), Softmax, Scaling, PV(Value 가중합) 연산을 하나의 하드웨어 커널로 결합합니다.
- **Blockwise Softmax**: 전체 데이터가 아닌 블록 단위로 Softmax 연산을 수행하여 지연 시간을 단축합니다.

### 런타임 통합
- **vLLM-RBLN 연동**: 오픈소스 서빙 엔진인 vLLM에서 리벨리온 NPU의 어텐션 가속 기능을 네이티브하게 호출할 수 있도록 플러그인 형태로 제공됩니다.
- **Causal Masking**: 생성형 모델의 인과적 마스킹 처리를 어텐션 연산 과정 중에 직접 수행하여 불필요한 연산을 제거합니다.

## 3. 지원 알고리즘
네이티브 어텐션 스택은 다음과 같은 최신 최적화 기법들을 포함합니다.
- [[wiki/Models/Optimization-and-Serving/FlashAttention.md|FlashAttention]]
- [[wiki/Models/Optimization-and-Serving/PagedAttention.md|PagedAttention]] (KV Cache 효율화)
- [[wiki/Models/Optimization-and-Serving/Sliding-Window-Attention.md|Sliding-Window Attention]]

## 4. 기대 효과
- **추론 속도 향상**: PyTorch 기본 구현 대비 월등한 속도를 제공하며, 특히 Batch Size와 Sequence Length가 증가할수록 GPU 대비 효율이 상승합니다.
- **전력 효율**: 불필요한 데이터 이동(DRAM 액세스)을 줄여 와트당 성능(Performance per Watt)을 극대화합니다.
- **TCO 절감**: 고가의 GPU를 대체하여 고성능 LLM 서비스를 낮은 비용으로 운영 가능하게 합니다.

## 연관 문서
- [[wiki/Models/Optimization-and-Serving/Rebellions-NPU-LLM-Serving.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Rebellions-Software-Stack.md]]
- [[wiki/Models/Optimization-and-Serving/000_Optimization-and-Serving-MOC.md]]
