---
id: mcp-python-package-skew-import-failure
title: "MCP Python 패키지 스키: import 실패와 JSON-RPC fallback"
status: canonical
owner: km
updated: "2026-08-05"
last_updated: "2026-08-05"
review_after: "2026-11-05"
sources:
  - ticket:112
  - ticket:60
  - ticket:172
tags: ["Engineering", "AI-Native", "MCP", "Python", "Packaging"]
type: "wiki"
---

# MCP Python 패키지 스키: import 실패와 JSON-RPC fallback

에이전트 이미지의 `leantime-mcp`(또는 동등 stdio MCP)가 **import 단계에서 죽으면** Cursor MCP host는 도구를 발견하지 못한다. 스케줄/스모크는 JSON-RPC Bearer로 티켓 IO를 마감할 수 있다.

## 전형 스키

| 증상 | 원인 후보 |
| :--- | :--- |
| `pydantic_settings` ImportError | venv에 `pydantic-settings` 미핀 |
| `McpError` vs `MCPError` | `fastmcp`가 `mcp.shared.exceptions.McpError`를 기대하는데 설치된 `mcp`는 `MCPError`만 export |
| PATH에 서버 바이너리 없음 | `/opt/.../bin/<server>` 미심볼릭 → discovery만 실패(설치와 별개) |
| `streamablehttp_client` ImportError | 앱 Docker가 lock 없이 `mcp` 2.x 해상 — [[wiki/Engineering/AI-Native-Engineering/MCP-Uv-Lock-Streamable-HTTP-Migrate.md]] |

## 운영 규칙

1. **이미지에 호환 세트 핀**: `mcp` / `fastmcp` / `pydantic-settings`를 함께 고정하고 CI에서 `python -c "import …"` 스모크.
2. **Active 티켓 IO**: MCP host 실패 ≠ 작업 불가 — JSON-RPC `getTicket`/`addComment`/`updateTicket` fallback ([[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]] Closeout tip).
3. Factory smoke가 JSON-RPC로 PASS여도 **이미지 rebake**는 별도 후속(런타임 stdio MCP 복구).

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/MCP-Uv-Lock-Streamable-HTTP-Migrate.md]]
- [[wiki/Engineering/AI-Native-Engineering/Sessionless-MCP-Status-Label-Cache-Poison.md]]
- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
