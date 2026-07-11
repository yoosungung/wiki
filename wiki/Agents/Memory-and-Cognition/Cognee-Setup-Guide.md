---
title: "Cognee 설치 및 시작 가이드"
related_raw: ["[[wiki/Agents/Memory-and-Cognition/Cognee 설치.md]]", "[[wiki/Agents/Memory-and-Cognition/Cognee 빠른 시작.md]]"]
tags: ['wiki', 'agents', 'memory', 'setup', 'tutorial']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
updated: "2026-04-20"
---

# Cognee 설정 가이드

이 문서는 Cognee를 설치하고 첫 번째 AI 메모리 예제를 실행하는 방법을 설명합니다.

## 1. 전제 조건
- **Python**: 3.9 ~ 3.13 버전 지원 (3.10 이상 권장).
- **패키지 관리**: `uv` 사용 권장.
- **LLM API**: OpenAI(기본값), Gemini, Anthropic, Ollama 등 지원.

## 2. 설치
```bash
# 가상 환경 생성 및 활성화
uv venv && source .venv/bin/activate

# Cognee 설치
uv pip install cognee
```

## 3. 환경 설정 (.env)
기본적으로 OpenAI를 사용하며, `.env` 파일에 API 키를 설정해야 합니다.
```env
LLM_API_KEY="your_openai_api_key"
```

## 4. 빠른 시작 예제 (Async Python)
Cognee는 비동기(async/await) 방식으로 작동합니다.
```python
import cognee
import asyncio

async def main():
    # 데이터 재설정 (선택 사항)
    await cognee.prune.prune_data()
    
    # 1. 데이터 추가
    await cognee.add("Cognee turns documents into AI memory.")
    
    # 2. 인지화 (지식 그래프 구축)
    await cognee.cognify()
    
    # 3. 검색
    results = await cognee.search(query_text="What does Cognee do?")
    for result in results:
        print(result)

if __name__ == '__main__':
    asyncio.run(main())
```

## 5. CLI 도구
명령줄에서도 동일한 기능을 수행할 수 있습니다:
- `cognee add`
- `cognee cognify`
- `cognee search`
- `cognee ui` (대시보드 실행)

## 관련 문서
- [[wiki/Agents/Memory-and-Cognition/Cognee-Architecture.md|Cognee 아키텍처]]
- [[wiki/Agents/Memory-and-Cognition/Cognee-Core-Concepts.md|Cognee 핵심 개념]]
- [[wiki/Agents/Memory-and-Cognition/Cognee-MOC.md|Cognee-MOC]]
