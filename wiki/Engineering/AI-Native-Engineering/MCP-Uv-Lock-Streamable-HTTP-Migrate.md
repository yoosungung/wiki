---
id: mcp-uv-lock-streamable-http-migrate
title: "Docker uv.lock 동결 + streamable_http_client 마이그레이션"
status: canonical
owner: km
updated: "2026-08-05"
last_updated: "2026-08-05"
review_after: "2026-11-05"
sources:
  - ticket:172
  - https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/migration.md
tags: ["Engineering", "AI-Native", "MCP", "Python", "Docker", "Packaging"]
type: "wiki"
---

# Docker uv.lock 동결 + streamable_http_client 마이그레이션

`Dockerfile`이 `uv pip install .`만 하고 **`uv.lock`을 동결하지 않으면** `mcp>=1.0`이 PyPI **mcp 2.x**로 올라가고, deprecated `streamablehttp_client`가 사라져 이미지가 CrashLoop(`ImportError`)한다.

## 전형 실패

```text
ImportError: cannot import name 'streamablehttp_client'
  from 'mcp.client.streamable_http'
```

롤백만 하면 payload/trim 등 후속 커밋이 클러스터에 안 올라온다. 배포 축은 [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]].

## 수정 패턴

1. `COPY uv.lock` + `uv export --frozen` (또는 동등 frozen install).
2. 범위 핀: `mcp>=1.27.1,<2` (2.x API와 분리).
3. 클라이언트 import를 **`streamable_http_client`**로 마이그레이션 ([python-sdk migration](https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/migration.md)).
4. CI/이미지에 `python -c "from mcp.client.streamable_http import streamable_http_client"` 계약 테스트.

## 교차 스키

stdio MCP host의 pydantic/fastmcp 스키와는 축이 다름 — [[wiki/Engineering/AI-Native-Engineering/MCP-Python-Package-Skew-Import-Failure.md]]. 본 패턴은 **앱 이미지 런타임 import**.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/MCP-Python-Package-Skew-Import-Failure.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/MCP-Host-Allowlist-DNS-Rebinding.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
