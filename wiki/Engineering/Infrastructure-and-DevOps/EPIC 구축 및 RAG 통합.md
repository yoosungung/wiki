# EPIC(Efficient Position-Independent Context Caching) 시스템 구축 절차 및 RAG 통합 파이프라인 연구 보고서

대규모 언어 모델(Large Language Models, LLMs)의 서빙 인프라에서 길고 복잡한 프롬프트 연산을 효율화하는 것은 서비스의 응답 지연 시간과 운영 비용을 결정짓는 핵심 과제이다. 최근 다중 문서 기반 질의응답, 복잡한 프롬프트 엔지니어링, 검색 증강 생성(Retrieval-Augmented Generation, RAG) 등 긴 컨텍스트(Long-context)를 활용하는 애플리케이션이 보편화됨에 따라 매 요청마다 반복되는 정적 문맥을 재계산하는 전통적인 방식은 심각한 컴퓨팅 병목을 유발하고 있다. 이를 극복하기 위해 이미 연산된 Key-Value(KV) 캐시를 재활용하는 프롬프트 캐싱 기술이 도입되었으나, 기존 서버 엔진의 캐싱 메커니즘은 엄격한 접두사 일치(Exact Prefix Match) 조건을 전제로 작동하기 때문에 실제 운영 환경에서 캐시 재사용률이 크게 떨어진다.   

본 연구 보고서는 접두사의 변화나 토큰 위치에 제약받지 않고 KV 캐시를 모듈식으로 재사용할 수 있게 하는 위치 독립적 컨텍스트 캐싱(Position-Independent Context Caching, PIC) 프레임워크인 EPIC(Efficient Position-Independent Context Caching)의 내부 구조, 핵심 알고리즘, 시스템 구축 절차, 그리고 엔터프라이즈 RAG 파이프라인과의 통합 전략을 종합적으로 분석한다.   

## 1. 접두사 기반 캐싱의 한계와 위치 독립적 캐싱(PIC)의 필요성

트랜스포머 기반 LLM 추론 과정은 크게 전체 입력 프롬프트를 한 번에 병렬 처리하여 첫 번째 토큰을 생성하는 프리필(Prefill) 단계와, 이후 토큰을 하나씩 순차적으로 생성하는 디코딩(Decode) 단계로 나뉜다. 이 중 프리필 단계는 연산 집약적(Compute-bound) 특성을 지니며, 클라이언트가 체감하는 첫 번째 토큰 생성 시간(Time-To-First-Token, TTFT)을 직접적으로 좌우한다.   

vLLM이나 SGLang과 같은 최신 추론 서빙 엔진에서 기본적으로 구현되어 있는 기존 프롬프트 캐싱 방식은 프리픽스 캐싱(Prefix Caching)에 의존한다. 이 방식은 요청 간 토큰 시퀀스가 프롬프트의 맨 처음부터 정확히 일치할 때만 사전 계산된 KV 캐시를 재사용한다. 그러나 다중 사용자 환경 및 실제 RAG 서비스에서는 시스템 프롬프트의 변경, 사용자별 가변 지침 삽입, 퓨샷(Few-shot) 예시의 순서 변경, 검색 결과 문서들의 재배치 등으로 인해 동일한 참조 문서가 프롬프트 내에서 서로 다른 위치에 배치되는 일이 빈번하게 발생한다. 이 경우 기존 프리픽스 캐싱 엔진은 동일한 지식 문서가 포함되어 있음에도 불구하고 접두사 불일치로 인해 캐시를 전량 폐기하고 전체 시퀀스를 처음부터 재계산(Full Prefill)할 수밖에 없다.   

위치 독립적 컨텍스트 캐싱(PIC)은 정적 토큰 청크(Chunk)가 프롬프트 내의 어떤 위치에 놓이더라도 해당 청크의 사전 계산된 KV 캐시를 모듈 형태로 재활용할 수 있게 만드는 차세대 서빙 아키텍처이다. EPIC 시스템은 이 위치 독립적 캐싱 원리를 체계화하여 기존 서빙 엔진 대비 TTFT를 최대 8배 단축하고 전체 추론 처리량(Throughput)을 7배 이상 향상시키는 성능을 제공한다.   

## 2. EPIC 코어 아키텍처 및 핵심 알고리즘 원리

EPIC 아키텍처는 불변 정적 문맥을 오프라인에서 사전 처리하는 단계와 런타임에서 동적 쿼리와 정적 캐시를 결합하는 단계를 명확히 분리하는 투스텝 컴파일-링크(Two-Step Compile-Link) 프레임워크를 기반으로 설계되었다.   

### 2.1 투스텝 컴파일-링크 프레임워크

컴파일 단계(Compile Step 또는 KVGen)에서는 시스템 메시지, 표준 참조 문서, 퓨샷 템플릿 등 변경되지 않는 정적 텍스트 청크를 독립적으로 언어 모델에 통과시켜 KV 텐서를 생성한다. 이 과정에서 각 청크는 다른 문맥과의 의존성 없이 Position ID 0부터 시작하도록 고정되어 컴파일되며, 생성된 KV 캐시는 고유한 식별자(`cache_id`)와 함께 KV Store에 저장된다.   

링크 단계(Link Step 또는 KVLink)에서는 런타임 요청이 들어왔을 때 유저 질의와 저장소에서 로드한 복수의 KV 캐시 블록들을 시퀀스로 병합한다. 단순한 캐시 병합은 토큰 간 교차 어텐션(Cross-attention) 손실 및 위치 임베딩의 불일치로 인해 출력 정확도가 급격히 떨어지는 문제가 발생하지만, EPIC은 연산량이 극히 적은 경계 재계산 커널을 실행하여 최적의 어텐션 분포와 정확도를 복원한다.   

### 2.2 어텐션 싱크(Attention Sink) 현상과 LegoLink 알고리즘

독립적으로 컴파일된 KV 캐시 블록들을 프롬프트 상에서 임의로 연결할 때 모델의 성능이 저하되는 주된 원인은 어텐션 싱크(Attention Sink) 현상에 있다. 청크가 Position ID 0부터 독립 컴파일되면, 해당 청크의 문두에 위치한 첫 번째 토큰(예: Llama 모델의 문장 시작 토큰 `<s>`)이 독점적으로 높은 어텐션 가중치를 흡수하는 어텐션 싱크 역할을 수행하게 된다. 이러한 청크가 추론 시 프롬프트의 중간이나 뒤쪽 위치로 배치되면, 기존에 형성된 어텐션 싱크 특성 때문에 후속 토큰들이 실제 의미상 중요한 앞쪽 다른 청크의 문맥에 제대로 어텐션을 할당하지 못하게 방해받는다.   

EPIC은 이 문제를 해결하기 위해 정적 어텐션 희소성(Static Attention Sparsity)을 활용하는 LegoLink(또는 AttnLink) 알고리즘을 도입한다. LegoLink는 프롬프트 전체 토큰을 재계산하는 대신, 첫 번째 청크를 제외한 각 정적 청크의 경계 시작점에 존재하는 극소수의 토큰 k개(k≤32)만을 선택하여 Q,K,V 벡터를 새로 계산한다. 이 과정을 통해 경계 토큰들은 자신이 프롬프트의 절대적 시작점이 아님을 인지하게 되며, 부적절한 어텐션 흡수 능력이 무력화되어 전체 문맥 간 올바른 교차 어텐션이 형성된다. 나아가 특수 시작 토큰이나 더미 토큰을 후속 청크에서 완전히 제거하는 LegoLink-0 변형 기법을 통해 추가적인 연산 비용을 거의 발생시키지 않으면서도 어텐션 싱크 오류를 차단할 수 있다.   

### 2.3 Semantic-Preserving KVSplit 기법

텍스트를 정적 캐시 블록으로 변환할 때 자르는 위치에 따라 의미 단절이 발생할 수 있다. EPIC은 문단 구조, 문장 경계, 의미론적 완결성을 기하학적으로 분석하여 독립 컴파일 시 정보 손실을 최소화하는 지점을 찾아내는 KVSplit 모듈을 제공함으로써 캐시 청크의 의미적 일관성을 보존한다.   

### 2.4 연산 복잡도 비교 및 OOM 방지 메커니즘

전체 프롬프트를 재계산하는 기존 프리필의 연산 복잡도가 프롬프트 토큰 길이 N에 대해 $O(N^2)$에 달하고, 이전 PIC 연구인 CacheBlend가 동적 어텐션 스코어 추적을 위해 전체 시퀀스에 걸쳐 넓은 범위의 토큰 재계산을 수행함에 따라 높은 컴퓨팅 오버헤드를 발생시켰던 것과 달리, LegoLink의 연산 복잡도는 선형 이하로 감소한다.   

ComplexityLegoLink​=O(k⋅N)

여기서 k는 청크당 재계산되는 경계 토큰의 수이며 전체 시퀀스 길이 N에 비해 현저히 작은 상수 값이다 (k≪N). CacheBlend와 같은 선행 기술이 35,000 토큰 이상의 긴 컨텍스트 환경에서 과도한 동적 메모리 할당으로 인해 GPU 메모리 초과(OOM) 오류를 발생시키는 반면, LegoLink는 재계산 메모리 오버헤드가 k 값에 고정되어 있으므로 수만 토큰 이상의 Ultra Long-context 서빙에서도 OOM 없이 안정적으로 작동한다.   

## 3. EPIC 서빙 인프라 단계별 구축 절차

EPIC 인프라를 상용 환경에 구축하는 과정은 추론 엔진 코어 모듈 확장, 오프라인 캐시 컴파일 파이프라인 구축, 그리고 온라인 명시적 서빙 API 구현의 3단계로 구성된다.   

### 3.1 1단계: 추론 엔진 코어 모듈 확장 및 PagedAttention 메모리 레이아웃 설계

EPIC을 탑재하기 위해서는 vLLM과 같은 오픈소스 추론 서빙 엔진의 내부 메모리 관리자와 어텐션 커널을 수정해야 한다.   

첫째, vLLM의 `BlockSpaceManager`를 확장하여 물리적으로 불연속적인 GPU HBM(High Bandwidth Memory) 블록들에 보관되어 있는 정적 청크의 KV 캐시를 논리적 가상 토큰 시퀀스로 매핑하는 가상 메모리 관리 레이어를 구축한다. 이를 통해 각 청크의 KV 캐시는 물리적 이동 없이 PagedAttention 메모리 공간상에 즉시 인덱싱될 수 있다.   

둘째, 상대적/절대적 위치 임베딩(Rotary Position Embedding, RoPE) 변환 레이어를 추가한다. Position ID 0으로 사전 계산된 KV 캐시의 Key 벡터에 대해, 런타임 시 프롬프트 내 실제 오프셋 위치에 맞춰 RoPE 위치 인덱스를 지연 보정(Deferred Positional Encoding Recovery)하거나 변환해 주는 로직을 어텐션 전처리 단계에 삽입한다.   

### 3.2 2단계: 오프라인 캐시 컴파일 파이프라인 및 KV Store 구축

시스템 데이터베이스 및 표준 문서를 정적 KV 캐시로 변환하여 관리하는 인프라를 구축한다.   

첫째, 입력 원문 문서를 KVSplit 모듈로 전달하여 의미 단위 및 토큰 제한 상한(예: 512, 1024, 2048 토큰)에 따라 최적의 청크로 절단한다.   

둘째, 절단된 각 청크를 오프라인 컴파일러(KVGen)에 통과시킨다. 이때 모델 입력 설정에서 `position_ids`를 0부터 시작하도록 고정하고 프리필을 수행하여 고유한 KV 텐서 블록을 추출한다.   

셋째, 생성된 KV 텐서 블록에 대해 청크 해시값 기반의 고유한 `cache_id`를 부여하고, 이를 GPU HBM 메모리 풀 또는 초고속 DRAM/NVMe 디스어그리게이션(Disaggregated) 저장소 계층에 인덱싱하여 배치한다.   

### 3.3 3단계: 온라인 추론 서빙 및 명시적 캐시 컨트롤러 API 구현

엔드포인트 요청을 수신하고 LegoLink 알고리즘을 구동하는 온라인 서빙 레이어를 구현한다.   

첫째, REST API 서빙 프레임워크를 확장하여 사용자가 요청 바디 내에 명시적으로 캐시 재사용 대상인 `cache_id` 리스트와 동적 사용자 질의(Dynamic User Query)를 함께 전달할 수 있도록 OpenAI 호환 호스트 API 인터페이스를 수정한다.   

둘째, 요청 수신 시 서빙 엔진은 전달받은 `cache_id` 리스트에 해당하는 KV 캐시 블록들을 메모리 공간에 가상 배치한다. 이때 첫 번째 청크를 제외한 각 정적 청크의 시작 부분 k개 토큰 지점의 토큰 ID를 추출하여 dynamic prefill 연산 배치(Batch)로 구성한다.   

셋째, 모델 순전파(Forward Pass) 시 지정된 k개 경계 토큰에 대해서만 Query, Key, Value 벡터를 실시간 재계산하고, 이 값으로 기존 저장되어 있던 캐시의 경계 영역을 덮어씌움(Overwrite)으로써 어텐션 싱크 효과를 즉시 제거한 뒤 디코딩 단계로 전환한다.   

## 4. RAG 및 CAG 시스템과의 엔터프라이즈 통합 전략

EPIC 아키텍처는 정적 지식 저장소를 활용하는 검색 증강 생성(RAG) 및 캐시 보강 생성(Cache-Augmented Generation, CAG) 파이프라인과의 통합을 통해 지연 시간을 획기적으로 낮출 수 있다.   

### 4.1 RAG 파이프라인에서의 모듈식 KV 캐시 인덱싱 및 온디맨드 재조립

기존 RAG 파이프라인은 질의 수신 후 Vector DB 검색, 프롬프트 텍스트 결합, 전체 텍스트 프리필 실행이라는 직렬 구조를 거치므로 심각한 TTFT 지연이 발생한다. EPIC을 RAG 파이프라인에 통합하면 텍스트 결합 및 프리필 단계가 KV 캐시의 직접적인 모듈식 재조립 과정으로 대체된다.   

지식 베이스 데이터 수집 단계에서 원문 문서는 KVSplit을 거쳐 미리 프리필 연산이 완료되어 KV Store에 저장되고, 각 청크의 고유 `cache_id`가 생성된다. Vector DB에는 문서의 임베딩 벡터와 함께 해당 문서 청크의 `cache_id`가 메타데이터 필드로 바인딩되어 저장된다.   

실시간 추론 시 클라이언트 질문이 입력되면 Vector DB는 유사도 검색을 수행한 후, 원문 텍스트 전체를 반환하는 대신 매칭된 상위 M개 청크의 `cache_id` 리스트를 즉시 반환한다. RAG 오케스트레이터는 이 `cache_id` 리스트와 동적 질문 텍스트를 패킹하여 EPIC 서빙 엔진으로 전송한다. EPIC 엔진은 이미 GPU 메모리에 로드되어 있는 해당 `cache_id`들의 KV 캐시 블록을 즉시 조합하고 LegoLink 경계 연산만을 수행한 후 생성을 시작하므로, 긴 문맥의 RAG 검색 환경에서도 수십 밀리초 이내에 첫 번째 토큰을 출력할 수 있게 된다.   

### 4.2 명시적 캐시 제어 모델 및 멀티테넌트 자원 할당

EPIC 시스템은 서버가 캐시 적재 및 폐기 여부를 불확실하게 추측하는 대신, 클라이언트나 RAG 오케스트레이터가 캐시 생명주기를 직접 관리하는 명시적 제어(Explicit Cache Control) 방식을 채택한다. 사용자는 특정 지식 문서 캐시를 GPU 메모리에 상주시킬 기간을 제어할 수 있으며, 시스템은 명시적인 해제 요청이 없는 한 해당 캐시를 유지한다.   

GPU HBM은 고비용 자원이므로 멀티테넌트 환경에서는 토큰 크기 및 점유 시간에 비례하는 산정 모델을 통해 캐시 자원을 관리한다:   

CostCache​=Pricetoken⋅hour​×LengthTokens​×DurationHours​

자원 관리자는 이 비용 모델을 기반으로 빈번하게 검색되는 Hot Document의 캐시를 GPU HBM에 지속 상주시추고, 참조 빈도가 낮은 Cold Document의 캐시는 DRAM/NVMe 계층으로 이관하거나 스왑아웃하는 동적 자원 오케스트레이션을 구현할 수 있다.   

## 5. 정량적 성능 평가 및 주요 시스템 비교 분석

EPIC 시스템의 연산 효율성과 타당성을 검증하기 위해 기존 대표적 캐싱 서빙 시스템들과의 정량적 성능 지표 및 메커니즘 차이를 종합 비교 분석한다.   

|**평가 및 비교 항목**|**Native vLLM (Prefix Caching)**|**CacheBlend (선행 PIC)**|**EPIC (LegoLink 적용)**|
|---|---|---|---|
|**캐시 재사용 메커니즘**|엄격한 접두사 일치 (Exact Prefix Match)|위치 독립적 캐시 재사용|위치 독립적 모듈식 캐시 재사용|
|**연산 복잡도 (Link 단계)**|전체 재계산: O(N2)<br><br>[cite: 2, 3]|동적 선택 재계산: O(N2)<br><br>[cite: 3, 12]|경계 선택 재계산: O(k⋅N)<br><br>[cite: 3, 9, 13]|
|**TTFT 개선 배율**|1.0x (기준선)|약 2.5x ~ 3.0x 단축|**최대 8.0x 단축**<br><br>[cite: 1, 3, 4, 5]|
|**시스템 추론 처리량**|1.0x (기준선)|약 2.0x ~ 3.0x 향상|**최대 7.0x 향상**<br><br>[cite: 1, 3, 4, 5]|
|**Long Context OOM 안정성**|프롬프트 길이에 따라 메모리 선형 증가|약 35,000 토큰 부근에서 OOM 발생|**수만 토큰 이상 OOM 없이 안정 동작**<br><br>[cite: 3, 10]|
|**모델 출력 정확도 보존율**|100% (손실 없음)|Full Prefill 대비 2~10% 손실|**손실율 0 ~ 7% 이내 보존**<br><br>[cite: 3, 4, 5]|

  

실험 결과에 따르면 EPIC은 프롬프트 길이가 길어지고 정적 청크의 비율이 높아질수록 TTFT 개선 폭이 커지는 경향을 보인다. 특히 동시 요청이 유입되는 비동기 서빙 환경에서 기존 vLLM 프리픽스 캐싱 대비 최대 7배 높은 처리량을 기록하였다.   

정확도 검증 측면에서는 HotpotQA, 2WikiMQA, Needle in a Haystack 등 다중 문서 추론 및 긴 문맥 검색 벤치마크에서 LegoLink 경계 재계산을 적용했을 때 전체 재계산 대비 F1 Score 및 Rouge-L 성능 감소가 0~7% 미만으로 제어됨이 확인되었다. 이는 어텐션 싱크 현상을 원천적으로 제거함으로써 문맥 간 정확한 교차 어텐션 연산이 복원되었음을 실증한다.   

## 6. 종합 결론 및 실무 적용 제언

EPIC(Efficient Position-Independent Context Caching) 시스템은 기존 LLM 서빙 프레임워크가 지니고 있던 접두사 일치 조건이라는 한계를 파괴하고, 정적 컨텍스트를 완전한 모듈 형태로 재사용할 수 있게 만드는 기술적 전환점이다. 어텐션 싱크 현상에 대한 세밀한 분석을 바탕으로 고안된 LegoLink 알고리즘은 극소수의 경계 토큰만을 연산하여 $O(k \cdot N)$의 복잡도로 모델 정확도를 안정적으로 복원해 낸다.   

실무 인프라 환경에 EPIC을 성공적으로 적용하기 위해서는 다음 세 가지 실행 전략이 요구된다.

첫째, 기존 RAG 파이프라인의 데이터 수집 로직을 오프라인 컴파일 체계로 재편해야 한다. 지식 베이스 문서를 KVSplit 기반의 정적 청크로 잘라 미리 KV 캐시를 컴파일하고, Vector DB 메타데이터에 `cache_id`를 매핑하는 인프라 구조 변경이 전제되어야 한다.   

둘째, 계층형 KV 캐시 메모리 관리 시스템을 구축해야 한다. 사용 빈도가 높은 코어 문서 캐시는 GPU HBM에 상주시키고, 빈도가 낮은 캐시는 DRAM이나 NVMe 저장소로 이관하는 스왑 파이프라인을 연동하여 GPU 메모리 효율을 극대화해야 한다.   

셋째, 서비스 도메인의 특성과 백본 LLM의 어텐션 구조에 맞춘 하이퍼파라미터 k의 최적화 작업이 수행되어야 한다. 경계 재계산 토큰 수 k를 16에서 32 사이에서 미세 조정함으로써, 지연 시간 단축과 출력 정확도 보존 사이의 최적의 밸런스를 달성할 수 있다.   

[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fwww.catalyzex.com%2Fpaper%2Fepic-efficient-position-independent-context)

catalyzex.com

EPIC: Efficient Position-Independent Context Caching for Serving

새 창에서 열기](https://www.catalyzex.com/paper/epic-efficient-position-independent-context)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fwww.researchgate.net%2Fpublication%2F385107655_EPIC_Efficient_Position-Independent_Context_Caching_for_Serving_Large_Language_Models)

researchgate.net

EPIC: Efficient Position-Independent Context Caching for Serving

새 창에서 열기](https://www.researchgate.net/publication/385107655_EPIC_Efficient_Position-Independent_Context_Caching_for_Serving_Large_Language_Models)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Ficml.cc%2Fvirtual%2F2025%2Fposter%2F43926)

icml.cc

EPIC: Efficient Position-Independent Caching for Serving Large

새 창에서 열기](https://icml.cc/virtual/2025/poster/43926)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fopenreview.net%2Fpdf%3Fid%3Dqjd3ZUiHRT)

openreview.net

Epic: Efficient Position-Independent Caching for Serving Large

새 창에서 열기](https://openreview.net/pdf?id=qjd3ZUiHRT)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fwww.themoonlight.io%2Fen%2Freview%2Fepic-efficient-position-independent-context-caching-for-serving-large-language-models)

themoonlight.io

[Literature Review] EPIC: Efficient Position-Independent Context

새 창에서 열기](https://www.themoonlight.io/en/review/epic-efficient-position-independent-context-caching-for-serving-large-language-models)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fgithub.com%2FDerekHJH%2Fepic)

github.com

DerekHJH/epic - GitHub

새 창에서 열기](https://github.com/DerekHJH/epic)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fwww.emergentmind.com%2Ftopics%2Fposition-independent-caching-pic)

emergentmind.com

Position-Independent Caching (PIC) - Emergent Mind

새 창에서 열기](https://www.emergentmind.com/topics/position-independent-caching-pic)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fopenreview.net%2Fforum%3Fid%3Dqjd3ZUiHRT)

openreview.net

EPIC: Efficient Position-Independent Caching for Serving Large

새 창에서 열기](https://openreview.net/forum?id=qjd3ZUiHRT)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Farxiv.org%2Fhtml%2F2410.15332)

arxiv.org

Epic: Efficient Position-Independent Caching for Serving ... - arXiv

새 창에서 열기](https://arxiv.org/html/2410.15332)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Farxiv.org%2Fhtml%2F2410.15332v2)

arxiv.org

Epic: Efficient Position-Independent Context Caching for Serving

새 창에서 열기](https://arxiv.org/html/2410.15332v2)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fwww.catalyzex.com%2Fauthor%2FXusheng%2520Chen)

catalyzex.com

Xusheng Chen - CatalyzeX

새 창에서 열기](https://www.catalyzex.com/author/Xusheng%20Chen)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fwww.semanticscholar.org%2Fpaper%2FCacheBlend%253A-Fast-Large-Language-Model-Serving-for-Yao-Li%2Fb1e600dfa7e61c54fb21fe4bd2d1edc7943166aa)

semanticscholar.org

[PDF] CacheBlend: Fast Large Language Model Serving for RAG

새 창에서 열기](https://www.semanticscholar.org/paper/CacheBlend%3A-Fast-Large-Language-Model-Serving-for-Yao-Li/b1e600dfa7e61c54fb21fe4bd2d1edc7943166aa)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fpaper.lingyunyang.com%2Fpaper-list%2Fsystems-for-ml%2Fllm)

paper.lingyunyang.com

Large Language Model (LLM) | Awesome Papers

새 창에서 열기](https://paper.lingyunyang.com/paper-list/systems-for-ml/llm)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fwww.semanticscholar.org%2Fpaper%2FPrompt-Cache%253A-Modular-Attention-Reuse-for-Inference-Gim-Chen%2Fbc5c73c101da795cfa44e4ac7751cdedca9b6d93)

semanticscholar.org

Prompt Cache: Modular Attention Reuse for Low-Latency Inference

새 창에서 열기](https://www.semanticscholar.org/paper/Prompt-Cache%3A-Modular-Attention-Reuse-for-Inference-Gim-Chen/bc5c73c101da795cfa44e4ac7751cdedca9b6d93)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fwww.themoonlight.io%2Fen%2Freview%2Fmepic-memory-efficient-position-independent-caching-for-llm-serving)

themoonlight.io

[Literature Review] MEPIC: Memory Efficient Position Independent

새 창에서 열기](https://www.themoonlight.io/en/review/mepic-memory-efficient-position-independent-caching-for-llm-serving)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fdiscuss.pytorch.kr%2Ft%2Fcag-cache-augmented-generation-llm-long-context-rag%2F5792)

discuss.pytorch.kr

LLM의 Long Context를 활용한 RAG 대체 기법에 대한 연구

새 창에서 열기](https://discuss.pytorch.kr/t/cag-cache-augmented-generation-llm-long-context-rag/5792)[

![](https://t0.gstatic.com/faviconV2?client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL&url=https%3A%2F%2Fchatpaper.com%2Fpaper%2F167714)

chatpaper.com

EPIC: Efficient Position-Independent Caching for Serving Large





](https://chatpaper.com/paper/167714)