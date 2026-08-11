---
id: asyncio-timeout-same-context-streaming
title: "asyncio.timeout으로 동일 Context에서 스트림 타임아웃"
status: canonical
owner: km
updated: "2026-08-11"
last_updated: "2026-08-11"
review_after: "2026-11-11"
sources:
  - ticket:391
  - https://github.com/python/cpython/issues/102123
tags: ["Engineering", "AI-Native", "Python", "asyncio", "ContextVar", "SSE"]
type: "wiki"
---

# asyncio.timeout으로 동일 Context에서 스트림 타임아웃

SSE/`AsyncIterator`에 `asyncio.wait_for(aiter.__anext__())`를 쓰면 **새 Task**가 생겨, request-scoped `ContextVar` token을 다른 Task에서 `reset`하면 `ValueError`(token mismatch)가 난다.

## 패턴

```python
# 개념: 동일 Task/Context에서 wall clock + aclosing
async with asyncio.timeout(wall_s), contextlib.aclosing(events) as it:
    async for event in it:
        yield map_sse(event)
```

| 하지 말 것 | 이유 |
| :--- | :--- |
| `wait_for(__anext__)` | 새 Task → ContextVar token 소유권 깨짐 |
| `aclosing(AsyncIterator)`만 어노테 | mypy type-var 실패 → `AsyncGenerator[T, None]`로 생산자/소비자를 표기 |

## 검증

- py3.11에서 스트림 pytest + `mypy src` (aclosing 경로 포함).
- request ContextVar set/reset이 timeout 경로에서도 같은 Task에서만 일어나는지 확인.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md]]
- [[wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md]]
