---
title: "JSON vs TOON LLM 토큰 효율성 비교"
related_raw: ["[[wiki/Engineering/Data-and-Security/JSON vs TOON LLM 토큰 효율성 비교.md]]"]
tags: ['wiki', 'ai_core', 'ai_ml_development', 'ai_data_formats']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# JSON vs TOON: LLM 토큰 효율성 비교

LLM 입력 포맷으로 JSON과 TOON의 토큰 효율성을 비교 분석한 글입니다.

### TOON 포맷

TOON은 반복적인 객체 리스트를 표 형식으로 표현하여 JSON보다 토큰 사용량을 줄이고 LLM이 구조를 더 효율적으로 해석하도록 설계되었습니다.

### 벤치마크 결과

벤치마크 결과 TOON은 JSON 대비 적은 토큰으로 더 높은 정확도를 보였습니다.

### HyperCLOVA X 모델 실험

HyperCLOVA X 모델 실험에서는 다음과 같은 결과를 보였습니다.

*   **TOON의 이점**: 단순 구조 데이터, RAG 기반 작업, API 응답/로그 분석에서 토큰 효율성과 성능 이점을 가짐
*   **JSON의 이점**: 추론 중심 작업에서는 JSON이 더 안정적임

### 결론

TOON은 모든 상황에 적용 가능한 해결책은 아니지만, 구조가 단순하고 반복적인 데이터가 많은 영역에서 효율적인 대안이 될 수 있습니다.

### 관련 링크

*   [TOON GitHub](https://github.com/toon-format/toon)

### 관련 이미지

![](https://www.ncloud-forums.com/assets/uploads/files/image.png.c39d4dd8630e3f6b571db585465b83ad.png)
![](https://www.ncloud-forums.com/assets/uploads/files/image.png.1e55abf5b05ce47f6e8fc7d80062e5c6.png)
![](https://www.ncloud-forums.com/assets/uploads/files/image.png.5f91888910068a1465b729ac3480516e.png)
![](https://www.ncloud-forums.com/assets/uploads/files/image.png.99fd90453490bc5ea5cd19cc24ceaee8.png)
![](https://www.ncloud-forums.com/assets/uploads/files/image.png.55921cc14bfa1d8a1541941041794444.png)

### 관련 노트

*   LLM
*   JSON
*   TOON
*   Tokenization
*   HyperCLOVA X
*   RAG
