---
id: mcp-host-allowlist-dns-rebinding
title: "MCP Host allowlist (DNS rebinding)와 임시 Host-rewrite sidecar"
status: canonical
owner: km
updated: "2026-08-05"
last_updated: "2026-08-05"
review_after: "2026-11-05"
sources:
  - ticket:172
  - https://github.com/modelcontextprotocol/rust-sdk/security/advisories/GHSA-89vp-x53w-74fx
tags: ["Infrastructure", "DevOps", "MCP", "Kubernetes", "Security"]
type: "wiki"
---

# MCP Host allowlist (DNS rebinding)와 임시 Host-rewrite sidecar

in-cluster MCP(Streamable HTTP)가 Service FQDN/`Host: <svc>:<port>`로 오면 **403**이 나고, Bearer 토큰을 먼저 의하게 된다. `rmcp` ≥1.4 기본 `allowed_hosts`가 **loopback만** 허용하면 DNS rebinding 방어가 Service Host를 거절한다.

## 진단 순서

1. backend·mcp Pod의 shared token **sha256 일치** 여부 확인.
2. mcp 로그에 `disallowed Host header (DNS rebinding)` / `rejected request with disallowed Host`가 있으면 **토큰 불일치가 아님**.
3. Service `initialize`를 `Host: <svc>:<port>`로 프로브: 403 → allowlist, 401 → 인증.

## 임시 우회 (sidecar)

nginx(또는 동등) sidecar가 ingress Host를 `127.0.0.1:<내부포트>`로 rewrite하고, mcp는 loopback에 bind. Service는 기존 포트를 유지. 검증 후 sidecar·보조 ConfigMap을 제거한다.

## 내구 수정

```text
MCP_ALLOWED_HOSTS=<svc>,<svc>:<port>,localhost,127.0.0.1,::1
→ Config.allowed_hosts
→ StreamableHttpServerConfig::with_allowed_hosts(...)
```

- 미설정 시 loopback 기본 유지(보안 기본값).
- 바이너리 릴리스·롤아웃·ConfigMap 반영 후 **proxy 없이 Host-200**을 확인한 다음에만 sidecar를 제거한다.
- Git overlay pin과 live release asset sha가 어긋날 수 있음 — [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/MCP-Python-Package-Skew-Import-Failure.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
