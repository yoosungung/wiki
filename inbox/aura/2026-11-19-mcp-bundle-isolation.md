# MCP·번들 격리 수준 (M3 정책)

- RuntimeClass 기본=`gvisor`(`runsc`) · 고위험=`kata`
- Egress NetworkPolicy deny-default allowlist: NATS · Pooler · LLM Gateway · aura-content · 등록 MCP · DNS
- 플랫폼 서명 vs 커스텀: 서명도 Egress 동일; 미서명+비샌드박스 금지
- 라이브 NP/실측 = 후속 (Egress 차단 검증)

증거: https://github.com/yoosungung/aura/pull/41 · `check-mcp-bundle-isolation.sh`
