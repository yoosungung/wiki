# Egress 차단 검증 (M3 / V3.3)

- NetworkPolicy deny-default + allowlist (NATS·Pooler·LLM Gateway·aura-content·DNS·등록 MCP)
- Offline simulator gate: `check-egress-block-verify.sh`
- Live cluster optional (`AURA_EGRESS_LIVE=1`)

증거: https://github.com/yoosungung/aura/pull/42
